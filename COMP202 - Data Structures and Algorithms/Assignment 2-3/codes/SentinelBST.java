package ds;

/**
 * COMP202 – Assignment 2: Operation Verdant Archives
 * Part 1 – Genome Index Module (Binary Search Tree)
 *
 * Students: ONLY modify code inside the // TODO blocks.
 * Do NOT change the package name, class names, or method signatures.
 */
public class SentinelBST {

    /** Node type for the BST. */
    private static class Node {
        int key;
        Node left;
        Node right;

        Node(int key) {
            this.key = key;
        }
    }

    /** Root of the BST (may be null if tree is empty). */
    private Node root;

    /** Creates an empty BST. */
    public SentinelBST() {
        root = null;
    }

    // ----------------------------------------------------------------------
    // Public API – you must implement these methods using recursion.
    // ----------------------------------------------------------------------

    /**
     * Inserts the given key into the BST.
     * Duplicate keys may either be ignored or consistently placed,
     * but your behavior must be documented in the analysis section.
     */
    public void insert(int key) {
        root = insertRec(root, key);
    }

    /**
     * Returns true if key exists in the BST, false otherwise.
     */
    public boolean contains(int key) {
        return containsRec(root, key);
    }

    /**
     * Deletes the given key from the BST, if it exists.
     * Must correctly handle leaf, one-child, and two-child cases.
     */
    public void delete(int key) {
        root = deleteRec(root, key);
    }

    /**
     * @return number of nodes in the BST.
     */
    public int size() {
        return sizeRec(root);
    }

    /**
     * @return height of the BST.
     * Height of an empty tree can be defined as -1 or 0,
     * but you must be consistent and state your choice.
     */
    public int height() {
        return heightRec(root);
    }

    /**
     * @return minimum key in the BST.
     * Precondition: tree is not empty.
     */
    public int min() {
        Node minNode = findMin(root);
        return minNode.key;
    }

    /**
     * @return maximum key in the BST.
     * Precondition: tree is not empty.
     */
    public int max() {
        Node current = root;
        while (current.right != null) {
            current = current.right;
        }
        return current.key;
    }

    /**
     * @return inorder traversal as a single string,
     * e.g., "1 3 7 10".
     */
    public String getInorder() {
        StringBuilder sb = new StringBuilder();
        inorderRec(root, sb);
        return sb.toString().trim();
    }

    /**
     * @return preorder traversal as a single string.
     */
    public String getPreorder() {
        StringBuilder sb = new StringBuilder();
        preorderRec(root, sb);
        return sb.toString().trim();
    }

    /**
     * @return postorder traversal as a single string.
     */
    public String getPostorder() {
        StringBuilder sb = new StringBuilder();
        postorderRec(root, sb);
        return sb.toString().trim();
    }

    /**
     * @return level-order traversal as a single string.
     * You MUST use SimpleNodeQueue (or provided queue) for this.
     */
    public String getLevelOrder() {
        if (root == null) {
            return "";
        }
        
        StringBuilder sb = new StringBuilder();
        SimpleNodeQueue queue = new SimpleNodeQueue();
        queue.enqueue(root);
        
        while (!queue.isEmpty()) {
            Node current = queue.dequeue();
            sb.append(current.key).append(" ");
            
            if (current.left != null) {
                queue.enqueue(current.left);
            }
            if (current.right != null) {
                queue.enqueue(current.right);
            }
        }
        
        return sb.toString().trim();
    }

    // ----------------------------------------------------------------------
    // Private recursive helper methods
    // Students must implement these
    // ----------------------------------------------------------------------

    /**
     * Recursive helper for insert.
     * @param node current node in recursion
     * @param key key to insert
     * @return the node after insertion (may be newly created)
     */
    private Node insertRec(Node node, int key) {
        // TODO: Implement this method using recursion.
    	if (node==null) {
    		return new Node(key);
    	}
    	else {
    		if (key>node.key)
    			node.right = insertRec(node.right, key);
    		else if (key<node.key)
    			node.left = insertRec(node.left, key);
    	}
        // Base case - if node is null, create and return new Node(key)
        // Recursive case - compare key with node.key and recurse left or right
        // Duplicates should be ignored or handled consistently (document in analysis).
		return node; // placeholder so starter code compiles
    }

