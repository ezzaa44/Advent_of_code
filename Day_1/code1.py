input_file = "input.txt"
list1 = []
list2 = []
with open(input_file, "r") as file:
    data = file.readlines()

    for line in data:
        num1,num2 = map(int,line.split())
        list1.append(num1)
        list2.append(num2)

    list1.sort()
    list2.sort()
    result = 0
    for num1,num2 in zip(list1,list2):
        result += abs(num1 - num2)

print (result)