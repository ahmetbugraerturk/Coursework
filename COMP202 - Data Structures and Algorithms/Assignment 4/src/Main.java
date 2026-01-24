import ds.*;

public class Main {
    public static void main(String[] args) {

        Graph g = new Graph(5);  // A,B,C,D,E

        g.addEdge_dijkstra('A', 'B', 10, true);
        g.addEdge_dijkstra('A', 'C', 3, true);
        g.addEdge_dijkstra('C', 'B', 4, true);
        g.addEdge_dijkstra('B', 'D', 1, true);
        g.addEdge_dijkstra('C', 'D', 1, false);
        g.addEdge_dijkstra('C', 'E', 2, true);
        g.addEdge_dijkstra('B', 'D', 2, true);
        g.addEdge_dijkstra('D', 'E', 7, true);
        g.addEdge_dijkstra('E', 'D', 9, true);

        Dijkstra d = new Dijkstra();
        char[] S = new char[g.size()];
        int[] dist = d.shortestPath(g, 0, S);


        // System.out.println();
        System.out.print("S: { ");
        for (int i = 0; i < S.length; i++)
            System.out.print(S[i] + " ");
        System.out.println("}");

        System.out.println("Distances from A:");
        for (int i = 0; i < dist.length; i++) {
            System.out.println(g.labelOf(i) + " : " + dist[i]);
        }

        /**
         * Expected output for the above test case:
            S: { A C D E B }
            Distances from A:
            A : 0
            B : 7
            C : 3
            D : 4
            E : 5
         */

        Graph gk = new Graph(8);

        gk.addEdge_kruskal('A','B',1);
        gk.addEdge_kruskal('C','A',7);
        gk.addEdge_kruskal('C','B',5);
        gk.addEdge_kruskal('C','D',11);
        gk.addEdge_kruskal('C','E',9);
        gk.addEdge_kruskal('A','D',10);
        gk.addEdge_kruskal('B','E',8);
        gk.addEdge_kruskal('E','D',3);

        gk.addEdge_kruskal('G','F',4);
        gk.addEdge_kruskal('G','H',6);
        gk.addEdge_kruskal('H','F',2);

        Kruskal k = new Kruskal();
        k.computeMST(gk);

        /**
         * Expected output
            Minimum Spanning Tree:
            A - B (1)
            H - F (2)
            E - D (3)
            G - F (4)
            C - B (5)
            B - E (8)
         */
    }
}
