numbers = [4,67,2,12,6,9]




def maximum_number(number):

    maximum = numbers[0]

    for index in range(1, len(numbers)):

        #len(users_words[index]) = 

        if(numbers[index] > maximum):
            
               maximum = numbers[index]

              
    return maximum          





print(maximum_number(numbers))
