package ds;

/**
 * In Operation: CipherSift, you need to remember which 4-character prefixes (quads)
 * you've seen to speed up pattern detection. Implement a simple Bag using a
 * singly linked list to support add and contains operations.
 *
 *
 * NOTE: This is intentionally lightweight. add(...) is O(1) (insert at head)
 * and contains(...) is O(n). Since we call contains for every element in the
 * optimized search, the overall worst-case is still O(n^2).
 */
public class MyBag {
    private Node head;

    /**
     * Adds a new data element to the bag by inserting at the head of the list.
     */
    public void add(String data) {
        // TODO: Create a new Node and push it to the front of the list
    	Node newNode = new Node(data);
    	newNode.next = head;
    	head = newNode;
    }

    /**
     * Checks whether the provided data already exists in the bag.
     * Return true on the first match; otherwise false after traversal.
     */
    public boolean contains(String data) {
        // TODO: Traverse from head and compare values (handle null safely)
    	Node currentNode = head;
    	while (currentNode != null) {
    		if (currentNode.data.equals(data))
    			return true;
    		currentNode = currentNode.next;
    	}
        return false;
    }
}

