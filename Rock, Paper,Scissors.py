#This is a game of Rock Paper Scissors
# After a summer of learning Python

import random  # purpose of random is for computers input


        
def main():

 options=["rock" , "paper", "scissors" ] # rock: 0, paper: 1 , scissors: 2
 
 user_wins=0

 computer_wins=0

 print('\nHello this is a simple game of Rock Paper Scissors')

 count=0     # the number of each round of rock, paper, scissors

 round=[]     # a list that contains the strings of whomever won
 
 round_result=str # who won for each round

 play=[]   # the list that contains the list of choices of each round 

 Round_Outcome={} # a dictionary that contains a keyword 'round_number' and a value 'i' look below
 

 while True:

    
    user_choice=input("\nChoose\n\tRock\n\tPaper\n\tScissors\n\tor Q to quit: ").lower()          # this will convert any string the user types to lower case 
                                                                                                     # this helps with putting less condiitonals for the 
    
    
    if user_choice =='q': # if user wants to quit rock paper scissors game 

        if count==0:     # if the user never played a round of the game 
            
            print("\nNo plays were given by User")
            
            print("Game is shutting down")

            break

        else:
         print("\nResults of game") #\n moves the text to the next line
        
         print(f'\tThe number of games was {count}') #\t tabs the text 
        
         print(f'\tThe number of games you won was {user_wins}')

         print(f'\tThe number of games the computer was {computer_wins}')
        
         print("\nOutcome for every round ")
           


         round_number=1    # round_numbers is a variable that is equal to the round number

     
         print(f"\t{'Round':<5}{'Player Chose': ^17}{'Computer Chose':^17}{'Outcome':^20}") # Header 

         
         for i in range(count):       # this for loop is used to initialize each part of the dictionary 
                                      # where flag repesents the round number and i represents the indexed number for who won
                                      # round_number is the keyword and value is i 



          # note this is the same as Round_Outcome={'round_number':round[i]}
          
          Round_Outcome[round_number]=round[i]   



          # note that play is a list that contains a list(a sublist of playlist)

          
        

          print(f"\t{round_number:<5}{play[i][0]:^17}{play[i][1]:^17}{Round_Outcome[round_number]:^20}")  # outputs results 
          
          round_number+=1

         
         print("\nGame is shutting down")
        
        
         break 
  
                                                          
    
    
    
                                                          # how to check it is equal to more than one thing 
    if user_choice not in options:                        # checks if user input is in this list then. User has to put rock, paper or scissors 
        print("Incorrect Input")                          # note this is a good way to avoid using a lot of conditionals 
        continue                                          # continues until user types in correct input
        
      

      
    print("\nYou chose" , user_choice +'.')  
    
    
                                           
    random_chosen = random.randint(0,2)    # generates a random number between 0 to 2 
                                           # rock: 0, paper: 1 , scissors: 2
                                           
    computer_choice=options[random_chosen]         # computer choice 

    
    
    print("Computer chose" , computer_choice +'.')

    playlist=[user_choice,computer_choice]       # creates a list that contains both users choice and computers choice
                                                 # then it is appended to the play list  
                                                 # note that playlist is a sublist to play
    
   
    play.append(playlist) 

   # The below code appends the results from each round 
   # round.append(round_result)
    
    
    if user_choice == "rock" and computer_choice == "scissors":
        
        print("You won!")

        
        print("One point for user")
       
        user_wins+=1
        
        count+=1

        round_result='You Won'

        round.append(round_result)
        
        continue
    
    elif user_choice == "paper" and computer_choice == "rock":
        
        print("You Won!")
        
        print("One point for user")
        
        user_wins+=1
        
        count+=1

        round_result='You Won'
        
        round.append(round_result)
        
        continue
    
    elif user_choice == "scissors" and computer_choice == "paper":
        
        print("You Won!")
        
        print("One point for user")
        
        user_wins+=1
        
        count+=1

        round_result='You Won'
        
        round.append(round_result)
        
        continue
    
    elif user_choice==computer_choice:
        
        print("It is a Tie!") 
        
        count+=1

        round_result='Tie'
        
        round.append(round_result)
        
        continue
    
    else:                                   # We can think of the complement, we already satisifed all preivous conditions for if we win 
        
        print("Computer Won!")              # simply taking the complement ( as in else) elinimates the need for more conditionals 
        
        print("One point for the computer")
        
        computer_wins+=1
        
        count+=1

        round_result='Computer Won '
        
        round.append(round_result)
        
        continue
    

if __name__ == "__main__":
    main()
