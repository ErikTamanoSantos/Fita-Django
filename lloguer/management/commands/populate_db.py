from django.core.management.base import BaseCommand
import random
from faker import Faker
from lloguer.models import Automobil

fake = Faker()

class Command(BaseCommand):

    def handle(self, *args, **options):
        generateVehicles(10)

def generateVehicles(count):
    for i in range(count):
        marca = fake.company()
        model = fake.random_element(elements=('SUV', '4X4', 'Truck', "Bike", "Car"))
        matricula = getRandomLicense()
        automobil = Automobil.objects.create(marca=marca, model=model, matricula=matricula)

def getRandomLicense():
    letras = [chr(i) for i in range(65, 91)]
    numeros = [str(i) for i in range(10)]
    matricula = ''.join(random.choices(letras, k=3)) + '-' + ''.join(random.choices(numeros, k=4)) + '-' + ''.join(random.choices(letras, k=2))
    return matricula

generateVehicles(200)