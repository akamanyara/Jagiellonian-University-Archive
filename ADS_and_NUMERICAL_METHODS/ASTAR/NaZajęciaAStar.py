import numpy as np
import random
from queue import PriorityQueue

rozmiarKomorki=46;
rozmiarPola=45;
ramka=1;


start=1;
stop=1;
labirynt=[];


def rysujLabirynt(labirynt,showNumbers=False):
        from PIL import Image, ImageDraw, ImageFont
        szer=labirynt.shape[0]
        wys=labirynt.shape[1];
        font = ImageFont.truetype("arial.ttf", 30, encoding="unic" )


        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (wys * rozmiarKomorki, szer * rozmiarKomorki),
            "black"
        )
        draw = ImageDraw.Draw(img)
        for i in range(szer):
            for j in range(wys):
                if labirynt[i][j]==1:
                    kolor=(240, 240, 240)
                elif labirynt[i][j]==3:
                    kolor=(160, 20, 20)
                elif labirynt[i][j]==2:
                    kolor=(20, 20, 160)
                elif labirynt[i][j]==4:
                    kolor=(30, 100, 30)
                elif labirynt[i][j]==7:
                    kolor=(200, 200, 10)
                else:
                    kolor=(60, 60, 60)

                draw.rectangle(([(j * rozmiarPola + ramka, i * rozmiarPola + ramka) , ((j + 1) * rozmiarPola - ramka, (i + 1) * rozmiarPola - ramka)]),   fill=kolor)

        if showNumbers==True:
            for i in range(wys):
                for j in range(szer):
                        ile=abs(stop[0]-j)+abs(stop[1]-i)
                        draw.text((i*rozmiarPola+2, j*rozmiarPola+5), str(ile), font=font, fill=(255, 50, 50, 200))
        img.show();


def liczMetryke(labirynt,metryka):
      szer=labirynt.shape[1]
      wys=labirynt.shape[0];
      for i in range(szer):
        for j in range(wys):
            ile=abs(stop[0]-j)+abs(stop[1]-i)
            metryka[j][i]=ile;




def detektStart(labirynt):
    return detektNumber(labirynt,2)

def detektStop(labirynt):
    return detektNumber(labirynt,3)


def detektNumber(labirynt, number):
    for i in range(labirynt.shape[0]):
        for j in range(labirynt.shape[1]):
            if labirynt[i][j]==number:
                return [i,j]

def wczytajLabirynt(plik):
    global start;
    global stop;
    global labirynt;
    labirynt=np.genfromtxt(plik, delimiter=";")
    start=detektStart(labirynt)
    stop=detektStop(labirynt)
    print(start,stop)





def wybierzWszystkichNieodwiedzonychSasiadow(labirynt,x,y):
    Wolne=[];
    if x-1>=0 and labirynt[x-1][y]>0 and [x-1,y] not in odwiedzone:
        Wolne.append([x-1,y])
    if y-1>=0 and labirynt[x][y-1]>0 and [x,y-1] not in odwiedzone:
        Wolne.append([x,y-1])
    if x+1<=labirynt.shape[0]-1 and labirynt[x+1][y]>0 and [x+1,y] not in odwiedzone:
        Wolne.append([x+1,y])
    if y+1<=labirynt.shape[1]-1 and labirynt[x][y+1]>0 and [x,y+1] not in odwiedzone:
        Wolne.append([x,y+1])

    #print(Wolne)
    if len(Wolne)==0:
        return None
    return Wolne;







def szukacz(start, rodzaj):
    global ilePolOdwiedzonych;
    ilePolOdwiedzonych=1;
    odwiedzone.append(start);
    sciezka.append(start);
    iter=0;
    while len(sciezka)>0:
            # od tego czy tu będzie 0 czy nie będzie nic zależy czy mamy stos czy kolejkę, zatem BFS albo DFS
            if rodzaj=="BFS":
                act=sciezka.pop(0);
            if rodzaj=="DFS":
                act=sciezka.pop();

            if act==stop:
                break
            if act!=start:
                labirynt[act[0]][act[1]]=4;
            sasiedzi=wybierzWszystkichNieodwiedzonychSasiadow(labirynt,act[0],act[1]);
            odwiedzone.append(act)
            ilePolOdwiedzonych+=1;
            iter+=1;
            if sasiedzi!=None:
                random.shuffle(sasiedzi); #mieszamy kolejnosc na liscie sasiadow, dla BFS to nie ma praktycznie znaczenia, dla DFS potrzebujemy tej losowosci
                for i in range(len(sasiedzi)):
                    sasiad=sasiedzi[i];
                    sciezka.append(sasiad)
                    predecessors[sasiad[0]][sasiad[1]]=act;



def BFS(start):
    szukacz(start,"BFS");

def DFS(start):
    szukacz(start,"DFS");


def sledzSciezke():
    global sciezkaDoCelu;
    sciezkaDoCelu=1;
    c=predecessors[stop[0]][stop[1]]
    while c!=start:
        sciezkaDoCelu+=1;
        labirynt[c[0]][c[1]]=7;
        c=predecessors[c[0]][c[1]]



wczytajLabirynt("labiryntTest2.txt")
#rysujLabirynt(labirynt,True)
predecessors=[[[-1,-1] for i in range(labirynt.shape[1])] for j in range(labirynt.shape[0])]
metryka=[[-1 for i in range(labirynt.shape[1])] for j in range(labirynt.shape[0])]
kosztDojsciaDoPola=[[0 for i in range(labirynt.shape[1])] for j in range(labirynt.shape[0])]
odwiedzone=[];
sciezka=[];
ilePolOdwiedzonych=0;
liczMetryke(labirynt,metryka)

DFS(start)


sledzSciezke();
rysujLabirynt(labirynt,False)

print("Algorytm odwiedził", ilePolOdwiedzonych);
print("Sciezka do celu ma", sciezkaDoCelu)
