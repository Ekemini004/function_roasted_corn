

users_words = ["welcome", "out", "weather", "mobile", "breakfast", "journey"]

longest = len(users_words[0])

for index in range(1, len(users_words)):

    #len(users_words[index]) = 

    if(len(users_words[index]) > longest):
        
           longest = len(users_words[index])

           print(users_words[index])
               

print(longest)

#main function



def find_longest(words):

    longest = len(users_words[0])

    for index in range(1, len(users_words)):

        #len(users_words[index]) = 

        if(len(users_words[index]) > longest):
            
               longest = len(users_words[index])
        
               return longest, users_words[index]





print(find_longest(users_words))

