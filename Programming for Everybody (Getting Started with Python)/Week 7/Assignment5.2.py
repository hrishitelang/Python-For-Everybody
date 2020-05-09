largest = None
smallest = None

while True:
    x = input("Enter the number ")
    if x == 'done':
        break
    try:
        a = int(x)
    except:
        print("Invalid input")
        continue
    if largest is None and smallest is None:
        largest = a
        smallest = a
    if largest < a:
        largest = a;
    if smallest > a:
        smallest = a;

print("Maximum is ", largest)
print("Minimum is ", smallest)
