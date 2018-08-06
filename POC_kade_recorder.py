import csv
from time import sleep
from datetime import datetime

from yoweb import base

OCEAN_NAME = 'Obsidian'
OCEAN = base.Ocean(OCEAN_NAME)
OUR_CREW_ID = 5001832  # Consider It Drunk
THEIR_CREW_ID = 5001155  # Guerrilla Warfare

while True:
    timestamp = datetime.utcnow().strftime('%d/%m/%y-%H:%M:%S')
    our_crew = OCEAN.getcrew(OUR_CREW_ID)
    their_crew = OCEAN.getcrew(THEIR_CREW_ID)
    try:
        our_j_crew_list = [pirate.name for pirate in our_crew.members.jobbing_pirate]
    except AttributeError:
        our_j_crew_list = []
    try:
        their_j_crew_list = [pirate.name for pirate in their_crew.members.jobbing_pirate]
    except AttributeError:
        their_j_crew_list = []

    for file_name, jcrew, name in [("CiS_job.csv", our_j_crew_list, our_crew.name),
                             ("GW_job.csv", their_j_crew_list, their_crew.name)]:
        with open(file_name, "ab") as crew_file:
            writer = csv.writer(crew_file, delimiter=',')
            jobber_count = len(jcrew)
            row = [timestamp, jobber_count, 'none']
            if jobber_count > 0:
                row.remove('none')
                row.append('|'.join(jcrew))
                writer.writewrow(row)
            print("As of {}: {} has {} jobbers".format(timestamp, name, jobber_count))

    sleep(60)