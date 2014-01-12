from Tkinter import *
import random

health=35
magic=10
EnHealth=45
def restart():
    human.set(
def update():
    global health
    global magic
    global EnHealth
    if health<1:
        title.set('You lose')
        title2.set('') 
        health=35
        magic=10
        EnHealth=45
    if magic<1:
        title.set('You lose')
        title2.set('')
        health=35
        magic=10
        EnHealth=45
    if EnHealth<1:
        title.set('You Win!!')
        title2.set('')
        health=35
        magic=10
        EnHealth=45
        
def enemyTurn():
    turn=random.randrange(1,10);
    if turn<7:
        y=random.randrange(2,9)
        title2.set('Duke attacks you for %d damage'% (y))
        global health
        health-=y
        human.set('Health: %d'%(health))
    else:
        y=random.randrange(5,8)
        title2.set('Duke heals for %d damage'% (y))
        global EnHealth
        EnHealth+=y
        enemy.set('Enemy Health: %d'%(EnHealth))
def Attack():
    x=random.randrange(3,8)
    title.set('You attack Duke for %d damage'% (x))
    global EnHealth
    EnHealth-=x
    enemy.set('Enemy Health: %d'%(EnHealth))
    enemyTurn()
    update()
def Heal():
    x=random.randrange(4,10)
    title.set('You heal for %d damage'% (x))
    global health
    health+=x
    human.set('Health: %d'%(health))
    global magic
    z=random.randrange(1,3)
    magic-=z
    mag.set('Magic: %d'%(magic))
    enemyTurn()
    update()
def recharge():
    x=random.randrange(2,10)
    title.set('You recharge for %d magic' %x)
    global magic
    magic+=x
    mag.set('Magic: %d'%(magic))
    enemyTurn()
    update()

main=Tk()
main.title('SS13 MiniGame')
main.geometry('270x200')

btnHeal=Button(main,text='Heal', command=Heal)
btnHeal.place(x=80,y=130)

btnAttack=Button(main,text='Attack', command=Attack)
btnAttack.place(x=10,y=130)

btnRecharge=Button(main,text='Recharge Power',command=recharge)
btnRecharge.place(x=140,y=130)

human=StringVar()
human.set('Health: %d'%(health))
lblHealth=Label(main, textvariable=human)
lblHealth.place(x=15,y=100)

mag=StringVar()
mag.set('Magic: %d'%(magic))
lblMagic=Label(main, textvariable=mag)
lblMagic.place(x=90,y=100)

enemy=StringVar()
enemy.set('Enemy Health: %d'%(EnHealth))
lblEnHealth=Label(main, textvariable=enemy)
lblEnHealth.place(x=160,y=100)

title=StringVar()
title.set('New Round')
lblTitle=Label(main, textvariable=title)
lblTitle.place(x=20,y=30)

title2=StringVar()
title2.set('')
lblTitle2=Label(main, textvariable=title2)
lblTitle2.place(x=20,y=60)

lblName=Label(main, text='Duke Peteoid')
lblName.place(x=80,y=10)

mainloop()
