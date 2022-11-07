# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
txt = input("Введите текст через пробел: ")
print(f'Исходный текст: {txt}')
find_text = "абв"
lst = [i for i in txt.split() if find_text not in i]
print(f'Результат: {" ".join(lst)}')