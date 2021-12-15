from os import listdir, remove


def export(lines, fileName):
    with open('lists'+'\\'+fileName, "w") as f:
        for line in lines:
            f.write(line)

def count_lines(file):
    lines = 0
    for _ in file:
        lines+=1
    return lines

txt_files = [f for f in listdir('lists')]

isCut = False

for fileName in txt_files:
    file = open('lists'+'\\'+fileName, "r")

    if count_lines(file) > 30:
        isCut = True
        file = open('lists'+'\\'+fileName, "r")
        lines = []
        i = 0
        filecounter = 1

        for line in file:
            lines.append(line)
            i+=1

            if i == 30:
                lines[-1] = lines[-1][:-1]
                export(lines, fileName[:-4]+str(filecounter)+'.txt')
                filecounter+=1
                i=0
                lines = []

    
        if i > 0 and filecounter > 1:
            lines[-1] = lines[-1][:-1]
            export(lines, fileName[:-4]+str(filecounter)+'.txt')
            filecounter+=1
            i=0
            lines = []

    file.close()

    if isCut:
        remove('lists\\'+fileName)
        isCut = False