#read input file into a list of strings

def get_first_digit_in_string(s):
    for c in s:
        if c.isdigit():
            #convert char to int
            return int(c)

def reverse_string(s):
    return s[::-1]


def addTwoDigits(firstDigit, lastDigit):
    return firstDigit * 10 + lastDigit


l = []

with open('1_input.txt') as f:
    for line in f.readlines():
        firstDigit = get_first_digit_in_string(line)
        lastDigit = get_first_digit_in_string(reverse_string(line))
        sum = addTwoDigits(firstDigit, lastDigit)
        print(sum, firstDigit, lastDigit)
        l.append(sum)


# sum list
sum = 0
for i in l:
    sum += i


print(sum)
