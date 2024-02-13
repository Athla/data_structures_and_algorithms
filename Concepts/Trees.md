# All programming leads to Trees
- Somehow everywhere
- A single point that expands 
- File system, DOM, everything may be a tree
Binary Tree Representation
###############################
          O
    O           O
O       O   O       O

## Types of  Traversal
- To traverse a tree is simply to walk through its nodes, there are, mainly, two types of traversal:
    - Depth First
        - Pre Order
        ``` typescript
            function walk(curr: BinaryNode<number> | null, path: number[]): number[] {
                if (!curr) {
                    return path;
                }
                //Recurse
 
                // Pre    
                path.push(curr.value);
                // Recurse
                walk(curr.left, path);
                walk(curr.right, path);
                // Post
                return path
            }
            export default function pre_order_search(head: BinaryNode<number>): number[] {
                return walk(head, []);
                }
        ```
        - In Order
            ``` typescript
            function walk(curr: BinaryNode<number> | null, path: number[]): number[] {
                if (!curr) {
                    return path;
                }
                //Recurse
 
                // Pre    
                // Recurse
                walk(curr.left, path);
                path.push(curr.value);
                walk(curr.right, path);
                // Post
                return path
            }
            export default function in_order_search(head: BinaryNode<number>): number[] {
                return walk(head, []);
                }
            ```
        - Post Order
        ``` typescript
            function walk(curr: BinaryNode<number> | null, path: number[]): number[] {
                if (!curr) {
                    return path;
                }
                //Recurse
 
                // Pre    
                // Recurse
                walk(curr.left, path);
                walk(curr.right, path);
                // Post
                path.push(curr.value);
                return path
            }
            export default function post_order_search(head: BinaryNode<number>): number[] {
                return walk(head, []);
                }
        ```
        - All of those have one thing in common:
            - they follow the base rule for a recursion problem/algorithm:
                - Define a base case
                - Define is scope
                - Recurse.
            - For most of the recursive algorithms, it's a good practive to follow a few rules:
                - Define a base case, where it's clear what should be done;
                - In the base case, define where it starts, end and where does it returns;
                - After that, define where the recursive step should be called.
        - Implicit usage of a Stack
        - Trees have unique properties related to search algorithms and such, allowing efficient search and ordering methods;
        - The file system ordering and storage may be a good example of how trees are used and how to visualize them
            - By defining it's core parameter, which means, what will categorize it, it becomes possible to exclude or include which branches will be included.
            - By doing that, it becomes way faster to find a specific parameter
            - However, there is a the cost of the filtering operation, be it in place, be it in memory
            - Both sides can be equally expensive, thus, it may be needed to use different DS

    - A quick tree search/traversal may have a Big O of O(log n) to O(N), depending on it's height.

    - Breadth First
        - Implicit use of a Queue, as it's the oppostire of a DFS
        - Go level by level of a tree
