import sys

def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

game_field = [[' ','1','2','3', ],[1 ,'_','_','_'],[2,'_','_','_'],[3,'_','_','_']] 
turns = 0
arr_size = len(game_field)
player1_win = 0

while turns <= 8:
    
    for item in game_field:
        print(*item, sep ='  ')
        print()
    
    print('First player, it`s your turn.Your symbol is X')
    print("Type row number")
    number1 = sys.stdin.readline() 
    print("Type column number")
    number2 = sys.stdin.readline()
    
    """ input control first player"""
    
    input_control = 0
    while input_control == False:
        while input_control == False:
            if( isint(number1) and  ( int(float(number1)) == 1 or  int(float(number1)) == 2 or  int(float(number1)) == 3) ):
                input_control = True
                number1 = int(float(number1))
            else:
                print("First player type correct row number(1, 2 or 3)")
                number1 = sys.stdin.readline()
    
        input_control = 0
        while input_control == False:
            if( isint(number2) and  ( int(float(number2)) == 1 or  int(float(number2)) == 2 or  int(float(number2)) == 3) ):
                input_control = True
                number2 = int(float(number2))
            else:
                print("First player type correct column number(1, 2 or 3)")
                number2 = sys.stdin.readline()
    
        if(game_field[number1][number2] == '_'):
            game_field[number1][number2] = 'X'
            input_control= True
        else:
            number1 = 0
            number2 = 0
            print('First player, this position already has a symbol. Set empty position in game field.Type numbers again. ')
            input_control = 0
            
            for item in game_field:
                print(*item, sep ='  ')
                print()
            print("Type row number")
            number1 = sys.stdin.readline() 
            print("Type column number")
            number2 = sys.stdin.readline()

    
    turns +=1

    """ win control first player"""

    row_win = 0
    column_win = 0
    cross_1 = 0
    cross_2 = 0
    a = 0
    b = 0
    
    """ row,cross win control """
    
    while a < arr_size:
        row_win =0
        for item in game_field[b]:
            if(item == 'X' ):
                row_win += 1
            if(row_win == 3):
                a=10
        
        if(game_field[b][b] == "X"):
            cross_1 += 1
            if(cross_1 == 3):
                a = 10    
        if(b >= 1):       
            if(game_field[b][4 - b] == "X"):
                cross_2 += 1
                if(cross_2 == 3):
                    a = 10    

        b += 1
        a +=1
    """ column win control """

    a = 1
    b =1
    while b < 4:
        a =1
        column_win = 0
        while a <=3:
            
            for item in game_field[a][b]:           
                a+=1
                if(item == 'X' ):
                    column_win += 1
        if(column_win == 3):
            break  
        b +=1  

    if(row_win == 3 or column_win == 3 or cross_1 == 3 or cross_2 == 3 ):
        for item in game_field:
            print(*item, sep ='  ')
            print()
        print('The first player wins!')
        turns = 10
    
    
    if turns < 8:
        for item in game_field:
            print(*item, sep ='  ')
            print()
        
        print('Second player, it`s your turn.Your symbol is O')
        print("Type row number")
        number1 = sys.stdin.readline()      
        print("Type column number")
        number2 = sys.stdin.readline()
        
        """ input control second player"""

        input_control = 0
        while input_control == False:
            while input_control == False:
                if( isint(number1) and  ( int(float(number1)) == 1 or  int(float(number1)) == 2 or  int(float(number1)) == 3) ):
                    input_control = True
                    number1 = int(float(number1))
                else:
                    print("Second player type correct row number(1, 2 or 3)")
                    number1 = sys.stdin.readline()
        
            input_control = 0
            while input_control == False:
                if( isint(number2) and  ( int(float(number2)) == 1 or  int(float(number2)) == 2 or  int(float(number2)) == 3) ):
                    input_control = True
                    number2 = int(float(number2))
                else:
                    print("Second player type correct column number(1, 2 or 3)")
                    number2 = sys.stdin.readline()
        
            if(game_field[number1][number2] == '_'):
                game_field[number1][number2] = 'O'
                input_control= True
            else:
                number1 = 0
                number2 = 0
                print('Second player, this position already has a symbol. Set empty position in game field.Type numbers again. ')
                input_control = 0
                
                for item in game_field:
                    print(*item, sep ='  ')
                    print()
                print("Type row number")
                number1 = sys.stdin.readline() 
                print("Type column number")
                number2 = sys.stdin.readline()
        """ win control second player"""

        row_win = 0
        column_win = 0
        cross_1 = 0
        cross_2 = 0
        a = 0
        b = 0
        
        """ row,cross win control """
        
        while a < arr_size:
            row_win =0
            for item in game_field[b]:
                if(item == 'O' ):
                    row_win += 1
                if(row_win == 3):
                    a=10
            
            if(game_field[b][b] == 'O'):
                cross_1 += 1
                if(cross_1 == 3):
                    a = 10    
            if(b >= 1):       
                if(game_field[b][4 - b] == "O"):
                    cross_2 += 1
                    if(cross_2 == 3):
                        a = 10    

            b += 1
            a +=1
        """ column win control """

        a = 1
        b =1
        while b < 4:
            a =1
            column_win = 0
            while a <=3:
                
                for item in game_field[a][b]:           
                    a+=1
                    if(item == 'O' ):
                        column_win += 1
            if(column_win == 3):
                break  
            b +=1  

        if(row_win == 3 or column_win == 3 or cross_1 == 3 or cross_2 == 3 ):
            for item in game_field:
                print(*item, sep ='  ')
                print()
            print('The second player wins!')
            turns = 10    
            
        turns +=1  
     
    for item in game_field:
        print(*item, sep ='  ')
        print()

