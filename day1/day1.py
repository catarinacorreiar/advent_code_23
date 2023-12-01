import re

file1 = open("day1/input.txt", "r")
sum = 0

while True:
    line = file1.readline()

    res = [int(char) for char in line if char.isdigit()]
    if res != []:
        first = res[0]  
        last = res[-1]
        whole_digit = str(first)+str(last)
        
        sum = int(whole_digit) + sum

    if not line:
        break
print(sum)

file1.close()