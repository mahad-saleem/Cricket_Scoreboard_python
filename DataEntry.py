from tkinter import *
import os
import datetime
def OnFrameConfigure(event):
    cnv.configure(scrollregion=cnv.bbox("all"))
def OnFrameConfigure2(event):
    cnv.configure(scrollregion=cnv.bbox("all"))


class Options:

    def __init__(self,master):
        Team1=['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6','Player 7','Player 8','Player 9','Player 10','Player 11']
        Team2=['2Player 1','2Player 2','2Player 3','2Player 4','2Player 5','2Player 6','2Player 7','2Player 8','2Player 9','2Player 10','2Player 11']
        BattingSide="Team 1"
        Opener1Var="Player 1"
        Opener2Var="Player 2"
        self.MAINHeader=Label(master, text='Please select an option',width=40,anchor=W,justify=LEFT,font="Arial 10 bold")
        self.MAINHeader.grid(row=0,column=0,pady=20,sticky=W)
        self.New=Button(master,text='NEW MATCH',command=lambda:NewMatch(master,self.MAINHeader,self.New,self.Old),width=10)
        self.New.grid(row=0,column=1,padx=20)
        self.Old=Button(master,text='OLD MATCH',width=10)#,command=lambda:OldMatch(master,Team1,Team2,BattingSide,Opener1Var,Opener2Var))
        self.Old.grid(row=0,column=2,padx=20)
###############################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################

class NewMatch:
    def __init__(self,master,b1,b2,b3):
        self.MaximumBallsODI=300
        self.MaximumBallsT20=120
        self.OverLimitODI=10
        self.OverLimitT20=4
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        self.NEWHeader=Label(master,text='NEW MATCH TYPE',width=40,anchor=W,justify=LEFT,font="Arial 10 bold")
        self.NEWHeader.grid(row=1,column=0,sticky=W,pady=20)
        self.ODI=Button(master,text='ONE DAY',command=lambda:MatchInfo(master,self.NEWHeader,self.ODI,self.T20,type='ODI'),width=10)
        self.ODI.grid(row=1,column=1,padx=20,pady=20)
        self.T20=Button(master,text='T20',width=10,command=lambda:MatchInfo(master,self.NEWHeader,self.ODI,self.T20,type='T20'))
        self.T20.grid(row=1,column=2,padx=20)
###############################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################

