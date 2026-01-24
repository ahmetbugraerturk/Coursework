package ds;

/**
 * priority queue using binary heap.
 * Stores entries of (key, value).
 */
public class Heap {

    public static class Entry {
        public int key;    // distance
        public Object value;  // store any object
        
        public Entry(int k, Object v) { 
            key = k; 
            value = v; 
        }
    }

    private Entry[] heap;
    private int size;

    public Heap() {
        heap = new Entry[100000]; // enough for project tests
        size = 0;
    }

    /** Insert a new entry with the given key and value */
    public void insert(int key, Object value) {
        heap[size] = new Entry(key, value);
        upheap(size);
        size++;
    }

    /** Removes and returns entry with smallest key */
    public Entry remove() {
        if (size == 0) return null;
        Entry min = heap[0];
        heap[0] = heap[size - 1];
        size--;
        if (size > 0) downheap(0);
        return min;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    /** Moves heap[i] upward */
    private void upheap(int i) {
        while (i > 0) {
            int p = (i - 1) / 2;
            if (heap[i].key >= heap[p].key) break;
            Entry temp = heap[i];
            heap[i] = heap[p];
            heap[p] = temp;
            i = p;
        }
    }

    /** Moves heap[i] downward */
    private void downheap(int i) {
        while (true) {
            int left = 2 * i + 1;
            int right = left + 1;
            int smallest = i;

            if (left < size && heap[left].key < heap[smallest].key) smallest = left;
            if (right < size && heap[right].key < heap[smallest].key) smallest = right;

            if (smallest == i) break;

            Entry temp = heap[i];
            heap[i] = heap[smallest];
            heap[smallest] = temp;

            i = smallest;
        }
    }
}
