#guess number game 
import random
print('hello welcome to the guess number game! ')
print('\nplease guess your number between 1 to 1000, good luck!')

the_number= random.randint(1,1000)

print(the_number)

while True:
        try:
            player_number=int(input('guess a number: '))

            if player_number > 1000 or player_number < 1:
                print("\nsorry choose for 1 to 1000")
            

            elif player_number == the_number:
                 print('wow you guessed right!')

            else:
                 print('your guess was wrong')
                 if (the_number - player_number) > 100:
                      print(f'\n{player_number} was too low try again')
                 elif (the_number - player_number) < -100:
                      print(f"\n{player_number} was too high try again")
                 elif  0 < (the_number - player_number) < 100:
                      print ("\n you are close the number is higher")
                      
                 elif  0 > (the_number - player_number) > -100:
                      print ("\n you are close the number is lower")

        except ValueError:
             print('\nplease enter a number not a word: ')