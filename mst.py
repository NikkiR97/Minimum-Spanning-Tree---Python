import numpy as np
import array
import operator

V = 128

column_inc = 0
city_inc = -1
state_inc = -1

city_names = [""] * V
city_states = [""] * V
city_map = [[0 for x in range(V)] for y in range(V)]


# city_map[2][3] = 3
# for i in range(0,5):
#     print(city_map[i])

# for i in range (128):
#     print (city_names[i])

# class MST:
#     def __init__ (self):
#         print ("Program Begins")

def mirror_elements():
    global city_map
    for i in range(V):
        for j in range(V):
            city_map[i][j] = city_map[j][i]

def store(line):
    name = ""
    state = ""
    dist = ""

    global column_inc
    global city_inc
    global state_inc

    global city_names
    global city_states
    global city_map

    if (ord(line[0]) >= 65) and (ord(line[0]) <= 90): #if it's a letter
        #parse and input the cities and the states, ignore the coordinates and population i.e. [4660,12051]49826
        for i in range(len(line)):
            if line[i] == ",":
                break
            name += line[i]

        city_inc+=1
        city_names[city_inc] = name
        i+=2
        for j in range(i, len(line)):
            if line[j] == "[":
                break
            state += line[j]
        state_inc+=1
        city_states[state_inc] = state

        name = ""
        state = ""
        column_inc=0

    elif (ord(line[0]) >= 48) and (ord(line[0]) <= 57): #if it's a number
        #input all the distances from each city
        #column_inc = 0 #reset the column
        i=0
        while i != len(line):
            for j in range (i, len(line)):
                if line[j] == ' ' or line[j] == '\n':
                    j+=1
                    break
                dist += line[j]
            city_map[city_inc][column_inc] = int(dist)
            column_inc+=1
            dist = ""
            i=j


def min_key(visited, min_keys):
    min = 10000000000
    min_idx = 0;

    for m in range(V):
        if visited[m] == False and min_keys[m] < min: #if the vertex is not visited and the key is less than the most minimum number
            min = min_keys[m] #make that key the new minimum
            min_idx = m #change the index to have the index of the vertex with the new minimum weight

    return min_idx

def min_span_tree(map):
    #implementing prim's algorithm
    #global city_map

    mst = [0]*V #our minimum spanning tree, references the vertex that that the indexed location is connected to
    min_weight = [1000000000]*V #1D list to keep track of all the minimum weights as they are checked in the adj matrix - first initialize all as max weight
    added = [False]*V #boolean list to mark all the vistied cities
    u=0
    min = 10000000000
    min_idx = 1000000000

    mymin = 1000000000
    idx = 0

    ###find min for the first row: Youngstown, OH by itself first###
    for i in range (1,V):
        if map[0][i] < mymin:
            mymin = map[0][i]
            idx = i

    min_weight[0] = mymin #we did the above to make at least one element be smaller than the other elements in the min_weight list
    mst[0] = idx
    ######

    for i in range(V-1):
        u = min_key(added,min_weight) #in first iteration of the for loop Youngstown, OH would be recognized as the minimum key
        added[u] = True #mark as visited
        for k in range(V):
            if (added[k] == False) and (map[u][k] < min_weight[k]):#map[u][k]
                        min_weight[k] = map[u][k]
                        mst[k] = u

    val = 0
    print("                   Edge                                              Weight")
    for i in range(V):
        print('{:20}'.format(city_names[i]) + ", " + city_states[i] + "  -  " + '{:15}'.format(city_names[mst[i]]) + ", " + city_states[mst[i]] + "               " + '{:>10}'.format(str(map[i][mst[i]])) + "\n")
        val+=map[i][mst[i]]

    print ("Max Distance:" + str(val))

def print_city():
    global city_map
    for i in city_map:
        print(i)

def modify():
    global test_val
    test_val = 90

#code execution begins here
file = open("miles.txt", "r")
#cont = file.read()
#print(cont)
for line in file:
    #print(line)
    if line[0] == '*':
        print("comment line is skipped")
        #nothing gets inputted
    elif len(line) == 0:
        print("empty line is skipped")
        #nothing gets inputted
    else:
        store(line)

file.close()

mirror_elements()

print_city() #enable to print the entire adjacency matrix

print("\n")

min_span_tree(city_map)

# modify()
# print(test_val)
