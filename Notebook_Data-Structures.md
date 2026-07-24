# 📚 Data Structures Study Guide
> A practical guide to the most common Data Structures & Problem Solving Patterns used in Coding Interviews and LeetCode.

---

# Table of Contents

1. 🗂️ Hash Maps
2. 👉👈 Two Pointers
3. 🪟 Sliding Window

---

# 🗂️ Hash Maps

## 📖 What is it?

A **Hash Map** (also called **Dictionary** in Python or **Hash Table** in many languages) is a data structure that stores information as **key-value pairs**.

Think of it like a **mailbox**:

```
Mailbox Number ─────► Letter
```

Instead of searching every mailbox, you immediately go to mailbox **#42**.

Programming works the same way:

```
"John" ─────► 98
"Emma" ─────► 75
"Lucas" ─────► 91
```

The key is used to instantly locate its value.

---

## 🎯 What is it used for?

Hash Maps are used whenever you need **fast lookups**.

Many interview problems become easy once you realize:

> Instead of asking the same question repeatedly, remember the answer.

### ❌ Brute Force Mindset

```
for every element:
    search entire array again
```

Time Complexity:

```
O(n²)
```

### ✅ Hash Map Mindset

```
Have I seen this before?

YES ➜ Get answer instantly.
NO  ➜ Save it.
```

Time Complexity:

```
O(n)
```

This is probably the **biggest mindset shift** beginners experience.

---

# 🧠 Visual Example

Imagine trying to find a student's grade.

Without a Hash Map:

```
Alice
Bob
Charlie
Daniel
Emma
Frank
...
```

Need to scan everything.

With a Hash Map:

```
{
    "Alice":90,
    "Bob":82,
    "Emma":99
}

Lookup:

"Emma"

↓

99
```

Instant.

---

# ⚙️ How does it work?

Internally, a Hash Map uses a **Hash Function**.

```
Key

↓

Hash Function

↓

Memory Address

↓

Stored Value
```

Example:

```
"apple"

↓

hash("apple")

↓

Index 17

↓

Table[17] = 45
```

---

# 💥 Hash Collisions

## What is a collision?

Sometimes **two different keys produce the same hash**.

Example:

```
hash("cat") = 15
hash("dog") = 15
```

Both want the same position.

```
Index 15

↓

cat
dog
```

This is called a **Hash Collision**.

---

## How is it solved?

### 1️⃣ Chaining (Most Common)

Store multiple values in the same bucket.

```
Index 15

↓

[
 cat,
 dog,
 bird
]
```

---

### 2️⃣ Open Addressing

If occupied:

```
15 ❌

↓

16 ✔
```

Move until an empty position is found.

---

# 📊 Time Complexity

| Operation | Average | Worst |
|-----------|---------|--------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Update | O(1) | O(n) |
| Delete | O(1) | O(n) |

Normally, interviews assume **Average O(1).**

---

# 💡 When should I think about using a Hash Map?

If the problem mentions...

✅ Finding duplicates

✅ Counting frequencies

✅ Fast lookup

✅ Previously seen elements

✅ Pair sum (Two Sum)

✅ Grouping items

✅ Caching previous work (Memoization)

✅ Mapping one thing to another

---

# 🏆 Common LeetCode Problems

- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements
- Longest Consecutive Sequence
- Happy Number
- Isomorphic Strings

---

# 💻 How it looks in Python

## 1. Storing data

```python
grades = {}

grades["Alice"] = 95
grades["Bob"] = 88
```

---

## 2. Looking something up

```python
print(grades["Alice"])
```

Output

```
95
```

---

## 3. Updating values

```python
grades["Alice"] += 5
```

---

## 4. Frequency Map

One of the most common interview patterns.

```python
freq = {}

for item in data:
    if item not in freq:
        freq[item] = 1
    else:
        freq[item] += 1
```

Shorter version:

```python
freq[item] = freq.get(item, 0) + 1
```

---

# 📈 Hash Map Workflow

```text
            Start
              │
              ▼
     Read next element
              │
              ▼
Already in Hash Map?
       │            │
      Yes          No
       │            │
       ▼            ▼
Use stored      Store it
information     in Hash Map
       │            │
       └──────┬─────┘
              ▼
        Continue
```

---

# 👉👈 Two Pointers

## 📖 What is it?

Two Pointers is a problem-solving technique where **two indices move through a data structure together**.

Instead of repeatedly scanning the same data, both pointers cooperate to solve the problem efficiently.

It is one of the most important interview patterns.

---

# 🎯 What is it used for?

Usually used with:

- Arrays
- Strings
- Linked Lists

It helps:

- eliminate nested loops
- reduce time complexity
- compare elements efficiently
- scan ranges

---

# 👀 Visual Example

```
Array

[1][2][3][4][5]

 ^
 L

             ^
             R
```

Two pointers moving independently.

---

# Pattern 1️⃣ Same Direction

Both pointers move left → right.

Usually:

```
Slow →

Fast →→
```

---

## Fast & Slow Pointer

```
1 → 2 → 3 → 4 → 5

S

F
```

After one step:

```
1 → 2 → 3 → 4 → 5

    S

        F
```

Fast moves twice as quickly.

---

## Uses

✅ Find middle of linked list

```
Fast reaches end

↓

Slow is in the middle.
```

---

### Detect cycles (Floyd's Cycle Detection)

```
A → B → C
     ↑   ↓
     E ← D
```

Fast eventually catches Slow.

```
S

      F

↓

Meet

↓

Cycle exists.
```

