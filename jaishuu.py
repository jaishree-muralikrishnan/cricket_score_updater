##def check(n):
##    count = 0
##    for i in range(0,len(n)):
##        if n[i]=='a':
##            count+=1
##    return count
##print(check('abrakadabra'))
##
##
##def email(mail_id):
##    for i in range(0,len(mail_id)):
##        if mail_id[i]=='@':
##            a=i
##            break
##    return(mail_id[0:a])
##print(email('sameyboi@gmail.com'))

#(team1=rahul,subhman,virat,sky,hardik,jadeja,axar,shami,siraj,bumrah,kuldeep)
#(team2=azam,rizwan,jos buttler,maxwell,kane,markram,liam,rashid,naseem,archer,boult)
#score update,wicket update,batter name,bowler name,runs add to bowler nd batter, strikerate, economy)
def scoreupdate(score,run):
    score+=run
    return score
def strikerate(runs,balls):
    return (runs/balls)*100
def economy(run,over):
    return (run/over)
def battername(name,runs):
    pass
def bowlername(name,runs):
    pass
def bowlerwicket(name, wicket):
    pass
def update(runs,battername, bowlername, nb=False,wide=False):
    pass

    

