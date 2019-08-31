Here, we use find method to find the corresponding node to a prefix, and then we iterate to every single node and return the nodes that have is_word as true.

The time complexity is O(m*n) and the space complexity is O(n) because we need to iterate over the entire trie and store the results in another array.
Here, m is the number of elements in the trie and n is the length of the elements.