class MatchInfo:
    def __init__(self,master,b1,b2,b3,type):
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        self.InningNum=1
        self.master=master
        self.alpha=''
        global cnv
        self.TeamDir=os.path.dirname(os.path.realpath(__file__))+str('\Teams')
        self.teamss=[]
        self.teamss2=[]
        for file in os.listdir(self.TeamDir):
            if file.endswith(".txt"):
                self.teamss2.append(file)
        for i in range(0,len(self.teamss2)):
            self.teamss.append(str(self.teamss2[i])[:-4])
        self.type=type
        if self.type=='ODI':
            self.ODIHeader=Label(master,text='ODI (300 Balls per Innings)',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=2,column=0,sticky=W,pady=20)
        else:
            self.T20Header=Label(master,text='T20 (120 Balls per Innings)',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=2,column=0,sticky=W,pady=20)
        self.Venue=Label(master,text='Please enter the VENUE',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=3,column=0,sticky=W,pady=20)
        self.VenueEnter=Entry(master,width=25)
        self.VenueEnter.grid(row=3,column=1,sticky=W)
        self.VenueSave=Button(master,text='SAVE',width=45,command=lambda:MatchInfo.TeamSelection(self)).grid(row=3,column=2,padx=70,pady=20)

    def TeamSelection(self):
        self.alpha=str(self.VenueEnter.get())
        if len(self.alpha)>0:
            self.Team1=Label(self.master,text='Please Choose TEAM 1',width=40,anchor=W,justify=LEFT,font="Arial 10 bold").grid(row=4,column=0,sticky=W,pady=20)
            self.teams=StringVar(self.master)
            self.teams.set("Choose")
            self.teamsoption=OptionMenu(self.master,self.teams,*self.teamss)
            self.teamsoption.grid(row=4,column=1,padx=0,pady=5,sticky=W)
            self.Team1Save=Button(self.master,text='OK',width=10,command=lambda:MatchInfo.Choose(self)).grid(row=4,column=2,padx=20,pady=20)
        else:
            self.VenueEnter.focus_set()
            self.ErrorL=Label(self.master,text='Please enter a venue').grid(row=3,column=4,sticky=W,pady=20)
        self.chosen=[]

    def Choose(self):
        for i in range(0,len(self.teamss)):
            if (self.teams.get())==self.teamss[i]:
                self.chosen.append(self.teamss[i])
                self.team1team2=[]
                self.team1team2.append(self.teamss[i])
                self.Team1Dir=self.TeamDir+str("\\")+str(self.teamss2[i])
                x=open(self.Team1Dir,'r')
                y=x.read()
                self.z=y.split('\n')
                self.label1=Label(self.master,text='Player 1',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=5,column=0,sticky=W)
                self.player1=StringVar(self.master)
                self.player1.set("Choose")
                self.player1option=OptionMenu(self.master,self.player1,*self.z)
                self.player1option.grid(row=5,column=1,sticky=W)
                self.next=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose1(self)).grid(row=5,column=2,padx=20)
        self.teamss.remove(self.teams.get())
        self.teamss2.remove(self.teams.get()+str('.txt'))

    def Choose1(self):
        self.chosen.append(self.player1.get())
        self.z.remove(self.player1.get())
        self.label2=Label(self.master,text='Player 2',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=6,column=0,sticky=W)
        self.player2=StringVar(self.master)
        self.player2.set("Choose")
        self.player2option=OptionMenu(self.master,self.player2,*self.z)
        self.player2option.grid(row=6,column=1,sticky=W)
        self.next1=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose2(self)).grid(row=6,column=2,padx=20)

    def Choose2(self):
        self.chosen.append(self.player2.get())
        self.z.remove(self.player2.get())
        self.label3=Label(self.master,text='Player 3',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=7,column=0,sticky=W)
        self.player3=StringVar(self.master)
        self.player3.set("Choose")
        self.player3option=OptionMenu(self.master,self.player3,*self.z)
        self.player3option.grid(row=7,column=1,sticky=W)
        self.next2=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose3(self)).grid(row=7,column=2,padx=20)

    def Choose3(self):
        self.chosen.append(self.player3.get())
        self.z.remove(self.player3.get())
        self.label4=Label(self.master,text='Player 4',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=8,column=0,sticky=W)
        self.player4=StringVar(self.master)
        self.player4.set("Choose")
        self.player4option=OptionMenu(self.master,self.player4,*self.z)
        self.player4option.grid(row=8,column=1,sticky=W)
        self.next3=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose4(self)).grid(row=8,column=2,padx=20)

    def Choose4(self):
        self.chosen.append(self.player4.get())
        self.z.remove(self.player4.get())
        self.label5=Label(self.master,text='Player 5',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=9,column=0,sticky=W)
        self.player5=StringVar(self.master)
        self.player5.set("Choose")
        self.player5option=OptionMenu(self.master,self.player5,*self.z)
        self.player5option.grid(row=9,column=1,sticky=W)
        self.next4=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose5(self)).grid(row=9,column=2,padx=20)

    def Choose5(self):
        self.chosen.append(self.player5.get())
        self.z.remove(self.player5.get())
        self.label6=Label(self.master,text='Player 6',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=10,column=0,sticky=W)
        self.player6=StringVar(self.master)
        self.player6.set("Choose")
        self.player6option=OptionMenu(self.master,self.player6,*self.z)
        self.player6option.grid(row=10,column=1,sticky=W)
        self.next5=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose6(self)).grid(row=10,column=2,padx=20)

    def Choose6(self):
        self.chosen.append(self.player6.get())
        self.z.remove(self.player6.get())
        self.label7=Label(self.master,text='Player 7',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=11,column=0,sticky=W)
        self.player7=StringVar(self.master)
        self.player7.set("Choose")
        self.player7option=OptionMenu(self.master,self.player7,*self.z)
        self.player7option.grid(row=11,column=1,sticky=W)
        self.next6=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose7(self)).grid(row=11,column=2,padx=20)

    def Choose7(self):
        self.chosen.append(self.player7.get())
        self.z.remove(self.player7.get())
        self.label8=Label(self.master,text='Player 8',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=12,column=0,sticky=W)
        self.player8=StringVar(self.master)
        self.player8.set("Choose")
        self.player8option=OptionMenu(self.master,self.player8,*self.z)
        self.player8option.grid(row=12,column=1,sticky=W)
        self.next7=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose8(self)).grid(row=12,column=2,padx=20)

    def Choose8(self):
        self.chosen.append(self.player8.get())
       
        self.z.remove(self.player8.get())
        self.label9=Label(self.master,text='Player 9',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=13,column=0,sticky=W)
        self.player9=StringVar(self.master)
        self.player9.set("Choose")
        self.player9option=OptionMenu(self.master,self.player9,*self.z)
        self.player9option.grid(row=13,column=1,sticky=W)
        self.next8=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose9(self)).grid(row=13,column=2,padx=20)

    def Choose9(self):
        self.chosen.append(self.player9.get())
       
        self.z.remove(self.player9.get())
        self.label10=Label(self.master,text='Player 10',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=14,column=0,sticky=W)
        self.player10=StringVar(self.master)
        self.player10.set("Choose")
        self.player10option=OptionMenu(self.master,self.player10,*self.z)
        self.player10option.grid(row=14,column=1,sticky=W)
        self.next9=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose10(self)).grid(row=14,column=2,padx=20)

    def Choose10(self):
        self.chosen.append(self.player10.get())
       
        self.z.remove(self.player10.get())
        self.label11=Label(self.master,text='Player 11',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=15,column=0,sticky=W)
        self.player11=StringVar(self.master)
        self.player11.set("Choose")
        self.player11option=OptionMenu(self.master,self.player11,*self.z)
        self.player11option.grid(row=15,column=1,sticky=W)
        self.next10=Button(self.master,text='DONE',width=12,font='Arial 10 bold',command=lambda:MatchInfo.Team2(self)).grid(row=15,column=2,padx=20)

    def Team2(self):
        self.chosen.append(self.player11.get())
        global cnv
        self.master.destroy()
        cnv=Canvas(super,borderwidth=0)
        self.master=Frame(cnv)
        cnv.place(x=0,y=0)
        cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        cnv.create_window((4,4),window=self.master,anchor='nw',tags='master')
        scrollbar=Scrollbar(super,orient="vertical",command=cnv.yview)
        cnv.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        self.master.bind("<Configure>",OnFrameConfigure2)
        self.Line=Label(self.master,text='___________________',width=40,anchor=W,justify=LEFT).grid(row=16,column=2,sticky=W,pady=30)
        self.Team2=Label(self.master,text='Please Choose TEAM 2',width=40,anchor=W,justify=LEFT,font="Arial 10 bold").grid(row=17,column=0,sticky=W,pady=20)
        self.teams1=StringVar(self.master)
        self.teams1.set("Choose")
        self.teamsoption1a=OptionMenu(self.master,self.teams1,*self.teamss)
        self.teamsoption1a.grid(row=17,column=1,padx=20,pady=5,sticky=W)
        self.Team1Save=Button(self.master,text='OK',width=10,command=lambda:MatchInfo.Choose21(self)).grid(row=17,column=2,padx=340,pady=20)
        self.chosen1=[]

    def Choose21(self):
        for i in range(0,len(self.teamss)):
            if (str(self.teams1.get()))==self.teamss[i]:
                self.chosen1.append(self.teamss[i])
                self.team1team2.append(self.teamss[i])
                self.Team2Dir=str(self.TeamDir)+str("\\")+str(self.teamss2[i])
                x1=open(self.Team2Dir,'r')
                y1=x1.read()
                self.z1=y1.split('\n')
                self.label21=Label(self.master,text='Player 1',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=18,column=0,sticky=W)
                self.player21=StringVar(self.master)
                self.player21.set("Choose")
                self.player21option=OptionMenu(self.master,self.player21,*self.z1)
                self.player21option.grid(row=18,column=1,sticky=W)
                self.next21=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose22(self)).grid(row=18,column=2,padx=0)

    def Choose22(self):
        self.chosen1.append(self.player21.get())
        self.z1.remove(self.player21.get())
        self.label22=Label(self.master,text='Player 2',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=19,column=0,sticky=W)
        self.player22=StringVar(self.master)
        self.player22.set("Choose")
        self.player22option=OptionMenu(self.master,self.player22,*self.z1)
        self.player22option.grid(row=19,column=1,sticky=W)
        self.next22=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose23(self)).grid(row=19,column=2,padx=20)

    def Choose23(self):
        self.chosen1.append(self.player22.get())
        self.z1.remove(self.player22.get())
        self.label23=Label(self.master,text='Player 3',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=20,column=0,sticky=W)
        self.player23=StringVar(self.master)
        self.player23.set("Choose")
        self.player23option=OptionMenu(self.master,self.player23,*self.z1)
        self.player23option.grid(row=20,column=1,sticky=W)
        self.next23=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose24(self)).grid(row=20,column=2,padx=20)

    def Choose24(self):
        self.chosen1.append(self.player23.get())
        self.z1.remove(self.player23.get())
        self.label24=Label(self.master,text='Player 4',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=21,column=0,sticky=W)
        self.player24=StringVar(self.master)
        self.player24.set("Choose")
        self.player24option=OptionMenu(self.master,self.player24,*self.z1)
        self.player24option.grid(row=21,column=1,sticky=W)
        self.next24=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose25(self)).grid(row=21,column=2,padx=20)

    def Choose25(self):
        self.chosen1.append(self.player24.get())
        self.z1.remove(self.player24.get())
        self.label25=Label(self.master,text='Player 5',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=22,column=0,sticky=W)
        self.player25=StringVar(self.master)
        self.player25.set("Choose")
        self.player25option=OptionMenu(self.master,self.player25,*self.z1)
        self.player25option.grid(row=22,column=1,sticky=W)
        self.next25=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose26(self)).grid(row=22,column=2,padx=20)

    def Choose26(self):
        self.chosen1.append(self.player25.get())
        self.z1.remove(self.player25.get())
        self.label26=Label(self.master,text='Player 6',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=23,column=0,sticky=W)
        self.player26=StringVar(self.master)
        self.player26.set("Choose")
        self.player26option=OptionMenu(self.master,self.player26,*self.z1)
        self.player26option.grid(row=23,column=1,sticky=W)
        self.next26=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose27(self)).grid(row=23,column=2,padx=20)

    def Choose27(self):
        self.chosen1.append(self.player26.get())
        self.z1.remove(self.player26.get())
        self.label27=Label(self.master,text='Player 7',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=24,column=0,sticky=W)
        self.player27=StringVar(self.master)
        self.player27.set("Choose")
        self.player27option=OptionMenu(self.master,self.player27,*self.z1)
        self.player27option.grid(row=24,column=1,sticky=W)
        self.next27=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose28(self)).grid(row=24,column=2,padx=20)

    def Choose28(self):
        self.chosen1.append(self.player27.get())
        self.z1.remove(self.player27.get())
        self.label28=Label(self.master,text='Player 8',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=25,column=0,sticky=W)
        self.player28=StringVar(self.master)
        self.player28.set("Choose")
        self.player28option=OptionMenu(self.master,self.player28,*self.z1)
        self.player28option.grid(row=25,column=1,sticky=W)
        self.next28=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose29(self)).grid(row=25,column=2,padx=20)

    def Choose29(self):
        self.chosen1.append(self.player28.get())
        self.z1.remove(self.player28.get())
        self.label29=Label(self.master,text='Player 9',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=26,column=0,sticky=W)
        self.player29=StringVar(self.master)
        self.player29.set("Choose")
        self.player29option=OptionMenu(self.master,self.player29,*self.z1)
        self.player29option.grid(row=26,column=1,sticky=W)
        self.next29=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose30(self)).grid(row=26,column=2,padx=20)

    def Choose30(self):
        self.chosen1.append(self.player29.get())
        self.z1.remove(self.player29.get())
        self.label30=Label(self.master,text='Player 10',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=27,column=0,sticky=W)
        self.player30=StringVar(self.master)
        self.player30.set("Choose")
        self.player30option=OptionMenu(self.master,self.player30,*self.z1)
        self.player30option.grid(row=27,column=1,sticky=W)
        self.next30=Button(self.master,text='NEXT',width=10,command=lambda:MatchInfo.Choose31(self)).grid(row=27,column=2,padx=20)

    def Choose31(self):
        self.chosen1.append(self.player30.get())
        self.z1.remove(self.player30.get())
        self.label31=Label(self.master,text='Player 11',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=28,column=0,sticky=W)
        self.player31=StringVar(self.master)
        self.player31.set("Choose")
        self.player31option=OptionMenu(self.master,self.player31,*self.z1)
        self.player31option.grid(row=28,column=1,sticky=W)
        self.next31=Button(self.master,text='DONE',width=12,font='Arial 10 bold',command=lambda:MatchInfo.Done(self)).grid(row=28,column=2,padx=20)

    def Done(self):
        self.chosen1.append(self.player31.get())
        self.success=Label(self.master,text='Selection of Teams and Players Successful!!!',width=40,anchor=W,justify=LEFT,font='Arial 14 bold').grid(row=29,column=2)
        self.pro=Label(self.master,text='Please Press the "Ball by Ball" Button to Proceed.',width=40,anchor=W,justify=LEFT,font='Arial 14 bold').grid(row=30,column=2)
        self.ballby=Button(self.master,text='BALL by BALL',width=20,font='Arial 20 bold',command=lambda:StartEntryS(self.master,self.type,self.team1team2,self.chosen,self.chosen1,self.alpha,self.InningNum))
        self.ballby.grid(row=31,column=2,pady=15)


