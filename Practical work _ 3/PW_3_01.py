grades = [4, 5, 3, 5, 4, 2, 5, 3, 4]
print(grades)

#•	Найти средний балл.

average = sum(grades) / len(grades)

print("Средняя", average)

#•	Определить количество пятерок.

count_5 = grades.count(5)
print("Кол-во 5",count_5)

#•	Вывести список без двоек.

filtered_non_2 = [grades for grades in grades if grades != 2]
print("Список без двоек", filtered_non_2)
