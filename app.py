from projektas import Projektas, engine
from sqlalchemy.orm import sessionmaker, Query

Session = sessionmaker(engine)
session = Session()

while True:
    choice = int(input("1 - peržiūrėti, 2 - įrašyti, 0 - išeiti: "))
    if choice == 1:
        projects = session.query(Projektas).all()
        print(projects)
    if choice == 2:
        print("Įveskite projektą")
        name = input("Pavadinimas: ")
        price = float(input("Kaina: "))
        project = Projektas(name=name, price=price)
        session.add(project)
        session.commit()
    if choice == 0:
        print("Viso gero")
        break