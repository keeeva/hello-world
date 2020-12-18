# a little program that counts how many times bob is in a string

s = 'azcbobobegghakl'

count = 0
for letter in range(0, len(s)):
    if s[letter: letter + 3] == 'bob':
        count += 1
print(count)

# same thing just as function count_bob()

def count_bob(st):
    count = 0
    for letter in range(0, len(st)):
        if st[letter: letter + 3] == 'bob':
            count += 1
    return count
    
print(count_bob(s))

