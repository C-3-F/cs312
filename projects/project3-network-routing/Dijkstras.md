### Dijkstra's Algorithm

# Given:
```
    G: graph
    l: function that gets the length of edge (we have this already)
    s: source
    𝑢 ∈ 𝑉: for all verticies of the graph

```

# Pseudocode:
```
 1  function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
```



# Book
```
Dijkstra(𝐺,𝑙,𝑠) 
        𝐟𝐨𝐫 all 𝑢∈𝑉 𝐝𝐨
                𝑑𝑖𝑠𝑡(𝑢)←∞
                𝑝𝑟𝑒𝑣(𝑢)←NULL
        𝑑𝑖𝑠𝑡(𝑠)←0
        𝐻.𝑚𝑎𝑘𝑒𝑞𝑢𝑒𝑢𝑒(𝑉, 𝑑𝑖𝑠𝑡)
        𝐰𝐡𝐢𝐥𝐞 𝐻 is not empty 𝐝𝐨
                𝑢←𝐻.𝑑𝑒𝑙𝑒𝑡𝑒𝑚𝑖𝑛()
                𝐟𝐨𝐫 all edges (𝑢,𝑣)∈𝐸 𝐝𝐨
                        𝐢𝐟 𝑑𝑖𝑠𝑡(𝑣)>𝑑𝑖𝑠𝑡(𝑢)+𝑙(𝑢,𝑣)  𝐭𝐡𝐞𝐧
                                𝑑𝑖𝑠𝑡(𝑣)←𝑑𝑖𝑠𝑡(𝑢)+𝑙(𝑢,𝑣)
                                𝑝𝑟𝑒𝑣(𝑣)←𝑢
                                𝐻.𝑑𝑒𝑐𝑟𝑒𝑎𝑠𝑒𝑘𝑒𝑦(𝑣)
        𝐫𝐞𝐭𝐮𝐫𝐧 𝑑𝑖𝑠𝑡,𝑝𝑟𝑒𝑣
```