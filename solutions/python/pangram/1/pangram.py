def is_pangram(sentence):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sentence_upper = sentence.upper()
    
    for letter in alphabet:
        if letter not in sentence_upper:
            return False
    
    return True