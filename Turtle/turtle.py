# coding: utf-8
from turtle import *
from random import randint
speed(0)


def rdc(couleur,porte):
    fillcolor(couleur)
    liste=["f","f","f"]
    a=randint(0,2)
    liste[a]="p"
    down()
    
    begin_fill()
    for i in range(2):
        fd(140)
        rt(90)
        fd(60)
        rt(90)
    up()
    fd(15)
    rt(90)
    fd(10)
    end_fill()
    for i in liste:
        down()  
        if i=="f":
            fillcolor("white")
            begin_fill()
            for i in range(4):
                fd(30)
                lt(90)
            up()
            lt(90)
            fd(40)
            rt(90)
            end_fill()
            
        if i=="p":
            fillcolor(porte)
            begin_fill()
            down()
            z=randint(1,2)
            if z==1:
                for i in range(2):                    
                    fd(50)
                    lt(90)
                    fd(30)
                    lt(90)
                up()
                lt(90)
                fd(40)
                rt(90)
                end_fill()
                
            else:
                begin_fill()
                up()
                fd(15)
                down()
                fd(35)
                lt(90)
                fd(30)
                lt(90)
                fd(35)
                circle(15,180)
                up()
                rt(180)
                fd(15)
                rt(90)
                fd(40)
                rt(90)
    up()
    lt(90)
    fd(5)
    lt(90)
    fd(10)

def etage(couleur):
    fillcolor(couleur)
    b=-1
    liste=[]
    for i in range(3):
        a=randint(1,2)
        if a==1:
            liste.append("p")
        else:
            liste.append("f")
    begin_fill()
    down()
    fd(60)
    lt(90)
    fd(140)
    lt(90)
    fd(60)
    end_fill()
    up()
    lt(180)
    fd(50)
    rt(90)
    fd(15)
    rt(90)
    for i in range(3):
        down()
        b=b+1
        if liste[b]=="p":
            fillcolor("white")
            begin_fill()
            for i in range(2):
                fd(50)
                lt(90)
                fd(30)
                lt(90)
            end_fill()
            fd(25)
            lt(90)
            fd(30)
            rt(180)
            for i in range(5):
                width(2)
                fd(3)
                lt(90)
                fd(25)
                rt(90)
                fd(3)
                rt(90)
                fd(25)
                lt(90)
            up()
            rt(90)
            fd(25)
            rt(90)
            fd(40)
            rt(90)
        
        if liste[b]=="f":
            fillcolor("white")
            begin_fill()
            for i in range(4):
                fd(30)
                lt(90)
            up()
            lt(90)
            fd(40)
            rt(90)
            end_fill()
            
    up()
    lt(90)
    fd(5)
    lt(90)
    fd(10)
def toit():
    z=randint(1,2)
    if z==1: 
        fillcolor("black")
        begin_fill()
        down()
        rt(90)
        fd(5)
        lt(90)
        fd(10)
        lt(90)
        fd(150)
        lt(90)
        fd(10)
        lt(90)
        fd(5)
        end_fill()
    elif z==2:
        fillcolor("black")
        begin_fill()
        pd()
        longueur_cote=150
        rt(90)
        fd(5)
        lt(360/3)
        fd(longueur_cote)
        lt(360/3)
        fd(longueur_cote)
        lt(360/3)
        fd(5)
        end_fill()

      
def principale():
    couleur=["black","grey","red","orange","green","blue","navy","yellow","gold","tan","brown","sienna","wheat","cyan","pink","salmon","violet","purple"]
    couleurchoisie=couleur[randint(0,len(couleur)-1)]
    up()
    goto(-333,-100)
    for i in range(4):
        couleurchoisie=couleur[randint(0,len(couleur)-1)]
        couleurporte=couleur[randint(0,len(couleur)-1)]
        a=randint(0,4)
        rdc(couleurchoisie,couleurporte)
        for i in range(a):
            etage(couleurchoisie)
        toit()
        rt(90)
        fd(60+60*a)
        lt(90)
        fd(170)
        up()
        lt(90)
        fd(60)
        rt(90)
    done()
        
principale()


