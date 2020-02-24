'''In this project we try to find the
cheapest method for every customer of a transportation company to dispatch their packages.
The company offers three different ways for transportation:
ground shipping, drone shipping and premium shipping.'''

premium_shipping = 125


def ground_shipping(weight):
    if weight <= 2:
        return weight * 1.50 + 20
    elif (weight > 2 and weight <= 6):
        return weight * 3.00 + 20
    elif (weight > 6 and weight <= 10):
        return weight * 4.00 + 20
    else:
        return weight * 4.75 + 20


def drone_shipping(weight):
    if weight <= 2:
        return weight * 4.50
    elif (weight > 2 and weight <= 6):
        return weight * 9.00
    elif (weight > 6 and weight <= 10):
        return weight * 12.00
    else:
        return weight * 14.25


def cheapest_method(weight):
    if ((ground_shipping(weight) < drone_shipping(weight)) and (ground_shipping(weight) < premium_shipping)):
        return "Ground shipping is the cheapest method"
    elif ((drone_shipping(weight) < ground_shipping(weight)) and (drone_shipping(weight) < premium_shipping)):
        return "Drone shipping is the cheapest method"
    else:
        return "Premium shipping is the cheapest method"


print(drone_shipping(1.5))

print(ground_shipping(8.4))

print(ground_shipping(23))

print(drone_shipping(23))

print(cheapest_method(23))
