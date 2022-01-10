class TikTakToe:
    X='X'
    O='O'
    U=' '
    RUN=1
    STOP=0
    def __init__(self,size=3,winlen=3):
        self.size=size
        self.winlen=winlen
        self.new_game()

    def new_game(self):
        self.field=[ [TikTakToe.U for i in range(self.size)] for i in range(self.size)]
        self.cur=TikTakToe.X
        self.state=TikTakToe.RUN
        
    def flip(self):
        if self.cur==TikTakToe.X:
            self.cur=TikTakToe.O
        else:
            self.cur=TikTakToe.X
    def get(self,x,y):
        return self.field[y][x]

    def possbile_step(self,x,y):
        if self.state==TikTakToe.STOP:
            return None
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
        print(self.field)
        # check by x
        for y in range(self.size):
            winxy=[]
            winp=TikTakToe.U
            for x in range(self.size):
                cc=self.get(x,y)
                if winp == TikTakToe.U:
                    if cc == TikTakToe.U:
                        continue
                    else:
                        winp=cc
                        winxy=[(x,y)]
                else:
                    if cc == TikTakToe.U:
                        winp=cc
                        winxy=[]
                    elif cc==winp:
                        winxy.append((x,y))
                    else:
                        winp=cc
                        winxy=[(x,y)]
                if len(winxy)==self.winlen:
                    print (winp,winxy)
                    self.state=TikTakToe.STOP
                    return winp,winxy
        
        #check by y
        for x in range(self.size):
            winxy=[]
            winp=TikTakToe.U
            for y in range(self.size):
                cc=self.get(x,y)
                if winp == TikTakToe.U:
                    if cc == TikTakToe.U:
                        continue
                    else:
                        winp=cc
                        winxy=[(x,y)]
                else:
                    if cc == TikTakToe.U:
                        winp=cc
                        winxy=[]
                    elif cc==winp:
                        winxy.append((x,y))
                    else:
                        winp=cc
                        winxy=[(x,y)]
                if len(winxy)==self.winlen:
                    print (winp,winxy)
                    self.state=TikTakToe.STOP
                    return winp,winxy
        #check diag1
        for k in range(self.winlen-1,2*self.size-self.winlen):
            winxy=[]
            winp=TikTakToe.U
            for x in range(self.size):
                y=k-x
                if y<0 or y>=self.size:
                    continue
                cc=self.get(x,y)
                if winp == TikTakToe.U:
                    if cc == TikTakToe.U:
                        continue
                    else:
                        winp=cc
                        winxy=[(x,y)]
                else:
                    if cc == TikTakToe.U:
                        winp=cc
                        winxy=[]
                    elif cc==winp:
                        winxy.append((x,y))
                    else:
                        winp=cc
                        winxy=[(x,y)]
                if len(winxy)==self.winlen:
                    print (winp,winxy)
                    self.state=TikTakToe.STOP
                    return winp,winxy
                
        #check diag2
        for k in range(-self.size+self.winlen,self.size-self.winlen+1):
            winxy=[]
            winp=TikTakToe.U
            for x in range(self.size):
                y=x-k
                if y<0 or y>=self.size:
                    continue
                cc=self.get(x,y)
                if winp == TikTakToe.U:
                    if cc == TikTakToe.U:
                        continue
                    else:
                        winp=cc
                        winxy=[(x,y)]
                else:
                    if cc == TikTakToe.U:
                        winp=cc
                        winxy=[]
                    elif cc==winp:
                        winxy.append((x,y))
                    else:
                        winp=cc
                        winxy=[(x,y)]
                if len(winxy)==self.winlen:
                    print (winp,winxy)
                    self.state=TikTakToe.STOP
                    return winp,winxy
        
        return None,None
