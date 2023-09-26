# What's an Algorithm
> A set of instructions to complete/finish a task.

- Its a estabelished body of knowledge to finish a task. Focused on the best possible solution for the current context and when/where to apply. 
***
### Algorithmic Thinking
> *Be able to solve each distinct component in a efficient way.*
	- Break problems in a minor problems.
	- **KEEP IT SIMPLE, STOOPID.**
- Clearly define the range/scope.
- [[Time complexity]] must be included in the thinking, as well [[Space Complexity]].
- **MUST** have a clear **input**/problem to solve and **output**.
- Consistent results.
# Search Algorithms

- **[[Linear Search]]**
	-  Start at the the beginning of the list, and go through each value until the desired value is found. 
-  **[[Binary Search]]**
	- Values **must** be sorted.
	- Starts at the middle position and then discard the lower/higher based on the target.
		- If smaller than target, discard the higher bound.
		- Else, if higher than the target, discard the smaller bound.
	- Repeat until the target is found.
	- For sorted data, may be one of the quickest ways to find something.

# Big O Notation // Upper Bound
- Is the theoretical complexity of an algorithm and its run time.
- It is important to know the scope of comparison.
- In Big O, the n is correlated to the input size of the input
- **[[Linear Search]]**
	- $O(n)$
- **[[Binary Search]]**
	- $O(log \ n)$  
### Common Big O Values
- $O(1) \to$ Constant Runtime
- $O(n) \to$ Linear Runtime
- $O(log \ n) \to$ Logarithmic Runtime
- $O(n^2) \to$ Quadratic Runtime
- $O(n^3) \to$ Cubic Runtime
- $O(n \ log \ n) \to$ Quasilinear Runtime (tends to happen in sorting algorithms, like [[Merge Sort]])  

***
