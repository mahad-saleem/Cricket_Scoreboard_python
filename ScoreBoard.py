from tkinter import *
import os


######################################################################################################################################################################


class Scoreboard:

    def __init__(self):
        def OnFrameConfigure(event):
            self.canvas.configure(scrollregion=self.screen.bbox("all"))


        self.master=Tk()
        self.w=self.master.winfo_screenwidth()
        self.h=self.master.winfo_screenheight()

    

        self.canvas = Canvas(self.master,borderwidth=0)
        self.screen=Frame(self.canvas)
        self.vsb = Scrollbar(self.master, command=self.canvas.yview)
        self.canvas.place(x=2,y=0)
        self.canvas.config(width=1200, height=700)                
        self.canvas.config(yscrollcommand=self.vsb.set)
        self.vsb.place(x=1320,y=0,height=660)
        self.canvas.create_window((4,4),window=self.screen,anchor='nw',tags="self.screen")
        self.screen.bind("<Configure>",OnFrameConfigure)

        
        self.master.resizable(width=False,height=False)
        self.master.wm_title("SCORE BOARD         BY BSCS14002 & BSCS14008")
        self.master.geometry('%dx%d-0-50'%(self.w-30,self.h-70))

        
        self.main=Label(self.screen,text="SCORE BOARD",font="Arial 20 bold underline")
        self.main.grid(row=0,column=5)
        self.empty1=Label(self.screen,text="              ",width=40)
        self.empty1.grid(row=0,column=4)
        self.empty=Label(self.screen,text=" ")
        self.empty.grid(row=1,column=0)

        self.MatchDir=os.path.dirname(os.path.realpath(__file__))
        self.MatchList=[]
        self.MatchTemp=[]
        self.MatchListFinal=[]
        
        for file in os.listdir(self.MatchDir):
            if file.endswith(".txt"):
                self.MatchTemp.append(file)
            
        for i in range(0,len(self.MatchTemp)):
            self.MatchList.append(str(self.MatchTemp[i])[:-4])
            
        for i in range(0,len(self.MatchList)):
            self.NameString=str(self.MatchList[i])
            self.x=int(len(self.NameString))-1
            if self.NameString[int(self.x)].isdigit()==True:
                self.MatchListFinal.append(self.MatchList[i])
        print(self.MatchListFinal)
            
        self.select=Label(self.screen,text="PLEASE CHOOSE A MATCH:",anchor=W,justify=LEFT)
        self.select.grid(row=2,column=0)
        self.option=StringVar(self.screen)
        self.option.set("Choose")
        self.drop=OptionMenu(self.screen,self.option,*self.MatchListFinal)
        self.drop.grid(row=3,column=0)
        self.butt=Button(self.screen,text='OK',width=10,command=lambda:Summary(self.screen,self.master,self.option))
        self.butt.grid(row=3,column=1,padx=20,pady=20)
    
        
######################################################################################################################################################################
##
##    def Choose(self):
##        self.chosen=[]
##        for i in range(0,len(self.MatchListFinal)):
##            if (self.option.get())==self.MatchListFinal[i]:
##                self.chosen.append(self.MatchListFinal[i])
####                self.team1team2=[]
####                self.team1team2.append(self.MatchListFinal[i])
####                self.Team1Dir=self.TeamDir+str("\\")+str(self.teamss2[i])
##                x=open(self.Team1Dir,'r')
##                y=x.read()
##                self.z=y.split('\n')
##                self.label1=Label(self.master,text='Player 1',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=5,column=0,sticky=W)
##                self.player1=StringVar(self.master)
##                self.player1.set("Choose")
##                self.player1option=OptionMenu(self.master,self.player1,*self.z)
##                self.player1option.grid(row=5,column=1,sticky=W)
##                self.next=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose1(self)).grid(row=5,column=2,padx=20)
##        self.teamss.remove(self.teams.get())
##        self.teamss2.remove(self.teams.get()+str('.txt'))

