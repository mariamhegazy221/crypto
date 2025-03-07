import numpy as np

def generate_playfair_matrix(keyword):
    keyword = keyword.lower().replace("j", "i")  
    seen = set()
    matrix = []

    for char in keyword:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    alphabet = "abcdefghiklmnopqrstuvwxyz"  
    for char in alphabet:
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    return np.array(matrix).reshape(5, 5)

def find_position(matrix, letter):
    index = np.where(matrix == letter)
    return index[0][0], index[1][0]

def process_digraphs(text):
    text = text.lower().replace("j", "i")  
    processed = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'x'

        if a == b:  
            processed.append(a + 'x')  
            i += 1  
        else:
            processed.append(a + b)  
            i += 2  
    return processed

def playfair_encrypt(text, matrix):
    text_pairs = process_digraphs(text)
    encrypted_text = ""

    for a, b in text_pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  
            encrypted_text += matrix[row1, (col1 + 1) % 5] + matrix[row2, (col2 + 1) % 5]
        elif col1 == col2:  
            encrypted_text += matrix[(row1 + 1) % 5, col1] + matrix[(row2 + 1) % 5, col2]
        else:  
            encrypted_text += matrix[row1, col2] + matrix[row2, col1]

    return encrypted_text.upper()

def playfair_decrypt(text, matrix):
    text_pairs = process_digraphs(text)
    decrypted_text = ""

    for a, b in text_pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  
            decrypted_text += matrix[row1, (col1 - 1) % 5] + matrix[row2, (col2 - 1) % 5]
        elif col1 == col2:  
            decrypted_text += matrix[(row1 - 1) % 5, col1] + matrix[(row2 - 1) % 5, col2]
        else:  
            decrypted_text += matrix[row1, col2] + matrix[row2, col1]

    return decrypted_text.lower()

keyword = input("Enter the key:").strip()
matrix = generate_playfair_matrix(keyword)

print("\n Playfair:")
print(matrix)

while True:
    choice = input("\n choose process (1-encryptin 2-decryption 3-exit ").strip()
    
    if choice == "1":
        plaintext = input("Enter text to encryption: ").replace(" ", "").lower()
        encrypted_text = playfair_encrypt(plaintext, matrix)
        print(f" encrypted text: {encrypted_text}")
    
    elif choice == "2":
        ciphertext = input("Enter text to decryption: ").replace(" ", "").lower()
        decrypted_text = playfair_decrypt(ciphertext, matrix)
        print(f"decrypted text: {decrypted_text}")
    
    elif choice == "3":
        break

    else:
        print("Invalid option, Try again")
