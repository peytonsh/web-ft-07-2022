import pickle


try: 
    with open('phonebook.pickle', 'rb') as fh:
        phonebook = pickle.load(fh)

except:
    phonebook = {'pey' : 1234}











def look_up ():
    print("look up entry?"   )
    response = input()
    print(phonebook.get[response])
   
   
            
def set_up ():
    print("name of person you want to add?"   )
    personName = input()
    print("what is your phone numbr?"  )
    personNumber = input()
    phonebook[personName] = personNumber
    print(f'entry stored for {personName}')
    

def delete_entry ():
    print("who do you want to delete?  ")
    personName = input()
    print(f'delete entry for {personName}')
    del phonebook[personName] 
    
    
def list_all():
    for x in phonebook:
        print(f"found entry for {x}: {phonebook[x]}")
        
        
def quit():
  with open('phonebook.pickle', 'wb') as fh:
    pickle.dump(phonebook, fh)
  print('GoodBye!')

    
    
while True: 
    selector = """
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    What do you want to do (1-5)?
    """
    print(selector)
    answer = int(input())
    
    if answer == 1:
        look_up()
    
    elif answer == 2:
        set_up()
        
    elif answer == 3: 
        delete_entry()
        
    elif answer == 4:
        list_all()
        
    elif answer == 5:
        quit()
        
        break