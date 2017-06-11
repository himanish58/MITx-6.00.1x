# Write a program that counts up the number of vowels contained in a string

s = input('Enter the string ..\n')
count = 0
for i in s:
    if (i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o'
    or i == 'O' or i == 'u' or i == 'U'):
        count += 1
print('Number of vowels:', count)
