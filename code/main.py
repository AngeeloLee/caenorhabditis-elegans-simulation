import neuronTypeMap
import filehelper
import Neuron

all = {}
sansor = {}
inter = {}
motor = {}
def action():
    neuronCounnect = filehelper.read_neuronConnect()
    neuronType = neuronTypeMap.read_neuronType()

    for i in range(0, len(neuronCounnect)):
        connectList = neuronCounnect[i]
        for j in range(0, len(connectList)):
            connect = connectList[j]
            if connect[0] not in all:
                if neuronType[connect[0]] == 'SENSORY':
                    all[connect[0]] = Neuron.SansorNeuron(connect[0])
                    sansor[connect[0]] = all[connect[0]]
                elif neuronType[connect[0]] == 'INTERNEURONS' or neuronType[connect[0]] == 'NEURON':
                    all[connect[0]] = Neuron.InterNeuron(connect[0])
                    inter[connect[0]] = all[connect[0]]
                elif neuronType[connect[0]] == 'MOTOR':
                    all[connect[0]] = Neuron.MotorNeuron(connect[0])
                    motor[connect[0]] = all[connect[0]]
            if connect[1] not in all:
                if neuronType[connect[1]] == 'SENSORY':
                    all[connect[1]] = Neuron.SansorNeuron(connect[1])
                    sansor[connect[1]] = all[connect[1]]
                elif neuronType[connect[1]] == 'INTERNEURONS' or neuronType[connect[1]] == 'NEURON':
                    all[connect[1]] = Neuron.InterNeuron(connect[1])
                    inter[connect[1]] = all[connect[1]]
                elif neuronType[connect[1]] == 'MOTOR':
                    all[connect[1]] = Neuron.MotorNeuron(connect[1])
                    motor[connect[1]] = all[connect[1]]
            if connect[2] == 'EJ':
                all[connect[0]].addNeuron("cellular", Neuron.Neuron(connect[1],all[connect[1]],'EJ',connect[3]))
                all[connect[1]].addNeuron("cellular", Neuron.Neuron(connect[0],all[connect[0]],'EJ',connect[3]))
            elif connect[2] == 'S':
                all[connect[0]].addNeuron("font", Neuron.Neuron(connect[1],all[connect[1]],'S',connect[3]))
                all[connect[1]].addNeuron("back", Neuron.Neuron(connect[0],all[connect[0]],'S',connect[3]))
            elif connect[2] == 'Sp':
                all[connect[0]].addNeuron("back", Neuron.Neuron(connect[1],all[connect[1]],'S',connect[3]))
                all[connect[1]].addNeuron("font", Neuron.Neuron(connect[0],all[connect[0]],'S',connect[3]))
            elif connect[2] == 'R':
                all[connect[0]].addNeuron("font", Neuron.Neuron(connect[1],all[connect[1]],'R',connect[3]))
                all[connect[1]].addNeuron("back", Neuron.Neuron(connect[0],all[connect[0]],'R',connect[3]))
            elif connect[2] == 'Rp':
                all[connect[0]].addNeuron("back", Neuron.Neuron(connect[1],all[connect[1]],'R',connect[3]))
                all[connect[1]].addNeuron("font", Neuron.Neuron(connect[0],all[connect[0]],'R',connect[3]))
    
    for name,neuron in all:
        neuron.start()
        print(name + " started")

    sleep(10000)


if __name__ == '__main__':
    action()