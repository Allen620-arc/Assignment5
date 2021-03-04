"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""

import Queue as Q

monster_list_1 = Q.Queue()
monster_list_2 = Q.Queue()
godzilla_list = []
mothra_list = []

monster_1 = open('monsters1.txt', 'r')
for line in monster_1:
    monster_name = line.rstrip()
    if monster_name == 'Godzilla' or monster_name == 'Mothra':
        defeated_monster = monster_list_1.dequeue()
        if monster_name == 'Godzilla':
            godzilla_list.append(defeated_monster)
        if monster_name == 'Mothra':
            mothra_list.append(defeated_monster)
    else:
        monster_list_1.enqueue(monster_name)

if monster_list_1.is_empty():
    print("The Space Monsters were beaten!")
    print("Godzilla defeated:", godzilla_list)
    print("Mothra defeated:", mothra_list)
else:
    print("The Space Monsters were not beaten!")

monster_2 = open('monsters2.txt', 'r')
for line in monster_2:
    monster_name = line.rstrip()
    if monster_name == 'Godzilla' or monster_name == 'Mothra':
        defeated_monster = monster_list_2.dequeue()
        if monster_name == 'Godzilla':
            godzilla_list.append(defeated_monster)
        if monster_name == 'Mothra':
            mothra_list.append(defeated_monster)
    else:
        monster_list_2.enqueue(monster_name)

if monster_list_2.is_empty():
    print("The Space Monsters were beaten!")
    print("Godzilla defeated:", godzilla_list)
    print("Mothra defeated:", mothra_list)
else:
    print("Oh no! The Space Monsters defeated Godzilla and Mothra!")