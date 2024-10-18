import random
from hangmanword import words
import string

def get_valid_word(words  ):
    word=random.choice(words)#it randomly chooses something form the list 
    while '-' in word or'-'in word:
            word=random.choice(words)
    return word.upper()
    
def hangman():
    word=get_valid_word(words)
    words_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    lives=5

    #getting user input 
    while len(words_letters)>0 and lives>0:
        
        # letter used 
        print("You have",lives,"You have used these letter ",''.join(used_letters))

        #what current word is (ie W_RD)
        word_list=[letter if letter in used_letters else '-'for letter in word]
        print("Current word :","".join(word_list))

        user_letter=input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in words_letters:
                words_letters.remove(user_letter)

            else:
                 lives=lives-1
                 print("Letter is not in word")
        
        elif user_letter in used_letters:
            print("You have already used that character .Please try again")

        else:
            print("invalid Character ")
    if lives ==0:
        print("You died,soory try again ")
    else:
     print("You gussed th word",words,"!!")






hangman()


user_input=input("type a letter:  ")
print(user_input)