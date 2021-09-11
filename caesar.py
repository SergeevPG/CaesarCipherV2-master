def test_input_data(key_word, alphabet, key):
    if len(key_word) != len(set(key_word)):
        print("::: ERROR #2 :::\nLetters Into Key Word Must Be Unique\n::: ERROR #2 :::")
        return 1
    elif len(key_word) < 2 or len(key_word) > len(alphabet):
        print(f"::: ERROR #3 :::\nLength Key Word Must Be [2,{len(alphabet)}]\n::: ERROR #3 :::")
        return 1
    elif key is not None:
        if not str(key).isdigit():
            print(f"::: ERROR #7 :::\nKey Must Must Consist From Digits And Be[1..{len(alphabet)-len(key_word)}]\n::: ERROR #7 :::")
            return 1
        elif int(key) < 1 or len(alphabet)-len(key_word) < int(key):
            print(f"::: ERROR #6 :::\nKey Must Be [1..{len(alphabet) - len(key_word)}]\n::: ERROR #6 :::")
            return 1
    else:
        for i in key_word:
            if i not in alphabet:
                print("::: ERROR #4 :::\nKey Word Must Consist From RU Alphabet\n::: ERROR #4 :::")
                return 1
    return 0

def caesar_encryption1(key, key_word, encrypt_message, alphabet):
    key = int(key)
    key_word = list(key_word)
    encrypt_message = list(encrypt_message)
    new_word = []
    new_alphabet = alphabet.copy()
    for i in key_word:
        new_alphabet.pop(new_alphabet.index(i))
    # сдвиг массива и вставка ключ-слова
    new_alphabet = new_alphabet[-key:] + key_word + new_alphabet[:-key]
    # print(f'\n::: Caesar Encryption v1.0 :::\n\nOriginal Alphabet:\t{alphabet}\nNew Alphabet:\t\t{new_alphabet}\nKey:\t\t{key}\nKey Word:\t{"".join(key_word)}')
    # print(f"\nMessage:\t\t\t\n\"{"".join(encrypt_message)}\"")
    for i in encrypt_message:
        if i in new_alphabet:
            new_word.append(new_alphabet[alphabet.index(i)])
        else:
            new_word.append(i)
    new_word = "".join(new_word)
    # print(f'Encrypted message:\n\"{"".join(new_word)}\"\n\n::: Caesar Encryption v1.0 :::')
    return "".join(new_word)

def caesar_encryption2(key_word, encrypt_message, alphabet):
    key_word = list(key_word)
    encrypt_message = list(encrypt_message)
    new_alphabet = []
    message = []
    counter = 0
    for i in range(len(alphabet)):
        new_alphabet.append(key_word[counter])
        counter += 1
        if counter == len(key_word):
            counter = 0
    print(f'\n::: Caesar Encryption v2.0 :::\n\nOriginal Alphabet:\t{alphabet}\nNew Alphabet:\t\t{new_alphabet}\nKey Word:\t{"".join(key_word)}\nMessage:\t\t\t\n\"{"".join(encrypt_message)}\"')
    for i in encrypt_message:
        if i in alphabet:
            og_index = alphabet.index(i)
            new_letter = new_alphabet[og_index]
            new_index = alphabet.index(new_letter)
            message.append(alphabet[(og_index + new_index) % len(alphabet)])
        else:
            message.append(i)
    print(f'Encrypted message:\n\"{"".join(message)}\"\n\n::: Caesar Encryption v2.0 :::')
    return "".join(message)