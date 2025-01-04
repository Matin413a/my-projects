import random
names=['matin','Bulat','Selin','Bulat','Dilara','Lilya','Jelal jan','Regina','Emiliya','Ahmad','Alperen','Aziz','Madina','Ceren',]
chosen_name= random.choice(names)
print(chosen_name)
print('welcome to the game!')

def count_letters(name1,name2):
    return len(set(name1.lower()) & set(name2.lower()))


while True:
    try:
        enterName=str(input('\n guess a name from your class mates: ')).lower()

        #if enterName.lower() not in names:
            #print("\n dude this not your classmate") 
        
        if enterName.lower() == chosen_name.lower():
            print('well done. you guessed right!')
            break
        else:
            common_letters = count_letters(enterName.lower(), chosen_name.lower())  
            print(f"\n Wrong guess but you have {common_letters} letter as common letter(s).  Try again!")
    
    except ValueError:
        print("there is no number in your friends name!!")