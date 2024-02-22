    import hashlib  
    print("# # # # # #  Password Hacking # # # # # #")  
              
    password_found = 0                                       
       
    inputinput_hashed = input(" Please enter the hashed password: ")  
       
    password_document = input(" \n Please enter the passwords file name including its path (root / home/): ")  
        
    try:  
        password_file = open(password_document, 'r')               
    except:  
        print("Error: ")  
        print(password_document, "is not found.\n Please enter the path of file correctly.")  
        quit()  
       
    for word in password_file:  
        encoding_word = word.encode('utf-8')   
        hashed_word = hashlib.md5(encoding_word.strip())     
        digesting = hashed_word.hexdigest()          
            
        if digesting == input_hashed:  
            print ("Password found.\n The required password is: ", word)    
            password_found = 1  
            break  
       
    if not password_found:  
        print(" The password is not found in the ", password_document, "file")    
        print('\n')  
    print(" # # # # # # Thank you # # # # # # ")  
