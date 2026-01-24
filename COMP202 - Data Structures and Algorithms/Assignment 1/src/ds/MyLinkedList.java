package ds;

public class MyLinkedList {
    /**
     * Simplified linked list for the cryptanalysis storyline. 
     * Implement basic operations: add, get, size, and optimized duplicate detection.
     */
    private Node head;
    private int size = 0;

    public MyLinkedList() {
        this.head = null;
    }

    /** Adds a new node with the specified data at the end of the list. */
    public void add(String data) {
        // TODO: Append new node to the tail of the list and increment size
    	if (head == null) {
    		head = new Node(data);
    	} else {
    		Node currentNode = head;
    		while (currentNode.next != null) {
    			currentNode = currentNode.next;
    		} currentNode.next = new Node(data);
    	}
    	size++;
    }

    /** Returns the data of the node at the specified index. */
    public String get(int index) {
        // TODO: Validate index, traverse and return data at index
    	if (index < size) {
    		Node currentNode = head;
    		for (int i = 0; i < index; i++) {
    			currentNode = currentNode.next;
    		}
    		return currentNode.data;
    	}
        return null;
    }

    /** Returns the number of elements in the list. */
    public int size() {
        // TODO: return size
        return size;
    }

    /*
     * Brute-force quad duplicate detection.
     * - Iterate i from 0..size-1, j from i+1..size-1
     * - Extract first 4 chars of data (quad) and compare
     * - Return formatted success string when found; otherwise not found
     */
    public String findDuplicateQuadsBruteForce() {
        // TODO: Implement nested loops to search for duplicate quads
    	Node currentNode = head;
    	while (currentNode != null) {
    		String quad1 = currentNode.data.substring(0, 4);
    		Node nestedCurrentNode = currentNode;
    		while (nestedCurrentNode.next != null) {
    			nestedCurrentNode = nestedCurrentNode.next;
    			String quad2 = nestedCurrentNode.data.substring(0, 4);
    			if (quad1.equals(quad2))
    				return String.format("Duplicate found: %s%n", quad1);
    		}
    		currentNode = currentNode.next;
    	}
        return "No duplicates found.";
    }

    /*
     * Optimized duplicate quad detection using MyBag.
     * - Create MyBag and scan once
     * - On each element, compute quad and check bag.contains(quad)
     * - If seen, return success; else add to bag
     *
     * Reminder: MyBag is just another singly linked list. contains(...) will be
     * a linear scan, so both duplicate-detection methods have an O(n^2) worst case 
     * for the updated version; the improvement is in practical early exits.
     * No hashing or additional libraries are expected for this homework.
     */
    public String findDuplicateQuadsOptimized() {
        // TODO: Use MyBag to track seen quads; return as soon as duplicate found
    	MyBag bag = new MyBag();
    	Node currentNode = head;
    	while (currentNode != null) {
    		String quad = currentNode.data.substring(0, 4);
    		if (bag.contains(quad))
    			return String.format("Duplicate found: %s%n", quad);
    		else
    			bag.add(quad);
    		currentNode = currentNode.next;
    	}
        return "No duplicates found.";
    }

    /*
     * COMPLEXITY ANALYSIS SECTION
     * 
     * After implementing both methods, run the benchmarks and fill in your analysis:
     * 
     * findDuplicateQuadsBruteForce Complexity: O(n^2)
     * findDuplicateQuadsOptimized Complexity: O(n^2)
     * 
     * Explanation: Both methods have O(n^2) time complexity. However, optimized one avoid unnecessary iterations with using MyBag.
     * Although this causes more memory usage, it works faster. 
     * 
     * Report your timing results from the benchmarks here:
   	 * N=32: brute(earlyDup)=0.012 ms, brute(noDup)=0.133 ms, opt(earlyDup)=0.017 ms, opt(noDup)=0.023 ms
	 * N=1024: brute(earlyDup)=0.019 ms, brute(noDup)=12.84 ms, opt(earlyDup)=0.031 ms, opt(noDup)=2.88 ms
	 * N=4096: brute(earlyDup)=0.037 ms, brute(noDup)=192 ms, opt(earlyDup)=0.033 ms, opt(noDup)=18.41 ms
	 * N=16384: brute(earlyDup)=0.048 ms, brute(noDup)=3072 ms, opt(earlyDup)=0.056 ms, opt(noDup)=271.05 ms
     * (If any single run would exceed 5 minutes, stop it and record "5 minutes (capped)" 
     * there will be no point deduction in such a case if you have the implementation.)
     * 
     */
}
