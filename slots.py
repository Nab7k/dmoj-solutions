# slots machine game 
# machine 1 pays 30 quarters every 35 go
# machine 2 pays 60 quarters every 100 go
# machine 3 pays 9 quarters every 10 go
#

quarters = int(input())

first = int(input())
second = int(input())
third = int(input())

plays = 0

while quarters >= 1:

    machine = plays % 3
    quarters = quarters - 1 

    if machine == 0:
        first = first + 1
        if first % 35 == 0:
            quarters = quarters + 35
    
    elif machine == 1:
        second = second + 1 
        if second % 100 == 0:
            quarters = quarters + 100

    elif machine == 2:
        third = third + 1
        if third % 10 == 0:
            quarters = quarters + 9
    
    plays = plays + 1

print('You have played',plays,'add more money to play again')