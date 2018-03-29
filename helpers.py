# Helper function for creating the time log text
def timeLog(time):
    return 'time ' + str(time) + 'ms: '

# Returns an empty result structure for each algorithm
def newResult():
    result = {
        'name': '',
        'avg_cpu_burst': 0,
        'avg_wait': 0,
        'avg_turnaround': 0,
        'total_ctx_switch': 0,
        'total_preemptions': 0
    }
    return result
    
    
def queueLog(queue):
    currentQueue = []
    for process in queue:
        currentQueue.append(process['proc_id'])
    # " ".join(currentQueue)
    if len(queue) == 0:
        return ' [Q <empty>]'
    else:
        return ' [Q ' + ' '.join(currentQueue) + ']'

def getProcess(queue, proc_id):
    for p in queue:
        if (p['proc_id'] == proc_id):
            return p
        
def removeFromQueue(queue, proc_id):
    Q = []
    for p in queue:
        if p['proc_id'] != proc_id:
            Q.append(p)
    return Q