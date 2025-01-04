#1) put vegetables ,etc(value)
#2)get somthing to put in my fridge
#3)show what is inside of my fridge
#4)get ice cubes
#5)get the time and date

import datetime

print('hello how may I help you?')

fridge=["ice cube","cola","eggs",'water']

while True:
    print('''
    1-to put somthing inside
    2-take out somthing
    3-what do I have 
    4-tell me time
    5-exit 
    ''')

    menu=int(input("chose an option: "))

    if menu == 1:
        products = input("write the name of your product: ")
        
        for product in products.split(" "):
            product = product.strip()
            if product:
                fridge.append(product)
                print(f"\n{product} was added to fridge")


    elif menu == 2:
        product_to_eat = input("\nwrite the name of your product: ")
        if product_to_eat in fridge:
            fridge.remove(product_to_eat)
            print(f"{product_to_eat} picked up from the fridge")
        else:
            print('we dont have this Item !')
        
        

    elif menu == 3:
        print(fridge)
    
    elif menu == 4:
        now = datetime.datetime.now()
        print("time: ", now.strftime("%Y-%m-%d %H:%M:%S"))

    if menu == 5:
        break
    

