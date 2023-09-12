#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self.items = []
    self.total = total
    self.last_price = 0
    self.lastQuantity = 0

  def add_item(self, title, price, quantity = 1):
    self.title = title
    self.price = price
    self.quantity = quantity
    item_total = price * quantity
    self.total+=item_total
    for n in range(quantity):
      self.items.append(title)
    self.last_price = price
    self.last_quantity = quantity
    
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      discount_total = (self.discount / 100) * self.total
      self.total -= discount_total
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    if self.last_quantity > 1:
      self.total-=(self.last_price * self.last_quantity)
    else:
      self.total-=self.last_price
