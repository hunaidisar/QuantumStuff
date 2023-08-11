# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:00:52 2023

@author: Acer
"""


from qiskit import QuantumCircuit , execute , Aer

#decode
qc4 = QuantumCircuit(2)
qc4.cx(0,1)
qc4.h(0)
decode = qc4.to_gate(label = "Decode")

#encode
encode = QuantumCircuit(2)
encode.h(0)
encode.cx(0,1)
encode = encode.to_gate(label= "Encode")

qc = QuantumCircuit(2,2)
QM = input("enter your choice , 00,01,10,11 ")

def selectedM(qm):
    
    try:

        if qm == "00" :
            qc0 = QuantumCircuit(2)
            qc0.i(0)
            firstchoice = qc0.to_gate(label= "Message 1")
            return (firstchoice)
            
            print (qc)
        elif qm == "01":
            qc1 = QuantumCircuit(2)
            qc1.x(0)
            secondchoice = qc1.to_gate(label= "Message 2")
            return (secondchoice)
            
            print (qc)
        elif qm == "10":
            qc2 = QuantumCircuit(2)
            qc2.z(0)
            thirdchoice = qc2.to_gate(label= "Message 3")
            return (thirdchoice)
            
            print(qc)
        elif qm == "11":
            qc3 = QuantumCircuit(2)
            qc3.x(0)
            qc3.z(0)
            fourthchoice = qc3.to_gate(label= "Message 4")
            return (fourthchoice)
            
            print(qc)
            
                
    except TypeError as er:
        #errorText = er
        pass


def quantumMessage(qm):
    
    qc.append(encode,[0,1])
    try:            
        qc.append(selectedM(qm),[0,1])   
        qc.append(decode, [0,1])
        print (qc)
        qc.measure([0,1],[0,1])
        job = execute(qc,Aer.get_backend('qasm_simulator'),shots=5)
        output = job.result().get_counts()
        print ("message is " + list(output)[0])
    except TypeError:
        print("please restart and enter a valid choice")
        print("session ended")
        #print ("error text: ",errorText)
        
        
        
    
    
quantumMessage(QM)