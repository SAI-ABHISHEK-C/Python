import tkinter as tk

# ---------- operations (no eval) ----------
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

OPS = {"+": add, "-": sub, "*": mul, "/": div}
PREC = {"+": 1, "-": 1, "*": 2, "/": 2}

# ---------- expression evaluator ----------
def evaluate_expr(expr: str) -> float:
    expr = expr.replace(" ", "")
    if not expr:
        return 0.0

    nums, ops = [], []

    def apply_op():
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        nums.append(OPS[op](a, b))

    def read_number(i: int):
        # optional unary sign if at start or after an operator
        sign = 1
        if expr[i] in "+-" and (i == 0 or expr[i - 1] in OPS):
            sign = -1 if expr[i] == "-" else 1
            i += 1
        j = i
        dot_seen = False
        while j < len(expr) and (expr[j].isdigit() or (expr[j] == "." and not dot_seen)):
            dot_seen = dot_seen or expr[j] == "."
            j += 1
        if j == i:  # not a number
            raise ValueError("number expected")
        return sign * float(expr[i:j]), j

    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch.isdigit() or ch == "." or (ch in "+-" and (i == 0 or expr[i - 1] in OPS)):
            num, i = read_number(i)
            nums.append(num)
        elif ch in OPS:
            # handle consecutive operators: replace previous op
            if i > 0 and expr[i - 1] in OPS:
                # disallow "5++" etc.
                raise ValueError("bad operator placement")
            while ops and PREC[ops[-1]] >= PREC[ch]:
                apply_op()
            ops.append(ch)
            i += 1
        else:
            raise ValueError(f"invalid char: {ch}")

    while ops:
        apply_op()
    return nums[-1]

# ---------- UI ----------
root = tk.Tk()
root.title("Calculator (no state / no eval)")
root.resizable(False, False)

display_var = tk.StringVar()

entry = tk.Entry(root, textvariable=display_var, font=("Arial", 20),
                 justify="right", bd=8, relief="groove")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)
entry.focus()

def append_digit(ch):
    display_var.set(display_var.get() + ch)

def append_op(op):
    s = display_var.get()
    if not s:
        # allow leading '-' for negatives
        if op == "-":
            display_var.set("-")
        return
    if s[-1] in OPS:
        # replace last operator (user changed mind)
        display_var.set(s[:-1] + op)
    else:
        display_var.set(s + op)

def clear():
    display_var.set("")

def backspace():
    display_var.set(display_var.get()[:-1])

def equals(event=None):
    try:
        result = evaluate_expr(display_var.get())
        display_var.set(str(result))
    except ZeroDivisionError:
        display_var.set("Error (÷0)")
    except Exception:
        display_var.set("Error")

buttons = [
    ("C", clear), ("⌫", backspace), ("", None), ("/", lambda: append_op("/")),
    ("7", lambda: append_digit("7")), ("8", lambda: append_digit("8")), ("9", lambda: append_digit("9")), ("*", lambda: append_op("*")),
    ("4", lambda: append_digit("4")), ("5", lambda: append_digit("5")), ("6", lambda: append_digit("6")), ("-", lambda: append_op("-")),
    ("1", lambda: append_digit("1")), ("2", lambda: append_digit("2")), ("3", lambda: append_digit("3")), ("+", lambda: append_op("+")),
    ("0", lambda: append_digit("0")), (".", lambda: append_digit(".")), ("=", equals), ("", None),
]

r = 1; c = 0
for text, cmd in buttons:
    if text == "":
        # spacer to keep a 4x5 grid tidy
        lbl = tk.Label(root, text="")
        lbl.grid(row=r, column=c, padx=4, pady=4)
    else:
        btn = tk.Button(root, text=text, command=cmd, font=("Arial", 16), width=4, height=2)
        btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)
    c += 1
    if c == 4:
        r += 1; c = 0

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# keyboard support
def on_key(e):
    ch = e.char
    if ch.isdigit() or ch == ".":
        append_digit(ch)
    elif ch in OPS:
        append_op(ch)
    elif e.keysym in ("Return", "KP_Enter"):
        equals()
    elif e.keysym == "Escape":
        clear()
    elif e.keysym == "BackSpace":
        backspace()

root.bind("<Key>", on_key)

root.mainloop()
