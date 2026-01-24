package ds;

import ds.Graph.Node;

/**
 * Dijkstra's shortest path algorithm.
 */
public class Dijkstra {

    /**
     * Runs Dijkstra from source s.
     * Returns array dist[] such that dist[v] = shortest distance s -> v.
     */
    public int[] shortestPath(Graph g, int s, char[] output) {

        int n = g.size();
        int[] dist = new int[n];
        boolean[] visited = new boolean[n];

        int x = 0; // output index
        char[] S = output;

        // TODO: Apply the dijkstra algorithm 
        for (int i = 0; i<n; i++) {
        	if (i==s) {
                dist[s]=0;
        	} else {
        		dist[i] = Integer.MAX_VALUE;
        	}
        }
        Heap heap = new Heap();
        heap.insert(0, s);
        while (!heap.isEmpty()) {
        	int v = (int) heap.remove().value;
        	if (visited[v]) continue;
	        visited[v]=true;
	        S[x]= (char)(v+'A');
	        x++;
	        Node temp = g.getAdj(v);
	        while (temp!=null) {
	        	int distance = dist[v] + temp.edge.weight;
	        	if (!visited[temp.edge.to] && (dist[temp.edge.to] > distance)) {
	        		dist[temp.edge.to] = distance;
	        		heap.insert(distance, temp.edge.to);
	        	}
	        	temp = temp.next;
	        }
        }
        //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        return dist;
    }
}
