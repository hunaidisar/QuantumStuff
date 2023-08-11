
from qiskit import QuantumCircuit, ClassicalRegister,QuantumRegister, execute,Aer
from random import randint
import numpy as np

# n can be randomized
n= 10
qc= QuantumCircuit(n,n)
#Alice's list pf random bits
l=[]
#Bob's list of bits he gets after measurment
lb=[]

# lists to keep Alice and Bob's random filter choices to compare them later
af=[]
bf=[]

#random list in bits for alice to send to bob
for i in range(n):
    l.append(randint(0,1))
print (l)

#3 more random lists to randomize alice, bob, and eve's filters
#Alic
ar=[]
for i in range(n):
    ar.append(randint(0,1))
#Bob
br=[]
for i in range(n):
    br.append(randint(0,1))
#Eve
er=[]  
for i in range(n):
    er.append(randint(0,1))   

##############
#initiallizing the random bits i the circuit

for i, e in enumerate(l):
    if e == 1:
        qc.x(i)
qc.barrier()   
#print(qc)

#########################

#applying Alice's filter

for i,e in enumerate(ar):
    if e == 1:
        qc.x(i)
        af.append("x")

    else:
        qc.h(i)
        af.append("h")
        
#applying Eve's filter

for i,e in enumerate(er):
    if e == 0:
        qc.x(i)
    else:
        qc.h(i)
        
#applying Bob's filter

for i,e in enumerate(br):
    if e == 0:
        qc.x(i)
        bf.append("x")
    else:
        qc.h(i)
        bf.append("h")
        
        
####################################    
         
print ("Alice's Filter" ,af)
print ("Bob's Filter", bf)    

qc.measure(range(n),range(n))
job = execute(qc, Aer.get_backend("qasm_simulator"),shots = 1)
count = job.result().get_counts()
print (count)

# counts represents the bits Bob gets after measurment
counts = list(count)[0]
qc.draw("mpl") 

###############################

#through classical communication Alice and Bob will compare notes

#Alice and Bob comparing filters
filterindex=[]
for i, e in enumerate(af):
    if bf[i] == e:
        filterindex.append(i)

# making counts into a list to be able to iterate over it
    
bbits=[] 
for i in reversed(counts) :
    bbits.append(int(i))
    

    
#print (filterindex)
print (bbits)

# new addition to the code
# #Alice and Bob comparing bits
# #Check List
cl = []
for i in filterindex:
    if (bbits[i])  == l[i]:
        cl.append("no prob bob")
    else:
        cl.append("hecking eve!")
        break
        
print(cl)
if ("hecking eve!") in cl:
    print ("The Chanel Has been Compromized! Abort and send again")



