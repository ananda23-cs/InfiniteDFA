# InfiniteDFA

By Aashish Anand and William Lau

This project tests whether the input DFA (using formal definition in JSON format) accepts an infinite language. 
If so, then it outputs a message saying that it is. If not, then the output message will say that it accepts a finite language.
The algorithm we are using involves heavily on graph theory, i.e., looking for cycles on the path from the start state to the accept states.
