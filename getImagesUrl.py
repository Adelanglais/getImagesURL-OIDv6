import argparse
import sys
import os
import random

"""
Gestion des entrées dans le terminal
"""
parser = argparse.ArgumentParser(description='Open Image Dataset Downloader')
parser.add_argument("command",
                    metavar="<command>" 'getURL',
                    help="'get images URL'")
parser.add_argument('--classes', required=False, nargs='+',
                    metavar="list of classes",
                    help="Sequence of 'strings' of the wanted classes")
parser.add_argument('--limit', required=False, type=int, default=None,
                    metavar="integer number",
                    help='Optional limit on number of images to download')
args = parser.parse_args()

if args.command == 'downloader':
    if args.limit is None:
        print('Missing the desired number of images')
        exit(1)

if args.command == 'downloader':
    if args.classes is None:
        print('Missing classes argument')
        exit(1)

"""
Accès à l'identifiant de la classe passée en paramètre
"""
file_class = 'class-descriptions-boxable.csv'
file_test_annotations = 'test-annotations-bbox.csv'
file_url = 'image_ids_and_rotation.csv'

name_classe = args.classes #liste
classe = "-".join(name_classe) #string
print('Get id of {} class.'.format(args.classes))

f = open(file_class,"r",encoding='utf8')
for l in f:
    if classe in l:
        mots = l.split(",")
        id_classe = (mots[0])
        print('id =',id_classe)

"""
Accès aux identifiants des images de la classe
"""
f = open(file_test_annotations,"r",encoding='utf8')
nb_images = args.limit
print('Limiting to {} images.'.format(args.limit))

img_list = [] * nb_images

a = 0
for l in f:
    if id_classe in l:
        mots = l.split(",")
        id_img = (mots[0])
        img_list.append(id_img)

""" 
Accès aux url des images
"""
while a < nb_images:
    f2 = open(file_url,"r",encoding='utf8')
    for l2 in f2:
        if random.choice(img_list) in l2:
            mots2 = l2.split(",")
            url_img = (mots2[2])
            print(url_img)
            
            a = a+1

        if a >= nb_images:
            exit(1)

