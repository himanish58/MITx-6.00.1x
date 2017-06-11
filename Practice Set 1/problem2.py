# Write a program that prints the number of times the string 'bob' occurs in a String

s = input('Enter the string..\n')
count = 0
for j in range(len(s)):
    if s[j:j+3] == 'bob':
        count += 1
print('Number of times bob occurs is:', count)
