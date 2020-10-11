n=int(input("Enter the number of users: \n"))
a=dict()
b=list(map(str,input("Enter the name: ").split()))
for i in range(n):
	a[i]=[b[i]]
for i in range(n):
	for j in range(1,n+1):
		a[i].append(0)
r=[]
print("1. INR \n2. USD\n3. BND\n4. CDF")
x=int(input("Enter the mode of payment: "))
if(x==1):
	f="Rs"
elif(x==2):
	f="$"
elif(x==3):
	f="B$"
elif(x==4):
	f="FC"
else:
	print("Enter a proper mode...\n")
y=str(input("Type New to enter new transaction and analyse for analysing the recent transactions: \n"))
while(y=="new" or y=="New" or y=="NEW"):
	m=str(input("Enter the name of the person who has payed: "))
	def ret(m):
		for key in a:
				if(a[key][0]==m):
					return key
	k=ret(m)
	q=float(input("Enter the amount: "))
	z=int(input("Press 1 to split equally \nPress 2 to split unequally \n"))
	if(z==1):
		for i in range(n):
			if(a[i][0]!=m):
				for j in range(1,n+1):
					if(j==i+1):
						a[i][k+1]-=q/n
					a[i][i+1]=0
			else:
				for j in range(1,n+1):
					a[i][j]+=q/n
					a[i][i+1]=0
		
	elif(z==2):
		print("Splitting Unequally\n")
		print("Enter the share of each person: ")
		for key in a:
			v=float(input(a[key][0]+" : "))
			a[key][k+1]-=v
			a[k][key+1]+=v
			if(a[key][0]==m):
				a[key][k+1]=0
		
	else:
		print("Enter a valid option...\n")
	y=str(input("\nType New to enter new transaction and analyse for analysing the recent transactions: "))
if(y=="analyse" or y=="Analyse" or y=="ANALYSE"):
	print("Press ",end=" ")
	for i in range(n-1):
		print(str(i+1)+ " for "+a[i][0],end=" || ")
	print(str(i+2)+" for "+a[i+1][0])
	print("\n Press all to analyse the transaction for all: \n")
	p=str(input("Enter the option: "))
	if(p=="all"):
		flag1=1
		for key in a:
			for j in range(1,n+1):
				if(a[key][j]>0):
					print(str(a[j-1][0])+" owes "+str(a[key][j])+" "+f+" for "+a[key][0],end="\n")
					flag1=0
				elif(a[key][j]<0):
					print(a[key][0]+" should pay "+str(-a[key][j])+" "+f+" to "+a[j-1][0],end="\n")
					flag1=0
		if(flag1==1):
			print("No one owes anyone... :)")
	else:
		flag=1
		q=int(p)-1
		for j in range(1,n+1):
			if(a[q][j]>0):
				print(a[j-1][0]+" owes "+str(a[q][j])+" "+f+" for "+a[q][0],end="\n")
				flag=0
			elif(a[q][j]<0):
				print(a[q][0]+" should pay "+str(-a[q][j])+" "+f+" to "+a[j-1][0],end="\n")
				flag=0
		if(flag==1):
			print(a[q][0]+" does not owe anyone and he has nothing to get from others... :)")