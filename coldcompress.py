# every character you send from your phone its charges you 
# you tend to send in symbols
# for each symbol write down the numbers of time it appears following the symbol]
# output consits of the number of symbols then its actual symbol from each line 

n = int(input())

charc = input()

i = 0
count = 0 

while i < len(charc):
    if charc[i] == charc[i + 1]:
        count += 1 
        print(count)
    else:
        continue



