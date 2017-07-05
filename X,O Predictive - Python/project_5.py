import random
import pprint
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
		            	   # 	    print 'o :'+str(m)
		        		#    break


	return position
#def rand_inp():
 #   count1=0
  #  count2=0
   # dict1{}
   # flag=1
   # if flag==1:
    #        x1=random.randrange(0,9)
 #"""           

p=gen_rand()
print str(cal_prob_win(p))+"  "+str(cal_prob_lose(p))
            

