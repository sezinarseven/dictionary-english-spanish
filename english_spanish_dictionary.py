import os
import sys
import time

english=[]
spanish=[]

user_home = os.path.expanduser("~")

english_path = os.path.join(user_home, "english.txt")
spanish_path = os.path.join(user_home, "spanish.txt")

def eng_list():
    i=0
    with open(english_path) as file:
        for line in file: 
            english.append(line.strip())
            i+=1
        return english
    
def span_list():
    i=0
    with open(spanish_path) as file:
        for line in file: 
            spanish.append(line.strip())
            i+=1
        return spanish
    
def new_eng_list():
    with open(english_path, 'w') as file:
        file.write('\n'.join(eng_list()))

def new_span_list():
    with open(spanish_path, 'w') as file:
        file.write('\n'.join(span_list()))

def add_new_words():
    eng=input("Enter the english word: ")
    if eng not in english:
        span=input("Enter the spanish word: ")
        english.append(eng)
        spanish.append(span)
        print(eng + " has been added from the dictionary")
    else:
        print(eng + " is already in dictionary.")

def eng_to_sp():
    word=input("Enter the english word: ")
    if word not in english:
        print("The translation of " + word + " is not found")
    else:
        index=english.index(word)
        print("The spanish word for " + word + " is " + spanish[index])
        
def upt_word():
    word=input("Enter the english word: ")
    new_trans=input("Enter the new translation: ")
    if word not in english:
        print("The translation of " + word + " is not found")
    else:
        index=english.index(word)
        spanish[index]=new_trans
        print("The translation for " + word + " has been updated to " + new_trans)

def del_word():
    word=input("Enter the english word: ")
    index=english.index(word)
    english.remove(word)
    spanish.remove(spanish[index])
    print(word + " has been deleted from the dictionary")

def disp_dict():
    print("The dictionary contains the following words: ")
    for i, j in zip(english, spanish):
        print(i + ": " + j)
        
def quit():
    sys.exit(0)

if __name__ == '__main__':
    eng_list()
    span_list()
    print("Welcome to the Spanish English Translator App:")

    while(True):
        print("-----------------------------------------------\n1. Add new words to dictionary.")
        print("2. Enter English words to see translations.")
        print("3. Update existing words")
        print("4. Delete the existing words.")
        print("5. Display the dictionary.")
        print("6. Quit the program")
        opt = int(input("Enter your choice: "))
        if opt==1:
            add_new_words()
        elif opt==2:
            eng_to_sp()
        elif opt==3:
            upt_word()
        elif opt==4:
            del_word()
        elif opt==5:
            disp_dict()
        elif opt==6:
            quit()
        time.sleep(1.5)
        new_eng_list()
        new_span_list()