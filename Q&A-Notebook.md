# 📙💡​​ Learning: Questions & Answers
All the small questions I've had while solving LeetCode problems.

## Q1: Why use a class `Solution`?

**Answer:**
Using a class wrapper serves several important purposes:

1. **Testing Framework Compatibility**: LeetCode and similar platforms run your function against hundreds of test cases. By wrapping your solution in a class, the platform can easily spin up a fresh, isolated instance of your code for each test case.

2. **Data Isolation**: This ensures that leftover data from Test Case #1 doesn't accidentally interfere with Test Case #2. Each instance is independent and clean.

3. **Standard Convention**: Most coding interview platforms expect solutions to follow this class-based structure, making it a standard practice in competitive programming.

## Q2: What is the time-complexity?

**Answer:**
Time complexity measures **how the runtime of an algorithm grows as the input size ($n$) increases.** Instead of measuring execution time in seconds (which changes depending on how fast a computer's processor is), time complexity looks at the *number of operations* the code performs. For example, if you pass an array of 10 items versus 1,000,000 items into your function, time complexity tells you how much more work your code has to do.

## Q3: What is Big O Notation, and why it matters for LeetCode?

**Answer:**
Big O notation is a mathematical notation used to describe the worst-case scenario of an algorithm's time (or space) complexity. It strips away all the minor details and focuses on the biggest factor driving the growth.

| Notation | Name | What it means | LeetCode Example |
| :--- | :--- | :--- | :--- |
| $O(1)$ | Constant Time | The execution time stays the same, no matter how big the input is. | Accessing an element in an array by its index (`arr[5]`). |
| $O(\log n)$ | Logarithmic Time | The problem size is cut in half with each step. Highly efficient. | **Binary Search** (looking up a word in a physical dictionary by splitting it in half repeatedly). |
| $O(n)$ | Linear Time | The runtime grows proportionally to the input size. | A single `for` loop looking through an array of size $n$. |
| $O(n \log n)$ | Linearithmic Time | Slightly worse than linear, but still very good. | Most efficient sorting algorithms (like Merge Sort or Quick Sort). |
| $O(n^2)$ | Quadratic Time | The runtime grows proportionally to the square of the input size. | **Nested loops**. If you loop through an array, and for every element, you loop through it again. |
| $O(2^n)$ | Exponential Time | The growth doubles with each addition to the input. Very slow. | Recursive algorithms that solve a problem by solving two smaller versions of it (like naive Fibonacci). |

### Why BigO matters for LeetCode:
Every LeetCode problem includes a **Constraints** section (e.g., $n \le 10^5$). These constraints are a massive hint telling you exactly what Big O efficiency your solution needs to achieve to avoid a **TLE (Time Limit Exceeded)** error.

As a general rule of thumb, Python, Java, and C++ can handle roughly $10^7$ to $10^8$ operations per second. You can use this cheat sheet to predict if your code will pass:

| Input Size ($n$) | Expected Big O Time Complexity |
| :--- | :--- |
| $n \le 10$ or $12$ | $O(n!)$ or $O(2^n)$ (Brute force / Backtracking) |
| $n \le 100$ | $O(n^3)$ (Dynamic Programming / Triple loops) |
| $n \le 500$ | $O(n^2)$ (Nested loops) |
| $n \le 10^5$ | $O(n \log n)$ or $O(n)$ (Sorting, Two Pointers, Hash Maps) |
| $n \le 10^9$ | $O(\log n)$ or $O(1)$ (Binary Search / Math formulas) |


