print('the Euler Project problem #1 solving')

current_number = 1
correct_numbers_list = []
answer = 0

while current_number < 1000:                                
    if (current_number % 3) == 0:                       #checking this number multiplies of 3
      
        correct_numbers_list.append(current_number)

    elif (current_number % 5) == 0:                     #checking this number multiplies of 5
      
        correct_numbers_list.append(current_number)
    
    current_number += 1
else:
    pass
    #print(correct_numbers_list)                         #printing list of numbers mutiplies of 3 and 5
for counter in correct_numbers_list:
    answer += counter                                   #finding sum of list of numbers
print("Answer is " + str(answer))
    

input()
