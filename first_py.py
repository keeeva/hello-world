# just a quick function that squares the elements of a list


a_random_list = [1, 3, 6, 8]

def sq(l):
  l = [i**2 for i in l]
  return l
  
print(sq(a_random_list))
  
