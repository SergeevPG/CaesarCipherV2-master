import caesar as caesarcipher
from collections import Counter
import re
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
# From wikipedia: https://ru.wikipedia.org/wiki/%D0%A7%D0%B0%D1%81%D1%82%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C
FrequencyOfLettersOg = list('оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё')
key = 0
key_word = ''


def coding(file):
    # read original text WarAndPeace
    OgWarAndPeace = open(f"Documents/WarAndPeaceFull{str(file)}.txt", "rt")
    textOg = OgWarAndPeace.read().lower()

    FrequencyOfLetters1 = Counter("".join([ch for ch in textOg if ch in alphabet]))
    print(f"Частота встречи букв в оригинале:\t\t{len(FrequencyOfLetters1)} {FrequencyOfLetters1}")
    list_d = list(FrequencyOfLetters1.items())
    list_d.sort(key=lambda i: i[1])
    list_d.reverse()
    FrequencyOfLetters1 = []
    for i in list_d:
        FrequencyOfLetters1.append(i[0])
    # Запись зашифрованной версии Война и мир в файл
    with open("Documents/CaesarWarAndPeace_Encrypted.txt", "w") as CaesarWarAndPeace_Encrypted:
        CaesarWarAndPeace_Encrypted.write(caesarcipher.caesar_encryption1(key, key_word, textOg, alphabet, 3))

    # процесс расшифровки через монограммы
    CaesarWarAndPeace_Encrypted = open("Documents/CaesarWarAndPeace_Encrypted.txt", "rt")
    textEncrypted = CaesarWarAndPeace_Encrypted.read()
    FrequencyOfLetters2 = Counter("".join([ch for ch in textEncrypted if ch in alphabet]))
    print(f"Частота встречи букв в шифре цезаря:\t{len(FrequencyOfLetters2)} {FrequencyOfLetters2}")
    list_d2 = list(FrequencyOfLetters2.items())
    list_d2.sort(key=lambda i: i[1])
    list_d2.reverse()
    FrequencyOfLetters2 = []
    for i in list_d2:
        FrequencyOfLetters2.append(i[0])
    # FrequencyOfLetters2 массив с буквами которые чаще всего встречаются в тексте цезаря
    while len(FrequencyOfLetters2) != len(alphabet):
        FrequencyOfLetters2.append('')
        FrequencyOfLetters1.append('')
    # Расшифровка 1 версия
    textDecrypted1 = decryption(textEncrypted, FrequencyOfLetters2)
    # print(f"\n\n{textDecrypted1}")
    # запись расшифрованной версии
    with open("Documents/CaesarWarAndPeace_Decrypted_v1.txt", "w") as CaesarWarAndPeace_Decrypted:
        CaesarWarAndPeace_Decrypted.write(textDecrypted1)
    # Красивый вывод
    result(FrequencyOfLetters1, FrequencyOfLetters2)


    # Работа с биграммами
    beGramsOg = Counter(re.findall(r'(?=([а-я]{2}))', textOg)).most_common(10)
    OgBeGrams = []
    for i in beGramsOg:
        OgBeGrams.append(i[0])
    print(f"Популярные биграммы в оригинальном тексте:\t\t{OgBeGrams}")
    beGrams = Counter(re.findall(r'(?=([а-я]{2}))', textDecrypted1)).most_common(10)
    DecryptedBeGrams = []
    for i in beGrams:
        DecryptedBeGrams.append(i[0])
    print(f"Популярные биграммы в расшифрованном тексте:\t{DecryptedBeGrams}")
    # меняем алфавит расшифровки
    print(f"Старый алфавит замены:\t{FrequencyOfLettersOg}")
    DecryptedBeGramsList = []
    OgBeGramsList = []
    for i in range(len(DecryptedBeGrams)):
        if DecryptedBeGrams[i] != OgBeGrams[i]:
            DecryptedBeGramsItem = list(DecryptedBeGrams[i])
            OgBeGramsItem = list(OgBeGrams[i])
            for i in range(len(DecryptedBeGramsItem)):
                if DecryptedBeGramsItem[i] != OgBeGramsItem[i]:
                    if DecryptedBeGramsItem[i] not in DecryptedBeGramsList and DecryptedBeGramsItem[i] not in OgBeGramsList:
                        DecryptedBeGramsList.append(DecryptedBeGramsItem[i])
                    if OgBeGramsItem[i] not in DecryptedBeGramsList and OgBeGramsItem[i] not in OgBeGramsList:
                        OgBeGramsList.append(OgBeGramsItem[i])
    for i in range(len(DecryptedBeGramsList)):
        if DecryptedBeGramsList[i] != OgBeGramsList[i]:
            print(f"{DecryptedBeGramsList[i]} <-> {OgBeGramsList[i]}")
            FrequencyOfLettersOg[FrequencyOfLettersOg.index(DecryptedBeGramsList[i])], FrequencyOfLettersOg[FrequencyOfLettersOg.index(OgBeGramsList[i])] = "EXP", DecryptedBeGramsList[i]
            FrequencyOfLettersOg[FrequencyOfLettersOg.index("EXP")] = OgBeGramsList[i]
    print(f"Новый алфавит замены:\t{FrequencyOfLettersOg}")


    # Расшифровка с обновленным словарем
    textDecrypted2 = decryption(textEncrypted, FrequencyOfLetters2)
    # print(f"\n\n{textDecrypted2}")
    # запись расшифрованной версии
    with open("Documents/CaesarWarAndPeace_Decrypted_v2.txt", "w") as CaesarWarAndPeace_Decrypted2:
        CaesarWarAndPeace_Decrypted2.write(textDecrypted2)
    # Красивый вывод
    result(FrequencyOfLetters1, FrequencyOfLetters2)
    # Закрытие файлов
    CaesarWarAndPeace_Encrypted.close()
    OgWarAndPeace.close()
    return