#team1team2=list of teams selected by user
#chosen1=index 0 is team name and remaining is the players
#chosen2=index 0 is team name and remaining is the players

###############################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################

class StartEntryS:
    def __init__(self,master,type,teams,players1,players2,venue,InningNum):
        global cnv
        master.destroy()
        cnv=Canvas(super,borderwidth=0)
        master=Frame(cnv)
        cnv.place(x=0,y=0)
        cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        cnv.create_window((4,4),window=master,anchor='nw',tags='master')
        scrollbar=Scrollbar(super,orient="vertical",command=cnv.yview)
        cnv.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        master.bind("<Configure>",OnFrameConfigure2)
        ##################################
        self.InningNum=InningNum
        if self.InningNum==1:
            self.Venue=venue
            self.players1=players1
            self.players2=players2
            self.Team1=[]
            self.Team2=[]
            self.type=type
            self.master=master
            self.teams=teams
            self.TossVar=StringVar(self.master)
            self.TossVar.set("Choose")
            self.TossDec=StringVar(self.master)
            self.TossDec.set("Choose")
            self.TossL=Label(self.master,text='Toss',font="Arial 12 bold",width=30,anchor=W,justify=LEFT).grid(row=0,column=0,sticky=W,pady=20)
            self.TossS=OptionMenu(self.master,self.TossVar,self.players1[0],self.players2[0])
            self.TossS.grid(row=0,column=1,padx=60)
            self.TossD=OptionMenu(self.master,self.TossDec,"BAT","FIELD")
            self.TossD.grid(row=0,column=2,padx=10)
            self.TossSave=Button(self.master,text="SAVE",command=lambda:StartEntryS.InningStart(self))
            self.TossSave.grid(row=0,column=3,padx=30)
            self.Filename=str(self.teams[0])+'vs'+str(self.teams[1])+'-on-'+datetime.datetime.now().strftime('%Y-%m-%d')+'.txt'
            self.BowlerInfoFile=str(self.teams[0])+'vs'+str(self.teams[1])+'-on-'+datetime.datetime.now().strftime('%Y-%m-%d')+' - BowlerInfo'+'.txt'
            self.BatsmanInfoFile=str(self.teams[0])+'vs'+str(self.teams[1])+'-on-'+datetime.datetime.now().strftime('%Y-%m-%d')+' - BatsmanInfo'+'.txt'
            self.BatsmanInfoList=[]
            self.BowlerInfoList=[]
            self.RemainingBatsman=[]
            self.RemainingBowler=[]
            for x in range (0,22):
                list2=[]
                for y in range(0,5):
                    list2.append(0)
                self.BatsmanInfoList.append(list2)
            for x in range(0,22):
                list1=[]
                for y in range(0,6):
                    list1.append(0)
                self.BowlerInfoList.append(list1)

    def InningStart(self):
        if self.type=='ODI':
            self.MatchHeader=Label(self.master,text="1st Innings - 50 Overs Maximum",width=40,anchor=W,justify=LEFT,font="Arial 10 bold").grid(row=1,column=0,sticky=W,pady=20)
            self.MaxBalls=300
            self.MaxWickets=10
            self.MaxOvers=50
            self.OverLimit=10
        else:
            self.MatchHeader=Label(self.master,text="1st Innings - 20 Overs Maximum",width=40,anchor=W,justify=LEFT,font="Arial 10 bold").grid(row=1,column=0,sticky=W,pady=20)
            self.MaxBalls=120
            self.MaxWickets=10
            self.MaxOvers=20
            self.OverLimit=4
    
        a=self.TossVar.get()
        b=self.TossDec.get()
        self.Opener1Var=StringVar(self.master)
        self.Opener1Var.set("Choose")
        self.Opener2Var=StringVar(self.master)
        self.Opener2Var.set("Choose")

        self.filerecord=open(self.Filename,'w')
        self.filerecord.write(str(self.players1[0])+' vs '+str(self.players2[0])+'\n')
        self.filerecord.write('Venue: '+str(self.Venue)+'\n')
        self.filerecord.write('Match Type:'+str(self.type)+'\n')
        self.filerecord.write('1st Innings'+'\n')
        self.filerecord.close()


        if a==str(self.players1[0]) and b=="BAT":
            for i in range(1,12):
                self.BattingSide=str(self.players1[0])
                self.BowlingSide=str(self.players2[0])
                self.Team1.append(self.players1[i])
                self.Team2.append(self.players2[i])

        elif a==str(self.players2[0]) and b=='BAT':
            for i in range(1,12):
                self.BattingSide=str(self.players2[0])
                self.BowlingSide=str(self.players1[0])
                self.Team1.append(self.players2[i])
                self.Team2.append(self.players1[i])

        elif a==str(self.players1[0]) and b=="FIELD":
            for i in range(1,12):
                self.BattingSide=str(self.players2[0])
                self.BowlingSide=str(self.players1[0])
                self.Team1.append(self.players2[i])
                self.Team2.append(self.players1[i])

        else:
            for i in range(1,12):
                self.BattingSide=str(self.players1[0])
                self.BowlingSide=str(self.players2[0])
                self.Team1.append(self.players1[i])
                self.Team2.append(self.players2[i])


        for x in range(0,11):
            self.BowlerInfoList[x][0]=self.Team2[x]
        for y in range(0,11):
            self.BatsmanInfoList[y][0]=self.Team1[y]
        for z in range(0,11):
            self.RemainingBatsman.append(self.BatsmanInfoList[z][0])
            self.RemainingBowler.append(self.BowlerInfoList[z][0])


        self.Opener1SelectL=Label(self.master,text="Please select Striker",width=40,anchor=W,justify=LEFT,font="Arial 9 bold").grid(row=2,column=0,sticky=W,pady=20)
        self.Opener1SelectB=Button(self.master,text="SAVE",width=10,command=lambda: StartEntryS.Opener1Select(self)).grid(row=2,column=2,padx=20)
        self.Opener1SelectS=OptionMenu(self.master,self.Opener1Var,*self.RemainingBatsman)
        self.Opener1SelectS.grid(row=2,column=1,padx=10)
        self.filerecord=open(self.Filename,'a')
        self.filerecord.write(str(self.BattingSide)+str(': '))
        for k in range(0,len(self.Team1)):
            self.filerecord.write(str(self.Team1[k])+str(','))
        self.filerecord.write(str('\n'))
        self.filerecord.write(str(self.BowlingSide)+str(': '))
        for k in range(0,len(self.Team2)):
            self.filerecord.write(str(self.Team2[k])+str(','))
        self.filerecord.write(str('\n'))
        self.filerecord.write('Batting Side: '+str(self.BattingSide)+'\n')
        self.filerecord.write('Bowling Side: '+str(self.BowlingSide)+'\n')
        self.filerecord.write('**********'+str('\n'))
        self.filerecord.close()

    def Opener1Select(self):
        self.RemainingBatsman.remove(self.Opener1Var.get())
        self.Opener2SelectL=Label(self.master,text="Please select Non-Striker",width=40,anchor=W,justify=LEFT,font="Arial 9 bold").grid(row=2,column=4,sticky=W,pady=20)
        self.Opener2SelectS=OptionMenu(self.master,self.Opener2Var,*self.RemainingBatsman)
        self.Opener2SelectS.grid(row=2,column=5,padx=10)
        self.OverStart=Button(self.master,text='PROCEED',command=lambda:StartEntryS.Opener2SelectFunc(self))
        self.OverStart.grid(row=2,column=6,padx=10)

    def Opener2SelectFunc(self):
        self.RemainingBatsman.remove(self.Opener2Var.get())
        print(self.RemainingBatsman)
        BallbyBall(self.master,self.Team1,self.Team2,self.BattingSide,self.Opener1Var,self.Opener2Var,self.type,self.Filename,self.BowlerInfoFile,self.BatsmanInfoFile,self.BowlingSide,self.BowlerInfoList,self.RemainingBowler,self.BatsmanInfoList,self.RemainingBatsman,self.InningNum)

