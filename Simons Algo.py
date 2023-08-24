# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:43:31 2023

@author: Acer
"""

from qiskit import QuantumCircuit, Aer, execute, QuantumRegister, ClassicalRegister
import numpy as np
from qiskit.visualization import plot_histogram
from random import randint

n=4

inpr = QuantumRegister(n, name = "Input")
ancr = QuantumRegister(n, name = "Anc")
cr = ClassicalRegister(n)
cr2 = ClassicalRegister(n)
qc = QuantumCircuit(inpr,ancr,cr,cr2)

def SimAlg():
    
    qc.h(inpr)
    qc.barrier()
    
    oracle()

    qc.measure(ancr,cr)
    job= execute(qc, Aer.get_backend('qasm_simulator'),shots =1000)
    output= job.result().get_counts()  
    print(output)
    o = []
    qc.barrier()   
    # for i in (list(output)[:]) :
    #         o.append((i))
    # print (o)
    # if str(key) in o :
    #     print ("its mapping to the same output")
    #     print (o.index(str(key)))
    #     #print(list(output)[o.index(str(key))])
    # else:
    #     print ("all good")
    qc.h(inpr)
    qc.measure(inpr,cr)
    job= execute(qc, Aer.get_backend('qasm_simulator'),shots =1000)
    output2= job.result().get_counts()  
    print(output)
    o = []
    plot_histogram(output2)
    
    
    
def oracle():
    
    key = [randint(0, 1) for i in range(n)] 
    while False :
        if key == [0] * n:
            False
        else: 
            True
            
        
    print (key)
    skey = "".join(str(e) for e in key)
    print (skey)
    qc.cx(inpr,ancr)
    
    x =[]
    for i, e in (enumerate(skey)):
        if e == "1":
            print (i)
            x.append(i)
            
    print ( "x is ", x )
    
    for i in (range(n)):
        if i in x:
            qc.cx(inpr[x[0]],ancr[i])
            
    qc.barrier()
    print (qc)           
   
SimAlg()
#qc.draw("mpl")