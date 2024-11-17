def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage to be applied.

  Returns:
    The final price after applying the discount, or the original price if the discount is less than 20%.
  """

  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Example usage:
original_price = 100
discount_rate = 25

final_price = calculate_discount(original_price, discount_rate)
print("Final price:", final_price)



