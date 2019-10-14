print('the Euler Project problem #2 solving')

#generating Fibonacci sequence list
Fibonacci_sequence = [1,2]
next_term=0
i=0         #firts term
j=1         #second term

while 1:
    next_term = Fibonacci_sequence[i]+Fibonacci_sequence[j]
    if next_term >= 4000000:
        break
    else:
        i+=1
        j+=1
        Fibonacci_sequence.append(next_term)

# finding the sum of even-valued terms in sequence

answer = 0

for term_number in range(0, len(Fibonacci_sequence)):
    if (Fibonacci_sequence[term_number] % 2) == 0:
        answer += Fibonacci_sequence[term_number]
        print(str(Fibonacci_sequence[term_number]), end = ', ')
   
    

print('\n' + str(Fibonacci_sequence) )
print("Answer is " + str(answer))
input()
