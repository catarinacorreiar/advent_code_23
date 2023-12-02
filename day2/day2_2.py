import re

file = open("day2/input.txt", "r")

power = 0
while True:
    line = file.readline()
    
    green = list(map(lambda x: int(re.findall("\d{1,3}", x)[0]), re.findall("\d{1,3} green", line)))
    red = list(map(lambda x: int(re.findall("\d{1,3}", x)[0]), re.findall("\d{1,3} red", line)))
    blue = list(map(lambda x: int(re.findall("\d{1,3}", x)[0]), re.findall("\d{1,3} blue", line)))

    if green != [] and red != [] and blue != []:
        power += max(green)*max(blue)*max(red)

    if not line:
        break

print(power)