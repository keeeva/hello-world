
#Reverse Word Order

example_string = "I am Julius Ceasar"


def reverse_word_order(s):
    res = example_string.split(" ")
    res = res[::-1]
    return " ".join(res)
    

print(reverse_word_order(example_string))

