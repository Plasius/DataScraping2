
from os import listdir
from os.path import isfile, join

# lists mappának az elérési útja
PATH = "C:\lists\\"

# lista a fileokkal
onlyfiles = [f for f in listdir(PATH) if isfile(join(PATH, f))]

# linkek beolvasása a fileokbol
for file in onlyfiles:
    open_file = open(PATH + "\\" + file, 'r', encoding='utf-8')

    # feldolgozás alatt álló linkek
    linkedIn_links = [line.strip().split() for line in open_file]

    open_file.close()


