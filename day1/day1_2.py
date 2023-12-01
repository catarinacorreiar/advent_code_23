import re

file1 = open("day1/input2.txt", "r")
sum = 0

our_nums = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}
our_numss = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

while True:
    line = file1.readline()
    res = []
    r = []
    nums = []
    new = ''
    #line = line.replace(our_nums.values(), our_nums.keys())
    
    for key in our_numss:
        if key in line:
            line = line.replace(key, key+our_numss[key]+key)
            
        
    print(line)

    res = [int(char) for char in line if char.isdigit()]
    print(res)
    
    if res != []:
        first = res[0]  
        last = res[-1]
        whole_digit = str(first)+str(last)
        
        sum = int(whole_digit) + sum

    if not line:
        break
print(sum)

file1.close()