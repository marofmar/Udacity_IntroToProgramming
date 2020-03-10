'''
1. Get a list of file names
2. Extract the place names from the file names
3. Make a directory for each place name
4. Move fiels into the right directories
'''

import os
import random


def extract_places(name):
    partial = name[name.find("_")+1:]
    return partial[:partial.find("_")]


def extract_places_using_split(name):
    return name.split("_")[1]


def list_of_places(originals):
    places = []
    for i in originals:
        place = extract_places(i)
        if place not in places:
            places.append(place)
    return places 


def make_place_directories(places):
    for i in range(len(places)):
        os.mkdir(places[i])


def relocate_files():
    for filename in originals:
        place = extract_places(filename)
        os.rename(filename, os.path.join(place, filename))


def organize_photos(directory):

    os.chdir('directory')
    originals = os.listdir()
    places = list_of_places(originals)
    make_place_directories(places)
    relocate_files()

# directory = "photo"
# if __name__ == "__main__":
#     organize_photos(directory)
    
    

print("TEST!")


