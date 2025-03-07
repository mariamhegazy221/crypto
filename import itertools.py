import itertools
import string

def decrypt_monoalphabetic(ciphertext):
    alphabet = string.ascii_lowercase  
    ciphertext = ciphertext.lower()

    for perm in itertools.permutations(alphabet):
        mapping = str.maketrans("".join(perm), alphabet) 
        decrypted_text = ciphertext.translate(mapping)
        print(f"Trying key: {''.join(perm)} -> {decrypted_text}")

        user_input = input("Is it true?(y/n): ")
        if user_input.lower() == 'y':
            print("successful encryprion method")
            break


ciphertext = "wklv lv d whvw phvvdjh"
decrypt_monoalphabetic(ciphertext)
