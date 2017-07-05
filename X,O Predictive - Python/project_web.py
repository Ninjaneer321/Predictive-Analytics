from bottle import route,run,Bottle,template,request
import random
import pprint

app = Bottle()

@app.route('/')
def home():
    return template('home')
maindict={}
probdata={}
i=range(0,9)
for k in i:
        maindict[k]={'x':{'positive':0,'negative':0},'o':{'positive':0,'negative':0},'b':{'positive':0,'negative':0}}
        probdata[k]={'x':{'win':0,'lose':0},'o':{'win':0,'lose':0},'b':{'win':0,'lose':0}}
#print maindict
def read_file():
        length=0
        file=open('datas_shuf.txt','r')
        for line in file :
                if len(line)==0:
                        break
                #line1=line.split('\n')
                line=line.strip()
                splitstring=line.split(',')
                c=[0]*10
                c[0]=splitstring[0]
                c[1]=splitstring[1]
                c[2]=splitstring[2]
                c[3]=splitstring[3]
                c[4]=splitstring[4]
                c[5]=splitstring[5]
                c[6]=splitstring[6]
                c[7]=splitstring[7]
                c[8]=splitstring[8]
                c[9]=splitstring[9]
               # print c
                for i in range(0,9):
                        maindict[i][c[i]][c[9]]+=1
                length+=1
        #return length

read_file()

pprint.pprint(maindict)
for k in range(0,9):
    probdata[k]['x']['win']=round(float(maindict[k]['x']['positive'])/(maindict[k]['x']['positive']+maindict[k]['x']['negative']),6)
    probdata[k]['x']['lose']=round(1-probdata[k]['x']['win'],6)

for k in range(0,9):
    probdata[k]['o']['win']=round(float(maindict[k]['o']['positive'])/(maindict[k]['o']['positive']+maindict[k]['o']['negative']),6)
    probdata[k]['o']['lose']=round(1-probdata[k]['o']['win'],6)

for k in range(0,9):
    probdata[k]['b']['win']=round(float(maindict[k]['b']['positive'])/(maindict[k]['b']['positive']+maindict[k]['b']['negative']),6)
    probdata[k]['b']['lose']=round(1-probdata[k]['b']['win'],6)

pprint.pprint(probdata)

def cal_prob_win(k):
    print k
    prob1=1
    prob2=1
    for i in k:
        if k[i]=='x':
            prob1*=probdata[i]['x']['win']
        elif k[i]=='o':
            prob2*=probdata[i]['o']['lose']
    return prob1+prob2

def cal_prob_lose(k):
    print k
    prob1=1
    prob2=1
    for i in k:
        if k[i]=='x':
            prob1*=probdata[i]['x']['lose']
        elif k[i]=='o':
            prob2*=probdata[i]['o']['win']
    return prob1+prob2

"""def cal_prob_win(k):
        print k
        prob1=1
        for i in k:
              if k[i]=='x':             
                 prob1*=probdata[i][k[i]]['win']
        return prob1
    
def cal_prob_lose(k):
    print k
    prob1=1
    for i in k:
            if k[i]=='o':
                    prob1*=probdata[i][k[i]]['lose']
    return prob1"""
@app.route('/gen_rand')
def gen_rand():
        flag=random.randrange(0,2)
        """if flag==0:
           flag=-1
        else :
           flag=1"""
        flag=1
        count=0
        #count2=0
        position={}
        while True:
                x1=random.randrange(0,9)
                if count==9:
                        break
                if x1 not in position:
                        if flag==1:
                                position[x1]='x'
                                flag*=-1
                                count+=1
                                #if count1 >=3:
                                 #   m=cal_prob(position)
#  if m>0.5:
                                   #     print 'x :'+str(m)
                                    #    break

                        else:
                                position[x1]='o'
                                flag*=-1
                                count+=1
                                #m=cal_prob(position)
                                #if count2>=3:
                                  #  if m<0.5:
                                   #        print 'o :'+str(m)
                                       #    break
	
	
	f1=cal_prob_win(position)
	f2=cal_prob_lose(position)
	str=''
	if f1>f2:
	    str1='x wins'
	else :
	    str1='o wins'
	return template('random',f1=str(f1),f2=str(f2),p0=position[0],p1=position[1],p2=position[2],p3=position[3],p4=position[4],p5=position[5],p6=position[6],p7=position[7],p8=position[8],str2=str1)
@app.route('/get_inp')
def get_inp():
    return template('design')
@app.route('/result')
def result():
    position={}
   # print "Give the inputs according to the cells positions , from left to right and top to bottom \n:"
    #for i in range(0,9):
    #position[i]=raw_input("x or o or blank (b) of cell "+str(i+1)+" :")
    position[0]=request.forms.get('cell0')
    position[1]=request.forms.get('cell1')
    position[2]=request.forms.get('cell2')
    position[3]=request.forms.get('cell3')
    position[4]=request.forms.get('cell4')
    position[5]=request.forms.get('cell5')
    position[6]=request.forms.get('cell6')
    position[7]=request.forms.get('cell7')
    position[8]=request.forms.get('cell8')
    prob1=1
    prob2=1
    for i in position:
            prob1*=probdata[i][position[i]]['win']
    for i in position:
            prob2*=probdata[i][position[i]]['lose']
    #return template('show',prob=prob1)
    str1=''
    if prob1>prob2:
           str1='x wins'
    else :
           str1='o wins'
    return template('show',prob=prob1,p0=position[0],p1=position[1],p2=position[2],p3=position[3],p4=position[4],p5=position[5],p6=position[6],p7=position[7],p8=position[8],str2=str1)       
run(app, host='localhost', port=7777, debug=True)
