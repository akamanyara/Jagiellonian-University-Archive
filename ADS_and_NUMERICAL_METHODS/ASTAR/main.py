import numpy as np
import random
from queue import PriorityQueue
from PIL import Image, ImageDraw, ImageFont

rozmiarKomorki = 46
rozmiarPola = 45
ramka = 1

start = 1
stop = 1
labirynt = []


def rysujLabirynt(labirynt, showNumbers=False):
    szer = labirynt.shape[0]
    wys = labirynt.shape[1]
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()
    img = Image.new("RGBA", (wys * rozmiarKomorki, szer * rozmiarKomorki), "black")
    draw = ImageDraw.Draw(img)

    for i in range(szer):
        for j in range(wys):
            if labirynt[i][j] == 1:
                kolor = (240, 240, 240)
            elif labirynt[i][j] == 3:
                kolor = (160, 20, 20)
            elif labirynt[i][j] == 2:
                kolor = (20, 20, 160)
            elif labirynt[i][j] == 4:
                kolor = (30, 100, 30)
            elif labirynt[i][j] == 7:
                kolor = (200, 200, 10)
            elif labirynt[i][j] == 8:
                kolor = (255, 120, 0)
            elif labirynt[i][j] == 9:
                kolor = (180, 0, 255)
            else:
                kolor = (60, 60, 60)
            draw.rectangle(([(j * rozmiarPola + ramka, i * rozmiarPola + ramka),
                             ((j + 1) * rozmiarPola - ramka, (i + 1) * rozmiarPola - ramka)]), fill=kolor)

    if showNumbers:
        for i in range(wys):
            for j in range(szer):
                ile = abs(stop[0] - j) + abs(stop[1] - i)
                draw.text((i * rozmiarPola + 2, j * rozmiarPola + 5), str(ile), font=font, fill=(255, 50, 50, 200))

    img.show()


def detektNumber(labirynt, number):
    for i in range(labirynt.shape[0]):
        for j in range(labirynt.shape[1]):
            if labirynt[i][j] == number:
                return [i, j]


def wczytajLabirynt(plik):
    global start, stop, labirynt
    labirynt = np.genfromtxt(plik, delimiter=";")
    start = detektNumber(labirynt, 2)
    stop = detektNumber(labirynt, 3)
    print("START:", start, "STOP:", stop)


def wybierzWszystkichNieodwiedzonychSasiadow(labirynt, x, y, odwiedzone):
    Wolne = []
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < labirynt.shape[0] and 0 <= ny < labirynt.shape[1]:
            if labirynt[nx][ny] > 0 and [nx, ny] not in odwiedzone:
                Wolne.append([nx, ny])
    return Wolne


def sledzSciezke(predecessors, labirynt, start, stop, znacznik):
    c = predecessors[stop[0]][stop[1]]
    sciezkaDoCelu = 1
    while c != start and c != [-1, -1]:
        sciezkaDoCelu += 1
        if labirynt[c[0]][c[1]] not in [2, 3]:
            labirynt[c[0]][c[1]] = znacznik
        c = predecessors[c[0]][c[1]]
    return sciezkaDoCelu


def szukacz(start, stop, labirynt, rodzaj):
    from collections import deque
    odwiedzone = []
    if rodzaj == "BFS":
        sciezka = deque([start])
    else:
        sciezka = [start]
    predecessors = [[[-1, -1] for _ in range(labirynt.shape[1])] for _ in range(labirynt.shape[0])]
    ilePolOdwiedzonych = 0

    while sciezka:
        act = sciezka.popleft() if rodzaj == "BFS" else sciezka.pop()
        if act in odwiedzone:
            continue
        odwiedzone.append(act)
        ilePolOdwiedzonych += 1
        if act == stop:
            break
        if act != start:
            labirynt[act[0]][act[1]] = 4
        for sasiad in wybierzWszystkichNieodwiedzonychSasiadow(labirynt, act[0], act[1], odwiedzone):
            if predecessors[sasiad[0]][sasiad[1]] == [-1, -1]:
                predecessors[sasiad[0]][sasiad[1]] = act
                if rodzaj == "BFS":
                    sciezka.append(sasiad)
                else:
                    sciezka.append(sasiad)

    return ilePolOdwiedzonych, predecessors


