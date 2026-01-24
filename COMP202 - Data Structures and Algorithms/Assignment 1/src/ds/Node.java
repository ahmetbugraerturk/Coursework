package ds;

/**
 * Node class for the string-based structures (linked list, bag, queue).
 * MySpecialStack defines its own private node type for integers.
 */

class Node {
    
    String data;
    Node next;

    public Node(String data) {
        this.data = data;
        this.next = null;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }
}

