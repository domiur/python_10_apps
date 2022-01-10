from tkinter import *
from ttt_backend import TikTakToe

game=TikTakToe(4,3)

window=Tk()
window.title('TikTakToe')

class Button1(Button):
    def proc(self):
        c=game.possbile_step(self.x,self.y)
        if c is not None:
            self['text']=c
        winp,winxy=game.check_win()
        if winp is not None:
            for (x,y) in winxy:
                but[y][x]['bg']='red'
    def pos(self,x,y):
        self.x=x
        self.y=y
        self['command']=self.proc
    

but=[[ Button1(window,text=game.field[y][x],width=10,height=6)  for x in range(game.size)] for y in range(game.size)]
for y in range(game.size):
    for x in range(game.size):
        but[y][x].pos(x,y)
        print(but[y][x]['bg'])
        

#but=[[ Button(window,text=str(y*game.size+x),width=10,height=6)  for y in range(game.size)] for x in range(game.size)]
for y in range(game.size):
    for x in range(game.size):
        but[x][y].grid(row=y,column=x)

def new_game():
    game.new_game()
    for y in range(game.size):
        for x in range(game.size):
            but[y][x]['text']=TikTakToe.U
            but[y][x]['bg']='#d9d9d9'


but_new=Button(window,text="New game",height=4,command=new_game)
but_close=Button(window,text=" Close  ",height=4,command=window.destroy)
but_new.grid(row=0,column=game.size+1,sticky="ew")
but_close.grid(row=1, column=game.size+1,sticky="ew")

window.mainloop()
