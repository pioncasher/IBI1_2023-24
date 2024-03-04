# What does this piece of code do?
# Answer: Generate random interger number between  1 to 10 for 100 times and print their sum.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0    
total_random_number=0    # set the initial value of progress and total_random_number
while progress<100:
	progress+=1  #  use while loop to make the following codes run 100 times
	n = randint(1,10) # generate random numbers  between  1 to 10
	total_random_number = total_random_number+n 

print(total_random_number) # print total_random_number