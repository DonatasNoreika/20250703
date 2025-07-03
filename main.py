from projektas import Projektas, engine
from sqlalchemy.orm import sessionmaker, Query

Session = sessionmaker(engine)
session = Session()

# (Crud)
# projektas1 = Projektas("Naujas pr.", 20000)
# session.add(projektas1)
# session.commit()

# projektas2 = Projektas("2 projektas", 55000)
# session.add(projektas2)
# session.commit()

# (cRud)
# search = session.query(Projektas).filter(Projektas.name.ilike("2%")).first()
# print(search)

# (crUd)
# projektas1 = session.get(Projektas, 1)
# projektas1.price = 22000
# session.commit()

# projektas2 = session.query(Projektas).filter_by(name="2 projektas").one()
# projektas2.name = "2 projektas tikrai"
# session.commit()

# (cruD)
# projektas1 = session.query(Projektas).filter_by(name="Naujas pr.").one()
# session.delete(projektas1)
# session.commit()
