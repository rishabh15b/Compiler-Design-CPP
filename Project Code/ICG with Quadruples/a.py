fp=open("out.txt","r")
lines=fp.readlines()
#print(lines)
#lines.pop()
c=0
d_value={}
d_reg={}
used=[0]*16
#print(lines)
i=0
while(i<len(lines)):
	stmt=lines[i]
	stmt=stmt.strip("\n")
	#print(stmt)
	if("=" in stmt):
		index=stmt.index("=")
		lhs=stmt[0:index]
		exp=stmt[index+1::]
		lhs=lhs.strip()
		exp=exp.strip()
		#print(lhs,exp)
		if(exp.isdigit()):
			i=i+1
			if(lhs not in d_reg):
				used[c]=1
				s="R"+(str(c))
				print("MOV ",s,",#",exp,sep="")
				c=c+1
				d_value[lhs]=int(exp)
				d_reg[lhs]=s
			else:
				d_value[lhs]=int(exp)
				print("MOV ",d_reg[lhs],",#",exp,sep="")
		elif(("*" in exp) or ("/" in exp) or ("%" in exp) or("+" in exp) or ("-" in exp)):
			operand1,op,operand2=exp.split()
			operand1=operand1.strip()
			operand2=operand2.strip()
			op=op.strip()
			#print(operand1,op,operand2)
			if(not operand1.isdigit() or not operand2.isdigit()):
				if(d_reg.get(operand1)==None and not operand1.isdigit()):
					s="R"+str(c)
					c=c+1
					d_reg[operand1]=s
					print("LDR ",s,",",operand1,sep="")
				if(d_reg.get(operand2)==None and not operand2.isdigit()):
					s="R"+str(c)
					c=c+1
					d_reg[operand2]=s
					print("LDR ",s,",",operand2,sep="")
			if(d_reg.get(operand1)!=None and d_reg.get(operand2)!=None):
				str1=d_reg[operand1]
				str2=d_reg[operand2]
			
			elif(operand1.isdigit()):
					str1="#"+operand1
					str2=d_reg[operand2]
			elif(operand2.isdigit()):
					str1=d_reg[operand1]
					str2="#"+operand2
			next_stmt=lines[i+1]
			next_stmt.strip()
			index=next_stmt.index("=")
			lhs=next_stmt[0:index]
			lhs=lhs.strip()

			if(d_reg.get(lhs)==None):
				s="R"+str(c)
				c=c+1
				d_reg[lhs]=s
				print("LDR ",s,",",lhs,sep="")
			if(op=="*"):
				print("MUL ",d_reg[lhs],",",str1,",",str2,sep="")
			elif(op=="+"):
				print("ADD ",d_reg[lhs],",",str1,",",str2,sep="")
			elif(op=="-"):
				print("SUB ",d_reg[lhs],",",str1,",",str2,sep="")
			elif(op=="/"):
				print("DIV ",d_reg[lhs],",",str1,",",str2,sep="")
			elif(op=="%"):
				print("MOD ",d_reg[lhs],",",str1,",",str2,sep="")
			i=i+2
		elif((">" in exp) or ("<" in exp)):
			#print(exp)
			operand1,op,operand2=exp.split()
			operand1=operand1.strip()
			operand2=operand2.strip()
			op=op.strip()
			
			if(d_reg.get(operand1)==None and not operand1.isdigit()):
				s="R"+str(c)
				c=c+1
				d_reg[operand1]=s
				print("LDR ",s,",",operand1,sep="")
			
			if(d_reg.get(operand2)==None and not operand2.isdigit()):
				s="R"+str(c)
				c=c+1
				d_reg[operand2]=s
				print("LDR ",s,",",operand2,sep="")
			if(d_reg.get(operand1)!=None and d_reg.get(operand2)!=None):
				str1=d_reg[operand1]
				str2=d_reg[operand2]
			
			elif(operand1.isdigit()):
				str1="#"+operand1
				str2=d_reg[operand2]
			elif(operand2.isdigit()):
				str2="#"+operand2
				str1=d_reg[operand1]
			s="R"+str(c)
			c=c
			print("SUB ",s,",",str1,",",str2,sep="")
			if(op=="<"):
				print("BGZ ",s,",",sep="",end="")
			elif(op==">"):
				print("BLZ ",s,",",sep="",end="")
			elif(op==">="):
				print("BLEZ ",s,",",sep="",end="")
			elif(op=="<="):
				print("BGEZ ",s,",",sep="",end="")
			next_stmt=lines[i+2]
			print(next_stmt.split()[3])
			i=i+3
	elif("L" in stmt.split()[0]):
		print(stmt)
		i=i+1
	elif(stmt.split()[0]=="goto"):
		print("BR ",stmt.split()[1])
		i=i+1

# handle "<="