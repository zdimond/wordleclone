def checker(guess,target_word):
    target_array = list(target_word)
    guess_array = list(guess)
    
    checked_word_array = []

    for l in guess_array:
        if l == target_array[guess_array.index(l)]:
            checked_word_array.append(l)
        elif l in target_array:
            checked_word_array.append("*")
        else:
            checked_word_array.append("-")
    
    return "".join(checked_word_array)
