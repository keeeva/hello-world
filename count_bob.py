s = 'azcbobobegghakl'

count = 0
for letter in range(0, len(s)):
    if s[letter: letter + 3] == 'bob':
        count += 1
print(count)






