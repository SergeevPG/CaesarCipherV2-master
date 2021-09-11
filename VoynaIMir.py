import caesar as caesarcipher
from collections import Counter
import string
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
# From wikipedia: https://ru.wikipedia.org/wiki/%D0%A7%D0%B0%D1%81%D1%82%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C
FrequencyOfLettersOg = list('оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё')
key = 0
key_word = ''
def enter():
    global key
    global key_word
    print("Введите ключ (сдвиг):")
    key = input()
    print("Введите ключ-слово:")
    key_word = input().lower()
    # FOR QUICK TEST
    # key = 16
    # key_word = 'привет'.lower()
    return caesarcipher.test_input_data(key_word, alphabet, key)

def coding(file):
    # , encoding='utf-8'
    with open(f"Documents/WarAndPeaceFull{str(file)}.txt", "rt") as OgWarAndPeace:
        text = OgWarAndPeace.read().lower()
        FrequencyOfLetters1 = Counter("".join([ch for ch in text if ch in alphabet]))
    with open("Documents/CaesarWarAndPeace.txt", "w") as CaesarWarAndPeace:
        CaesarWarAndPeace.write(caesarcipher.caesar_encryption1(key, key_word, text, alphabet, 3))
    list_d2 = list(FrequencyOfLetters1.items())
    list_d2.sort(key=lambda i: i[1])
    list_d2.reverse()
    return list_d2

def decoding():
    CaesarWarAndPeace = open("Documents/CaesarWarAndPeace.txt", "rt")
    text = CaesarWarAndPeace.read()
    FrequencyOfLetters2 = Counter("".join([ch for ch in text if ch in alphabet]))
    list_d = list(FrequencyOfLetters2.items())
    list_d.sort(key=lambda i: i[1])
    list_d.reverse()
    FrequencyOfLetters3 = []
    for i in list_d:
        FrequencyOfLetters3.append(i[0])
    # FrequencyOfLetters3 массив с буквами которые чаще всего встречаются в тексте цезаря
    while len(FrequencyOfLetters3) != len(alphabet):
        FrequencyOfLetters3.append('')
    newtext = []
    for i in text:
        if i in FrequencyOfLettersOg:
            newtext.append(FrequencyOfLettersOg[FrequencyOfLetters3.index(i)])
        else:
            newtext.append(i)
    newtext = "".join(newtext)
    print(f"\n\n{newtext}")
    # print(f"Как часто буквы встречались в шифре цезаря:\t{str(FrequencyOfLetters2)}\tкол-во разных встречающихся букв: {len(FrequencyOfLetters2)}/{len(alphabet)}")
    # print(f"Как часто буквы встречались в оригинале:\t{FrequencyOfLetters1}\tкол-во разных встречающихся букв: {len(FrequencyOfLetters1)}/{len(alphabet)}")
    print("Заменяем буквы из шифра цезаря на:")
    # print(f"{'           '.join([i for i in FrequencyOfLettersOg])}")
    counter=0
    counterRightLetters = 0
    print("+---+------------+---------------+-----+---------+")
    for i in list_d:
        if FrequencyOfLettersOg[counter] == FrequencyOfLetters1[counter][0]:
            counterRightLetters += 1
            print(f"| {counter+1} | \"{i[0]}\" -> \"{FrequencyOfLettersOg[counter]}\" | А ДОЛЖНО БЫТЬ | \"{FrequencyOfLetters1[counter][0]}\" |  ВЕРНО  |")
        else:
            print(f"| {counter+1} | \"{i[0]}\" -> \"{FrequencyOfLettersOg[counter]}\" | А ДОЛЖНО БЫТЬ | \"{FrequencyOfLetters1[counter][0]}\" | НЕВЕРНО |")
        if counter > 9:
            print("+----+------------+---------------+-----+---------+")
        else:
            print("+---+------------+---------------+-----+---------+")
        counter += 1
    print(f"Кол-во верно расшифрованных букв: {counterRightLetters}/{len(alphabet)}")
    CaesarWarAndPeace.close()


if __name__ == '__main__':
    while True:
        print(f"\n:::\t\t\t\t\t\t:::\n1 - Шифр цезаря 1-й вариант\n2 - Шифр цезаря 2-й вариант\n3 - Частотного анализа монограмм\n4 - Выход\nВведите номер задачи:")
        program = input()
        if program.isdigit():
            program = int(program)
            if program == 1:
                print("\nШифр цезаря 1-й вариант\n")
                print("Введите ключ (сдвиг):")
                key = input()
                print("Введите ключ-слово:")
                key_word = input().lower()
                print("Введите фразу, которую хотите зашифровать:")
                word = input().lower()
                # FOR QUICK TEST
                # key = 3
                # key_word = 'ключ'.lower()
                # word = 'привет'.lower()
                if caesarcipher.test_input_data(key_word, alphabet, key):
                    continue
                string1 = caesarcipher.caesar_encryption1(key, key_word, word, alphabet, 1)
            elif program == 2:
                print("\nШифр цезаря 2-й вариант\n")
                print("Введите ключ-слово:")
                key_word = input().lower()
                print("Введите фразу, которую хотите зашифровать:")
                word = input().lower()
                # FOR QUICK TEST
                # key_word = 'ключ'.lower()
                # word = 'привет'.lower()
                if caesarcipher.test_input_data(key_word, alphabet, None):
                    continue
                string2 = caesarcipher.caesar_encryption2(key_word, word, alphabet)
            elif program == 3:
                print("\nчастотного анализа монограмм\n\n1 - Кодирование и Декодирование 1 Тома \"Война и Мир\" (worst decryption)\n2 - Кодирование и Декодирование 2 Тома \"Война и Мир\" (worst decryption)\n3 - Кодирование и Декодирование 3 Тома \"Война и Мир\" (best decryption)\n4 - Кодирование и Декодирование 4 Тома \"Война и Мир\"\n5 - Кодирование и Декодирование 1-4 Тома \"Война и Мир\"")
                program3 = input()
                if program3.isdigit():
                    program3 = int(program3)
                    if program3 == 1:
                        if enter() == 1:
                            continue
                        FrequencyOfLetters1 = coding('1')
                    elif program3 == 2:
                        if enter() == 1:
                            continue
                        FrequencyOfLetters1 = coding('2')
                    elif program3 == 3:
                        if enter() == 1:
                            continue
                        FrequencyOfLetters1 = coding('3')
                    elif program3 == 4:
                        if enter() == 1:
                            continue
                        FrequencyOfLetters1 = coding('4')
                    elif program3 == 5:
                        if enter() == 1:
                            continue
                        FrequencyOfLetters1 = coding('1-4')
                    else:
                        print("::: ERROR #1 :::\nEntered Incorrect Number\n::: ERROR #1 :::")
                        continue
                    decoding()
                else:
                    print("::: ERROR #5 :::\nEntered Not Number\n::: ERROR #5 :::")
                    continue
            elif program == 4:
                print("\nВыход...")
                break
            else:
                print("::: ERROR #1 :::\nEntered Incorrect Number\n::: ERROR #1 :::")
                continue
        else:
            print("::: ERROR #5 :::\nEntered Not Number\n::: ERROR #5 :::")
            continue