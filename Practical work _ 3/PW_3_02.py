sales = {
    "яблоки": 120,
    "груши": 85,
    "бананы": 150,
    "апельсины": 60,
  }

#•	Найти самый продаваемый товар.
max_prod = max(sales, key = sales.get)
print("Лидер продаж", max_prod)



#•	Вывести товары, где продажи больше 80.
for product, amount in sales.items():
  if amount > 80:
    print(product, " ", amount)
