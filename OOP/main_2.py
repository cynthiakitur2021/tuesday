from main import Vehicle


vehicle_one = Vehicle("Toyota", "Purple",  "Kinuthia", "Power", "Lexus")
vehicle_two = Vehicle("BMW", "Pink", "Rayan",  "Mary", "Toyota")
vehicle_three = Vehicle("RollRoyce", "Red", "Subaru", "Joy", "Maybach")
vehicle_four = Vehicle("Mercedez", "Black", "Hamilton", "Jane", "Lexus")


print(vehicle_one.owner, vehicle_one.color, vehicle_one.wheels, vehicle_one.engine)
print(vehicle_two.owner, vehicle_two.color, vehicle_two.wheels, vehicle_two.engine)
print(vehicle_three.owner, vehicle_three.color, vehicle_three.wheels, vehicle_three.engine)
print(vehicle_four.owner, vehicle_four.color, vehicle_four.wheels, vehicle_four.engine)