class Summary:
    def refresh(self):
        self.x=open(self.option.get()+" - CurrentMatchInfo.txt",'r')
        self.y=self.x.read()
        self.z=self.y.split('\n')
        self.runy.set(str(self.z[1]))
        self.ini.set(str(self.z[0]))
        self.wici.set(10-int(self.z[3]))
        self.ovi.set(str(self.z[2]))

        self.userin=str(self.ovi.get())
        self.userin1=str(self.userin[:-2])
        self.userin2=str(self.userin[len(self.userin)-1])
        self.userin1=int(self.userin1)
        self.userin2=int(self.userin2)
        self.BallsPlayed=((self.userin1)*6)+(self.userin2)
        self.ballss.set(str(self.BallsPlayed))

##        self.userin.set(self.ovi)
##        self.userin1.set(self.userin[:-2])
##        self.userin2.set(self.userin[len(self.userin)-1])
##        self.userin1.set(self.userin1)
##        self.userin2.set(self.userin2)
##        self.ballss.set((self.userin1)*6+(self.userin2))
        
        self.batty.set(str(self.z[4]))
        self.bowly.set(str(self.z[5]))
        self.screen.after(1000 , self.refresh)
    def __init__(self,screen,master,option):
        self.screen=screen
        self.master=master
        self.option=option
        self.screen.destroy()
        global canvas
        self.canvas=Canvas(self.master,borderwidth=0)
        self.screen=Frame(self.canvas)
        self.canvas.place(x=2,y=0)
        self.canvas.config(width=1200, height=700)
        self.canvas.create_window((4,4),window=self.screen,anchor='nw',tags="self.screen")
#########################################################################
        
        self.ballss=StringVar(self.screen)
        self.ballss.set("  ")
        self.runy=StringVar(self.screen)
        self.runy.set("  ")
        self.userin=StringVar(self.screen)
        self.userin.set("  ")
        self.userin1=StringVar(self.screen)
        self.userin1.set("  ")
        self.userin2=StringVar(self.screen)
        self.userin2.set("  ")
        self.ini=StringVar(self.screen)
        self.ini.set("  ")
        self.wici=StringVar(self.screen)
        self.wici.set("  ")
        self.ovi=StringVar(self.screen)
        self.ovi.set("  ")
        self.batty=StringVar(self.screen)
        self.batty.set("  ")
        self.bowly=StringVar(self.screen)
        self.bowly.set("  ")
        self.main=Label(self.screen,text="SCORE BOARD",font="Arial 20 bold underline").grid(row=0,column=4,stick=W)
        self.loading=Label(self.screen,text="WELCOME TO MATCH!!",anchor=W,justify=LEFT,font="Arial 10 bold").grid(row=1,column=3,sticky=W,pady=20)
        self.select=Label(self.screen,textvariable=self.ini,anchor=W,justify=LEFT,font='Arial 8 bold').grid(row=2,column=0,sticky=W,pady=20)
        self.batside=Label(self.screen,text="BATTING SIDE:",anchor=W,justify=LEFT,font='Arial 8 bold').grid(row=3,column=0,sticky=W)
        self.batteam=Label(self.screen,textvariable=self.batty,anchor=W,justify=LEFT,width=20).grid(row=3,column=1,sticky=W)
        self.bowlside=Label(self.screen,text="BOWLING SIDE:",anchor=W,justify=LEFT,width=23,font='Arial 8 bold').grid(row=3,column=2)
        self.bowlteam=Label(self.screen,textvariable=self.bowly,anchor=W,justify=LEFT).grid(row=3,column=3,sticky=W)
        self.status=Label(self.screen,text="CURRENT STATUS",anchor=W,justify=LEFT,font="Arial 10 underline").grid(row=6,column=3,sticky=W,pady=20)
        self.score=Label(self.screen,text="SCORE:",anchor=W,justify=LEFT,font='Arial 8 bold').grid(row=7,column=0,sticky=W,pady=5)
        self.scorecount=Label(self.screen,textvariable=self.runy,anchor=W,justify=LEFT).grid(row=7,column=1,sticky=W,pady=5)
        self.wickets=Label(self.screen,text="WICKETS:",anchor=W,justify=LEFT,font='Arial 8 bold').grid(row=8,column=0,sticky=W,pady=5)
        self.wicketscount=Label(self.screen,textvariable=self.wici,anchor=W,justify=LEFT).grid(row=8,column=1,sticky=W,pady=5)
        self.overs=Label(self.screen,text="OVERS PLAYED:",anchor=W,justify=LEFT,font='Arial 8 bold').grid(row=9,column=0,sticky=W,pady=5)
        self.overscount=Label(self.screen,textvariable=self.ovi,anchor=W,justify=LEFT).grid(row=9,column=1,sticky=W,pady=5)
        self.balls=Label(self.screen,text="BALLS PLAYED:",anchor=W,justify=LEFT,font='Arial 8 bold').grid(row=10,column=0,sticky=W,pady=5)
        self.ballscount=Label(self.screen,textvariable=self.ballss,anchor=W,justify=LEFT).grid(row=10,column=1,sticky=W,pady=5)
        self.battbutt=Button(self.screen,text="FULL SCOREBOARD",font="Arial 20 bold underline",width=20,command=lambda:FullScoreBoard(self.screen,self.master,self.option))
        self.battbutt.grid(row=11,column=4,sticky=E)
        
        Summary.refresh(self)

