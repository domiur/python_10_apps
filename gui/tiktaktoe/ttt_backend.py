class TikTakToe:
    X='X'
    O='O'
    U=' '
    def __init__(self,size=3,winlen=3):
        self.size=size
        self.winlen=winlen
        self.new_game()
        self.cur=TikTakToe.X

    def new_game(self):
        self.field=[ [TikTakToe.U for i in range(self.size)] for i in range(self.size)]
        #self.field=[ [str(x*self.size+y) for x in range(self.size)] for y in range(self.size)]

    def flip(self):
        if self.cur==TikTakToe.X:
            self.cur=TikTakToe.O
        else:
            self.cur=TikTakToe.X
    def get(self,x,y):
        return self.field[y][x]

    def possbile_step(self,x,y):
        if self.field[y][x]==TikTakToe.U:
            c=self.cur
            self.field[y][x]=self.cur
            self.flip()
            return c
        else:
            return None

    def get_cur(self):
        return self.cur

    def check_win(self):
        for y in range(self.size):
            win={TikTakToe.X:[],
                 TikTakToe.O:[]
                }
            prev=None
            for x in range(self.size):
                if prev is not None:
                else:
                    prev=self.get(x,y)

            
            

