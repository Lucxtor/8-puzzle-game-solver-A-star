from states import State

states = [State(['1', '2', '3', '4', '5', '6', '7', '0', '8'], 1, 'primeiro', 1), State(['1', '2', '3', '4', '5', '6', '0', '7', '8'], 2, 'segundo', 2)]

state = State(['1', '2', '3', '4', '5', '6', '0', '7', '8'], 3, 'terceiro', 3)

for i in states:
    print(i)
print(state)
print(state in states)
index = states.index(state)
print(state.pathLen)
print(states[index].pathLen)
print(state.pathLen > states[index].pathLen)
if state.pathLen > states[index].pathLen:
    states[index] = state
for i in states:
    print(i)
print(state)