#####################################################################################################################################################################

class FullScoreBoard:
    def refresh(self):
        self.a=open(self.option.get()+" - BatsmanInfo.txt",'r')
        self.b=self.a.read()
        self.c=self.b.split('**********')
        self.d=self.c[0].split('\n')
        self.d1=self.c[1].split('\n')
        self.d2=self.c[2].split('\n')
        self.d3=self.c[3].split('\n')
        self.d4=self.c[4].split('\n')
        self.d5=self.c[5].split('\n')
        self.d6=self.c[6].split('\n')
        self.d7=self.c[7].split('\n')
        self.d8=self.c[8].split('\n')
        self.d9=self.c[9].split('\n')
        self.d10=self.c[10].split('\n')
        print(self.c)
        self.name.set(str(self.d[0]))
        self.name1.set(str(self.d1[1]))
        self.name2.set(str(self.d2[1]))
        self.name3.set(str(self.d3[1]))
        self.name4.set(str(self.d4[1]))
        self.name5.set(str(self.d5[1]))
        self.name6.set(str(self.d6[1]))
        self.name7.set(str(self.d7[1]))
        self.name8.set(str(self.d8[1]))
        self.name9.set(str(self.d9[1]))
        self.name10.set(str(self.d10[1]))
        
##        self.ini.set(str(self.z[0]))
##        self.wici.set(10-int(self.z[3]))
##        self.ovi.set(str(self.z[2]))

        self.screen.after(1000 , self.refresh)
    def __init__(self,screen,master,option):
        def OnFrameConfigure(event):
            self.canvas.configure(scrollregion=self.screen.bbox("all"))
        self.option=option
        self.screen=screen
        self.master=master
        self.screen.destroy()
        global canvas
        self.canvas=Canvas(self.master,borderwidth=0)
        self.screen=Frame(self.canvas)
        self.canvas.place(x=2,y=0)
        self.canvas.config(width=1200, height=700)
        self.canvas.create_window((4,4),window=self.screen,anchor='nw',tags="self.screen")
        
        self.scrollbar=Scrollbar(self.master,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=1320,y=0,height=660)
        self.screen.bind("<Configure>",OnFrameConfigure)
        ############################################################################
    
        #####################################################
##        self.ballss=StringVar(self.screen)
##        self.ballss.set("  ")
        self.name=StringVar(self.screen)
        self.name.set("  ")
        self.name1=StringVar(self.screen)
        self.name1.set("  ")
        self.name2=StringVar(self.screen)
        self.name2.set("  ")
        self.name3=StringVar(self.screen)
        self.name3.set("  ")
        self.name4=StringVar(self.screen)
        self.name4.set("  ")
        self.name5=StringVar(self.screen)
        self.name5.set("  ")
        self.name6=StringVar(self.screen)
        self.name6.set("  ")
        self.name7=StringVar(self.screen)
        self.name7.set("  ")
        self.name8=StringVar(self.screen)
        self.name8.set("  ")
        self.name9=StringVar(self.screen)
        self.name9.set("  ")
        self.name10=StringVar(self.screen)
        self.name10.set("  ")
        
