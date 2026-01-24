package ds;

/**
 * Disjoint-set (Union-Find) data structure.
 */
public class UnionFind {

    private int[] parent;

    public UnionFind(int n) {
        parent = new int[n];
        // TODO: Creates a singleton cluster containing new element x.
        
        for (int i = 0; i<n; i++) {
            parent[i] = i;
        }

        ///////////////////////////////////////////
    }

    public int find(int x) {
        // TODO: Finds the cluster parent containing the element x.
    	if (parent[x] != x) {
        	parent[x] = find(parent[x]);
        }
        ///////////////////////////////////////////
        return parent[x];
    }

    public void union(int a, int b) {
        // TODO: merge cluster (a) and cluster (b) into one cluster
    	int A = find(a);
        int B = find(b);

        parent[A] = B;
        ///////////////////////////////////////
    }
}
