package ds;

/*
 * A stack that supports getMax() in O(1) time.
 * Approach: Keep an auxiliary stack of current maxima.
 * Space: O(N) in worst case (strictly more nodes to track plateaus of maxima).
 *
 * NOTE: The shared Node class only stores String data for the linked-list based
 * structures. To avoid any type-mismatch headaches, we provide a tiny private
 * node for integer stacks below. You do not need any additional classes.
 */
public class MySpecialStack {
    /* Simple node that stores an int value for the stack implementations. 
     * Please use this one for stack ops.
     */
    private static class IntNode {
        int value;
        IntNode next;

        IntNode(int value, IntNode next) {
            this.value = value;
            this.next = next;
        }
    }

    private IntNode dataTop; // top of the main stack
    private IntNode maxTop;  // top of the auxiliary stack tracking current maxima

    // TODO: track the stack size if you need it (not required for grading but handy for debugging)

    // TODO: Implement push/pop/getMax with O(1) getMax using the auxiliary stack described in the handout.
    // You may add private helper methods if they make your code cleaner.
    public void push(int data) {
        // TODO
    	IntNode newNode = new IntNode(data, null);
    	if(dataTop==null && maxTop==null) {
    		dataTop = newNode;
    		maxTop = newNode;
    	}
    	else {
    		IntNode current = new IntNode(dataTop.value, dataTop.next);
    		newNode.next = current;
    		dataTop = newNode;
    		if (data >= maxTop.value) {
    			IntNode currentMax = new IntNode(maxTop.value, maxTop.next);
        		IntNode newMax = new IntNode(data, currentMax);
        		maxTop = newMax;
        	} else {
        		IntNode currentMax = new IntNode(maxTop.value, maxTop);
        		maxTop = currentMax;
        	}
    	}
    }

    public int pop() {
        // TODO
    	if (dataTop == null)
    		return 0;
    	int value = dataTop.value;
    	dataTop = dataTop.next;
    	maxTop = maxTop.next;
        return value;
    }

    public int getMax() {
        // TODO
        return maxTop.value;
    }

    // Note: No size() method needed for simplified version
}
