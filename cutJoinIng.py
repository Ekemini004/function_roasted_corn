

def cut_join_ing (word):

    if( len(word) < 3):

        pass

    else :

        index = 0
        LastSet = ""

        while(index <= len(word)-1):
            
            if(index >= len(word)-3):

                LastSet += word[index]
                
            index += 1

        if(LastSet == "ing"):
            word += "ly"
        else:
            word += "ing"     


    return word        
            
              
                


print(cut_join_ing("quieting"))
