# -*- coding: UTF-8 -*-

import csv
import random

TRACKS_PATH = 'porto_subset_100k_int50.csv'
ASSIGNMENTS_PATH = 'assignments.csv'
NEW_TRACKS_PATH = 'porto_subset_100k_int50_plot.csv'
NEW_ASSIGNMENTS_PATH = 'assignments_plot.csv'
N_1S = 1500


def main():
    with open(TRACKS_PATH, 'rb') as tracks, \
            open(ASSIGNMENTS_PATH, 'rb') as assignments, \
            open(NEW_TRACKS_PATH, 'w') as new_tracks, \
            open(NEW_ASSIGNMENTS_PATH, 'w') as new_assignments:

        tracks_reader = csv.reader(tracks, delimiter=';')
        assignments_reader = csv.reader(assignments, delimiter=';')
        tracks_reader.next()
        assignments_reader.next()

        tracks_writer = csv.writer(new_tracks, delimiter=';', quotechar='',
                                   escapechar='\\', quoting=csv.QUOTE_NONE)
        assignments_writer = csv.writer(new_assignments, delimiter=';',
                                        quotechar='', escapechar='\\',
                                        quoting=csv.QUOTE_NONE)
        tracks_writer.writerow(['Points'])
        assignments_writer.writerow(['zn'])

        lines = 0
        for assignment in assignments_reader:
            if int(assignment[0]) == 0:
                tracks_writer.writerow([tracks_reader.next()[0]])
                assignments_writer.writerow([assignment[0]])
            lines += 1

        tracks.seek(0)
        assignments.seek(0)
        tracks_reader.next()
        assignments_reader.next()

        i_samples = random.sample(range(1, lines), N_1S)
        for i, track in enumerate(tracks_reader):
            if i in i_samples:
                tracks_writer.writerow([track[0]])
                assignments_writer.writerow([1])


if __name__ == '__main__': main()