def decryption(textEncrypted, FrequencyOfLetters2):
    # Расшифровывает текст и возвращает его в виде строки
    textDecrypted = []
    for i in textEncrypted:
        if i in FrequencyOfLettersOg:
            textDecrypted.append(FrequencyOfLettersOg[FrequencyOfLetters2.index(i)])
        else:
            textDecrypted.append(i)
    textDecrypted = "".join(textDecrypted)
    return textDecrypted


def result(FrequencyOfLetters1, FrequencyOfLetters2):
    # выводит итоговое количество совпавших букв с оригиналом
    print("Заменяем буквы из шифра цезаря на:")
    counter = 0
    counterRightLetters = 0
    print("+---+------------+---------------+-----+---------+")
    for i in FrequencyOfLetters2:
        if FrequencyOfLettersOg[counter] == FrequencyOfLetters1[counter]:
            print(
                f"| {counter + 1} | \"{i}\" -> \"{FrequencyOfLettersOg[counter]}\" | А ДОЛЖНО БЫТЬ | \"{FrequencyOfLetters1[counter]}\" |  ВЕРНО  |")
            counterRightLetters += 1
        elif FrequencyOfLetters1[counter] == FrequencyOfLetters2[counter] == "":
            print(f"| {counter + 1} |     \"{FrequencyOfLettersOg[counter]}\"    |  БУКВЫ НЕТ В ТЕКСТЕ |  ВЕРНО  |")
            counterRightLetters += 1
        else:
            print(
                f"| {counter + 1} | \"{i}\" -> \"{FrequencyOfLettersOg[counter]}\" | А ДОЛЖНО БЫТЬ | \"{FrequencyOfLetters1[counter]}\" | НЕВЕРНО |")
        if counter > 7:
            print("+----+------------+---------------+-----+---------+")
        else:
            print("+---+------------+---------------+-----+---------+")
        counter += 1
    print(f"Кол-во верно расшифрованных букв: {counterRightLetters}/{len(alphabet)}")
    return


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


if __name__ == '__main__':
    while True:
        print(f"\n:::\t\t\t\t\t\t:::\n1 - Шифр цезаря 1-й вариант\n2 - Шифр цезаря 2-й вариант\n3 - Частотный анализ\n4 - Выход\nВведите номер задачи:")
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
                print("\nЧастотного анализа\n\n1 - Кодирование и Декодирование 1 Тома \"Война и Мир\" (worst decryption)\n2 - Кодирование и Декодирование 2 Тома \"Война и Мир\" (worst decryption)\n3 - Кодирование и Декодирование 3 Тома \"Война и Мир\" (best decryption)\n4 - Кодирование и Декодирование 4 Тома \"Война и Мир\"\n5 - Кодирование и Декодирование 1-4 Тома \"Война и Мир\"")
                program3 = input()
                if program3.isdigit():
                    program3 = int(program3)
                    if program3 == 1:
                        if enter() == 1:
                            continue
                        coding('1')
                    elif program3 == 2:
                        if enter() == 1:
                            continue
                        coding('2')
                    elif program3 == 3:
                        if enter() == 1:
                            continue
                        coding('3')
                    elif program3 == 4:
                        if enter() == 1:
                            continue
                        coding('4')
                    elif program3 == 5:
                        if enter() == 1:
                            continue
                        coding('1-4')
                    else:
                        print("::: ERROR #1 :::\nEntered Incorrect Number\n::: ERROR #1 :::")
                        continue
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
