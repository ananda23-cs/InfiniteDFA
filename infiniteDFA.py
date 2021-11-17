import json
import networkx as nx

# f1 = open('test1.json')
# data1 = json.load(f1)
# f2 = open('test2.json')
# data2 = json.load(f2)
# f3 = open('test3.json')
# data3 = json.load(f3)
# f4 = open('test4.json')
# data4 = json.load(f4)
# f5 = open('test5.json')
# data5 = json.load(f5)

# dfa1 = nx.DiGraph()
# dfa1.add_nodes_from(data1["states"])
# dfa2 = nx.DiGraph()
# dfa2.add_nodes_from(data2["states"])
# dfa3 = nx.DiGraph()
# dfa3.add_nodes_from(data3["states"])
# dfa4 = nx.DiGraph()
# dfa4.add_nodes_from(data4["states"])
# dfa5 = nx.DiGraph()
# dfa5.add_nodes_from(data5["states"])

sampleF = open("sampleDFA.json")
sampleData = json.load(sampleF)

if (sampleData["start_state"] not in sampleData["states"]):
    raise ValueError("Invalid DFA")

for final in sampleData["final_states"]:
    if final not in sampleData["states"]:
        raise ValueError("Invalid DFA")

sampleDFA = nx.DiGraph()
sampleDFA.add_nodes_from(sampleData["states"])
for transition in sampleData["trans_func"]:
    sampleDFA.add_edge(transition[0], transition[2], weight=transition[1])

for accept_state in sampleData["final_states"]:
    sources = sampleData['states'][0:len(sampleData['states'])]
    for source in sources:
        if nx.has_path(sampleDFA,source,accept_state):
            if nx.find_cycle(sampleDFA,source,'original') is not None:
                print("DFA is Infinite")
                exit(0)
    
print("DFA is not infinite")