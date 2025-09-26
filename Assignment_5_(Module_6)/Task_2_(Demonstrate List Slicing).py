l = []
for i in range(1,11):
    l.append(i)
print("Original list: ",l)
el = l[:5]
print("Extracted first five elements :",el)
el.reverse()
print("Reversed the extracted elements: ",el)

