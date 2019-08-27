def cost_of_ground_shipping(weight):
  flat_charge = 20
  if weight <= 2:
    price_per_pound = 1.5
  elif 2 < weight <= 6:
    price_per_pound = 3
  elif 6 < weight <= 10:
    price_per_pound = 4
  else:
    price_per_pound = 4.75
  cost = weight * price_per_pound + flat_charge
  return cost

# Test cost_of_ground_shipping function
print(cost_of_ground_shipping(8.4))

cost_of_premium_ground_shipping = 125

def cost_of_drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.5
  elif 2 < weight <= 6:
    price_per_pound = 9
  elif 6 < weight <= 10:
    price_per_pound = 12
  else:
    price_per_pound = 14.25
  cost = weight * price_per_pound
  return cost

# Test cost_of_drone_shipping function
print(cost_of_drone_shipping(1.5))