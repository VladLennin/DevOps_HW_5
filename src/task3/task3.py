with open('count.txt', 'r') as file:
    content = file.read()
    array = content.split(" ")
    array = [int(x) for x in array]
    array.sort()
    print(f"The largest number from file count.txt is : {array[-1]}")
