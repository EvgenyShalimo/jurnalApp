import random
from faker import Faker
from .models import Person

def generate_fake_persons(n):
    fake = Faker()
    for _ in range(n):
        name = fake.name()
        phone_number = fake.phone_number()
        person = Person(name=name, phone_number=phone_number)
        person.save()