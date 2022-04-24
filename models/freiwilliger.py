from dataclasses import dataclass
from .datatypes import Geschlecht

@dataclass
class Freiwilliger:
    name : str
    nachname : str
    alter : int
    region : int
    geschlecht : Geschlecht
    einsatzbereich : str
    dienstart : str