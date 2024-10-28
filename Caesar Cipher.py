# القاموس بتاع الحروف و الارقام بتاعتها
dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
        'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
cipher = "" 
key = 3   
plain_text = input("Enter text to encrypt: ").upper()  
for chr in plain_text:
    if chr in dict:
    
        shifted_value = (dict[chr] + key) % 26
        for letter, value in dict.items():
            if value == shifted_value:
                cipher += letter  
                break
    else:
        cipher += chr
print("Ciphered Text:", cipher)  
plain_text = "" 
key = 3   
chipher_text = input("Enter text to decrypt: ").upper()  
for chr in chipher_text:
    if chr in dict:
        shifted_value = (dict[chr]-key) % 26
        for letter, value in dict.items():
            if value == shifted_value:
                plain_text += letter  
                break
    else:
        plain_text += chr
print("plian Text:", plain_text)  