##############################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################

class BallbyBall:
    def __init__(self,master,Team1,Team2,BattingSide,Opener1Var,Opener2Var,type,filename,bowlerfile,batsmanfile,BowlingSide,BowlerInfoList,RemainingBowler,BatsmanInfoList,RemainingBatsman,InningNum):
        global cnv
        master.destroy()
        self.cnv=Canvas(super,borderwidth=0)
        self.master=Frame(self.cnv)
        self.cnv.place(x=0,y=0)
        self.cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        self.cnv.create_window((4,4),window=self.master,anchor='nw',tags='master')
        self.scrollbar=Scrollbar(super,orient="vertical",command=self.cnv.yview)
        self.cnv.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        self.master.bind("<Configure>",OnFrameConfigure2)

        self.FileName=filename
        self.BowlerInfoFile=bowlerfile
        self.BatsmanInfoFile=batsmanfile
        self.BowlerInfoList=BowlerInfoList
        self.RemainingBowler=RemainingBowler
        self.BatsmanInfoList=BatsmanInfoList
        self.RemainingBatsman=RemainingBatsman
        self.MatchType=type
        self.Team1=Team1
        self.Team2=Team2
        self.BattingSide=BattingSide
        self.BowlingSide=BowlingSide
        self.Batsman1=Opener1Var.get()
        self.Batsman2=Opener2Var.get()
        self.OverBowlerVar=StringVar(self.master)
        self.OverBowlerVar.set("Choose")
        self.InningNum=InningNum

        self.OverNum=0                                      ########changes these for OLD MATCH
        self.BallNum=1
        self.MaxWickets=10
        self.TotalRuns=0
        self.ExtraBalls=0
        self.ExtraRuns=0

        self.OverRun=0
        self.OverBallCount=0

        if self.MatchType=='ODI':
            self.MaxBalls=300
            self.OverLimit=10
            self.MaxOvers=50
        else:
            self.MaxBalls=120
            self.OverLimit=4
            self.MaxOvers=20

        self.BowlerSelectL=Label(self.master,text='Select Bowler',width=15,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=3,column=2,sticky=W,pady=20,padx=30)
        self.BowlerSelectS=OptionMenu(self.master,self.OverBowlerVar,*self.RemainingBowler)
        self.BowlerSelectS.grid(row=3,column=3,sticky=W,pady=20,padx=30)
        self.BallStartB=Button(self.master,text='PROCEED',command=lambda:BallbyBall.BallStart(self))
        self.BallStartB.grid(row=3,column=4,padx=30,pady=20)

    ####################################################################################################
        
    def RunoutNext(self):
        self.strikercurrent=[]
        print(self.currentTwoBat)
        self.currentTwoBat.remove(str(self.BatsmanTwoVar.get()))
        self.strikercurrent.append(self.BatsmanNextVar.get())
        self.strikercurrent.append(self.currentTwoBat[0])
        self.AfterRunOut=StringVar(self.master)
        self.AfterRunOut.set("Choose")
        self.AfterRunOption=OptionMenu(self.master,self.AfterRunOut,*self.strikercurrent).grid(row=3,column=1,sticky=W,pady=20,padx=30)
        self.AfterRunOption=Label(self.master,text="On Strike:",width=30,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=3,column=0,sticky=W,pady=20,padx=30)
        self.wiclaB=Button(self.master,text="NEXT",width=20,command=lambda:BallbyBall.RunoutNext11(self))
        self.wiclaB.grid(row=3,column=2,padx=30,pady=20)

    def RunoutNext11(self):
        if self.Batsman1!=self.AfterRunOut.get():
            self.Batsman2=self.Batsman1
            self.Batsman1=self.AfterRunOut.get()
        else:
            self.Batsman1=self.AfterRunOut.get()
        self.wiclaBa=Button(self.master,text="DONE",width=25,command=lambda:BallbyBall.Runy(self))
        self.wiclaBa.grid(row=4,column=2,padx=30,pady=20)

    def Runy(self):
        global cnv
        self.master.destroy()
        self.cnv=Canvas(super,borderwidth=0)
        self.master=Frame(self.cnv)
        self.cnv.place(x=0,y=0)
        self.cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        self.cnv.create_window((4,4),window=self.master,anchor='nw',tags='master')
        self.scrollbar=Scrollbar(super,orient="vertical",command=self.cnv.yview)
        self.cnv.configure(yscrollcommand=scrollbar.set)
        self.scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        self.master.bind("<Configure>",OnFrameConfigure2)
        ########################################
        self.RemainingBatsman.remove(self.BatsmanNextVar.get())
        BallbyBall.BallStart(self)
###################################################################################################################

    def Runout(self):
        global cnv
        self.master.destroy()
        self.cnv=Canvas(super,borderwidth=0)
        self.master=Frame(self.cnv)
        self.cnv.place(x=0,y=0)
        self.cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        self.cnv.create_window((4,4),window=self.master,anchor='nw',tags='master')
        self.scrollbar=Scrollbar(super,orient="vertical",command=self.cnv.yview)
        self.cnv.configure(yscrollcommand=scrollbar.set)
        self.scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        self.master.bind("<Configure>",OnFrameConfigure2)
        
        #################################################################

        self.currentTwoBat=[]
        self.currentTwoBat.append(self.Batsman1)
        self.currentTwoBat.append(self.Batsmanyo)
        self.BatsmanTwoVar=StringVar(self.master)   
        self.BatsmanTwoVar.set("Choose")
        self.BatsmanNextVar=StringVar(self.master)   
        self.BatsmanNextVar.set("Choose")
        self.Fielder=StringVar(self.master)
        self.Fielder.set("Choose")
        
        self.wiclabel=Label(self.master,text="Please select Batsman which is run out:",width=40,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=0,column=0,sticky=W,pady=20,padx=30)
        self.wiclabelOption=OptionMenu(self.master,self.BatsmanTwoVar,*self.currentTwoBat).grid(row=0,column=1,sticky=W,pady=20,padx=30)
        self.BatsmanNext=OptionMenu(self.master,self.BatsmanNextVar,*self.RemainingBatsman).grid(row=1,column=1,sticky=W,pady=20,padx=30)
        self.wicla=Label(self.master,text="Please select the next Batsman:",width=30,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=1,column=0,sticky=W,pady=20,padx=30)
        self.runby=Label(self.master,text="Run Out by:",width=30,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=2,column=0,sticky=W,pady=20,padx=30)
        self.running=OptionMenu(self.master,self.Fielder,*self.RemainingBowler).grid(row=2,column=1,sticky=W,pady=20,padx=30)
        self.wiclaBat=Button(self.master,text="NEXT",width=20,command=lambda:BallbyBall.RunoutNext(self))
        self.wiclaBat.grid(row=2,column=2,padx=30,pady=20)
