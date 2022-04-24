from models.freiwilliger import Freiwilliger
import random

def create_dummy_data(size : int):
    freiwillige = []
    chars = "abcdefghijklmnqrstuvwxyz"
    bereiche = ["A", "B", "C", "D", "E", "F"]
    dienste = ["BFD", "FSJ"]
    regionen = ["Aachen", "Aachen", "Aachen-Land", "Düren", "Heinsberg", "Mönchengladbach", "Krefeld", "Eifel"]

    for i in range(size):
        name = chars[random.randint(0, len(chars) - 1)] + chars[random.randint(0, len(chars) - 1)] \
                + chars[random.randint(0, len(chars) - 1)]
        region = random.choice(regionen)
        geschlecht = random.randint(1,2)
        einsatzbereich = random.choice(bereiche)
        dienstart = random.choice(dienste)
        f = Freiwilliger(name=name, nachname=str(i),alter=random.randint(16, 25), region=region,
                         geschlecht=geschlecht,einsatzbereich=einsatzbereich,
                         dienstart=dienstart)
        freiwillige.append(f)
    return freiwillige