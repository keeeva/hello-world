# hello-world
#python basics/ quick function that squares list elements

a_random_list = [1, 3, 6, 8]

def sq(l):
  l = [i**2 for i in l]
  return l
  
  print(sq(a_random_list))
  
