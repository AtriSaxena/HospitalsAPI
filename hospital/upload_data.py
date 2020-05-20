from .models import Hospitals
# # Register your models here.
import csv

path = 'Hospital_with_discipline_jul_15.csv'
with open(path) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Hospitals.objects.get_or_create(
            id=row[0],
            state=row[1],
            city=row[2],
            name = row[3],
            category = row[4],
            medicine = row[5],
            address = row[6],
            website = row[7],
            specilization = row[8]
            )