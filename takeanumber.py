# numbers from 1 - 999
# open at 9:00 - 3:00
# when a student arrives they take a number when attendance is ready he calls the number and so on 
# input n represents the number it is currenlty in 
# other inputs will be 'TAKE', 'SERVE', 'CLOSE' and 'EOF'
# TAKE means a student has taken a number 
# SERVE means a student has been served by the secretary 
# CLOSE means a the secratey has closed for the day
# EOF means end the loop maybe 

# each time close has been printed we have to print out three intergers on a line 
# nof stduents who were late how many remained in line after closure and next number in machine

#current number that needs to be taken 


number = 0
late_student = 0 
line = 0

number = int(input())

while True:
    if 1 <= number <= 999:
        status = input()
        if status == 'TAKE':
            number += 1 
            late_student += 1
            line += 1 
        if status == 'SERVE':
            line -= 1
        elif status =='CLOSE':
            print(late_student ,line ,number)
            line = 0 
            late_student = 0 
        elif status =='EOF':
            break
    else:
        number = 1

                




        