---

# Pattern 2️⃣ Opposite Direction

```
[1][2][4][7][10]

 ^
 L

             ^
             R
```

Pointers move toward each other.

---

## Uses

### Find pair with target sum

Example:

```
Target = 9

1 2 3 6 7

L       R

1+7 = 8

Too small

Move Left
```

---

### Palindrome

```
racecar

r a c e c a r

L           R
```

Compare both ends.

---

### Reverse Array

```
Before

1 2 3 4 5

↓

Swap

5 2 3 4 1
```

---

# 📊 Time Complexity

| Operation | Complexity |
|------------|------------|
| Single Pass | O(n) |
| Opposite Direction | O(n) |
| Fast & Slow | O(n) |
| Extra Space | O(1) |

---

# 💡 When should I think about Two Pointers?

The problem mentions...

✅ Sorted array

✅ Palindrome

✅ Reverse array/string

✅ Merge arrays

✅ Remove duplicates

✅ Find pair

✅ Linked list

✅ Constant space

---

# 🏆 Common LeetCode Problems

- Two Sum II
- Valid Palindrome
- Merge Sorted Array
- Remove Duplicates from Sorted Array
- Move Zeroes
- Linked List Cycle
- Middle of Linked List
- Container With Most Water

---

# 💻 Python Example

Reverse an array

```python
left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
```

---

# 📈 Decision Flow

```text
          Problem
             │
             ▼
      Two positions?
             │
             ▼
 Is array sorted?
      │          │
     Yes        No
      │          │
      ▼          ▼
Opposite     Same Direction
Pointers        Pattern
```

---

# 🪟 Sliding Window

## 📖 What is it?

Sliding Window is an optimization technique that processes a **contiguous range of elements** (called the **window**) instead of examining every possible subarray or substring from scratch.

Rather than rebuilding the range every time, the window **slides** through the data by expanding or shrinking as needed.

You can think of it as looking through a moving window:

```
Array

[1][2][3][4][5][6]

 └─────┘

Window
```

Move one step:

```
[1][2][3][4][5][6]

    └─────┘
```

---

# 🎯 What is it used for?

Sliding Window is useful whenever the problem involves **contiguous elements**.

Examples:

- Subarrays
- Substrings
- Consecutive elements
- Running sums
- Maximum/minimum values within a range

Without this pattern, many solutions are **O(n²)**.

With Sliding Window, they often become **O(n)**.

---

# 🧠 How to identify it in a problem

Look for phrases like:

✅ Longest substring...

✅ Shortest subarray...

✅ Maximum sum of...

✅ Consecutive elements

✅ Window of size K

✅ Continuous sequence

If the elements **must stay together**, Sliding Window is often the right approach.

---

# Pattern 1️⃣ Fixed Window

The window size is predetermined.

Example:

```
Find the maximum sum of 3 consecutive numbers.

Array

[2][1][5][1][3][2]

Window size = 3

[2][1][5]

↓

[1][5][1]

↓

[5][1][3]
```

Each move:

- Remove left value
- Add right value

No need to recalculate everything.

---

# Pattern 2️⃣ Dynamic Window

The window size changes during execution.

```
Expand →

Need constraint?

↓

Shrink ←
```

Example:

Longest substring without repeating characters.

```
abcabcbb

[a][b][c]

↓

Duplicate found

↓

Shrink

↓

Continue
```

---

# 📊 Time Complexity

| Operation | Complexity |
|------------|------------|
| Fixed Window | O(n) |
| Dynamic Window | O(n) |
| Extra Space | O(1) to O(n) (depends on auxiliary structures like Hash Maps) |

---

# 💡 When should I think about Sliding Window?

The problem mentions...

✅ Contiguous subarray

✅ Contiguous substring

✅ Window size K

✅ Longest/Shortest valid segment

✅ Maximum/Minimum consecutive sum

✅ Character frequency in a substring

---

# 🏆 Common LeetCode Problems

- Maximum Average Subarray I
- Maximum Sum Subarray of Size K
- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum
- Permutation in String
- Minimum Window Substring
- Find All Anagrams in a String

---

# 💻 Python Examples

## Fixed Window

```python
k = 3

window_sum = sum(nums[:k])
best = window_sum

for right in range(k, len(nums)):
    window_sum += nums[right]
    window_sum -= nums[right - k]
    best = max(best, window_sum)
```

---

## Dynamic Window

```python
left = 0

for right in range(len(nums)):

    while window_is_invalid():
        left += 1

    update_answer()
```

---

# 📈 Sliding Window Workflow

```text
          Start
            │
            ▼
      Expand Window
            │
            ▼
 Window satisfies rules?
      │             │
     Yes           No
      │             │
      ▼             ▼
Update Answer   Shrink Window
      │             │
      └──────┬──────┘
             ▼
       Continue
```

---

# 🎯 Pattern Recognition Cheat Sheet

| If you see... | Think... |
|---------------|----------|
| Fast lookup | 🗂️ Hash Map |
| Count frequencies | 🗂️ Hash Map |
| Previously seen values | 🗂️ Hash Map |
| Sorted array + pair | 👉👈 Two Pointers |
| Reverse / Palindrome | 👉👈 Two Pointers |
| Middle of Linked List | 👉👈 Fast & Slow |
| Subarray / Substring | 🪟 Sliding Window |
| Consecutive elements | 🪟 Sliding Window |
| Longest / Shortest valid segment | 🪟 Sliding Window |
| Window size K | 🪟 Fixed Sliding Window |