#######################################################################################

    def Caught(self):  
        global cnv
        self.master.destroy()
        self.cnv=Canvas(super,borderwidth=0)
        self.master=Frame(self.cnv)
        self.cnv.place(x=0,y=0)
        self.cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        self.cnv.create_window((4,4),window=self.master,anchor='nw',tags='master')
        self.scrollbar=Scrollbar(super,orient="vertical",command=self.cnv.yview)
        self.cnv.configure(yscrollcommand=scrollbar.set)
        self.scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        self.master.bind("<Configure>",OnFrameConfigure2)
        
        #################################################################
    
        self.BatsmanNextVar=StringVar(self.master)  
        self.BatsmanNextVar.set("Choose")
        self.Fielder=StringVar(self.master)
        self.Fielder.set("Choose")
        self.BatsmanNext=OptionMenu(self.master,self.BatsmanNextVar,*self.RemainingBatsman).grid(row=0,column=1,sticky=W,pady=20,padx=30)
        self.wicla=Label(self.master,text="Please select the next Batsman:",width=30,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=0,column=0,sticky=W,pady=20,padx=30)
        self.catchby=Label(self.master,text="Caught by:",width=30,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=1,column=0,sticky=W,pady=20,padx=30)
        self.catching=OptionMenu(self.master,self.Fielder,*self.Team2).grid(row=1,column=1,sticky=W,pady=20,padx=30)
        self.wiclaB=Button(self.master,text="OK",width=20,command=lambda:BallbyBall.WickyNext(self))
        self.wiclaB.grid(row=3,column=2,padx=30,pady=20)
            
#################################################################################################
 
    def Bowled(self):            
        global cnv
        self.master.destroy()
        self.cnv=Canvas(super,borderwidth=0)
        self.master=Frame(self.cnv)
        self.cnv.place(x=0,y=0)
        self.cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        self.cnv.create_window((4,4),window=self.master,anchor='nw',tags='master')
        self.scrollbar=Scrollbar(super,orient="vertical",command=self.cnv.yview)
        self.cnv.configure(yscrollcommand=scrollbar.set)
        self.scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        self.master.bind("<Configure>",OnFrameConfigure2)
        
        #################################################################
   
        self.BatsmanNextVar=StringVar(self.master)  
        self.BatsmanNextVar.set("Choose")
        self.BatsmanNext=OptionMenu(self.master,self.BatsmanNextVar,*self.RemainingBatsman).grid(row=0,column=1,sticky=W,pady=20,padx=30)
        self.wicla=Label(self.master,text="Please select the next Batsman:",width=30,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=0,column=0,sticky=W,pady=20,padx=30)
        self.wiclaB=Button(self.master,text="OK",command=lambda:BallbyBall.WickyNext(self))
        self.wiclaB.grid(row=0,column=2,padx=30,pady=20)
            
            
    def WickyNext(self):
        for x in range(0,len(self.BatsmanInfoList)):
            if self.Wicket=='Run out':
                if str(self.BatsmanTwoVar.get())==str(self.BatsmanInfoList[x][0]):
                    dest1=x
                    self.BatsmanInfoList[dest1][4]=str(self.Fielder)
            if self.Wicket=='Caught' or self.Wicket=='Stump':
                if str(self.Player)==str(self.BatsmanInfoList[x][0]):
                    dest1=x
                    self.BatsmanInfoList[dest1][4]=str(self.Fielder)

        global cnv
        self.master.destroy()
        self.cnv=Canvas(super,borderwidth=0)
        self.master=Frame(self.cnv)
        self.cnv.place(x=0,y=0)
        self.cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        self.cnv.create_window((4,4),window=self.master,anchor='nw',tags='master')
        self.scrollbar=Scrollbar(super,orient="vertical",command=self.cnv.yview)
        self.cnv.configure(yscrollcommand=scrollbar.set)
        self.scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        self.master.bind("<Configure>",OnFrameConfigure2)
        ########################################
        self.RemainingBatsman.remove(self.BatsmanNextVar.get())
        self.Batsman1=self.BatsmanNextVar.get()
        #self.WicketVar.set("NONE")
        BallbyBall.BallStart(self)
        
#####################################################################################################




    def InfoUpdate(self):
        self.Bowler=str(self.OverBowlerVar.get())
        self.Player=str(self.FacingBatsMan)
        self.Extra=str(self.ExtrasVar.get())
        self.Runs=str(self.RunsVar.get())
        self.Wicket=str(self.WicketVar.get())
        #########################################################
        #########################################################
        global cnv
        self.master.destroy()
        self.cnv=Canvas(super,borderwidth=0)
        self.master=Frame(self.cnv)
        self.cnv.place(x=0,y=0)
        self.cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        self.cnv.create_window((4,4),window=self.master,anchor='nw',tags='master')
        self.scrollbar=Scrollbar(super,orient="vertical",command=self.cnv.yview)
        self.cnv.configure(yscrollcommand=scrollbar.set)
        self.scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        self.master.bind("<Configure>",OnFrameConfigure2)
        #########################################################
        #########################################################

#########################################################WICKET CHECK#########################################################
        if self.Wicket!='NONE' and self.Wicket!='Run out' and self.Wicket!='Stump':
            if self.Runs!='0':
                self.WicketErrorL=Label(self.master,text='Error, CANNOT select this WICKET type with RUNS or EXTRAS',fg='red')
                self.WicketErrorL.grid(row=6,column=0,sticky=W,pady=20,padx=30,columnspan=6)
                return BallbyBall.BallStart(self)
            elif self.Extra!='0':
                self.WicketErrorL=Label(self.master,text='Error, CANNOT select this WICKET type with RUNS or EXTRAS',fg='red')
                self.WicketErrorL.grid(row=6,column=0,sticky=W,pady=20,padx=30,columnspan=6)
                return BallbyBall.BallStart(self)
            else:
                self.WicketErrorL=Label(self.master,text='',fg='red')
                self.WicketErrorL.grid(row=6,column=0,sticky=W,pady=20,padx=30)
        elif self.Wicket=='Stump':
            if self.Runs!='0':
                self.WicketErrorL=Label(self.master,text='Error, CANNOT select this WICKET type with RUNS or EXTRAS',fg='red')
                self.WicketErrorL.grid(row=6,column=0,sticky=W,pady=20,padx=30,columnspan=6)
                return BallbyBall.BallStart(self)
            elif self.Extra!='Wide' and self.Extra!='0':
                self.WicketErrorL=Label(self.master,text='Error, CANNOT select this WICKET type with RUNS or EXTRAS',fg='red')
                self.WicketErrorL.grid(row=6,column=0,sticky=W,pady=20,padx=30,columnspan=6)
                return BallbyBall.BallStart(self)
            else:
                self.WicketErrorL=Label(self.master,text='',fg='red')
                self.WicketErrorL.grid(row=6,column=0,sticky=W,pady=20,padx=30)
        else:
            self.WicketErrorL=Label(self.master,text='',fg='red')
            self.WicketErrorL.grid(row=6,column=0,sticky=W,pady=20,padx=30)
#########################################################WICKET CHECK#########################################################

#########################################################WICKET DEDUCT#########################################################

#########################################################WICKET DEDUCT#########################################################

        self.Batsmanyo=self.Batsman2

        if str(self.RunsVar.get())=="1" or str(self.RunsVar.get())=="3" or str(self.RunsVar.get())=="5" or str(self.RunsVar.get())=="7":
            self.boootman1=self.Batsman1
            self.Batsman1=self.Batsman2
            self.Batsman2=self.boootman1
#########################################################BOWLER LIST UPDATE#########################################################
        for x in range(0,len(self.BowlerInfoList)):
            if self.Bowler==str(self.BowlerInfoList[x][0]):
                dest=x
                if self.Extra!='Wide' and self.Extra!='No Ball':
                    self.BowlerInfoList[dest][1]+=1
                self.BowlerInfoList[dest][2]+=int(self.Runs)                                        #Add runs to bowler
                if self.Wicket!='NONE' and self.Wicket!='Run out':                                  #Check for run out or no wicket
                    self.BowlerInfoList[dest][3]+=1                                                 #Add wicket to bowler
                if self.Extra=='No Ball':
                    self.BowlerInfoList[dest][4]=str(self.BowlerInfoList[dest][4])+'n'
                    self.BowlerInfoList[dest][2]+=1
                elif self.Extra=='Wide':
                    self.BowlerInfoList[dest][4]=str(self.BowlerInfoList[dest][4])+'w'
                    self.BowlerInfoList[dest][2]+=1
