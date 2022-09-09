# when a person 'p' gets the disease it infects exaclty 'r' people 
# they are only infected the very next day
# No on is infected more than once 
# 'n' is the number of people infected at day 0 

p = int(input())
n = int(input())
r = int(input())

inf_people = n
inf_last_day = n
time = 0 

while inf_people <= p:
    time += 1
    inf_people += inf_last_day * r
    inf_last_day *= r

print(time)
