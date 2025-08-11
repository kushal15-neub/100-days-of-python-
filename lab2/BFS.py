from collections import deque


adj = [[0] * 1000 for _ in range(1000)]

def bfs(no_vertices, root):
    visited = [0] * no_vertices
    q = deque()

    q.append(root)
    visited[root] = 1

    while q:
        s = q.popleft()
        print(s, end=" ")

        for i in range(no_vertices):
            if adj[s][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1

def main():
    V = int(input("Enter the number of Vertex's::"))
    E = int(input("Enter the number of Edges::"))


    for i in range(V):
        for j in range(V):
            adj[i][j] = 0

    print("Enter the Edge's::")
    for _ in range(E):
        node1, node2 = map(int, input().split())
        adj[node1][node2] = 1
        adj[node2][node1] = 1

    root = int(input("Enter the root node::"))
    bfs(V, root)

if __name__ == "__main__":
    main()
