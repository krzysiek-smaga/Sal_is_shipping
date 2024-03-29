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
  return weight * price_per_pound + flat_charge

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
  return weight * price_per_pound

# Test cost_of_drone_shipping function
print(cost_of_drone_shipping(1.5))

def cheapest_shipping_method(weight):
  ground = cost_of_ground_shipping(weight)
  premium = cost_of_premium_ground_shipping
  drone = cost_of_drone_shipping(weight)
  if ground < premium and ground < drone:
    method = "ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone
  return print("The cheapest method is " + method + " shipping and it cost " + str(cost) +"$.")
  
# Test cheapest_shipping_method function
print(cheapest_shipping_method(4.8))
print(cheapest_shipping_method(41.5))