#########################################################BOWLER LIST UPDATE#########################################################

#########################################################BATSMAN LIST UPDATE#########################################################
        for x in range(0,len(self.BatsmanInfoList)):
            if self.Player==self.BatsmanInfoList[x][0]:
                dest1=x
                if self.Extra!='Bye' and self.Extra!='Leg Bye' and self.Extra!='Wide':
                    self.BatsmanInfoList[dest1][1]+=int(self.Runs)
                if self.Extra!='No Ball' and self.Extra!='Wide':
                    self.BatsmanInfoList[dest1][2]+=1
                if self.Wicket!='NONE' and self.Wicket!='Run out':
                    self.BatsmanInfoList[dest1][3]=str(self.Bowler)
                    #self.BatsmanInfoList[dest1][4]=str(self.Fielder)
#########################################################BATSMAN LIST UPDATE#########################################################
        if self.Wicket!='NONE':
            self.MaxWickets-=1

        self.TotalRuns+=int(self.Runs)
#########################################################MAIDEN OVER CHECK#########################################################
        self.OverRun+=int(self.Runs)
        if self.Extra=='No Ball' or self.Extra=='Wide':
            self.OverRun+=1
        self.OverBallCount+=1
        if self.OverBallCount==6:
            self.OverBallCount=0
            if self.OverRun==0:
                for x in range(0,len(self.BowlerInfoList)):
                        if self.Bowler==str(self.BowlerInfoList[x][0]):
                            dest=x
                            self.BowlerInfoList[dest][5]+=1
            else:
                self.OverRun=0
#########################################################MAIDEN OVER CHECK#########################################################

#########################################################BOWLER INFO TEXT RECORDING#########################################################
        self.bowlerrecord=open(self.BowlerInfoFile,'w')
        for x in range(0,len(self.BowlerInfoList)):
            for y in range(0,6):
                self.bowlerrecord.write(str(self.BowlerInfoList[x][y]))
                self.bowlerrecord.write(str('\n'))
            self.bowlerrecord.write(str('**********'))
            self.bowlerrecord.write(str('\n'))
        self.bowlerrecord.close()
#########################################################BOWLER INFO TEXT RECORDING#########################################################

#########################################################BATSMAN INFO TEXT RECORDING#########################################################
        self.batsmanrecord=open(self.BatsmanInfoFile,'w')
        for x in range(0,len(self.BatsmanInfoList)):
            for y in range(0,5):
                self.batsmanrecord.write(str(self.BatsmanInfoList[x][y]))
                self.batsmanrecord.write(str('\n'))
            self.batsmanrecord.write(str('**********'))
            self.batsmanrecord.write(str('\n'))
        self.batsmanrecord.close()
