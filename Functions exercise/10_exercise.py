# 10. Call Function using both positional and keyword arguments
# Define a function describe_pet(animal_type, pet_name) that prints a description of a pet.
# Call this function using both positional and keyword arguments.

def describe_pet(animal_type, pet_name):
    print(f"Pet name is: {pet_name}\nAnimal is: {animal_type}")

describe_pet(pet_name='Phoenix',animal_type='Dog')
describe_pet('Cat','Mr.Whiskers')