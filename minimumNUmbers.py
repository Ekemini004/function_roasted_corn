
numbers = [4,67,2,12,6,9]




def minimum_number(number):

    minimum = numbers[0]

    for index in range(1, len(numbers)):

        #len(users_words[index]) = 

        if(numbers[index] < minimum):
            
               minimum = numbers[index]

              
    return minimum          





print(minimum_number(numbers))
