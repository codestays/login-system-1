import random

def generate_random_numbers():
    numbers = [str(random.randint(0, 9)) for _ in range(4)] 
    return ''.join(numbers) 