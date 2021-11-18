import json
import networkx as nx

#parses json file
def test(filename):
    f = open(filename)
    data = json.load(f)

    #constructs DFA and performs edge cases for badly formatted DFA's
    if (data["start_state"] not in data["states"]):
        raise ValueError("Invalid DFA")

    for final in data["final_states"]:
        if final not in data["states"]:
            raise ValueError("Invalid DFA")

    dfa = nx.DiGraph()
    dfa.add_nodes_from(data["states"])

    #adds edges to directed graph
    for transition in data["trans_func"]:
        if transition[0] not in dfa.nodes or transition[2] not in dfa.nodes:
            raise ValueError("Invalid DFA")
        if transition[1] not in data["alphabet"]:
            raise ValueError("Invalid DFA")
        
        dfa.add_edge(transition[0], transition[2], weight=transition[1])

    for accept_state in data["final_states"]:
        #check to see if there is a final state is reachable
        sources = data['states'][0:len(data['states'])-1]
        for source in sources:
            if nx.has_path(dfa,source,accept_state):
                #if cycle exists along path, then DFA is infinite
                for c in list(nx.simple_cycles(dfa)):
                    if accept_state in c:
                        print("DFA is infinite.")
                        exit(0)

    #if conditions don't meet, DFA is not infinite  
    print("No. DFA is not infinite")

if __name__ == '__main__':
    test('sampleDFA.json')