#########################################################BATSMAN INFO TEXT RECORDING#########################################################

        if self.Extra=='No Ball' or self.Extra=='Wide':
            self.TotalRuns+=1
            self.BallNum-=1
            self.ExtraBalls+=1
            self.ExtraRuns+=1
        if self.Extra=='Bye' or self.Extra=='Leg Bye':
            self.ExtraRuns+=int(self.Runs)

        self.filerecord=open(self.FileName,'a')
        self.filerecord.write(self.Bowler+str('\n'))                                             #Bowler name
        if self.BallNum==-1:
            self.filerecord.write(str(self.OverNum)+'.0'+str('\n'))                              #Over and ball
        else:
            self.filerecord.write(str(self.OverNum)+'.'+str(self.BallNum)+str('\n'))             #Over and ball
        self.filerecord.write(str(self.Player))                                                  #Batsman
        self.filerecord.write('\n')
        self.filerecord.write(str(self.Extra))                                                   #Extras
        self.filerecord.write('\n')
        self.filerecord.write(str(self.Runs))                                                    #Runs Scored
        self.filerecord.write('\n')
        self.filerecord.write(str(self.Wicket))                                                  #out type e.g bowled, caught etc
        self.filerecord.write('\n')
        self.filerecord.write(str(self.TotalRuns))                                               #Total Runs of team
        self.filerecord.write('\n')
        self.filerecord.write(str(self.ExtraRuns))                                               #Total Extras of team
        self.filerecord.write('\n')
        self.filerecord.write('**********'+str('\n'))
        self.filerecord.close()
        print(self.BowlerInfoList)######################################################################################################
        print(self.BatsmanInfoList)


        if float(self.OverNum)==0:
            if abs((float(self.OverNum)-float(self.BallNum)/10))<=0.4:
                    #print(abs(float(self.OverNum)-float(self.BallNum)/10))
                    self.BallNum+=1
                    self.MaxBalls-=1
                    if self.BallNum==1:
                        self.BowlerSelectL=Label(self.master,text='Select Bowler',width=15,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=3,column=2,sticky=W,pady=20,padx=30)
                        self.BowlerSelectS=OptionMenu(self.master,self.OverBowlerVar,*self.RemainingBowler)
                        self.BowlerSelectS.grid(row=3,column=3,sticky=W,pady=20,padx=30)
                        self.BallStartB=Button(self.master,text='PROCEED',command=lambda:BallbyBall.BallStart(self))
                        self.BallStartB.grid(row=3,column=4,padx=30,pady=20)

            else:
                self.OverNum+=1
                self.BallNum=0
                self.MaxBalls-=1
                self.MaxOvers-=1


        elif float(self.OverNum)>3 and float(self.OverNum)<16:
            if abs(float(self.OverNum)-(float(self.OverNum)+(float(self.BallNum)/10)))<0.5:
                self.BallNum+=1
                self.MaxBalls-=1
                if self.BallNum==1:
                        self.boootman1=self.Batsman1
                        self.Batsman1=self.Batsman2
                        self.Batsman2=self.boootman1
                        self.FacingBatLa=Label(self.master,text=self.Batsman1,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=5,column=1,sticky=W,pady=20,padx=30)
                        self.FacingBatsMan=self.Batsman1
                        self.BowlerSelectL=Label(self.master,text='Select Bowler',width=15,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=3,column=2,sticky=W,pady=20,padx=30)
                        self.BowlerSelectS=OptionMenu(self.master,self.OverBowlerVar,*self.RemainingBowler)
                        self.BowlerSelectS.grid(row=3,column=3,sticky=W,pady=20,padx=30)
                        self.BallStartB=Button(self.master,text='PROCEED',command=lambda:BallbyBall.BallStart(self))
                        self.BallStartB.grid(row=3,column=4,padx=30,pady=20)
            else:
                self.OverNum+=1
                self.BallNum=0
                self.MaxBalls-=1
                self.MaxOvers-=1



        else:
            if abs(float(self.OverNum)-(float(self.OverNum)+(float(self.BallNum)/10)))<=0.4:
                self.BallNum+=1
                self.MaxBalls-=1
                if self.BallNum==1:
                        self.boootman1=self.Batsman1
                        self.Batsman1=self.Batsman2
                        self.Batsman2=self.boootman1
                        self.FacingBatLa=Label(self.master,text=self.Batsman1,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=5,column=1,sticky=W,pady=20,padx=30)
                        self.FacingBatsMan=self.Batsman1
                        self.BowlerSelectL=Label(self.master,text='Select Bowler',width=15,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=3,column=2,sticky=W,pady=20,padx=30)
                        self.BowlerSelectS=OptionMenu(self.master,self.OverBowlerVar,*self.RemainingBowler)
                        self.BowlerSelectS.grid(row=3,column=3,sticky=W,pady=20,padx=30)
                        self.BallStartB=Button(self.master,text='PROCEED',command=lambda:BallbyBall.BallStart(self))
                        self.BallStartB.grid(row=3,column=4,padx=30,pady=20)
            else:
                self.OverNum+=1
                self.BallNum=0
                self.MaxBalls-=1
                self.MaxOvers-=1

        if self.MaxBalls==0 or self.MaxOvers==0:
            print("Innings END")

        self.CurrentInningRunsL=Label(self.master,text='Runs: %d'% self.TotalRuns,fg='green',font='Arial 12 bold',anchor=E,justify=RIGHT)
        self.CurrentInningRunsL.grid(row=8,column=5,sticky=W,pady=10,padx=30)
        if self.BallNum==0:
            OverString=str((int(self.OverNum)-1))+'.5'
            self.CurrentInningOversL=Label(self.master,text='Over: %s'% str(OverString),fg='blue',font='Arial 12 bold',anchor=E,justify=RIGHT)
            #self.CurrentInningOversL=Label(self.master,text='Over: %s'% str(self.OverString1),fg='blue',font='Arial 12 bold',anchor=E,justify=RIGHT)
        else:
            OverString=str(self.OverNum)+'.'+str(int(self.BallNum)-1)
            self.CurrentInningOversL=Label(self.master,text='Over: %s'% str(OverString),fg='blue',font='Arial 12 bold',anchor=E,justify=RIGHT)
            # self.CurrentInningOversL=Label(self.master,text='Over: %s'% str(self.OverString2),fg='blue',font='Arial 12 bold',anchor=E,justify=RIGHT)
        self.CurrentInningOversL.grid(row=9,column=5,sticky=W,pady=10,padx=30)
        self.CurrentWicketsL=Label(self.master,text='Wickets Remaining: %d'% self.MaxWickets,fg='dark red',font='Arial 12 bold',anchor=E,justify=RIGHT)
        self.CurrentWicketsL.grid(row=10,column=5,sticky=W,pady=10,padx=30)
        self.CurrentMatchRecordName=str(self.BatsmanInfoFile[:-18])+' - CurrentMatchInfo.txt'
        self.CurrentMatchRecord=open(self.CurrentMatchRecordName,'w')
        self.CurrentMatchRecord.write(str('Inning Number ')+str(self.InningNum)+str('\n'))
        self.CurrentMatchRecord.write(str(self.TotalRuns)+str('\n'))
        self.CurrentMatchRecord.write(str(OverString)+str('\n'))
        # self.CurrentMatchRecord.write(str(self.OverString1)+str('\n'))
        # self.CurrentMatchRecord.write(str(self.OverString2)+str('\n'))
        self.CurrentMatchRecord.write(str(self.MaxWickets)+str('\n'))
        self.CurrentMatchRecord.write(str(self.BattingSide)+str('\n'))
        self.CurrentMatchRecord.write(str(self.BowlingSide)+str('\n'))
        self.CurrentMatchRecord.write(str(self.Batsman1)+str('\n'))
        self.CurrentMatchRecord.write(str(self.Batsman2)+str('\n'))
        self.CurrentMatchRecord.write(str(self.Bowler)+str('\n'))
        self.CurrentMatchRecord.write(str(self.FileName)+str('\n'))
        self.CurrentMatchRecord.write(str(self.BowlerInfoFile)+str('\n'))
        self.CurrentMatchRecord.write(str(self.BatsmanInfoFile)+str('\n'))
        self.CurrentMatchRecord.write(str(self.BowlerInfoList)+str('\n'))
        self.CurrentMatchRecord.write(str(self.RemainingBowler)+str('\n'))
        self.CurrentMatchRecord.write(str(self.BatsmanInfoList)+str('\n'))
        self.CurrentMatchRecord.write(str(self.RemainingBatsman)+str('\n'))
        self.CurrentMatchRecord.write(str(self.MatchType)+str('\n'))
        self.CurrentMatchRecord.write(str(self.Team1)+str('\n'))
        self.CurrentMatchRecord.write(str(self.Team2)+str('\n'))
        #self.CurrentMatchRecord.write(str(self.teams)+str('\n'))
        self.CurrentMatchRecord.write(str(self.OverNum)+str('\n'))
        self.CurrentMatchRecord.write(str(self.BallNum)+str('\n'))
        self.CurrentMatchRecord.write(str(self.MaxWickets)+str('\n'))
        self.CurrentMatchRecord.write(str(self.TotalRuns)+str('\n'))
        self.CurrentMatchRecord.write(str(self.ExtraBalls)+str('\n'))
        self.CurrentMatchRecord.write(str(self.ExtraRuns)+str('\n'))
        self.CurrentMatchRecord.write(str(self.OverRun)+str('\n'))
        self.CurrentMatchRecord.write(str(self.OverBallCount)+str('\n'))
        self.CurrentMatchRecord.write(str(self.MaxBalls)+str('\n'))
        self.CurrentMatchRecord.write(str(self.OverLimit)+str('\n'))
        self.CurrentMatchRecord.write(str(self.MaxOvers)+str('\n'))
        self.CurrentMatchRecord.write(str(self.Player)+str('\n'))
        self.CurrentMatchRecord.write(str(self.Extra)+str('\n'))
        self.CurrentMatchRecord.write(str(self.Runs)+str('\n'))
        self.CurrentMatchRecord.write(str(self.Wicket)+str('\n'))
        self.CurrentMatchRecord.write(str(self.CurrentMatchRecordName)+str('\n'))
        self.CurrentMatchRecord.close()

        if self.WicketVar.get()=='Bowled' or self.WicketVar.get()=='LBW' or self.WicketVar.get()=='Hit Wicket':     #MAHAD
            return BallbyBall.Bowled(self)
        
        if self.WicketVar.get()=='Caught' or self.WicketVar.get()=='Stump':    #MAHAD
            return BallbyBall.Caught(self)

        if self.WicketVar.get()=='Run out':    #MAHAD
            return BallbyBall.Runout(self)


        if self.MaxBalls>0 and self.MaxWickets>0:
            BallbyBall.BallStart(self)
        else:
            dummyTeam=self.Team1                ###SWITCHING TEAMS###
            self.Team1=self.Team2               ###SWITCHING TEAMS###
            self.Team2=dummyTeam                ###SWITCHING TEAMS###

            dummySide=self.BattingSide                ###SWITCHING SIDES###
            self.BattingSide=self.BowlingSide         ###SWITCHING SIDES###
            self.BowlingSide=dummySide                ###SWITCHING SIDES###

            # dummyteams=self.teams
            # self.teams[0],self.teams[1]=dummyteams[1],dummyteams[0]

            self.Target=self.TotalRuns
            self.InningEndL=Label(self.master,text='End of Innings, Target = '+str(self.Target),width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=11,column=0,sticky=W,pady=20)
#Remove self.teams from second innings
            SecondInnings(self.master,self.Team1,self.Team2,self.BattingSide,self.MatchType,self.FileName,self.BowlerInfoFile,self.BatsmanInfoFile,self.BowlingSide,self.BowlerInfoList,self.BatsmanInfoList,self.Target)



    def BallStart(self):
        self.FacingBatLa=Label(self.master,text=self.Batsman1,font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=5,column=1,sticky=W,pady=20,padx=30)
        self.FacingBatsMan=self.Batsman1
        self.ExtrasVar=StringVar(self.master)
        self.ExtrasVar.set("0")
        
        self.RunsVar=IntVar(self.master)
        self.RunsVar.set(0)
        
        self.WicketVar=StringVar(self.master)
        self.WicketVar.set("NONE")
        
        self.ExtrasList=['No Ball','Wide','Leg Bye','Bye','0']
        self.RunsList=[0,1,2,3,4,5,6,7,8]
        self.WicketList=['Bowled','Caught','Stump','LBW','Run out','Hit Wicket','NONE']


        self.OverL=Label(self.master,text='OVER',font='Arial 8 bold',anchor=W,justify=LEFT).grid(row=3,column=0,sticky=W,pady=20,padx=30)
        self.OverL2=Label(self.master,text=str(self.OverNum)+'.'+str(self.BallNum),anchor=W,width=15,justify=LEFT).grid(row=3,column=1,sticky=W,pady=20,padx=30)
        
        if self.BallNum==0:
            self.Ball1L=Label(self.master,text='Ball 6',width=20,anchor=W,justify=LEFT).grid(row=5,column=0,sticky=W,pady=20,padx=30)
        else:
            self.Ball1L=Label(self.master,text='Ball %d'%self.BallNum,width=20,anchor=W,justify=LEFT).grid(row=5,column=0,sticky=W,pady=20,padx=30)
            
        self.NumSign=Label(self.master,text='#',width=20,anchor=W,justify=LEFT).grid(row=4,column=0,sticky=W,pady=20,padx=30)
        self.StrikerL=Label(self.master,text='                    Striker',width=20,anchor=W,justify=LEFT).grid(row=4,column=1,sticky=W,pady=20,padx=30)
        self.ExtrasL=Label(self.master,text='                Extras',width=20,anchor=W,justify=LEFT).grid(row=4,column=2,sticky=W,pady=20,padx=30)
        self.RunsL=Label(self.master,text='                Runs',width=20,anchor=W,justify=LEFT).grid(row=4,column=3,sticky=W,pady=20,padx=30)
        self.WicketL=Label(self.master,text='                Wicket',width=20,anchor=W,justify=LEFT).grid(row=4,column=4,sticky=W,pady=20,padx=30)

        self.BallExtras=OptionMenu(self.master,self.ExtrasVar,*self.ExtrasList)
        self.BallExtras.grid(row=5,column=2,sticky=W,pady=20,padx=30)
        self.BallRuns=OptionMenu(self.master,self.RunsVar,*self.RunsList)
        self.BallRuns.grid(row=5,column=3,sticky=W,pady=20,padx=30)
        self.BallWicket=OptionMenu(self.master,self.WicketVar,*self.WicketList)
        self.BallWicket.grid(row=5,column=4,sticky=W,pady=20,padx=30)
        self.BallSave=Button(self.master,text='SAVE',command=lambda:BallbyBall.InfoUpdate(self))
        self.BallSave.grid(row=5,column=5,sticky=W,pady=20,padx=30)
