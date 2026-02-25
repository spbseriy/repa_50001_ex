words = ["кот", "собака", "кит", "слон", "крокодил", "сом"]

#Создать словарь, где:•	ключ — длина слова •	значение — список слов этой длины
result = {
    
}

for words in words:
  lenght = len(words)

  if lenght not in result:
    result[lenght] = []

  result[lenght].append(words)

print(result)