def greedy(start, stop, labirynt):
    odwiedzone = set()
    kolejka = PriorityQueue()
    kolejka.put((0, start))
    predecessors = [[[-1, -1] for _ in range(labirynt.shape[1])] for _ in range(labirynt.shape[0])]
    ilePolOdwiedzonych = 0

    while not kolejka.empty():
        _, akt = kolejka.get()
        if tuple(akt) in odwiedzone:
            continue
        odwiedzone.add(tuple(akt))
        ilePolOdwiedzonych += 1
        if akt == stop:
            break
        if akt != start:
            labirynt[akt[0]][akt[1]] = 8
        for sasiad in wybierzWszystkichNieodwiedzonychSasiadow(labirynt, akt[0], akt[1], list(odwiedzone)):
            if tuple(sasiad) not in odwiedzone:
                h = abs(stop[0] - sasiad[0]) + abs(stop[1] - sasiad[1])
                kolejka.put((h, sasiad))
                if predecessors[sasiad[0]][sasiad[1]] == [-1, -1]:
                    predecessors[sasiad[0]][sasiad[1]] = akt

    return ilePolOdwiedzonych, predecessors


def astar(start, stop, labirynt):
    odwiedzone = set()
    kolejka = PriorityQueue()
    kolejka.put((0, start))
    koszt = {tuple(start): 0}
    predecessors = [[[-1, -1] for _ in range(labirynt.shape[1])] for _ in range(labirynt.shape[0])]
    ilePolOdwiedzonych = 0

    while not kolejka.empty():
        _, akt = kolejka.get()
        if tuple(akt) in odwiedzone:
            continue
        odwiedzone.add(tuple(akt))
        ilePolOdwiedzonych += 1
        if akt == stop:
            break
        if akt != start:
            labirynt[akt[0]][akt[1]] = 9
        for sasiad in wybierzWszystkichNieodwiedzonychSasiadow(labirynt, akt[0], akt[1], list(odwiedzone)):
            new_cost = koszt[tuple(akt)] + 1
            if tuple(sasiad) not in koszt or new_cost < koszt[tuple(sasiad)]:
                koszt[tuple(sasiad)] = new_cost
                h = abs(stop[0] - sasiad[0]) + abs(stop[1] - sasiad[1])
                f = new_cost + h
                kolejka.put((f, sasiad))
                predecessors[sasiad[0]][sasiad[1]] = akt

    return ilePolOdwiedzonych, predecessors


# ====== TEST =======
wczytajLabirynt("labiryntTest2.txt")

lab1 = np.copy(labirynt)
il1, pred1 = szukacz(start, stop, lab1, "BFS")
sc1 = sledzSciezke(pred1, lab1, start, stop, 7)
rysujLabirynt(lab1)
print("BFS odwiedził", il1, "pól, ścieżka dł.", sc1)

wczytajLabirynt("labiryntTest2.txt")
lab2 = np.copy(labirynt)
il2, pred2 = greedy(start, stop, lab2)
sc2 = sledzSciezke(pred2, lab2, start, stop, 7)
rysujLabirynt(lab2)
print("Greedy odwiedził", il2, "pól, ścieżka dł.", sc2)

wczytajLabirynt("labiryntTest2.txt")
lab3 = np.copy(labirynt)
il3, pred3 = astar(start, stop, lab3)
sc3 = sledzSciezke(pred3, lab3, start, stop, 7)
rysujLabirynt(lab3)
print("A* odwiedził", il3, "pól, ścieżka dł.", sc3)
