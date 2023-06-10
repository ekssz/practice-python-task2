# -*- coding: utf-8 -*-

dictionary = {
    "яблуко": "apple",
    "кіт": "cat",
    "собака": "dog",
    "будинок": "house",
    "кінь": "horse"
}

while True:
    # використовую цикл вайл для повторення
    word = input("Введіть слово (або натисніть 'q' для виходу): ")

    if word == 'q':
        break

# перевірка чи є введене слово у словнику
    if word in dictionary:
        translation = dictionary[word]
        print(f"Переклад слова '{word}': {translation}")
    else:
        print(f"Відсутній переклад для слова '{word}'")

