from copy import deepcopy
from random import choice

def contract(graph):
    #choice returns a random element from the non-empty sequence seq
    chosen_key = choice(list(graph.keys()))
    chosen_elems = choice(graph[chosen_key])
    new_key = chosen_key + "-" + chosen_elems
    graph[new_key] = graph[chosen_key] + graph[chosen_elems]
    del graph[chosen_key], graph[chosen_elems]
    for key in graph.keys():
        copy = graph[key][:]
        if new_key != key:
            for item in copy:
                if item == chosen_key or item == chosen_elems:
                    graph[key].remove(item)
                    graph[key].append(new_key)
        else:
            for item in copy:
                if item == chosen_key or item == chosen_elems:
                    graph[key].remove(item)
                    
    
def minCut(graph):
    n = len(graph)
    minimum = n * (n-1) // 2
    for i in range(n):
        copy =  deepcopy(graph)
        while len(copy) > 2:
            contract(copy)
            minimum = min(minimum, len(list(copy.values())[0]))
    return minimum
        

graph = {}
#1	37	79	164	155	32	87	39	113....
#separate the first and 
with open('kargerMinCut.txt') as f:
    data = f.readlines()
    for line in data:
        #e.g. 
        #create a list separated by tabs. Do not include the last element \n
        arr_line = line.split('\t')[:-1]
        #convert to a list of strings
        elements = list(map(str, arr_line))
        #first element 
        key = str(elements[0])
        #key : [rest of elements in the line]
        graph[key] = elements[1:]
        
f.close()       
print(minCut(graph)) #17
