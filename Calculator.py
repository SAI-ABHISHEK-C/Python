class Solution:
    def calculate(self,n1,n2, s):
        if s == "+":
            return n1 + n2
        elif s == "*":
            return n1 * n2
        elif s == "-":
            return n1 - n2
        elif s == "/":
            return n1 / n2

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
op = input("Enter the operation: ")

s = Solution()
res = s.calculate(n1,n2, op)
print(res)
