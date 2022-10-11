from unicodedata import decimal


def dis(full_price, discount):
    dis = full_price*(discount/100)
    selling_price= full_price - discount
    return selling_price
actual_price  = float(input("enter the full price :  "))
discounted_price = float(input("enter the discount percentage :  "))
print(dis(actual_price, discounted_price))






