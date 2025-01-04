import random 
lists=[]
positive=[]
negative=[]
zero = []
while len(lists) <100 :
    numbers= random.randint(-100, 100)
    lists.append(numbers)

for num in lists:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
        
    else:
        zero.append(num)
print (len(positive))
print (len(negative))
print (len(zero))