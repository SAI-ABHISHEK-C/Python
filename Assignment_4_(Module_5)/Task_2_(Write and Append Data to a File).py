t = input("Enter text to write to the file: ")
with open("output.txt", 'w') as f:
    f.write(t + "\n")
    print("Data successfully written to output.txt \n")

A = input("Enter additional text to write to the file: ")
with open("output.txt", 'a') as f:
    f.writelines(A)
    print("Data successfully appended \n")

print("Final content of Output.txt")
with open("output.txt", 'r') as f:
    R = f.read()
    print(R)