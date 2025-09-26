count = 0
try:
    with open('sample.txt', 'r') as file:
        content = file.readlines()
        for i in content:
            count += 1
            print("Line",count,":",i.strip())
except FileNotFoundError:
    print("The file sample.txt was not found.")