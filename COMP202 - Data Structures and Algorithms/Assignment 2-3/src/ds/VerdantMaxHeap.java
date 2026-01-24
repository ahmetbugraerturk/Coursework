package ds;

/**
 * COMP202 – Assignment 2: Operation Verdant Archives
 * Part 2 – Toxicity Prediction Module (Max-Heap)
 *
 * Students: ONLY modify code inside the // TODO blocks.
 * Do NOT change the package name, class name, or method signatures.
 */
public class VerdantMaxHeap {

    /** Internal array storage for heap elements. */
    private int[] heap;
    /** Number of elements currently stored. */
    private int size;

    /** Default initial capacity (you may change this constant if desired). */
    private static final int DEFAULT_CAPACITY = 16;

    public VerdantMaxHeap() {
        this.heap = new int[DEFAULT_CAPACITY];
        this.size = 0;
    }

    // ----------------------------------------------------------------------
    // Public API
    // ----------------------------------------------------------------------

    /**
     * Inserts a new hazard score into the max-heap.
     */
    public void insert(int value) {
        // TODO: Insert value at the end of the array, resize if needed,
    	ensureCapacity();
    	heap[size] = value;
    	heapifyUp((++size)-1);
        // then call heapifyUp to restore the max-heap property.
    }

    /**
     * @return the maximum hazard score without removing it.
     * Precondition: heap is not empty.
     */
    public int peekMax() {
        // TODO: Return the root element of the heap (maximum value).
        return heap[0]; // placeholder so starter code compiles
    }

    /**
     * Removes and returns the maximum hazard score.
     * Precondition: heap is not empty.
     */
    public int extractMax() {
        // TODO: Remove and return the maximum element.
        int max = heap[0];
    	if (size>0) {
	    	swap(0,size-1);
	    	heap[size-1] = 0;
	    	heapifyDown(0);
	    	size--;
    	}
        // 1. Save heap[0].
        // 2. Move last element to index 0 and decrease size.
        // 3. Call heapifyDown(0) to restore heap property.
        return max;
    }

    /**
     * @return true if heap is empty, false otherwise.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * @return current number of elements in the heap.
     */
    public int size() {
        return size;
    }

    // ----------------------------------------------------------------------
    // Private helpers (students will need to implement these).
    // ----------------------------------------------------------------------

    /** Restores heap property going upwards from index i. */
    private void heapifyUp(int i) {
        // TODO: Restore the max-heap property by swapping the element at index i
    	int parentIdx = (i-1)/2;
    	while (heap[parentIdx]<heap[i]) {
    		swap(i, parentIdx);
    		i = parentIdx;
    		parentIdx = (i-1)/2;
    	}
        // with its parent while it is greater than the parent. Parent index is (i - 1) / 2.
    }

    /** Restores heap property going downwards from index i. */
    private void heapifyDown(int i) {
        // TODO: Restore the max-heap property by comparing the element at index i
    	int highest = i;
    	int l = 2*i+1;
    	int r = 2*i+2;
    	if (l<size && heap[l]>heap[highest]) highest = l;
    	if (r<size && heap[r]>heap[highest]) highest = r;
    	
    	while (highest != i) {
            swap(i,highest);
            i = highest;
            highest = i;
        	l = 2*i+1;
        	r = 2*i+2;
        	if (l<size && heap[l]>heap[highest]) highest = l;
        	if (r<size && heap[r]>heap[highest]) highest = r;
        }
        // with its children and swapping with the larger child until the property holds.
    }

    /** Doubles internal array capacity when full. */
    private void ensureCapacity() {
        // TODO: When the internal array is full, create a new array with double capacity,
    	if (heap.length==size) {
	    	int[] newHeap = new int[2*size];
	    	for (int i=0 ; i<size; i++) {
	    		newHeap[i]=heap[i];
	    	}
	    	heap = newHeap;
    	}
        // copy existing elements, and update the heap reference.
    }

    /** Swaps two entries in the heap array. */
    private void swap(int i, int j) {
        // TODO: Swap heap[i] and heap[j].
    	int temp = heap[i];
    	heap[i] = heap[j];
    	heap[j] = temp;
    }
}

