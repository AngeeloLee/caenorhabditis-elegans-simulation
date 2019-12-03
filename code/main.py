import code.Neuron
from code.neuronTypeMap import read_neuronType
from code.filehelper import read_neuronConnet

all = {}
sansor = {}
inter = {}
motor = {}
def start():
    neuronCounnect = read_neuronConnet()
    neuronType = read_neuronType()
    for i in range(0, len(neuronCounnect)):
        connectList = neuronCounnect[i]
        for j in range(0, len(connectList)):
            connect = connectList[j]
            if connect[0] not in all.keys():
                if neuronType[connect[0]] == 'SANSORY':
                    all[connect[0]] = SansorNeuron(connect[0])
                    sansor[connect[0]] = all[connect[0]]
                elif neuronType[connect[0]] == 'IINTERNEURON' or neuronType[connect[0]] == 'NEURON':
                    all[connect[0]] = InterNeuron(connect[0])
                    inter[connect[0]] = all[connect[0]]
                elif neuronType[connect[0]] == 'MOTOR':
                    all[connect[0]] = MotorNeuron(connect[0])
                    motor[connect[0]] = all[connect[0]]
            if connect[1] not in all.keys():
                if neuronType[connect[1]] == 'SANSORY':
                    all[connect[1]] = SansorNeuron(connect[1])
                    sansor[connect[1]] = all[connect[1]]
                elif neuronType[connect[1]] == 'IINTERNEURON' or neuronType[connect[1]] == 'NEURON':
                    all[connect[1]] = InterNeuron(connect[1])
                    inter[connect[1]] = all[connect[1]]
                elif neuronType[connect[1]] == 'MOTOR':
                    all[connect[1]] = MotorNeuron(connect[1])
                    motor[connect[1]] = all[connect[1]]
            if connect[2] == 'EJ':
                