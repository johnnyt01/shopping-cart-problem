import json

TAX_RATE = 0.0825

# loading in coupon and shopping cart information
with open('coupons.json', 'r') as f:
    coupon_data = json.load(f)

with open('shopping_cart.json', 'r') as f:
    shopping_cart = json.load(f)

# Feature 1: Calculate total price of items in shopping cart
def calculate_total(shopping_cart):
    total = sum(item['price'] for item in shopping_cart)
    return total

# Feature 2: Calculate total price of items in shopping cart with sales tax
def calculate_total_with_tax(shopping_cart):
    subtotal = calculate_total(shopping_cart)
    tax_total = subtotal * TAX_RATE
    grand_total = subtotal + tax_total
    return (subtotal, tax_total, grand_total)

# Feature 3: Calculate total price of items in shopping cart with sales tax, with tax exemption for some items
def calculate_total_with_tax_and_exempt(shopping_cart):
    subtotal = 0
    tax_total = 0
    for item in shopping_cart:
        if item['isTaxable'] is False:
            subtotal += item['price']
        else:
            subtotal += item['price']
            tax_total += item['price'] * TAX_RATE
    grand_total = subtotal + tax_total
    return (subtotal, tax_total, grand_total)

# Feature 4: Apply coupons to items in shopping cart
def apply_coupons(shopping_cart, coupons):
    subtotal = 0
    tax_total = 0
    for item in shopping_cart:
        if item['item_id'] in coupons:
            coupon = coupons[item['item_id']]
            if item['price'] - coupon > 0:
                item['price'] -= coupon
            else:
                item['price'] = 0
    return (shopping_cart)

# Feature 1: Calculate total 
total = calculate_total(shopping_cart)
print("Grand total: %.2f" % total, "\n")

# Feature 2: Calculate total with tax
subtotal, tax_total, grand_total = calculate_total_with_tax(shopping_cart)
print("Subtotal: %.2f" % subtotal)
print("Tax total: %.2f" % tax_total)
print("Grand total: %.2f" % grand_total, "\n")

# Feature 3: Calculate total with tax and exemption
subtotal, tax_total, grand_total = calculate_total_with_tax_and_exempt(shopping_cart)
print("Subtotal: %.2f" % subtotal)
print("Tax total: %.2f" % tax_total)
print("Grand total: %.2f" % grand_total, "\n")

# Feature 4: Apply coupons
final = apply_coupons(shopping_cart, coupon_data)
print(shopping_cart, "\n") 

# Final totals after coupon has been applied 
subtotal, tax_total, grand_total = calculate_total_with_tax_and_exempt(final)
print("Subtotal: %.2f" % subtotal)
print("Tax total: %.2f" % tax_total)
print("Grand total: %.2f" % grand_total)