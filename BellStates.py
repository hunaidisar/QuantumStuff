# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 17:02:24 2023

@author: Acer
"""


from qiskit import QuantumCircuit , execute , Aer
from qiskit.visualization import plot_state_qsphere , plot_bloch_multivector

def BellStates():
    print ("first Ball state") 
    qc = QuantumCircuit(2,1)
    qc.h(0)
    qc.cx(0,1)
    print(qc)
    job= execute(qc, Aer.get_backend('statevector_simulator'))
    output= job.result().get_statevector()
    plot_state_qsphere(output)
    #plot_bloch_multivector(output)
    
    print ("Second Ball state") 
    qc = QuantumCircuit(2,1)
    qc.h(0)
    qc.cx(0,1)
    qc.z(0)
    job= execute(qc, Aer.get_backend('statevector_simulator'))
    output= job.result().get_statevector()
    plot_state_qsphere(output)
    #plot_bloch_multivector(output)
    
    
    print(qc)
    
    print ("Third Ball state") 
    qc = QuantumCircuit(2,1)
    qc.h(0)
    qc.cx(0,1)
    qc.x(0)
    job= execute(qc, Aer.get_backend('statevector_simulator'))
    output= job.result().get_statevector()
    plot_state_qsphere(output)
    #plot_bloch_multivector(output)
    
    print(qc)
    
    print ("Fourth Ball state") 
    qc = QuantumCircuit(2,1)
    qc.h(0)
    qc.cx(0,1)
    qc.x(0)
    qc.z(1)
    print(qc)
    job= execute(qc, Aer.get_backend('statevector_simulator'))
    output= job.result().get_statevector()
    plot_state_qsphere(output)
    #plot_bloch_multivector(output)

BellStates()