    /**
     * Recursive helper for contains.
     * @param node current node in recursion
     * @param key key to search for
     * @return true if key exists in subtree rooted at node
     */
    private boolean containsRec(Node node, int key) {
        // TODO: Implement this method using recursion.
    	if (node==null) {
    		return false;
    	}
    	else {
    		if (key>node.key)
    			return containsRec(node.right, key);
    		else if (key<node.key)
    			return containsRec(node.left, key);
    		else
    			return true;
    	}
        // Base case - if node is null, return false
        // If key matches, return true
        // Otherwise, recurse left or right based on comparison.
    }

    /**
     * Recursive helper for delete.
     * @param node current node in recursion
     * @param key key to delete
     * @return the node after deletion (may be null or different node)
     */
    private Node deleteRec(Node node, int key) {
        // TODO: Implement this method using recursion.
    	if (node==null) {
    		return null;
    	}
    	else {
    		if (key>node.key)
    			node.right = deleteRec(node.right, key);
    		else if (key<node.key)
    			node.left = deleteRec(node.left, key);
    		else {
    			if (node.left == null) 
    				return node.right;
                else if (node.right == null) 
                	return node.left;
    			if (node.right.left == null) {
    				node.key=node.right.key;
    				node.right = node.right.right;
    			} else {
	    			Node newNode = node.right;
	    			while (newNode.left.left != null)
	    				newNode = newNode.left;
	    			node.key = newNode.left.key;
	    			newNode.left = newNode.left.right;
    			}
    		}
    	}
        // 1. If node is null, return null.
        // 2. Recurse left or right based on comparison with node.key.
        // 3. When key == node.key, handle:
        //    - leaf node,
        //    - node with one child,
        //    - node with two children (use inorder successor).
        return node; // placeholder so starter code compiles
    }

    /**
     * Helper to find minimum node in a subtree.
     */
    private Node findMin(Node node) {
        // TODO: Implement this helper to return the minimum node in a subtree.
    	if (node.left==null)
    		return node;
    	else
    		return findMin(node.left);
    }

    /**
     * Recursive helper for size.
     * @param node current node in recursion
     * @return number of nodes in subtree rooted at node
     */
    private int sizeRec(Node node) {
        // TODO: Implement this method recursively.
    	if (node==null)
    		return 0;
    	else
    		return 1 + sizeRec(node.left) + sizeRec(node.right);
        // Base case - if node is null, return 0
        // Recursive case - return 1 + sizeRec(left) + sizeRec(right)
    }

    /**
     * Recursive helper for height.
     * @param node current node in recursion
     * @return height of subtree rooted at node
     */
    private int heightRec(Node node) {
        // TODO: Implement this method recursively.
    	if (node==null)
    		return -1;
    	int leftH = heightRec(node.left);
    	int rightH = heightRec(node.right);
    	return 1 + (rightH > leftH ? rightH : leftH);
        // Base case - if node is null, return height of empty tree (be consistent with emptyTreeHeight()).
        // Recursive case - return 1 + max(heightRec(left), heightRec(right)).
    }

    /**
     * Recursive helper for inorder traversal.
     * @param node current node in recursion
     * @param sb StringBuilder to accumulate result
     */
    private void inorderRec(Node node, StringBuilder sb) {
        // TODO: Implement inorder traversal recursively.
    	if (node==null)
    		return;
    	inorderRec(node.left, sb);
    	sb.append(node.key).append(" ");
    	inorderRec(node.right, sb);
        // Base case - if node is null, return.
        // Recurse left, append node.key + \" \", then recurse right.
    }

    /**
     * Recursive helper for preorder traversal.
     * @param node current node in recursion
     * @param sb StringBuilder to accumulate result
     */
    private void preorderRec(Node node, StringBuilder sb) {
        // TODO: Implement preorder traversal recursively.
    	if (node==null)
    		return;
    	sb.append(node.key).append(" ");
    	preorderRec(node.left, sb);
    	preorderRec(node.right, sb);
        // Base case - if node is null, return.
        // Append node.key + \" \", then recurse left and right.
    }

