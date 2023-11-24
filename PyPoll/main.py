import os
import csv

path=os.path.join("Resources", "election_data.csv")
with open(path) as file:
    csv_reader=csv.reader(file, delimiter=",")
    ballotcount=-1
    tally={}
    countylist=[]
    candidatelist=[]
    countytemp=str()
    candidatetemp=str()
    cvotes=0
    dvotes=0
    rvotes=0
    for i in csv_reader:
        if i[2]=='Charles Casper Stockham':
            cvotes+=1
        if i[2]=='Diana DeGette':
            dvotes+=1
        if i[2]=='Raymon Anthony Doane':
            rvotes+=1
        ballotcount+=1
        if i[1]!=countytemp:
            countytemp=i[1]
            countylist.append(countytemp)
        if i[2]!=candidatetemp:
            candidatetemp=i[2]
            candidatelist.append(candidatetemp)
    countylist.remove(countylist[0])
    candidatelist.remove(candidatelist[0])
    candidatelist2=[]
    for i in candidatelist:
        if i not in candidatelist2:
            candidatelist2.append(i)
    cpercent=cvotes/ballotcount
    dpercent=dvotes/ballotcount
    rpercent=rvotes/ballotcount
    tally['Charles Casper Stockham']=cvotes
    tally['Diana DeGette']=dvotes
    tally['Raymon Anthony Doane']=rvotes
    winner=max(cvotes, dvotes, rvotes)
    winnerlist=[]
    for i in tally:
        if tally[i]==winner:
            winnerlist.append(i)
            winnerlist.append(tally[i])

print('Election Results')
print('-------------------------------------------')
print('Total Votes: '+str(ballotcount))
print('-------------------------------------------')
print('Charles Casper Stockham: '+str(round(cpercent, 5)*100)+'%  ('+str(cvotes)+')')
print('Diana DeGette: '+str(round(dpercent, 5)*100)+'%  ('+str(dvotes)+')')
print('Raymon Anthony Doane: '+str(round(rpercent, 5)*100)+'%  ('+str(rvotes)+')')
print('-------------------------------------------')
print('Winner: '+winnerlist[0])
print('-------------------------------------------')

path2=os.path.join("analysis", "analysis.txt")
with open(path2, 'w') as notes:
    notes.write('Election Results')
    notes.write('\n-------------------------------------------')
    notes.write('\nTotal Votes: '+str(ballotcount))
    notes.write('\n-------------------------------------------')
    notes.write('\nCharles Casper Stockham: '+str(round(cpercent, 5)*100)+'%  ('+str(cvotes)+')')
    notes.write('\nDiana DeGette: '+str(round(dpercent, 5)*100)+'%  ('+str(dvotes)+')')
    notes.write('\nRaymon Anthony Doane: '+str(round(rpercent, 5)*100)+'%  ('+str(rvotes)+')')
    notes.write('\n-------------------------------------------')
    notes.write('\nWinner: '+winnerlist[0])
    notes.write('\n-------------------------------------------')
       
        
    

        
    

        