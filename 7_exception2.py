def discounted(price, discount, max_discount=20):
    try:
        price = float(abs(price))
        discount = float(abs(discount))
        max_discount = int(abs(max_discount))
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
            if discount >= max_discount:
                return price
            else:
                return price - (price * discount / 100)
    except(ValueError, TypeError):
        return price
print(discounted(100, 2))
print(discounted(100, "3"))
print(discounted("100", "4.5"))
print(discounted("five", 5))
print(discounted("сто", "десять"))
print(discounted(100.0, 5, "10"))
