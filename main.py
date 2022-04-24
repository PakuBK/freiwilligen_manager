from tests.dummydata import create_dummy_data
from models.datatypes import Group, RegionGraph
from helpers.displaying import pretty_print_lst
from helpers.group_mangement import choose_random_and_pop, calculate_max_region_diff
import math
import random

def start():
    freiwillige = create_dummy_data(60)
    prepare_splitting(freiwillige)

def prepare_splitting(data):
    fsjler = [f for f in data if f.dienstart=="FSJ"]
    bfdler = [b for b in data if b.dienstart=="BFD"]
    #print("fsjler", len(fsjler))
    #print("bfdler", len(bfdler))

    fw = fsjler.copy()

    # calculate initial groups
    groups, fw = initial_groups(fw, "FSJ")

    # weise freiwillige ein
    for f in fw:
        # calculate fitting score for every group
        winner_group = (0, 0)
        for idx,g in enumerate(groups):
            score = fitting_score(f, g)
            if score > winner_group[0]:
                winner_group = (score, idx)
        groups[winner_group[1]].append(f)


    for g in groups:
        pass
        #pretty_print_lst(g.freiwillige)
        #print(f"Size: {g.size}, Avg Age : {g.average_age()}")


def initial_groups(fw, _type : str):
    groups = [Group(_type) for a in range(6)]
    # pick 3 girls and 3 boys from different regions
    initial_fw = []
    gender = [0,0]
    f, fw = choose_random_and_pop(fw)
    initial_fw.append(f)
    gender[int(f.geschlecht) - 1] += 1
    while len(initial_fw) < 6:
        f_idx = random.randint(0, len(fw)-1)
        f = fw[f_idx]
        is_correct = True
        for i in initial_fw:
            if i.region == f.region or gender[f.geschlecht-1] + 1 > 3:
                is_correct = False
        if is_correct:
            initial_fw.append(fw.pop(f_idx))
            gender[int(f.geschlecht) - 1] += 1


    for g,f in zip(groups, initial_fw):
        g.append(f)
    return (groups, fw)


def fitting_score(freiwilliger, group : Group):
    avg_age = group.average_age()
    male_percentage = group.gender_percentage(1)
    # age
    age_diff = math.fabs(avg_age - freiwilliger.alter)
    age_score = 1 - (age_diff / 9)  # 9 is max age diff
    # region
    group.get_region_factors()


    return 1 * (age_score * group.pull_force)

if __name__ == '__main__':
    start()


