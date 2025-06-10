products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
def sum_sales(items):
    all_sales = 0
    for item in items:
        all_sales = all_sales + item
    return (all_sales)
sum_sales_all_product = 0
sum_sales_all_product_avg = 0
for one_product in products:
    sum_sales_product = sum_sales(one_product['items_sold'])
    sales_product_avg = int(sum_sales(one_product['items_sold']) / len(one_product['items_sold']))
    sum_sales_all_product = sum_sales_all_product + sum_sales_product
    sum_sales_all_product_avg = int(sum_sales_all_product / len(products)) #тут не поняла как среднее посчитать
    print(f'Сумма продаж для: {one_product["product"]}: {sum_sales_product}')
    print(f'Cреднее количество продаж для: {one_product["product"]}: {sales_product_avg}')
    print(f'Суммарное количество продаж всех товаров: {sum_sales_all_product}')
    print(f'Среднее количество продаж всех товаров: {sum_sales_all_product_avg}') #вообще не уверена в этом

