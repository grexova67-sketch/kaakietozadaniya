# //1 

# def format_price(price, currency="руб", discount=0):
#     if price < 0 or discount < 0 or discount > 100:
#         return "Ошибка: неверные данные"
#     price_with_discount = price * (1 - discount / 100)
#     return f"{price_with_discount:.2f} {currency}"


# print(format_price(1500))
# print(format_price(1500, "$", 20))


# //2
# nums = [-5, 0, 3, 7, -2, 9, 1, -8]
# result = list(map(lambda x: x * x, filter(lambda x: x > 0, nums)))
# print(result)

# //3
# def transform_list(data, func):
#     return [func(x) for x in data]

# print(transform_list(["a", "b", "c"], lambda x: x.upper()))
# print(transform_list([1, 2, 3], lambda x: x * 2))

# //4
products = [
    {"name": "Laptop", "price": 950, "rating": 4.5, "in_stock": True},
    {"name": "Mouse", "price": -10, "rating": 4.8, "in_stock": True},
    {"name": "Keyboard", "price": 120, "rating": 3.9, "in_stock": False},
    {"name": "Monitor", "price": 300, "rating": 4.2, "in_stock": True},
    {"name": "Headphones", "price": 80, "rating": 4.6, "in_stock": True},
]


def is_valid(product):
    return product["price"] > 0 and product["rating"] >= 4.0 and product["in_stock"] is True

valid_products = list(filter(is_valid, products))

products_with_discount = list(map(lambda item: {**item, "final_price": item["price"] * 0.85}, valid_products))

sorted_products = sorted(products_with_discount, key=lambda item: item["final_price"])


def print_catalog(items):
    for item in items:
        print(f"{item['name']} | Цена: {item['price']:.2f} | Итог: {item['final_price']:.2f}")


print_catalog(sorted_products)