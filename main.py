import  sys
import re
from MinSpannbaum import Kruskal

try:
    argc = len(sys.argv);
    argv = sys.argv;
    argI = argv[argc - 1]  # last argument

    fileName = argI;

    with open(fileName, 'r') as file_obj:
        next(file_obj)
        lines = file_obj.readlines()
        n = lines[0]
        n = int(re.sub("\D", "", n))
        m = lines[1]
        m = int(re.sub("\D", "", m))
        kante = []
        for line in lines[2:]:
            s = int(line[0])  # der erste Knoten
            StrList = line.split()
            for k in StrList[2:]:
                lst = k.split("w")
                lst = list(map(int, lst))
                lst.insert(0,s)
                kante.append(lst)

        Kruskal(kante, n)

        file_obj.close()
except FileNotFoundError:
    print('File does not exists: ' + fileName)
    sys.exit(-1);