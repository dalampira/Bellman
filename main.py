#Osia Dalampira-Kiprigli

#defining infinity and the destination point
inf = float('inf')
destination = "F"

#opening the file
with open('city1.txt') as fp:
    dataset = [line.split() for line in fp.readlines() if line]

#adding the vertices to a set
vertices = set()
for connection in dataset:
    vertices.add(connection[0])
    vertices.add(connection[1])

dataset2 = list()

for connection in dataset:
    dataset2.append([connection[1],connection[0], connection[2]])

dataset.extend(dataset2)


neighbours = {vertex: set() for vertex in vertices}
distances = {vertex: inf for vertex in vertices}
paths = {vertex: list() for vertex in vertices}
distances[destination] = 0

#creating an array to store the neighbours of each vertex
for current_vertex in vertices:
    for row in dataset:
        if row[0] == current_vertex:
            neighbours[current_vertex].add(row[1])

#we check the neighbour of every vertex to see its distance
#if the current distance is smaller, we update that
for i in range(1, len(vertices)):
    for current_vertex in vertices:
        for neighbour in neighbours[current_vertex]:
            if distances[current_vertex] == inf:
                break
            cost = 0
            for connection in dataset:
                if (connection[0]==current_vertex) & (connection[1]==neighbour):
                    cost = int(connection[2])
            other_route = distances[current_vertex] + cost
            if other_route < distances[neighbour]:
                distances[neighbour] = other_route
                #if there is a previous vertex for the path, remove that because we changed the route
                if len(paths[neighbour]) != 0 :
                    paths[neighbour].pop()
                paths[neighbour].append(current_vertex)

#insert the starting vertex in each path
for current_vertex in vertices:
    paths[current_vertex].insert(0,current_vertex)

#we append all the routes to the paths array
#we find the last vertex of the route and check whether that is the destination
#if not, we find the the path beginning from that last vertex and we append that
#path to the previous route. In the end we have an array with all the paths
for i in range(1,len(vertices)):
    for current_vertex in vertices:
        last = paths[current_vertex][-1]
        if last != destination:
            for j in range(1,len(paths[last])):
                 paths[current_vertex].append(paths[last][j])

#printing the distances and the paths of each vertex
for vertex in vertices:
    print("VALUE ( "+str(vertex)+" ): -" + str(distances[vertex]))
    print("PATH: " + str(paths[vertex]))
    print("---------------------------------------------------------")
