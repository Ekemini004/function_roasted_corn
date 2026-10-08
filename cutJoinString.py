

def cut_join (word):

    if( len(word) < 2):

        result = ""

    else :

        firstSet = ""
        secondSet = ""
        index = 0
        while(index <= len(word)-1):
            if(index < 2):

                firstSet += word[index]


            elif(index >= len(word)-2):

                   secondSet += word[index] 

            index += 1


        result = firstSet + secondSet
        return result  
          
                


print(cut_join ("semicolon"))
