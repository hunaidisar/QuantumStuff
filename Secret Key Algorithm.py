
"""
Created on Mon Au...........
............................g  7 16:14:48 2023

@author: Acer
"""

from qiskit import QuantumCircuit, Aer, execute
from random import randint


n = 4
qc = QuantumCircuit(n+1,n)

def oracle ():
    
    S=[]
    # generating a secret key of length n 
    
    for i in range(n):
        x = randint(0,1)
        S.append(x)
        
        
    # printing the secret key to be able to confirm after running the measuremnt.    
    print (" S = ", S)
    
    # iterating over the secret key values and applying the corresponding gates
    for r , e in enumerate(S) :
        
        if e == len(S)-2:
            pass
        elif e == 0:
            qc.i(r)
            
        elif e == 1:            
            qc.cx(r,n)
            
def alg():
            
    qc.x(n)
    qc.h(range(n+1))
    
    qc.barrier()
    oracle()
    qc.barrier()
    qc.h(range(n))
    print (qc)
    qc.measure(range(n), range(n))
    
    job = execute(qc, Aer.get_backend("qasm_simulator"), shots =1000)
    output= job.result().get_counts()    
    print(output)
    qc.draw("mpl")
    
    key=[] 
    for i in reversed(list(output)[0]) :
        key.append(int(i))
        
    print ("the key is " , key)

alg()

            

            
            