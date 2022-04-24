from enum import Enum
import json


class Geschlecht(Enum):
    MÄNNLICH = 1
    WEIBLICH = 2
    ANDERS = 3


class RegionGraph():
    def __init__(self):
        self.nodes = {}
        with open("region_data.json", encoding="utf-8") as file:
            self.nodes = json.load(file)
        self.regions = list(self.nodes.keys())




class Group:
    def __init__(self, dienstart : str):
        self.freiwillige = []
        self.dienst = dienstart

    @property
    def size(self):
        return len(self.freiwillige)

    @property
    def pull_force(self):
        return (25 - len(self.freiwillige)) / 25

    @property
    def group_performance_index_for_new_member(self, m) -> float:
        temp_group = self.freiwillige.copy().append(m)
        # find biggest age diff
        min_age, max_age = 1000,0
        for f in temp_group:
            if f.alter < min_age:
                min_age = f.alter
            if f.alter > max_age:
                max_age = f.alter
        max_age_diff = max_age - min_age
        age_score = max_age_diff / 9
        # calculate region score


    def append(self, arg):
        self.freiwillige.append(arg)

    def gender_count(self, geschlecht : int) -> int:
        count = 0
        for f in self.freiwillige:
            if f.geschlecht == geschlecht:
                count += 1
        return count

    def gender_percentage(self, geschlecht : int) -> float:
        count = self.gender_count(geschlecht)
        return count / self.size

    def average_age(self) -> float:
        sum_age = 0
        for f in self.freiwillige:
            sum_age += f.alter
        return sum_age/len(self.freiwillige)

    def get_regions(self):
        return [f.region for f in self.freiwillige]


    def __repr__(self):
        return f"Gruppe_{self.dienst}(anzahl={self.size})"