    /**
     * Recursive helper for postorder traversal.
     * @param node current node in recursion
     * @param sb StringBuilder to accumulate result
     */
    private void postorderRec(Node node, StringBuilder sb) {
        // TODO: Implement postorder traversal recursively.
    	if (node==null)
    		return;
    	postorderRec(node.left, sb);
    	postorderRec(node.right, sb);
    	sb.append(node.key).append(" ");
        // Base case - if node is null, return.
        // Recurse left, recurse right, then append node.key + \" \".
    }

    // ----------------------------------------------------------------------
    // Package-private helper queue for level-order traversal.
    // This is fully implemented and should NOT be modified by students.
    // ----------------------------------------------------------------------

    /** Simple linked-list queue specialized for BST Node. */
    static class SimpleNodeQueue {
        private static class QNode {
            Node value;
            QNode next;
            QNode(Node v) { value = v; }
        }

        private QNode head;
        private QNode tail;

        boolean isEmpty() {
            return head == null;
        }

        void enqueue(Node n) {
            if (n == null) return;
            QNode qn = new QNode(n);
            if (tail == null) {
                head = tail = qn;
            } else {
                tail.next = qn;
                tail = qn;
            }
        }

        Node dequeue() {
            if (head == null) return null;
            Node v = head.value;
            head = head.next;
            if (head == null) tail = null;
            return v;
        }
    }

    // ----------------------------------------------------------------------
    // COMPLEXITY ANALYSIS SECTION – Part 4 of the assignment
    // Students must fill this out carefully. Do NOT remove or modify method signatures.
    // Return simple complexity strings like "O(n)", "O(log n)", "O(1)", etc.
    // These will be autograded.
    // ----------------------------------------------------------------------

    /**
     * @return worst-case time complexity of insert
     * Example: "O(n)" or "O(log n)" or "O(1)"
     */
    public String insertWorstCase() {
        // TODO: Return the correct worst-case time complexity for BST insert.
        return "O(n)";
    }

    /**
     * @return average-case time complexity of insert
     */
    public String insertAverageCase() {
        // TODO: Return the correct average-case time complexity for BST insert.
        return "O(log n)";
    }

    /**
     * @return worst-case time complexity of contains (search)
     */
    public String containsWorstCase() {
        // TODO: Return the correct worst-case time complexity for BST search.
        return "O(n)";
    }

    /**
     * @return average-case time complexity of contains (search)
     */
    public String containsAverageCase() {
        // TODO: Return the correct average-case time complexity for BST search.
        return "O(log n)";
    }

    /**
     * @return worst-case time complexity of delete
     */
    public String deleteWorstCase() {
        // TODO: Return the correct worst-case time complexity for BST delete.
        return "O(n)";
    }

    /**
     * @return average-case time complexity of delete
     */
    public String deleteAverageCase() {
        // TODO: Optionally document the average-case time complexity of BST delete.
        return "O(log n)";
    }

    /**
     * @return time complexity of traversals (inorder, preorder, postorder, level-order)
     */
    public String traversalComplexity() {
        // TODO: Return the overall time complexity of each full tree traversal.
        return "O(n)";
    }

    /**
     * @return what causes worst-case behavior in BST
     * Example: "sorted input" or "random input" or "balanced input"
     */
    public String worstCaseCause() {
        // TODO: Briefly describe what kind of input causes worst-case behavior in a plain BST.
        return "sorted input";
    }

    /**
     * @return height of empty tree in your implementation ("-1" or "0")
     */
    public String emptyTreeHeight() {
        // TODO: Return the height you use for an empty tree (must match heightRec()).
        return "-1";
    }

    /**
     * @return worst-case time complexity for search in a max-heap
     */
    public String heapSearchComplexity() {
        // TODO: Return the worst-case time complexity when searching for an arbitrary key in a max-heap.
        return "O(n)";
    }

    /**
     * @return time complexity of trie operations where m is the length of the string
     * Example: "O(m)" or "O(n)" or "O(log n)"
     */
    public String trieOperationComplexity() {
        // TODO: Return the time complexity of typical trie operations in terms of m (string length).
        return "O(m)";
    }
}
