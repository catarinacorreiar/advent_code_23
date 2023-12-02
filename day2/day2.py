import re

file = open("day2/input.txt", "r")

max_cubes = {
    'red': '12',
    'green': '13',
    'blue': '14'
}

total = 0
while True:
    line = file.readline()

    for key in max_cubes:
        if key in line:
            line = line.replace(key, max_cubes[key])

    compare_nums = re.findall("\d{1,3}", line)

    check_list = []
    if compare_nums != []:
        id = int(compare_nums[0])
        i = 0
        while i < len(compare_nums)-2:
            if int(compare_nums[i+1]) <= int(compare_nums[i+2]):
                check_list.append('True')
            else:
                check_list.append('False')
            i=i+2

        if 'False' not in check_list:
            total = total + id
        
    if not line:
        break

print(total)