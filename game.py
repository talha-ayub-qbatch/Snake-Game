import random

posi1 = 0
posi2 = 0


                

def decorator1(func):

    def inner(value_check):
        '''check the value is 1 or not'''
        while(True):
            try:
               
                print("\n\n************* Player 1's turn *****************")
                value_check = int(input("\nPlayer 1: Enter (1) to throw dice: "))

                if value_check != 1:
                    raise Exception()
                else:
                    break
            except Exception:
                print("Please Enter the correct number (1)")
        return func
    return inner

@decorator1
def take_input1():
    pass


def decorator2(func):

    def inner(value_check):
        '''check the value is 2 or not'''
        while(True):
            try:
                print("\n\n############## Player 2's turn ################")
                value_check = int(input("\nPlayer 2: Enter (2) to throw dice: "))
                
                if value_check != 2:
                    raise Exception()
                else:
                    break
            except Exception:
                print("Please Enter the correct number(2)")
        return func
    return inner

@decorator2
def take_input2():
    pass

def victory_msg1():
    print("/////////////// Snake Ladder Game/////////////////")
    print("\n           Player:1 wins\n           Player:2 lose\n           Game Over!\n")
    print("/////////////// THE END //////////////////////////\n")

def victory_msg2():
    print("/////////////// Snake Ladder Game/////////////////")
    print("\n           Player:2 wins\n           Player:1 lose\n           Game Over!\n")
    print("/////////////// THE END //////////////////////////\n")
    exit()

class Snake_Ladder:

    snake = { 29:8, 89:68 , 98:79 , 86:63 }
    ladder = { 4:15, 14:35 , 31:70 , 22:78 }
    
    def __init__(self, posi1, posi2):
        print("\n\n          $ Game Start $")
        self.posi1 = posi1
        self.posi2 = posi2

       

    def move_player(self, pos, player_name, game_limit):
        '''This function will move the player and will call again when user's get 6'''
        dice_player1_flag = True
        dice_player2_flag = True
        get_pos = pos
        dice = random.randint(1,6)
        end_game = game_limit
        
        if(dice == 6 and player_name == 1):
            while(dice_player1_flag):
                print(f"\nPrevious position:{pos}")
                
                
                print(f"Dice:{dice}")
                pos = pos + 6
                print(f"Current position:{pos}")
                
                
                print("Hurry You got 6, take one more turn!")
                if(pos >= end_game):
                    victory_msg1()
                    
                
                
                self.player_1 = take_input1(1)
                dice_player1_flag = False
                self.posi1 = self.move_player(pos, 1, end_game)
                return self.posi1
                
        elif (dice ==6 and player_name == 2):
            while(dice_player2_flag):
                print(f"\nPrevious position:{pos}")
                
                print(f"Dice:{dice}")
                pos = pos + 6
                print(f"Current position:{pos}")
                print("Hurry You got 6, take one more turn!")
                if(pos >= end_game):
                    victory_msg2()
                    
               
                self.player_2 = take_input2(2)                
                dice_player2_flag = False      
                self.posi2 = self.move_player(pos, 2 , end_game)
                return  self.posi2
                
        else:     
            print(f"\nPrevious position:{pos}")  
            print(f"Dice:{dice}")
            get_pos = get_pos + dice
           
            if get_pos in Snake_Ladder.snake:
                print("Snake bitten")
                get_pos = Snake_Ladder.snake[get_pos]
                print(f"Now at Position:{get_pos}\n")
            elif get_pos in Snake_Ladder.ladder:
                print("Taking Ladder")
                get_pos = Snake_Ladder.ladder[get_pos]
                print(f"Now at Position:{get_pos}\n")
            else:
                print(f"Current position:{get_pos}")
            return get_pos
            
       
  
    def taking_input(self,game_limit):
        '''This Function will take the input from the user and use move_player function'''
        while True:
            

            self.player_1 = take_input1(1)
            
            self.posi1 = self.move_player(self.posi1, 1, game_limit) 
            print("                 ********\n")
            if(self.posi1 >= game_limit):
                victory_msg1()
                
            
            self.player_2 = take_input2(2)
            
            self.posi2 = self.move_player(self.posi2, 2, game_limit)     
            print("                 ########\n")
            if(self.posi2 >= game_limit):
                victory_msg2()
                
   
def log_file():
    file = open("game_data.txt", "a")
    file.write("*************Player 1*****************")
    file.close

end_value = 15
log_file()
obj = Snake_Ladder(posi1, posi2)
obj.taking_input(end_value)