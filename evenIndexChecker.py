
word = "ekemini"



def check_even_index(word):

    #index = 0
    odd_word = ""


    for index in range(0, len(word)):

        if(index % 2 != 0):     

            odd_word += word[index]


    return odd_word
        




print(check_even_index(word))
