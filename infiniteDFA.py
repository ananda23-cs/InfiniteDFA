import json, os
import networkx as nx

#parses json file
def test(filename):
    #opens the JSON input file
    with open(filename) as f:
        if os.path.getsize(filename) == 0:
            raise OSError("Empty JSON input file")
        data = json.load(f)
        if len(data) == 2:
            raise IOError("JSON has no data.")

    #constructs DFA and performs edge cases for badly formatted DFA's
    if data["start_state"] not in data["states"]:
        raise ValueError("Invalid DFA")

    for final in data["final_states"]:
        if final not in data["states"]:
            raise ValueError("Invalid DFA")

    dfa = nx.DiGraph()
    dfa.add_nodes_from(data["states"])

    if len(data["trans_func"]) < (len(data["alphabet"]) * len(dfa.nodes)):
        raise ValueError("Invalid DFA")
    
    #adds edges to directed graph
    for transition in data["trans_func"]:
        if transition[0] not in dfa.nodes or transition[2] not in dfa.nodes:
            raise ValueError("Invalid DFA")
        if transition[1] not in data["alphabet"]:
            raise ValueError("Invalid DFA")
        
        dfa.add_edge(transition[0], transition[2], weight=transition[1])

    #create sets of nodes and edges belonging in a cycle
    cycleNodeSet = set()
    for cycle_node_list in nx.simple_cycles(dfa):
        for node in cycle_node_list:
            cycleNodeSet.add(node)
    transitionSet = set()
    for node in cycleNodeSet:
        for edge in dfa.out_edges(node):
            transitionSet.add(edge) 

    for accept_state in data["final_states"]:
        #check to see if there is a final state is reachable
        sources = data['states'][0:len(data['states'])]
        for source in sources:
            if nx.has_path(dfa,source,accept_state):
                #if cycle exists along path, then DFA is infinite
                for path in nx.all_simple_edge_paths(dfa,source,accept_state):
                    for edge in path:
                        if edge in transitionSet:
                            print("DFA is infinite.")
                            exit(0)

    #if conditions don't meet, DFA is not infinite  
    print("No. DFA is not infinite")

if __name__ == '__main__':
    #test('sampleDFA.json')
    test('test1.json')