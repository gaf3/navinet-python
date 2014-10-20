import os

def tally_file(file_name):

    file = open(file_name)

    tally = 0

    for line in file:
        tally += float(line)

    file.close()

    return tally


def tally_directory(directory_name):

    tally = 0

    for entity in os.listdir(directory_name):
        if os.path.isfile(os.path.join(directory_name,entity)):
            tally += tally_file(os.path.join(directory_name,entity))
        elif os.path.isdir(os.path.join(directory_name,entity)):
            tally += tally_directory(os.path.join(directory_name,entity))

    return tally
