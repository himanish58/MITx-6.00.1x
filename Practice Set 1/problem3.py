# Write a program that prints the longest substring of a String in which the letters occur in alphabetical order

s = input('Enter the string..\n')
longestStr = ''
temp = ''
tempOneLetter = ''
for i in range(len(s)-1):
    if ord(s[i]) <= ord(s[i+1]):
        if temp == '':
            temp += s[i] + s[i + 1]
        else:
            temp += s[i+1]

    else:
        if len(temp) > len(longestStr):
            longestStr = temp
        temp = ''
        if tempOneLetter == '':
            tempOneLetter = s[i]
    if len(temp) > len(longestStr):
        longestStr = temp
    if len(tempOneLetter) > len(longestStr):
        longestStr = tempOneLetter

print('Longest substring in alphabetical order is:', longestStr)