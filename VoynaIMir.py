import caesar as caesarcipher
from collections import Counter
import string
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
# From wikipedia: https://ru.wikipedia.org/wiki/%D0%A7%D0%B0%D1%81%D1%82%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C
FrequencyOfLettersOg = list('оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё')



if __name__ == '__main__':
    while True:
        print(f"\n:::\t\t\t\t\t\t:::\n1 - Шифр цезаря 1-й вариант\n2 - Шифр цезаря 2-й вариант\n3 - Шифр цезаря 1-й вариант из произведения \"Война и мир\"\n4 - Выход\nВведите номер задачи:")
        program = input()
        if program.isdigit():
            program = int(program)
            if program == 1:
                print("\nШифр цезаря 1-й вариант\n")
                print("Введите ключ (сдвиг):")
                # key = input()
                print("Введите ключ-слово:")
                # key_word = input().lower()
                print("Введите фразу, которую хотите зашифровать:")
                # word = input().lower()
                # FOR QUICK TEST
                key = 3
                key_word = 'ключ'.lower()
                word = 'привет'.lower()
                if caesarcipher.test_input_data(key_word, alphabet, key):
                    continue
                string1 = caesarcipher.caesar_encryption1(key, key_word, word, alphabet)
            elif program == 2:
                print("\nШифр цезаря 2-й вариант\n")
                print("Введите ключ-слово:")
                # key_word = input().lower()
                print("Введите фразу, которую хотите зашифровать:")
                # word = input().lower()
                # FOR QUICK TEST
                key_word = 'ключ'.lower()
                word = 'привет'.lower()
                if caesarcipher.test_input_data(key_word, alphabet, None):
                    continue
                string2 = caesarcipher.caesar_encryption2(key_word, word, alphabet)
            elif program == 3:
                print("\n//////////////////////\n")
                print("Введите ключ (сдвиг):")
                # key = input()
                print("Введите ключ-слово:")
                # key_word = input().lower()
                # FOR QUICK TEST
                key = 16
                key_word = 'привет'.lower()
                if caesarcipher.test_input_data(key_word, alphabet, key):
                    continue
                # , encoding='utf-8'
                with open("Documents/WarAndPeaceFULL1-4.txt", "rt") as OgWarAndPeace:
                    text = OgWarAndPeace.read().lower()
                    s = Counter("".join([ch for ch in text if ch in alphabet]))
                with open("Documents/CaesarWarAndPeace.txt", "w") as CaesarWarAndPeace:
                    CaesarWarAndPeace.write(caesarcipher.caesar_encryption1(key, key_word, text, alphabet))
                CaesarWarAndPeace = open("Documents/CaesarWarAndPeace.txt", "rt")
                text = CaesarWarAndPeace.read()
                FrequencyOfLetters = Counter("".join([ch for ch in text if ch in alphabet]))
                list_d = list(FrequencyOfLetters.items())
                list_d.sort(key=lambda i: i[1])
                list_d.reverse()
                FrequencyOfLetters2 = []
                for i in list_d:
                    FrequencyOfLetters2.append(i[0])
                # FrequencyOfLetters2 массив с буквами которые чаще всего встречаются в тексте цезаря
                while len(FrequencyOfLetters2) != len(alphabet):
                    FrequencyOfLetters2.append('')
                newtext = []
                for i in text:
                    if i in FrequencyOfLettersOg:
                        newtext.append(FrequencyOfLettersOg[FrequencyOfLetters2.index(i)])
                    else:
                        newtext.append(i)
                newtext = "".join(newtext)
                print(f"\nOUR Decoding text:\n{newtext}")
                print("Как часто буквы встречались в оригинале:\t", str(s))
                print("Как часто буквы встречались в шифре цезаря:\t", FrequencyOfLetters)
                print(f"Заменяем буквы из шифра цезаря на:                     {'            '.join([i for i in FrequencyOfLettersOg])}")
                #     print(f"\n--------------------------------------------------------------/"
                #           f"--------------------------------------------------------------------------------------------------\n\n{CaesarWarAndPeace.read()}")
                CaesarWarAndPeace.close()
            elif program == 4:
                print("\nВыход...")
                break
            else:
                print("::: ERROR #1 :::\nEntered Incorrect Number\n::: ERROR #1 :::")
        else:
            print("::: ERROR #5 :::\nEntered Not Number\n::: ERROR #5 :::")