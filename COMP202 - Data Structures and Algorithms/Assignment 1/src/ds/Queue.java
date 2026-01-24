package ds;

/**
 * Complete Queue implementation - DO NOT MODIFY THIS FILE.
 * This is a working queue implementation provided for the assignment.
 * 
 * DO NOT MODIFY THIS FILE.
 * 
 */
public class Queue {
    private Node front;
    private Node rear;
    private int size = 0;

    public Queue() {
        this.front = null;
        this.rear = null;
    }

    /** Adds an element to the rear of the queue. */
    public void enqueue(String data) {
        Node newNode = new Node(data);
        if (rear == null) {
            front = rear = newNode;
        } else {
            rear.setNext(newNode);
            rear = newNode;
        }
        size++;
    }

    /** Removes and returns the element from the front of the queue. */
    public String dequeue() {
        if (front == null) {
            throw new RuntimeException("Queue is empty");
        }
        String data = front.getData();
        front = front.getNext();
        if (front == null) {
            rear = null;
        }
        size--;
        return data;
    }

    /** Returns true if the queue is empty. */
    public boolean isEmpty() {
        return front == null;
    }

    /** Returns the number of elements in the queue. */
    public int size() {
        return size;
    }

    /** Returns the front element without removing it. */
    public String peek() {
        if (front == null) {
            throw new RuntimeException("Queue is empty");
        }
        return front.getData();
    }
}
