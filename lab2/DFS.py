maxi = 1000
adj = [[0] * maxi for _ in range(maxi)]
visited = [False] * maxi

def dfs(V, root):
    visited[root] = True
    print(root, end=" ")
    for i in range(V):
        if adj[root][i] == 1 and not visited[i]:
            dfs(V, i)

def main():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))

  
    for i in range(V):
        for j in range(V):
            adj[i][j] = 0


    print("Enter the edges (node1 node2):")
    for _ in range(E):
        node1, node2 = map(int, input().split())
        adj[node1][node2] = 1
        adj[node2][node1] = 1  

   
    for i in range(V):
        visited[i] = False

    
    root = int(input("Enter the root node: "))

 
    print(f"DFS traversal starting from node {root}: ", end="")
    dfs(V, root)
    print()

if __name__ == "__main__":
    main()
