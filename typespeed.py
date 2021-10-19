from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry('800x600+300+50')
root.title('Tahsan Nayem [Python_Programmer')

root.configure(bg='black')
words = ['Mao sir','Ekramul-Hossain','Mahfuz sir','Mustakim sir','Fazlul sir','Bijoy sir','Noob-Hacker','Cyberking','CyberNinja','THBD','Termux','kali-Linux','Tahsan','Nayem']
random.shuffle(words)
########## function section
def welcomeLabel():
    global count,sliderWrod
    text = 'Welcome To Typing Speed Testing Game'
    if(count >= len(text)):
        count=0
        sliderWrod=''
    sliderWrod += text[count]
    count += 1
    titleLabel.configure(text=sliderWrod)
    titleLabel.after(140,welcomeLabel)


def startGame(event):
    global score,miss
    if(timeLeft == 60):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreCountLabel.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)

def time():
    global timeLeft,score,miss
    if(timeLeft >=11):
        pass
    else:
        timeCountLabel.configure(fg='red')
    if(timeLeft >0):
        timeLeft -= 1
        timeCountLabel.configure(text=timeLeft)
        timeCountLabel.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        notific = messagebox.askretrycancel('Notification','Play Again Please click Retry !')
        if(notific==True):
            score=0
            timeLeft=60
            miss=0
            timeCountLabel.configure(text=timeLeft)
            wordLabel.configure(text=words[0])
            scoreCountLabel.configure(text=score)
########## variables
score = 0
miss = 0
timeLeft = 60
count = 0
sliderWrod = ''

############## label section
titleLabel = Label(root,text='',bg='black',fg='green',font=('arial',30,'italic bold'),width=33)
titleLabel.place(x=10,y=10)
welcomeLabel()

scoreLabel = Label(root,text='Your Score :',bg='black',fg='white',font=('arial',25,'italic bold'))
scoreLabel.place(x=10,y=100)
scoreCountLabel = Label(root,text=score,bg='black',fg='white',font=('arial',25,'italic bold'))
scoreCountLabel.place(x=80,y=180)

timeLabel = Label(root,text='Time Left :',bg='black',fg='white',font=('arial',25,'italic bold'))
timeLabel.place(x=600,y=100)
timeCountLabel = Label(root,text=timeLeft,bg='black',fg='white',font=('arial',25,'italic bold'))
timeCountLabel.place(x=680,y=180)

wordLabel = Label(root,text=words[0],bg='black',fg='blue',font=('arial',35,'italic bold'))
wordLabel.place(x=250,y=200)

############## Entry Section
wordEntry = Entry(root,font=('arial',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=200,y=300)
wordEntry.focus_set()


######## game play detail label
gamePlayDetailLabel = Label(root,text='Type Word And Hit Enter Button',bg='black',fg='powder blue',font=('arial',30,'italic bold'))
gamePlayDetailLabel.place(x=100,y=450)

root.bind('<Return>',startGame)
root.mainloop()




