package ds;

/**
 * Directed weighted graph for Dijkstra's algorithm.
 * Vertices are numbered (0..n-1). 
 * Edges are stored in an adjacency list.
 */
public class Graph {

    private Node[] adj;   // each Node stores an Edge and a next pointer
    private int n_vertices; 


    /** A directed graph with n vertices (0..n-1) */
    public Graph(int n) {
        n_vertices = n;
        adj = new Node[n];
    }

    /** Returns number of vertices. */
    public int size() { 
        return n_vertices; 
    }

    /** Singly linked list node for edges */
    public static class Node {
        public Edge edge;
        public Node next;
        public Node(Edge edge, Node next) {
            this.edge = edge;
            this.next = next;
        }
    }
    
    /**
     * Edge object storing destination and weight.
     */
    public static class Edge {
        public int from;
        public int to;
        public int weight;

        public Edge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }
    }

    /** Converts char vertex ('A','B',...) to numbers */
    public int indexOf(char ch) {           
        return ch - 'A';
    }
    /** Converts numbers to char vertex */
    public char labelOf(int i) {            
        return (char)('A' + i);
    }

    /** Adds edge u -> v with weight w (char version) */
    public void addEdge_dijkstra(char u, char v, int w, boolean directed) {
        // TODO: Add a directed edge u -> v
		addEdge(indexOf(u),indexOf(v),w);
    	if (!directed)
    		addEdge(indexOf(v),indexOf(u),w);

        /////////////////////////////////////////////////
    }

    /** Adds edge u -- v with weight w (char version) */
    public void addEdge_kruskal(char u, char v, int w) {
        // TODO: convert vertices from characters to indices, then add their edge.
    	addEdge(indexOf(u),indexOf(v),w);
        //////////////////////////////////////
    }
    
    /** Adds an edge with weight w */
    public void addEdge(int u, int v, int w) {
        // TODO: Create a new edge from u to v with weight w.
        // TODO: Insert it at the front of adj[u]
    	Edge e = new Edge(u, v, w);
    	Node n = new Node(e, adj[u]);
        adj[u] = n;
        /////////////////////////////////////////
    }

    /** Returns outgoing edges from vertex u. */
    public Node getAdj(int u) { 
        // TODO:  Return outgoing edges from vertex u.
    	return adj[u];

        /////////////////////////////////////////////
    }

    /** Return all edges */
    public Edge[] edges() {
        // TODO: Return all edges in the graph
    	Edge[] edges = new Edge[n_vertices*(n_vertices-1)];
    	int e = 0;
    	for (int i = 0; i<n_vertices; i++) {
    		Node temp = adj[i];
    		while (temp!=null) {
    			edges[e] = temp.edge;
    			e++;
    			temp = temp.next;
    		}
    	}
        //////////////////////////////////////
        return edges;
    }
    
}
