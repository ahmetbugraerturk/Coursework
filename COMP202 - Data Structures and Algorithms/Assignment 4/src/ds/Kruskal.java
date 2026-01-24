package ds;

import ds.Graph.Edge;

/**
 * Kruskal’s Minimum Spanning Tree Algorithm
 * Computes a minimum spanning tree of graphg using Kruskal's algorithm.
 */
public class Kruskal {

    public void computeMST(Graph g) {

        // TODO: Initialize the data structures required by Kruskal’s algorithm
    	UnionFind ds = new UnionFind(g.size()); 
    	Edge[] edges = g.edges();
    	
    	Heap sortedEdges = new Heap();
    	for (Edge e: edges) {
    		if (e==null) break;
    		sortedEdges.insert(e.weight, e);
    	}

        // TODO: Implement Kruskal's algorithm
    	System.out.println("Minimum Spanning Tree:");
    	while (!sortedEdges.isEmpty()) {
    		Edge e = (Edge)sortedEdges.remove().value;
    		
    		if (ds.find(e.from) != ds.find(e.to)) {
                ds.union(e.from, e.to);
                System.out.printf("%c - %c (%d)%n", e.from+'A', e.to+'A', e.weight);
            }
    	}
        
        // TODO: Print the MST
        
    }
}
