from collections import defaultdict

def erandjuhud(a,b):
    pik = len(a) if len(a) < len(b) else len(b)
    total_cost = 0
    vahetus = ''
    for i in range(pik):
        cost = 0
        if (a[i] == 'ž' and b[i] == 'z') or (a[i] == 'š' and b[i] == 's'):
            if i+1 <= len(b):
                if b[i+1] == 'h':
                    vahetus = b[i]
                    cost = 0.1
        total_cost += cost
    if vahetus != '':
        if vahetus == 'z':
            a = a.replace('ž', 'zh')
        else:
            a = a.replace('š', 'sh')
    return total_cost, a

def kaugus(xs, ys):
    memory = defaultdict(lambda: defaultdict(int))
    cost, xs = erandjuhud(xs, ys)
    xs = " " + xs
    ys = " " + ys
    if len(xs) ==0:
        return len(ys)
    if len(ys) ==0:
        return len(xs)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            if i == 0:
                memory[i][j] = j + cost
            elif j == 0:
                memory[i][j] = i + cost
            else:
                if x == y:
                    cost = 0
                else:
                    cost = 1
                    if (x == 'ö' and y == '8') or (y == 'ö' and x == '8'):
                        cost = 0.1
                    elif (x == 'y' and y == 'ü') or (y == 'y' and x == 'ü'):
                        cost = 0.1
                    elif (x == 'õ' and y == '6') or (y == 'õ' and x == '6'):
                        cost = 0.1
                    elif (x == 'ä' and y == '2') or (y == 'ä' and x == '2'):
                        cost = 0.1
                    elif (x.lower() == y.lower()):
                        cost = 0.1

                if memory[i][j] == 0:
                    if cost != 0 and (i + 1 != len(xs) and j + 1 != len(ys)) and (xs[i] == ys[j+1] and xs[i+1] == ys[j]):
                        memory[i][j] = min(memory[i-1][j] + 1,
                                           memory[i][j-1] + 1,
                                           memory[i-1][j-1] + 0.5)
                        memory[i+1][j+1] = memory[i][j]
                    else:
                        memory[i][j] = min(memory[i-1][j] + 1, 
                                       memory[i][j-1] + 1,
                                       memory[i-1][j-1] + cost)
    return memory[len(xs)-1][len(ys)-1]

def sõned(failinimi):
    sisu = []
    f = open(failinimi, encoding="utf8")
    for word in f:
        sisu.append(word.replace("|",""))
    f.close()
    return sisu

def soovitus(m, sõne):
    cost = []
    for i in m:
        cost.append((i, kaugus(i.strip("\n"), sõne)))
    cost.sort(key=lambda x: x[1])
    return [s.strip("\n") for (s, k) in cost[0:3]]
