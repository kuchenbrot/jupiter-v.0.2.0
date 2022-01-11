import json
import math


def d(xi, xj):
    i = 0
    max_ = len(xi)
    abst = 0
    e = []
    while i < max_:
        ze = xi[i] - xj[i]
        ze = math.pow(ze, 2)
        ze = math.sqrt(ze)
        e.append(ze)
        i += 1
    for i in e:
        abst += i
    return abst


file = open('../zwischenergebnise.txt', 'w')
file.write('')
file.close()
with open('../text.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    i = len(data)
    o = ""
    b = []
    y = list(input("Jo, tu mal dein Text da unten rein\n"))
    while i > 0:
        file = open('../zwischenergebnise.txt', 'a')
        ergebnis = 0
        wiederholung = False
        # idee: zum aufteilen spliten und fuer jedes element list() anwenden
        g = 0
        x = data['text' + str(i - 1)]['content']  # str(i-1)
        x = x.split(' ')
        r = len(x) % 5
        dl = 0
        b = []
        for f in x:
            dl += 1
            g += 1
            if r != 0:
                if dl + r <= len(x):
                    o += f + " "
                if dl + r > len(x):
                    if r == 2 and g == 5:
                        o += f
                        b.append(list(o))
                        o = ""
                    elif r == 2 and g >= 1:
                        o += f + " "
                    elif r == 1:
                        o += f
                        b.append(list(o))
                        o = ""
            else:
                o += f + " "
            if int(g / 5) == 1:
                b.append(list(o))
                o = ""
                g = 0
        j = []
        l = []
        for charf in b:
            length = len(charf)
            for char in charf:
                j.append(char)
            l = []
            dl = 0
            buchs = ""
            for h in y:
                dl += 1
                buchs += h + ''
                if len(y) >= length:
                    if dl == length:
                        l = list(buchs)

                elif length > len(y):
                    if dl == len(y):
                        while dl < len(j):
                            del j[-1]
                        l = list(buchs)
            x_ub = []
            y_ub = []
            az = 0
            print(len(l), len(j))
            print(j, l)
            for letter in j:
                print(az)
                if letter == l[az]:
                    x_ub.append(1)
                    y_ub.append(1)
                elif letter != l[az]:
                    x_ub.append(1)
                    y_ub.append(0)
                else:
                    print("dang ther somtjhing no good")
                az += 1
            #for char in l:
                #asciiw.append(ord(char))

            file.write(str(d(x_ub, y_ub)) + ' :' + "text" + str(i - 1) + '\n')
            j = []
        file.close()
        i -= 1
    file = open('../zwischenergebnise.txt', 'r')
    za = []
    for line in file:
        dwe = line.replace("\n", '')
        z = dwe.split(' :')
        za.append(float(z[0]))
    file.close()
    za = min(za)
    print(za)
    if za == 0.0:
        za = 0

    file = open('../zwischenergebnise.txt', 'r')
    for i in file:
        if i.startswith(str(za)):
            sth = i.split(' :')
            sth[1] = sth[1].replace('\n', '')
            if data[str(sth[1])]['mark'] == 0:
                print("unformal")

            elif data[str(sth[1])]['mark'] == 1:
                print("formal")

    file.close()
    # file = open('zwischenergebnise.txt', 'w')
    # file.write('')
    # file.close()
