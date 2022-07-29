import random
import os




class open_file():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type , exc_val, traceback):
        self.file.close()


posi1 = 0
posi2 = 0

def decorator1(func):

    def inner(value_check):
        '''check the value is 1 or not'''
        while(True):
            try:
               
                print("\n\n************* Human's turn *****************")
                value_check = int(input("\nHuman: Enter (1) to throw dice: "))

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
     print("\n\n          $ Game Start $")



def take_input2():
    print("\n\n############## Computer's turn ################")


def victory_msg1():
    '''if Human wins it will print the final result and store it in the game_data.txt'''

    print("/////////////// Snake Ladder Game/////////////////")
    print("\n           Human wins\n           Computer lose\n           Game Over!\n")
    print("/////////////// THE END //////////////////////////\n")
    with open_file("humanvscomputer.txt","a") as f:
        f.write("Game Result:\nHuman wins\nComputer lose\n\n")

    exit()

def victory_msg2():
    '''if Computer wins it will print the final result and store it in the game_data.txt'''

    print("/////////////// Snake Ladder Game/////////////////")
    print("\n           Computer wins\n           Human lose\n           Game Over!\n")
    print("/////////////// THE END //////////////////////////\n")
    with open_file("humanvscomputer.txt","a") as f:
        f.write("Game Result:\nComputer wins\nHuman lose\n\n")

    exit()


class SnakeLadder:
    
    with open_file("snakeladder.txt", "r") as f: 
        data = f.readlines()                               

    snake_keys = list(map(int, data[0].split()))   
    snake_values = data[1].split()                         
    snake = dict(zip(snake_keys, snake_values))  

    ladder_keys = list(map(int, data[2].split()))            
    ladder_values = data[3].split()                         
    ladder = dict(zip(ladder_keys, ladder_values))           



        # This will be the actual dictonary after reading from file 
    # snake = { 29:8, 89:68 , 98:79 , 86:63 , 95:62 , 81:30 }
    # ladder = { 4:15, 14:35 , 31:70 , 22:78 , 20:28 ,9:52 }

    
    def __init__(self, posi1, posi2):
       
        self.posi1 = posi1
        self.posi2 = posi2

       

    def move_player(self, pos, player_name, game_limit):
        '''This function will move the player and will call again when user's get 6'''
        dice_player1_flag = True
        dice_player2_flag = True
        get_pos = pos
        dice = random.randint(1, 6)
        end_game = game_limit
        
        if(dice == 6 and player_name == 1):
            while(dice_player1_flag):

                print(f"\nPrevious position:{pos}")
                print
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
                
        elif (dice == 6 and player_name == 2):
            while(dice_player2_flag):
                print(f"\nPrevious position:{pos}")
                print(f"Dice:{dice}")
                pos = pos + 6
                print(f"Current position:{pos}")
                print("Hurry You got 6, take one more turn!")
                if(pos >= end_game):
                    victory_msg2()
        
                self.player_2 = take_input2()                
                dice_player2_flag = False      
                self.posi2 = self.move_player(pos, 2 , end_game)
                return  self.posi2
                
        else:     
            print(f"\nPrevious position:{pos}")  
            print(f"Dice:{dice}")
            get_pos = get_pos + dice
            if get_pos in SnakeLadder.snake:
                print("Snake bitten")
                get_pos = SnakeLadder.snake[get_pos]
                print(f"Now at Position:{get_pos}\n")
            elif get_pos in SnakeLadder.ladder:
                print("Taking Ladder")
                get_pos = SnakeLadder.ladder[get_pos]
                print(f"Now at Position:{get_pos}\n")
            else:
                print(f"Current position:{get_pos}")
            return int(get_pos)
            
    def taking_input(self, game_limit):
     
        '''This Function will take the input from the user and use move_player function'''
        
        while True:
            
            self.player_1 = take_input1(1)
            self.posi1 = self.move_player(self.posi1, 1, game_limit) 
           
            print("                 ********\n")
            if(self.posi1 >= game_limit):
                victory_msg1()
        
            self.player_2 = take_input2()
            
            self.posi2 = self.move_player(self.posi2, 2, game_limit)     
            print("                 ########\n")
            if(self.posi2 >= game_limit):
                victory_msg2()


end_value = 100
os.system('clear')
obj = SnakeLadder(posi1, posi2)
obj.taking_input(end_value)