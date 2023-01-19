# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('encoding.txt', 'w', encoding='UTF-8') as my_file:
    my_file.write(input('Введите текст для сжатия: '))
with open('encoding.txt', 'r') as my_file:
    my_txt = my_file.readline()
    txt_compress = my_txt.split()

#print(my_txt)

def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


txt_compress = file_encod(my_txt)

with open('coding.txt', 'w', encoding='UTF-8') as my_file:
    my_file.write(f'{txt_compress}')
print(f'Сжатый текст -> {txt_compress}')
print(f'Исходный текст -> {my_txt}')