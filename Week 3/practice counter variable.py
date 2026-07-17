#confusion

#type 1
#outside the loop !
word = "python"
count = 0

for letter in word:
    count = count + 1

print(count)

#the output
# 6




#type 2
#inside the loop

count = 0
for letter in word:
    count = count + 1
    print(count)

#the output
1
2
3

#so how does the for loop run when the print(count) is inside the loop
#the exact same as the outside loop !



#but i am confused ! why do we not start at 0
#we actually do start with 0 !
#count = 0        ← starting point
#loop runs
#counter increases each iteration
#final result printed after loop

#probably the most important thing to know !
#The loop runs once for each element in the container
#for loop confision !
#a for loop runs its body once for each element in the sequence not "once total"
#the important confusion it does not loop = 0
#count = 0 does not cause a loop
#we just use count = 0 as a starting point!