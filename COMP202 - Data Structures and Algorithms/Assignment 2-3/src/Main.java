import ds.SentinelBST;
import ds.VerdantMaxHeap;
import ds.SpeciesTrie;

/**
 * Simple, optional testing harness for Assignment 2.
 * The real grading will be done with a hidden autograder.
 *
 * Students may modify this file freely for local testing.
 * It will NOT be submitted or graded unless specified.
 */
public class Main {

    public static void main(String[] args) {
        testBST();
        testHeap();
        testTrie();
    }

    private static void testBST() {
        System.out.println("=== SentinelBST comprehensive test ===");
        SentinelBST bst = new SentinelBST();
        int[] values = { 50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 90, 5, 15, 85, 95 };

        System.out.println("Inserting: 50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65, 90, 5, 15, 85, 95");
        for (int v : values) {
            bst.insert(v);
        }

        System.out.println("\nTraversals:");
        System.out.println("Inorder   : " + bst.getInorder());
        System.out.println("Preorder  : " + bst.getPreorder());
        System.out.println("Postorder : " + bst.getPostorder());
        System.out.println("LevelOrder: " + bst.getLevelOrder());
        
        System.out.println("\nTree Properties:");
        System.out.println("Size: " + bst.size());
        System.out.println("Height: " + bst.height());
        System.out.println("Min / Max: " + bst.min() + " / " + bst.max());
        
        System.out.println("\nSearch Tests:");
        System.out.println("Contains 35? " + bst.contains(35));
        System.out.println("Contains 65? " + bst.contains(65));
        System.out.println("Contains 100? " + bst.contains(100));
        System.out.println("Contains 1? " + bst.contains(1));
        
        System.out.println("\nDeletion Tests:");
        System.out.println("Deleting leaf node (5)...");
        bst.delete(5);
        System.out.println("Inorder after delete: " + bst.getInorder());
        
        System.out.println("\nDeleting node with one child (90)...");
        bst.delete(90);
        System.out.println("Inorder after delete: " + bst.getInorder());
        
        System.out.println("\nDeleting node with two children (30)...");
        bst.delete(30);
        System.out.println("Inorder after delete: " + bst.getInorder());
        System.out.println("Size after deletions: " + bst.size());
        
        System.out.println("\n--- Complexity Analysis ---");
        System.out.println("Insert worst case: " + bst.insertWorstCase());
        System.out.println("Insert average case: " + bst.insertAverageCase());
        System.out.println("Contains worst case: " + bst.containsWorstCase());
        System.out.println("Contains average case: " + bst.containsAverageCase());
        System.out.println("Delete worst case: " + bst.deleteWorstCase());
        System.out.println("Traversal complexity: " + bst.traversalComplexity());
        System.out.println("Worst case cause: " + bst.worstCaseCause());
        System.out.println("Empty tree height: " + bst.emptyTreeHeight());
        System.out.println("Heap search complexity: " + bst.heapSearchComplexity());
        System.out.println("Trie operation complexity: " + bst.trieOperationComplexity());
    }

    private static void testHeap() {
        System.out.println("\n=== VerdantMaxHeap comprehensive test ===");
        VerdantMaxHeap heap = new VerdantMaxHeap();
        int[] scores = { 45, 23, 67, 12, 89, 34, 56, 78, 90, 21, 43, 65, 87, 9, 32, 54, 76, 98 };

        System.out.println("Inserting 18 hazard scores...");
        for (int s : scores) {
            heap.insert(s);
        }
        
        System.out.println("Heap size: " + heap.size());
        System.out.println("Max element (peek): " + heap.peekMax());
        
        System.out.println("\nExtracting all elements in descending order:");
        while (!heap.isEmpty()) {
            System.out.print(heap.extractMax() + " ");
        }
        System.out.println();
        System.out.println("Heap empty? " + heap.isEmpty());
    }

    private static void testTrie() {
        System.out.println("\n=== SpeciesTrie comprehensive test ===");
        SpeciesTrie trie = new SpeciesTrie();
        String[] species = { 
            "rosa", "rosemary", "rosewood", "rose", "rosetree",
            "rootleaf", "root", "rooted", "rootstock",
            "abutilon", "abelia", "abies", "acacia", "acer",
            "bamboo", "bambusa", "baobab",
            "cactus", "camellia", "cannabis"
        };

        System.out.println("Inserting 20 species names...");
        for (String s : species) {
            trie.insert(s);
        }

        System.out.println("\nExact Match Tests:");
        System.out.println("Contains 'rosa'? " + trie.contains("rosa"));
        System.out.println("Contains 'rose'? " + trie.contains("rose"));
        System.out.println("Contains 'roses'? " + trie.contains("roses"));
        System.out.println("Contains 'bamboo'? " + trie.contains("bamboo"));
        
        System.out.println("\nPrefix Tests:");
        System.out.println("StartsWith 'ro'? " + trie.startsWith("ro"));
        System.out.println("StartsWith 'ros'? " + trie.startsWith("ros"));
        System.out.println("StartsWith 'xyz'? " + trie.startsWith("xyz"));
        
        System.out.println("\nPrefix Counting:");
        System.out.println("CountPrefix 'ro': " + trie.countPrefix("ro"));
        System.out.println("CountPrefix 'ros': " + trie.countPrefix("ros"));
        System.out.println("CountPrefix 'root': " + trie.countPrefix("root"));
        System.out.println("CountPrefix 'a': " + trie.countPrefix("a"));
        System.out.println("CountPrefix 'b': " + trie.countPrefix("b"));
        System.out.println("CountPrefix 'c': " + trie.countPrefix("c"));
        
        System.out.println("\nPrefix Listing (lexicographic order):");
        System.out.println("ListPrefix 'ros':");
        System.out.print(trie.listPrefix("ros"));
        System.out.println("\nListPrefix 'ab':");
        System.out.print(trie.listPrefix("ab"));
        System.out.println("\nListPrefix 'bam':");
        System.out.print(trie.listPrefix("bam"));
    }
}