##        self.userin=StringVar(self.screen)
##        self.userin.set("  ")
##        self.userin1=StringVar(self.screen)
##        self.userin1.set("  ")
##        self.userin2=StringVar(self.screen)
##        self.userin2.set("  ")
##        self.ini=StringVar(self.screen)
##        self.ini.set("  ")
##        self.wici=StringVar(self.screen)
##        self.wici.set("  ")
##        self.ovi=StringVar(self.screen)
##        self.ovi.set("  ")
        ######################################################
        self.fullcard=Label(self.screen,text="FULL SCORECARD",anchor=W,justify=LEFT,font="Arial 20 bold underline").grid(row=0,column=3,sticky=W,pady=20)
        self.bs=Label(self.screen,text="BATTING SIDE:",anchor=W,justify=LEFT,width=25).grid(row=1,column=0,sticky=W)
        self.bsname=Label(self.screen,text="   ",anchor=W,justify=LEFT,width=25).grid(row=1,column=1,sticky=W)
        self.player0=Label(self.screen,text="PLAYER NAME",anchor=W,justify=LEFT,font="Arial 10 underline",width=25).grid(row=2,column=0,sticky=W,pady=5)
        self.runs=Label(self.screen,text="RUNS",anchor=W,justify=LEFT,font="Arial 10 underline").grid(row=2,column=1,sticky=W,pady=5)
        self.balls=Label(self.screen,text="BALLS FACED",anchor=W,justify=LEFT,font="Arial 10 underline",width=20).grid(row=2,column=2,sticky=W,pady=5)
        self.out=Label(self.screen,text="OUT",anchor=W,justify=LEFT,font="Arial 10 underline",width=25).grid(row=2,column=3,sticky=W,pady=5)
        self.by=Label(self.screen,text="BY",anchor=W,justify=LEFT,font="Arial 10 underline",width=25).grid(row=2,column=4,sticky=W,pady=5)
        self.line=Label(self.screen,text="__________",anchor=W,justify=LEFT,font="Arial 10 underline").grid(row=14,column=3,pady=20)


        self.bs1=Label(self.screen,text="BOWLING SIDE:",anchor=W,justify=LEFT,width=25).grid(row=15,column=0,sticky=W)
        self.bsname1=Label(self.screen,text="   ",anchor=W,justify=LEFT,width=25).grid(row=15,column=1,sticky=W)
        self.player00=Label(self.screen,text="PLAYER NAME",anchor=W,justify=LEFT,font="Arial 10 underline",width=25).grid(row=16,column=0,sticky=W,pady=5)
        self.runs1=Label(self.screen,text="OVERS",anchor=W,justify=LEFT,font="Arial 10 underline").grid(row=16,column=1,sticky=W,pady=5)
        self.balls1=Label(self.screen,text="WICKETS",anchor=W,justify=LEFT,font="Arial 10 underline",width=20).grid(row=16,column=2,sticky=W,pady=5)
        self.out1=Label(self.screen,text="MAIDENS",anchor=W,justify=LEFT,font="Arial 10 underline",width=25).grid(row=16,column=3,sticky=W,pady=5)
        self.by1=Label(self.screen,text="ECONOMY",anchor=W,justify=LEFT,font="Arial 10 underline",width=25).grid(row=16,column=4,sticky=W,pady=5)
        self.battbutt=Button(self.screen,text="SUMMARY",font="Arial 20 bold underline",width=20,command=lambda:Summary(self.screen,self.master,self.option))#,self.main,self.select,self.loading,self.batside,self.batteam,self.bowlside,self.bowlteam,self.status,self.score,self.scorecount,self.wickets,self.wicketscount,self.overs,self.overscount,self.
        self.battbutt.grid(row=29,column=3)

        self.player1=Label(self.screen,textvariable=self.name,anchor=W,justify=LEFT).grid(row=3,column=0,sticky=W,pady=5)
        self.player2=Label(self.screen,textvariable=self.name1,anchor=W,justify=LEFT).grid(row=4,column=0,sticky=W,pady=5)
        self.player3=Label(self.screen,textvariable=self.name2,anchor=W,justify=LEFT).grid(row=5,column=0,sticky=W,pady=5)
        self.player4=Label(self.screen,textvariable=self.name3,anchor=W,justify=LEFT).grid(row=6,column=0,sticky=W,pady=5)
        self.player5=Label(self.screen,textvariable=self.name4,anchor=W,justify=LEFT).grid(row=7,column=0,sticky=W,pady=5)
        self.player6=Label(self.screen,textvariable=self.name5,anchor=W,justify=LEFT).grid(row=8,column=0,sticky=W,pady=5)
        self.player7=Label(self.screen,textvariable=self.name6,anchor=W,justify=LEFT).grid(row=9,column=0,sticky=W,pady=5)
        self.player8=Label(self.screen,textvariable=self.name7,anchor=W,justify=LEFT).grid(row=10,column=0,sticky=W,pady=5)
        self.player9=Label(self.screen,textvariable=self.name8,anchor=W,justify=LEFT).grid(row=11,column=0,sticky=W,pady=5)
        self.player10=Label(self.screen,textvariable=self.name9,anchor=W,justify=LEFT).grid(row=12,column=0,sticky=W,pady=5)
        self.player11=Label(self.screen,textvariable=self.name10,anchor=W,justify=LEFT).grid(row=13,column=0,sticky=W,pady=5)

        self.player01=Label(self.screen,text="test1",anchor=W,justify=LEFT).grid(row=18,column=0,sticky=W,pady=5)
        self.player02=Label(self.screen,text="test2",anchor=W,justify=LEFT).grid(row=19,column=0,sticky=W,pady=5)
        self.player03=Label(self.screen,text="test3",anchor=W,justify=LEFT).grid(row=20,column=0,sticky=W,pady=5)
        self.player04=Label(self.screen,text="test4",anchor=W,justify=LEFT).grid(row=21,column=0,sticky=W,pady=5)
        self.player05=Label(self.screen,text="test5",anchor=W,justify=LEFT).grid(row=22,column=0,sticky=W,pady=5)
        self.player06=Label(self.screen,text="test6",anchor=W,justify=LEFT).grid(row=23,column=0,sticky=W,pady=5)
        self.player07=Label(self.screen,text="test7",anchor=W,justify=LEFT).grid(row=24,column=0,sticky=W,pady=5)
        self.player08=Label(self.screen,text="test8",anchor=W,justify=LEFT).grid(row=25,column=0,sticky=W,pady=5)
        self.player09=Label(self.screen,text="test9",anchor=W,justify=LEFT).grid(row=26,column=0,sticky=W,pady=5)
        self.player010=Label(self.screen,text="test10",anchor=W,justify=LEFT).grid(row=27,column=0,sticky=W,pady=5)
        self.player011=Label(self.screen,text="test11",anchor=W,justify=LEFT).grid(row=28,column=0,sticky=W,pady=5)

        FullScoreBoard.refresh(self)

#######################################################################################################################################################################

##
##master=Tk()
##w=master.winfo_self.screenwidth()
##h=master.winfo_self.screenheight()
##
##def OnFrameConfigure(event):
##    canvas.configure(scrollregion=self.screen.bbox("all"))
##
##canvas = Canvas(master,borderwidth=0)
##self.screen=Frame(canvas)
##vsb = Scrollbar(master, command=canvas.yview)
##canvas.place(x=2,y=0)
##canvas.config(width=1200, height=700)                
##canvas.config(yscrollcommand=vsb.set)
##vsb.place(x=1320,y=0,height=660)
##canvas.create_window((4,4),window=self.screen,anchor='nw',tags="self.screen")
##self.screen.bind("<Configure>",OnFrameConfigure)

score=Scoreboard()

##master.resizable(width=False,height=False)
##master.wm_title("SCORE BOARD         BY BSCS14002 & BSCS14008")
##master.geometry('%dx%d-0-50'%(w-30,h-100))
##master.mainloop()