###############################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################
#Change Line 31 in main file (not this)
#Change Line 32 in main file (not this)
#Def InningStart Line 414 to 426 changed
class SecondInnings:
    def __init__(self,master,Team1,Team2,BattingSide,type,FileName,BowlerInfoFile,BatsmanInfoFile,BowlingSide,BowlerInfoList,BatsmanInfoList,Target):
        global cnv
        master.destroy()
        self.cnv=Canvas(super,borderwidth=0)
        self.master=Frame(self.cnv)
        self.cnv.place(x=0,y=0)
        self.cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
        self.cnv.create_window((4,4),window=self.master,anchor='nw',tags='master')
        self.scrollbar=Scrollbar(super,orient="vertical",command=self.cnv.yview)
        self.cnv.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
        self.master.bind("<Configure>",OnFrameConfigure2)
        ###########################################################################################

        self.Team1=Team1
        self.Team2=Team2
        self.BattingSide=BattingSide
        self.FileName=FileName
        self.BowlerInfoFile=BowlerInfoFile
        self.BatsmanInfoFile=BatsmanInfoFile
        self.BowlingSide=BowlingSide
        self.BowlerInfoList=BowlerInfoList
        self.BatsmanInfoList=BatsmanInfoList
        self.Target=Target
        self.type=type

        self.RemainingBatsman=[]
        self.RemainingBowler=[]
        for x in range(11,len(self.Team2)):
            self.BowlerInfoList[int(x)][0]=self.Team2[x]
        for y in range(11,len(self.Team1)):
            self.BatsmanInfoList[int(y)][0]=self.Team1[y]
        for z in range(11,len(self.BatsmanInfoList)):
            self.RemainingBatsman.append(self.BatsmanInfoList[z][0])
            self.RemainingBowler.append(self.BowlerInfoList[z][0])

        if self.type=='ODI':
            self.ODIHeader=Label(self.master,text='Innings 2 ODI (300 Balls per Innings)',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=0,column=0,sticky=W,pady=20)
            self.MaxBalls=300
            self.MaxWickets=10
            self.MaxOvers=50
            self.OverLimit=10
        else:
            self.T20Header=Label(self.master,text='Innings 2 T20 (120 Balls per Innings)',width=40,anchor=W,justify=LEFT,font="Arial 8 bold").grid(row=0,column=0,sticky=W,pady=20)
            self.MaxBalls=120
            self.MaxWickets=10
            self.MaxOvers=20
            self.OverLimit=4
        self.BattingSideL=Label(self.master,text='Batting Side: '+str(self.BattingSide),width=40,anchor=W,justify=LEFT).grid(row=0,column=0,sticky=W,pady=20)
        self.BowlingSideL=Label(self.master,text='Batting Side: '+str(self.BowlingSide),width=40,anchor=W,justify=LEFT).grid(row=1,column=0,sticky=W,pady=20)
        self.TargetL=Label(self.master,text='Target: '+str(self.Target),width=40,anchor=W,justify=LEFT).grid(row=0,column=2,sticky=W,pady=20)
        self.Opener1Var=StringVar(self.master)
        self.Opener1Var.set("Choose")
        self.Opener2Var=StringVar(self.master)
        self.Opener2Var.set("Choose")
        self.filerecord=open(self.FileName,'a')
        self.filerecord.write('??????????')
        self.filerecord.write(str(self.BattingSide)+' vs '+str(self.BowlingSide)+'\n')

        self.filerecord.write('Match Type:'+str(self.type)+'\n')
        self.filerecord.write('2nd Innings'+'\n')
        self.filerecord.close()
        self.Opener1SelectL=Label(self.master,text="Please select Striker",width=40,anchor=W,justify=LEFT,font="Arial 9 bold").grid(row=2,column=0,sticky=W,pady=20)
        self.Opener1SelectB=Button(self.master,text="SAVE",width=10,command=lambda: StartEntryS.Opener30Select(self)).grid(row=2,column=2,padx=20)
        self.Opener1SelectS=OptionMenu(self.master,self.Opener1Var,*self.RemainingBatsman)
        self.Opener1SelectS.grid(row=2,column=1,padx=10)
        self.filerecord=open(self.Filename,'a')
        self.filerecord.write(str(self.BattingSide)+str(': '))
        for k in range(0,len(self.Team1)):
            self.filerecord.write(str(self.Team1[k])+str(','))
        self.filerecord.write(str('\n'))
        self.filerecord.write(str(self.BowlingSide)+str(': '))
        for k in range(0,len(self.Team2)):
            self.filerecord.write(str(self.Team2[k])+str(','))
        self.filerecord.write(str('\n'))
        self.filerecord.write('Batting Side: '+str(self.BattingSide)+'\n')
        self.filerecord.write('Bowling Side: '+str(self.BowlingSide)+'\n')
        self.filerecord.write('**********'+str('\n'))
        self.filerecord.close()

    def Opener30Select(self):
        self.RemainingBatsman.remove(self.Opener1Var.get())
        self.Opener2SelectL=Label(self.master,text="Please select Non-Striker",width=40,anchor=W,justify=LEFT,font="Arial 9 bold").grid(row=2,column=4,sticky=W,pady=20)
        self.Opener2SelectS=OptionMenu(self.master,self.Opener2Var,*self.RemainingBatsman)
        self.Opener2SelectS.grid(row=2,column=5,padx=10)
        self.OverStart=Button(self.master,text='PROCEED',command=lambda:StartEntryS.Opener31SelectFunc(self))
        self.OverStart.grid(row=2,column=6,padx=10)

    def Opener31SelectFunc(self):
        self.RemainingBatsman.remove(self.Opener2Var.get())
        print(self.RemainingBatsman)
        BallbyBall(self.master,self.Team1,self.Team2,self.BattingSide,self.Opener1Var,self.Opener2Var,self.type,self.Filename,self.BowlerInfoFile,self.BatsmanInfoFile,self.BowlingSide,self.BowlerInfoList,self.RemainingBowler,self.BatsmanInfoList,self.RemainingBatsman,self.InningNum)
###############################################################################################################################################################################################################################################################
###############################################################################################################################################################################################################################################################

super=Tk()
w=super.winfo_screenwidth()
h=super.winfo_screenheight()
##############################
cnv=Canvas(super,borderwidth=0)
screen=Frame(cnv)
scrollbar=Scrollbar(super,orient="vertical",command=cnv.yview)
cnv.configure(yscrollcommand=scrollbar.set)

scrollbar.place(x='%d'%int(w-40),y=0,height='%d'%int(h-100))
cnv.place(x=0,y=0)
cnv.config(width='%d'%int(w-50),height='%d'%int(h-110))
cnv.create_window((4,4),window=screen,anchor='nw',tags='screen')
screen.bind("<Configure>",OnFrameConfigure)
##############################

option1=Options(screen)

super.geometry('%dx%d-0-50'%(w-20,h-100))
super.resizable(width=False,height=False)
mainloop()
