import random

def roll():
    left_num=random.randint(1,6)
    right_num=random.randint(1,6)
    return (left_num,right_num)

result= roll()
print("HelloWorld!")
print(result)
