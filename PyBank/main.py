import os
import csv

path=os.path.join("Resources", "budget_data.csv")
with open(path) as file:
    csv_reader=csv.reader(file, delimiter=",")
    csvlist=[]
    monthcount=-1
    profits=0
    profitchangelist=[]
    pclsum=0
    greatestincval=0
    greatestincdate=str()
    greatestdecval=0
    greatestdecdate=str()
    for i in csv_reader:
        monthcount+=1
        csvlist.append(i)
    csvlist.remove(csvlist[0])
    for i in range(len(csvlist)):
        profits+=int(csvlist[i][1])
        if i!=0:
            change=int(csvlist[i][1])-int(csvlist[i-1][1])
            profitchangelist.append(change)
            if change>greatestincval:
                greatestincval=change
                greatestincdate=csvlist[i][0]
            if change<greatestdecval:
                greatestdecval=change
                greatestdecdate=csvlist[i][0]
    for i in profitchangelist:
        pclsum+=i
    avgchange=pclsum/len(profitchangelist)
    print('Financial Analysis')
    print('-----------------------------------------------')
    print('Total Months: '+str(monthcount))
    print('Total: '+str(profits))
    print('Average Change: '+str(avgchange))
    print('Greatest Increase in Profits: '+greatestincdate+' ('+str(greatestincval)+')')
    print('Greatest Decrease in Profits: '+greatestdecdate+' ('+str(greatestdecval)+')')
    
    path2=os.path.join('analysis', 'analysis.txt')
    with open(path2, 'w') as notes:
        notes.write('Financial Analysis')
        notes.write('\n-----------------------------------------------')
        notes.write('\nTotal Months: '+str(monthcount))
        notes.write('\nTotal: '+str(profits))
        notes.write('\nAverage Change: '+str(avgchange))
        notes.write('\nGreatest Increase in Profits: '+greatestincdate+' ('+str(greatestincval)+')')
        notes.write('\nGreatest Decrease in Profits: '+greatestdecdate+' ('+str(greatestdecval)+')')
    