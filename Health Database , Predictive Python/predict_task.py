import pprint
import random
data={}
def read_file():
	length=0
        file=open('E:\SWECHA\pythonproject\data_med.txt','r')
        for line in file :
		#line1=line.split('\n')
		line=line.strip()
                splitstring=line.split('||')
                name=splitstring[0]
                gender=splitstring[1]
                age=splitstring[2]
                symtom=splitstring[3].lower()
                disease=splitstring[4].lower()
                l=[]
		length+=1
                l.append(gender)
                l.append(age)
                l.append(symtom)
                l.append(disease)
                data[name]=l
	return length

def count_uniq(names):
	counts={}
	for name in names:
		if name in counts:
			counts[name] += 1
		else:
			counts[name] = 1
	return counts
length=read_file()
#print data
m=data.values()
diseases=[]
for listl in m:
	#co=1
	#for s1 in listl:
#		if co==4 :
#			diseases.append(s1)
#			break
#		else :
#			co+=1
	diseases.append(listl[-1])
#print diseases	
uniq_diseases= count_uniq(diseases)
len_dis=len(uniq_diseases.keys())
#print uniq_diseases
#print length
def random_gen():
	r=random.randrange(0,len_dis)
	i=0
	for name in uniq_diseases:
		if i<r-1:
			i+=1
		else :
			print "Random : "+name
			break	
random_gen()


s1=''
def most_probable():
	val=0
	s1=''
	for name in uniq_diseases :
		#rev[uniq_diseases[name]]=name
		val1=uniq_diseases[name]
		if val1>val :
			val=val1
			s1=name
	return s1+"  "+str(val)

print "Most Probable : "+most_probable()	

qualities=[]
def get_qualities():
	for name in data:
		qualities.append(data[name])
get_qualities()
#print qualities

def search_record(symptom):
	for name in data:
		if data[name][-2]==symptom :
			q=[]	
			q.append(name)
			print q+data[name]
	
search_record("loose stools")
		
def creating_mle():
	health_db={}
#	f=open("/home/swecha/team-5-predictive/data/data.txt",'r')
	for line in qualities:
		fsymptom=line[-2]
		fdisease=line[-1]
		if fsymptom not in health_db:
			health_db[fsymptom]={}
		if fdisease in health_db[fsymptom]:
					health_db[fsymptom][fdisease]+=1
		else :
					health_db[fsymptom][fdisease]=1  
		
	return health_db
health_db=creating_mle()
pprint.pprint(health_db)		


def search_mle(symptom):
	print health_db[symptom]

#pprint.pprint(search_mle("Pain Abdomen"))


def two_symptoms(symp1,symp2):
	u={}
	for line1 in qualities:
		f1symptom=line1[-2]
                f1disease=line1[-1]
		for line2 in qualities:
			f2symptom=line2[-2]
			f2disease=line2[-1]
		 	if symp1==f1symptom and symp2==f2symptom:
				if f1symptom==f2symptom:
					continue
				if f1disease==f2disease:
					if f1disease not in u:
						u[f1disease]=1
						print f1disease
					

two_symptoms('cough','pain abdomen')



def scale_disease(fsymptom):
	s=0
	scale={}
	for line in health_db[fsymptom]:
		s+=health_db[fsymptom][line]
#	print s
	for line in health_db[fsymptom]:
		scale[line]=round(float(health_db[fsymptom][line])/s,5)
	return scale

print scale_disease("fever")		
	

def multiple_probability(f1symptom,f2symptom,fdisease):
		scale1=scale_disease(f1symptom)
		scale2=scale_disease(f2symptom)
		prob=0.0
		if fdisease in scale1 :
			if fdisease in scale2:
				prob=scale1[fdisease]*scale2[fdisease]
				
		return prob
print multiple_probability('giddiness','stomatitis and mucositis','depression')



def intersect_symptoms(symp1,symp2,symp3):
	dict1=health_db[symp1]
	dict2=health_db[symp2]
	dict3=health_db[symp3]
	a=set(dict1.keys())
	b=set(dict2.keys())
	c=set(dict3.keys())
	
	
