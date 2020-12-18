# just a quick function that squares the elements of a list using list comprehension

a_random_list = [1, 3, 6, 8]

def sq(l):
  l = [i**2 for i in l]
  return l
  
print(sq(a_random_list)) # [1, 9, 36, 64]

# the same idea without using list comprehension 

def sq2(l):
  l2 = []
  for i in l:
    l2.append(i**2)
  return l2

print(sq2(a_random_list)) # [1, 9, 36, 64]
