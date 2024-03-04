# python-journey

<details>
<summary>Harvard CS50 AI - Lecture 0 - Search</summary>

### Depth First Search (StackFrontier)

A depth-first search algorithm exhausts each one direction before trying another direction. In these cases, the frontier is managed as a stack data structure. The catchphrase you need to remember here is **“last-in first-out.”** After nodes are being added to the frontier, the first node to remove and consider is the last one to be added. This results in a search algorithm that goes as deep as possible in the first direction that gets in its way while leaving all other directions for later.

_(An example from outside lecture: Take a situation where you are looking for your keys. In a depth-first search approach, if you choose to start with searching in your pants, you’d first go through every single pocket, emptying each pocket and going through the contents carefully. You will stop searching in your pants and start searching elsewhere only once you will have completely exhausted the search in every single pocket of your pants.)_

**Pros:**

- At best, this algorithm is the fastest. If it “lucks out” and always chooses the right path to the solution (by chance), then depth-first search takes the least possible time to get to a solution.

**Cons:**

- It is possible that the found solution is not optimal.
- At worst, this algorithm will explore every possible path before finding the solution, thus taking the longest possible time before reaching the solution.

</details>

<details>
<summary>Harvard CS50 AI - Lecture 1 - Knowledge</summary>

### You can add a header

</details>

## Resources

- [Beginner / Setup](https://www.youtube.com/watch?v=rfscVS0vtbw&t=11s)
- [Harvard AI with Python](https://pll.harvard.edu/course/cs50s-introduction-artificial-intelligence-python)
- [Neural Networks](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
- [LLM](https://learn.activeloop.ai/)
