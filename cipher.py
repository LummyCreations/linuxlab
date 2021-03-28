#Ceaser Cipher
def cipher():
    print ("Welcome to the encoding system")
    shift = int(input("What is your shift position: "))
    print("Enter text to be ciphered")
    text = input("")
    ciphered = ""

    for letter in text:
        if letter.isupper():
            #find the position
            letter_unicode = ord(letter) - ord("A")

            #perform the shift cipher and covert to new letter
            letter_cipher = (letter_unicode + shift) % 26
            shifted_letter = letter_cipher + ord("A")
            converted = chr(shifted_letter)

            #append encrypted
            ciphered = ciphered + converted
            
        elif letter.islower():
            convertLetter = letter.upper() 
            letter_unicode = ord(convertLetter) - ord("A")

            letter_cipher = (letter_unicode + shift) % 26
            shifted_letter = letter_cipher + ord("A")
            converted = chr(shifted_letter)

            ciphered = ciphered + converted
            
        else: 
            #return the rest if neither alphabet or number
            ciphered +=  letter
            
    print("Encrypted Message is:")      
    print (ciphered)
            

cipher()