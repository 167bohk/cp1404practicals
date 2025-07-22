from prac_09.unreliable_car import UnreliableCar
uc = UnreliableCar("xiaomi", 100, 30.0)
count = 0
while uc.fuel > 0:
    uc.drive(100)
    count += 1
print(count)
print(uc)
