from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, Date, Time
from sqlalchemy.orm import declarative_base, DeclarativeBase
from sqlalchemy.dialects.mssql import VARCHAR

class Base(DeclarativeBase):
    pass

class Facultate(Base):
    __tablename__ = 'Facultate'

    # Define columns
    id_Facultate = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key
    nume = Column(VARCHAR(100), nullable=False)  # Faculty Name

class Profesor(Base):
    __tablename__ = 'Profesor'

    # Define columns
    id_Profesor = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key
    nume = Column(VARCHAR(50), nullable=False)  # Last Name
    prenume = Column(VARCHAR(50), nullable=False)  # First Name
    grad = Column(VARCHAR(50))  # Rank
    id_Facultate = Column(Integer, ForeignKey('Facultate.id_Facultate'), nullable=False)  # Foreign Key
    email = Column(VARCHAR(100), nullable=False, unique=True)  # Email
    parola = Column(VARCHAR(50), nullable=False)  # Password

class Materie(Base):
    __tablename__ = 'Materie'

    # Define columns
    id_Materie = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key
    nume = Column(VARCHAR(50), nullable=False)  # Last Name
    id_Profesor = Column(Integer, ForeignKey('Profesor.id_Profesor'), nullable=False)  # Foreign Key
    tip_examen = Column(VARCHAR(50))
    an_studiu = Column(Integer, nullable=False)
    semestru = Column(Integer, nullable=False)

class Student(Base):
    __tablename__ = 'Student'

    # Define columns
    id_Student = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key
    nume = Column(VARCHAR(50), nullable=False)  # Last Name
    prenume = Column(VARCHAR(50), nullable=False)  # First Name
    grupa = Column(VARCHAR(10), nullable=False)  # Group
    id_Facultate = Column(Integer, ForeignKey('Facultate.id_Facultate'),  nullable=False)  # Foreign Key
    email = Column(VARCHAR(100), nullable=False, unique=True)  # Email
    parola = Column(VARCHAR(50), nullable=False)  # Password


class Cerere(Base):
    __tablename__ = 'Cerere'

    # Define columns
    id_Cerere = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key
    id_Profesor = Column(Integer, ForeignKey('Profesor.id_Profesor'), nullable=False)  # Foreign Key
    id_Facultate = Column(Integer, ForeignKey('Facultate.id_Facultate'), nullable=False)  # Foreign Key
    id_Materie = Column(Integer, ForeignKey('Materie.id_Materie'), nullable=False)  # Foreign Key
    data = Column(Date, nullable=False)
    status = Column(VARCHAR(20), nullable=False)

class Examen(Base):
    __tablename__ = 'Examen'

    # Define columns
    id_Examen = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key
    id_Profesor = Column(Integer, ForeignKey('Profesor.id_Profesor'), nullable=False)  # Foreign Key
    id_Cerere = Column(Integer, ForeignKey('Cerere.id_Cerere'), nullable=False)  # Foreign Key
    id_Materie = Column(Integer, ForeignKey('Materie.id_Materie'), nullable=False)  # Foreign Key
    ora = Column(Time, nullable=False)
    sala = Column(VARCHAR(20), nullable=False)


# Tabel de legătură Facultate_Profesor
class FacultateProfesor(Base):
    __tablename__ = 'Facultate_Profesor'

    id_Facultate = Column(Integer, ForeignKey('Facultate.id_Facultate'), primary_key=True, nullable=False)
    id_Profesor = Column(Integer, ForeignKey('Profesor.id_Profesor'), primary_key=True, nullable=False)


# Tabel de legătură Asistent_Examen
class AsistentExamen(Base):
    __tablename__ = 'Asistent_Examen'

    id_Examen = Column(Integer, ForeignKey('Examen.id_Examen'), primary_key=True, nullable=False)
    id_Profesor = Column(Integer, ForeignKey('Profesor.id_Profesor'), primary_key=True, nullable=False)


# Tabel de legătură Grupa_Examen
class GrupaExamen(Base):
    __tablename__ = 'Grupa_Examen'

    id_Examen = Column(Integer, ForeignKey('Examen.id_Examen'), primary_key=True, nullable=False)
    grupa = Column(VARCHAR(10), primary_key=True, nullable=False)