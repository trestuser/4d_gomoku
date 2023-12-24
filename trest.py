# import sys
# perem = 1
# perem_2 = 1.0
# print(perem.__sizeof__())
# print(perem_2.__sizeof__())
# print(sys.getsizeof(float()))
# print(sys.getsizeof(int()))


# def filter_odd_num(text: str) -> bool:
#     black_list = set("<>@#$%^*-")
#     for elem in text:
#         if elem in black_list:
#             return False
#         else:
#             return True


# def encodding(text: list,
#               encode: dict
#               ) -> list:
    
#     new_list  = []
#     for elem in text:
#         new_list.append(encode[elem])

#     return new_list

# def shifr(text: list,
#           word: list) -> list:
    
#     return None

# def main():
#     alphavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz;:.,!?' `"
#     print(len(alphavit))
#     encode = {elem: number+1 for number, elem in enumerate(alphavit)}
#     decode = {number+1 : elem for number, elem in enumerate(alphavit)}

#     # ToDo предобработку изначального текста и слова
#     text = "Привет, меня зовут Д<>аня. Я - Д<>аня"

#     word = "утка"

#     out_text = list(filter(filter_odd_num, text.lower()))

#     encoded_text = encodding(out_text, encode)
#     encoded_word = encodding(word, encode)

#     # for idx in range(len(encoded_word)):
#     #     if encoded_word[idx] % 2 == 0:
#     #         encoded_text = [i*2 for i in encoded_text]
#     #     else:
#             #ToDo
#     # print(encoded_word)


# if __name__ == "__main__":
#     main()


import numpy as np

def print_matrix(matrix):
    for line in range(len(matrix)):
        print(*matrix[line])

# x, y - координаты внутри маленького поля
# z - выбор поля в срезе
# w - выбор среза

#        x,  y,  z,  w
shape = (15, 15, 15, 15)
# Начальный ход в (7,7,7,7)

GAME_POLIGON = np.zeros(shape,
                        dtype=int)

print_matrix(GAME_POLIGON[:,:,0,0])

# while True: # Запуск игрового цикла
    # ToDo должно предложение выбора одного из 15 полей 
    # Которые есть в данном срезе
    # нужен функционал перехода к конткретному полю
    # нужен функционал перехода между срезами
    # нужен функционал выхода из конретного поля
    # добавить функционал выбора координаты поставновки точки
    # добавить рандомный ход компьютером - ходит рядом с существующими точками
    # Смотреть в сторону визуализации

# print(GAME_POLIGON.shape)

