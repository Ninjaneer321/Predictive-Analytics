from bottle import route,run,Bottle,template,request
app=Bottle()
data ={'':[]}
def read_file():
	file=open('/home/swecha/team-5-predictive/data/data.txt','r')
	for line in file.readlines():
		splitstring=line.split('||')
		name=splitstring[0]
		gender=splitstring[1]
		age=splitstring[2]
		symtom=splitstring[3]
		disease=splitstring[4]
		l=[]
		l.append(gender)
		l.append(age)
		l.append(symtom)
		l.append(disease)
		data[name]=l
read_file()
fruits=[]
#print data
def read_fruits():
	file=open("/home/swecha/team-5-predictive/data/apples_oranges.txt","r")
	for line in file.readlines():
		line=line.strip()
		ss=line.split('\t')
		size=ss[0]
		shape=ss[1]
		color=ss[2]
		texture=ss[3]
		weight=ss[4]
		taste=ss[5]
		class1=ss[6]
@app.route('/')
def home():
	return template('home')
@app.route('/head_tail')
def head_tail():
	return template('head_tail')
@app.route('/count_item')
def count_item():
	return template('count_item')
@app.route('/customer')
def customer():
        return template('customer')
@app.route('/customer_count')
def customer_count():
        return template('customer_count')
run (app,host='localhost',port=7777,debug=True)
