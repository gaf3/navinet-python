import os
import random

def random_file(file_name):

    file = open(file_name,"wb")

    for line in range(random.randint(0,1000)):
        file.write("%s\n" % random.random())

    file.close()


def random_files(directory_name):

    if not os.path.isdir(directory_name):
        os.makedirs(directory_name)

    for file in range(random.randint(0,100)):
        random_file(os.path.join(directory_name,"%s.txt" % file))


def random_directories(directory_name,depth=0):

    if not os.path.isdir(directory_name):
        os.makedirs(directory_name)

    for sub_name in range(random.randint(0,10)):

        random_files(os.path.join(directory_name,"dir%s" % sub_name))

        if depth > 0:
            random_directories(os.path.join(directory_name,"dir%s" % sub_name),depth-1)


