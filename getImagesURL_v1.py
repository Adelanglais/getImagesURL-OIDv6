import argparse
import random

def parser_arguments():
    """
    Manage the input from the terminal.
    :return : pasrer
    """
    parser = argparse.ArgumentParser(description='Open Image Dataset Downloader')

    parser.add_argument("command",
                        metavar= "<command> 'getURL' or 'listClasses'.",
                        help = "'getURL' or 'listClasses'.")
    parser.add_argument('--classes', required=False, nargs='+',
                    metavar="list of classes",
                    help="Sequence of 'strings' of the wanted classes")
    parser.add_argument('--limit', required=False, type=int, default=None,
                    metavar="integer number",
                    help='Optional limit on number of images to download')

    args = parser.parse_args()
    return args

def getListClasses():
    """
    Access to a list of class
    :return: list
    """ 

    f=open('csv_files/class-descriptions-boxable.csv',"r",encoding='utf8') 
    for ligne in f:
        a=0
        while a < 600:
            ligne = f.readline()
            mots = ligne.split(",") # places each word separated by "," in a box in a table
            name_classe = (mots[1]) # access to the second box of the precedent table
            print(name_classe)
            a+=1
        #reading the file line by line and displaying the name of each class

if parser_arguments().command == 'listClasses':
    print("List of all classes.")
    getListClasses()

def getIdClass():
    """
    Access to the label Name of the requested class
    :return: id of the class asked in the terminal
    """
    name = parser_arguments().classes #list format
    classe = "-".join(name) #string format
    f=open('csv_files/class-descriptions-boxable.csv',"r",encoding='utf8')
    for l in f:
        a=0
        while a < 599:
            l = f.readline()
            mots = l.split(",")
            name = mots[1].replace(" ","")
            
            if classe in name:
                id_classe = mots[0]
                return id_classe
                # line by line of the file, we check if the name of the class passed in parameter is present.
                # if yes, return the identifier of this class
                # if not, test the file's following line
            else:
                a = a+1
            
def getImgList(id_classe):
    """
    List of images present in the class
    :return : list of identifier
    """
    f=open('csv_files/test-annotations-bbox.csv',"r",encoding='utf8')
    img_list0 = []
    img_list = []
    a = 0
    nb_img = parser_arguments().limit
    for l in f:
        if id_classe in l:
            mots = l.split(",")
            id_img = mots[0]
            img_list0.append(id_img)
    # lists all the identifiers of the images present in the requested class

    while a < nb_img:
        img_list.append(random.choice(img_list0))
        a = a+1
    return img_list
    # select randomly in a new list the required number (requested in the terminal) of image identifiers

def getImgURL(img_list):
    """
    Access to image's URL of the requested class
    :return : url
    """
    f = open('csv_files/test-images-with-rotation.csv',"r",encoding='utf8')
    for l in f:
        mots = l.split(",")
        id = mots[0]    
        for i in range(len(img_list)):
            if img_list[i] == id:
                url = mots[2]
                print (url)
    # For the file's first line,we check if the first element of the ID list is present
    # If yes, display the url and test the following line
    # If not, look for the next item until you've tested all ID. If non of them are in the line, test the following.
   
if parser_arguments().command == 'getURL':
    if parser_arguments().classes is None:
        print('Missing classes argument')
        exit (1)
    else:
        print("Get URL of {} class.".format(parser_arguments().classes))
        getImgURL(getImgList(getIdClass()))
        

    if parser_arguments().limit is None:
        print('Missing the desired number of images')
        exit (1)
