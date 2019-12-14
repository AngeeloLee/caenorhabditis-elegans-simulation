import neuronTypeMap
import filehelper
import Readenv
import Neuron
from time import sleep

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
                if connect[0] == 'NMJ':
                    pass
                elif neuronType[connect[0]] == 'SENSORY':
                    all[connect[0]] = Neuron.SansorNeuron(connect[0],'SENSORY')
                    sansor[connect[0]] = all[connect[0]]
                elif neuronType[connect[0]] == 'INTERNEURONS' or neuronType[connect[0]] == 'NEURON':
                    all[connect[0]] = Neuron.InterNeuron(connect[0],'INTERNEURONS')
                    inter[connect[0]] = all[connect[0]]
                elif neuronType[connect[0]] == 'MOTOR':
                    all[connect[0]] = Neuron.MotorNeuron(connect[0],'MOTOR')
                    motor[connect[0]] = all[connect[0]]
            if connect[1] not in all:
                if connect[1] == 'NMJ':
                    pass
                elif neuronType[connect[1]] == 'SENSORY':
                    all[connect[1]] = Neuron.SansorNeuron(connect[1],'SENSORY')
                    sansor[connect[1]] = all[connect[1]]
                elif neuronType[connect[1]] == 'INTERNEURONS' or neuronType[connect[1]] == 'NEURON':
                    all[connect[1]] = Neuron.InterNeuron(connect[1],'INTERNEURONS')
                    inter[connect[1]] = all[connect[1]]
                elif neuronType[connect[1]] == 'MOTOR':
                    all[connect[1]] = Neuron.MotorNeuron(connect[1],'MOTOR')
                    motor[connect[1]] = all[connect[1]]
            if connect[2] == 'NMJ':
                pass
            elif connect[2] == 'EJ':
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
    i = 0
    for name in all:
        all[name].start()
        print(str(i) + " : " + name + " of " + all[name].type + " Neuron has born")
        i += 1

    print('==============================')
    print('all Neurons has been activated')
    # sleep(2000)

    env = Readenv.read_env()

    for i in range(0, len(env)):
        signal = env[i]
        sansor[signal[0]].Sansor(Neuron.Signal(signal[1],signal[3],signal[2]))
        print(signal[0] + ' get a signal' + signal[1] + ' from env')

    # i = 0
    # print('==============================')
    # for name in all:
    #     all[name].stop()
    #     print(str(i) + " : " + name + " was dead")
    #     i += 1

    # print('==============================')
    # print('all Neurons was dead')

if __name__ == '__main__':
    action()