from helpers import timeLog, newResult

# Anish
# Round Robin Algorithm
def round_robin(queue, add):
    time = 0
    result = newResult()

    print(timeLog(time) + 'Simulator started for RR')
    
    for process in queue:
        print(process)
        
    print(timeLog(time) + 'Simulator ended for RR')
    return result

# RR - define whether processes are added to the end or beginning of the ready queye when they arrive. Use rr_add and define distinct values BEGINNING and END (with END being the default behavior). An option third command-line argument can specify either BEGINNING or END to set this parameter

# Runtime output:
# time 0ms: Simulator started for RR [Q <empty>]
# time 0ms: Process A arrived and added to ready queue [Q A]
# time 0ms: Process B arrived and added to ready queue [Q A B]
# time 4ms: Process A started using the CPU [Q B]
# time 84ms: Time slice expired; process A preempted with 16ms to go [Q B]
# time 92ms: Process B started using the CPU [Q A]
# time 172ms: Time slice expired; process B preempted with 20ms to go [Q A]
# time 180ms: Process A started using the CPU with 16ms remaining [Q B]
# time 196ms: Process A terminated [Q B]
# time 204ms: Process B started using the CPU with 20ms remaining [Q <empty>]
# time 224ms: Process B terminated [Q <empty>]
# time 228ms: Simulator ended for RR

'''
def getElementsInList(Q):
    if(len(Q) > 0):
        output = "[Q"
        for alph in Q:
            output += " " + alph
        
        output += "]"
        return output
        
    return "[Q <empty>]"

def addElementsToQ(Q, processes, currTime):
    #Check to see which processes aren't in the Q
    #If not in the Q, and the process has arrived
    #If the process still has bursts left -> append it
    for key, value in processes.items():
        if(key not in Q):
            if(value[0] <= currTime):
                if(value[2] > 0):
                    #print(value)
                    Q.append(key)
                    elementsInList = getElementsInList(Q)
                    if(value[4] > 0):
                        print("time " + str(int(currTime)) + "ms: Process " + key + " completed I/O; added to ready queue " + elementsInList)
                    else:
                        print("time " + str(int(currTime)) + "ms: Process " + key + " arrived and added to ready queue " + elementsInList)
                    
    return Q    
    
#this function only runs when the Q is empty
#checks to make sure that all the processes have finished
#if not all processes finished: return false, else true
def checkIfAllProcessesDone(processes):
    for key, value in processes.items():
        if(value[2] > 0):
            return False
    return True

def roundRobin(processes):
    elementsInList = getElementsInList([])
    print("time 0ms: Simulator started for FCFS " + elementsInList)
    
    Q = []
    currTime = 0
    Q = addElementsToQ(Q, processes, currTime)
    
    t_cs = 8
    
    #Continually run each process then check to see if new processes need to be added to the Q
    
    #tf is a boolean flag that tells whether all the processes in the dict have finished or not -> primarily used if there is a gap between a set of processes finishing and a new one arriving (would make the Q empty temporarily)
    done = False
    currTime += t_cs / 2
    while(not done):
        Q = addElementsToQ(Q, processes, currTime)
        while(Q):
            currProcess = Q.pop(0)
            elementsInList = getElementsInList(Q)
            print("time " + str(int(currTime)) + "ms: Process " + currProcess + " started using the CPU " + elementsInList)
            #print(processes[currProcess])
            burstTime = processes[currProcess][1]
            ioTime = processes[currProcess][3]
            #processes[currProcess][0] += burstTime + ioTime + t_cs
            processes[currProcess][0] = currTime + burstTime + ioTime + t_cs/2
            processes[currProcess][2] -= 1
            processes[currProcess][4] += 1
            
            finTime = currTime + burstTime 
            while(currTime < finTime):
                currTime += 1
                Q = addElementsToQ(Q, processes, currTime)        
            elementsInList = getElementsInList(Q)            
            
            if(processes[currProcess][2] == 0):
                print("time " + str(int(currTime)) + "ms: Process " + currProcess + " terminated " + elementsInList)
            else:
                print("time " + str(int(currTime)) + "ms: Process " + currProcess + " completed a CPU burst; " + str(processes[currProcess][2]) + " bursts to go " + elementsInList)
                print("time " + str(int(currTime)) + "ms: Process " + currProcess + " switching out of CPU; will block on I/O until time " + str(int(currTime + ioTime + t_cs/2)) + "ms " + elementsInList)
                
                
            
            currTime += t_cs
            
            
        
        done = checkIfAllProcessesDone(processes)
        
        if(not done):
            currTime += 1

    currTime -= t_cs / 2
    print("time " + str(int(currTime)) + "ms" + " Simulator ended for FCFS")
        
        
file = open('p1-input01.txt','r')

processes = dict()


#Extract info from input file
for line in file:
    if(len(line) > 0 and line[0] != '#'):
        elements = line.split('|')        
        for i in range(1,len(elements)):
            elements[i] = int(elements[i])
            processes[line[0]] = elements[1:]
            processes[line[0]].append(0)

file.close()


roundRobin(processes)
'''