from collections import Counter

english_freq_order = "etaoinshrdlcumwfgypbvkjxqz"

def frequency_analysis_decrypt(ciphertext):
    ciphertext = ciphertext.lower()
    ciphertext = ''.join(filter(str.isalpha, ciphertext)) 

    letter_counts = Counter(ciphertext)
    sorted_cipher_letters = [pair[0] for pair in letter_counts.most_common()]  

   
    decrypt_mapping = {sorted_cipher_letters[i]: english_freq_order[i] for i in range(len(sorted_cipher_letters))}

    decrypted_text = ''.join(decrypt_mapping.get(char, char) for char in ciphertext)

    return decrypted_text

ciphertext = "wklv lv d whvw phvvdjh"

decrypted_text = frequency_analysis_decrypt(ciphertext)
print("possible loss text:", decrypted_text)
