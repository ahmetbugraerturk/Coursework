package ds;

/**
 * COMP202 – Assignment 2: Operation Verdant Archives
 * Part 3 – Taxonomic Signature Module (Trie)
 *
 * Students: ONLY modify code inside the // TODO blocks.
 * Do NOT change the package name, class name, or method signatures.
 */
public class SpeciesTrie {

    /** Node type for the trie (only lowercase 'a'–'z' are assumed). */
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isWord;
        // You may store extra info here if needed (e.g., counts).
    }

    /** Root node of the trie. */
    private final TrieNode root = new TrieNode();

    public SpeciesTrie() {
        // nothing to initialize beyond root
    }

    // ----------------------------------------------------------------------
    // Public API
    // ----------------------------------------------------------------------

    /**
     * Inserts the given species name into the trie.
     * You may assume input is lowercase letters a–z.
     */
    public void insert(String species) {
        // TODO: Traverse the trie, creating nodes as needed, and mark the last node as a word.
        // Hint: Use index = c - 'a' to convert each char to an array index (0–25).
    	TrieNode curr = root;
    	for (int i=0; i<species.length(); i++) {
    		if (curr.children[(species.charAt(i)-'a')]==null)
    			curr.children[(species.charAt(i)-'a')] = new TrieNode();
    		curr = curr.children[(species.charAt(i)-'a')];
    	}
    	curr.isWord = true;
    }

    /**
     * @return true if the exact species name exists in the trie.
     */
    public boolean contains(String species) {
        // TODO: Use findNode(species) and check that the node is not null AND node.isWord is true.
    	TrieNode node = findNode(species);
    	if (node == null || !node.isWord)
    		return false;
    	else
    		return true;
    }

    /**
     * @return true if there is any species with the given prefix.
     */
    public boolean startsWith(String prefix) {
        // TODO: Return true if findNode(prefix) is not null.
        return findNode(prefix) != null; // placeholder so starter code compiles
    }

    /**
     * @return number of species that start with the given prefix.
     */
    public int countPrefix(String prefix) {
        // TODO: Use findNode(prefix); if null, return 0. Otherwise, return countWords(node).
        return countWords(findNode(prefix)); // placeholder so starter code compiles
    }

    /**
     * Returns all species starting with the given prefix in
     * lexicographic order concatenated into a single string
     * (e.g., "abacus\nabalone\n...").
     */
    public String listPrefix(String prefix) {
        // TODO: Use findNode to get the node for the prefix.
    	TrieNode node = findNode(prefix);
    	if (node==null)
    		return "";
    	StringBuilder sb = new StringBuilder();
    	collectWords(node, prefix, sb);
        // If null, return the empty string.
        // Otherwise, call collectWords starting from that node to build the result string.
        return sb.toString().trim(); // placeholder so starter code compiles
    }

    // ----------------------------------------------------------------------
    // Helper methods
    // ----------------------------------------------------------------------

    /**
     * Finds and returns the node corresponding to the given prefix.
     * @return the node at the end of prefix, or null if prefix doesn't exist
     */
    private TrieNode findNode(String prefix) {
        // TODO: Traverse the trie following the characters of prefix.
    	TrieNode curr = root;
    	for (int i=0; i<prefix.length(); i++) {
    		if (curr.children[(prefix.charAt(i)-'a')]==null)
    			return null;
    		curr = curr.children[(prefix.charAt(i)-'a')];
    	}
        return curr;
        // If at any step the required child is null, return null.
        // Otherwise, return the node reached after processing all characters.
    }

    /**
     * Counts all words in the subtrie rooted at the given node.
     * @param node root of subtrie to count
     * @return total number of words in this subtrie
     */
    private int countWords(TrieNode node) {
        // TODO: Recursively count all words in the subtrie rooted at node.
    	if (node==null)
    		return 0;
    	int count = 0;        
        if (node.isWord)
            count++;
        for (int i = 0; i < 26; i++) {
        	if (node.children[i] != null )
        		count += countWords(node.children[i]);
        }
        // Base case - if node is null, return 0.
        // Increment count when node.isWord is true and sum counts from all 26 children.
        return count; // placeholder so starter code compiles
    }

    /**
     * Collects all words in the subtrie using DFS, maintaining lexicographic order.
     * @param node current node in traversal
     * @param currentWord the string formed by path from original prefix to current node
     * @param result StringBuilder to accumulate results
     */
    private void collectWords(TrieNode node, String currentWord, StringBuilder result) {
        // TODO: Use DFS to collect all words under this node in lexicographic order.
        if (node.isWord)
	        result.append(currentWord).append("\n");
    	for (int i = 0; i < 26; i++) {
        	if (node.children[i] != null) {
        		collectWords(node.children[i], currentWord + (char) (i+'a'), result);
        	}
        }
        // If node.isWord is true, append currentWord + \"\\n\" to result.
        // Then, for i from 0 to 25, recurse into any non-null child, appending the corresponding character.
    }
}

