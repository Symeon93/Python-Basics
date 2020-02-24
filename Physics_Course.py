# measures are in the SI

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1


# Converts Celsius to Farheneit
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


# Converts Fahreneit to Celsius
def c_to_f(c_temp):
    f_temp = 9 / 5 * c_temp + 32
    return f_temp


# Calculates force given mass and acceleration
def get_force(mass, accelaration):
    return mass * accelaration


# Calculates energy given mass
def get_energy(mass, c=3 * 10 ** 8):
    return mass * c ** 2


# Calculates  work given mass, acceleration and distance
def get_work(mass, acceleration, distance):
    return mass * acceleration * distance


# Here we test the previous
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
print(c_to_f(0))
print(get_force(train_mass, train_acceleration))

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

print(get_energy(bomb_mass))

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies" + str(bomb_mass) + " Joules.")

print(get_work(train_mass, train_acceleration, train_distance))

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")



