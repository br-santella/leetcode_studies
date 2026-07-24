# 🗂️ Hash Maps

> Fast key-value lookup data structure.

---

# 📌 Definition

A **Hash Map** stores data as **key → value** pairs, allowing values to be accessed directly through a key instead of searching sequentially.

```
key ─────► value
```

**Main idea**

> Trade **memory** for **speed**.

---

# 🎯 When to Use

Think about a Hash Map when a problem mentions:

- ✅ Fast lookup
- ✅ Previously seen values
- ✅ Duplicates
- ✅ Count frequency
- ✅ Key → Value relationship
- ✅ Memoization
- ✅ Cache
- ✅ Grouping objects

Typical interview phrases:

- "Find duplicates"
- "Return indices"
- "Count occurrences"
- "Have we seen this before?"
- "Store previous results"

---

# 🧠 Visual Representation

Without Hash Map

```
Emma?

↓

Alice
Bob
Charlie
Daniel
Emma
```

Search complexity

```
O(n)
```

---

With Hash Map

```
{
    "Alice":91,
    "Bob":84,
    "Emma":99
}
```

```
Emma

↓

99
```

Search complexity

```
O(1)
```

---

# ⚙️ Internal Structure

```
          Key

           │

           ▼

    Hash Function

           │

           ▼

      Bucket Index

           │

           ▼

         Value
```

Example

```
"apple"

↓

hash()

↓

bucket 7

↓

15
```

---

# 🔑 Hashable Types

A key **must be immutable**.

| Type | Hashable |
|-------|----------|
| int | ✅ |
| float | ✅ |
| bool | ✅ |
| str | ✅ |
| tuple | ✅ |
| list | ❌ |
| dict | ❌ |
| set | ❌ |

---

# ⚠️ Hash Collision

A collision happens when two keys map to the same bucket.

```
hash("cat")

↓

5

hash("dog")

↓

5
```

```
Bucket 5

cat
dog
```

### Common solutions

**Chaining**

```
Bucket

↓

[
 cat,
 dog,
 bird
]
```

**Open Addressing**

```
5 occupied

↓

6 empty

↓

Insert
```

Average complexity remains **O(1)**.

---

# 📊 Complexity

| Operation | Average | Worst |
|----------|:-------:|:-----:|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Update | O(1) | O(n) |
| Delete | O(1) | O(n) |

---

# 💻 Python

## Create

```python
my_map = {}
```

---

## Insert

```python
my_map["apple"] = 5
```

---

## Lookup

```python
value = my_map["apple"]
```

---

## Safe Lookup

```python
value = my_map.get("apple")
```

---

## Update

```python
my_map["apple"] += 1
```

---

## Delete

```python
del my_map["apple"]
```

---

# 📈 Frequency Map

One of the most common interview patterns.

```python
freq = {}

for item in data:
    freq[item] = freq.get(item, 0) + 1
```

Equivalent to

```python
if item not in freq:
    freq[item] = 1
else:
    freq[item] += 1
```

---

# 📝 Common Templates

## Count Frequencies

```python
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1
```

---

## Store First Index

```python
seen = {}

for i, n in enumerate(nums):
    if n not in seen:
        seen[n] = i
```

---

## Check Duplicate

```python
seen = set()

for n in nums:

    if n in seen:
        return True

    seen.add(n)

return False
```

---

## Reverse Mapping

```python
reverse = {}

for k, v in original.items():
    reverse[v] = k
```
---

# 🧩 Common Patterns

## 1. Frequency Counter

**Use when**

- Count occurrences
- Find the most/least frequent element
- Compare frequencies

Problems

- Top K Frequent Elements
- Valid Anagram
- Majority Element

---

## 2. Lookup Table

Store values to avoid repeated searches.

```python
lookup = {}

for item in data:
    lookup[item.id] = item
```

---

## 3. Visited Set

Track processed elements.

```python
visited = set()

for node in nodes:

    if node in visited:
        continue

    visited.add(node)
```

---

## 4. Two Sum Pattern

Store previously visited values.

```python
seen = {}

for i, n in enumerate(nums):

    target_value = target - n

    if target_value in seen:
        return [seen[target_value], i]

    seen[n] = i
```

---

## 🎯 Pattern Recognition

| If the problem says... | Think Hash Map? |
|------------------------|:---------------:|
| Count occurrences | ✅ |
| Find duplicates | ✅ |
| Previously seen | ✅ |
| Return indices | ✅ |
| Fast lookup | ✅ |
| Key → Value | ✅ |
| Group objects | ✅ |
| Memoization | ✅ |
| Cache | ✅ |

---

# 🏆 Common LeetCode Problems

| Problem | Pattern |
|----------|---------|
| Two Sum | Lookup |
| Contains Duplicate | Membership |
| Valid Anagram | Frequency Map |
| Group Anagrams | Grouping |
| Top K Frequent Elements | Frequency Map |
| Longest Consecutive Sequence | Membership |
| Happy Number | Visited Set |
| Isomorphic Strings | Mapping |
| Ransom Note | Frequency Counter |
| Word Pattern | Mapping |

---

# ⚠️ Common Mistakes

❌ Using mutable objects as keys.

```python
my_map[[1,2,3]] = 5
```

---

❌ Forgetting to initialize counters.

```python
freq[x] += 1
```

Correct

```python
freq[x] = freq.get(x, 0) + 1
```

---

❌ Assuming every language preserves insertion order.

Python dictionaries preserve insertion order (Python ≥ 3.7), but this is **not guaranteed** for every language or Hash Map implementation.

---

❌ Using a Hash Map when ordering matters.

If sorted traversal is required, consider:

- TreeMap (Java)
- std::map (C++)
- Ordered Dictionary

---

# 🚀 Interview Tips

### Need O(1) lookup?

✅ Hash Map

---

### Need to know if you've seen something?

✅ Hash Map / Hash Set

---

### Need to count?

✅ Frequency Map

---

### Need to associate two values?

✅ Hash Map

---

### Need ordering?

❌ Probably not a Hash Map.

---

# 📝 Cheat Sheet

| Task | Solution |
|------|----------|
| Store values | `dict` |
| Unique elements | `set` |
| Count frequency | `dict.get()` |
| Safe lookup | `dict.get()` |
| Update counter | `+= 1` |
| Membership | `in` |
| Remove key | `del` |

---

# 🐍 Python Quick Reference

```python
# Create
d = {}

# Insert
d[key] = value

# Lookup
d[key]

# Safe lookup
d.get(key)

# Exists
key in d

# Delete
del d[key]

# Iterate keys
for k in d:

# Iterate values
for v in d.values():

# Iterate pairs
for k, v in d.items():

# Frequency
freq[x] = freq.get(x, 0) + 1

# Default value
d.setdefault(key, [])

# Merge
d1.update(d2)

# Size
len(d)

# Clear
d.clear()
```

---

# 🧠 Decision Flow

```
            Problem
                │
                ▼
     Need fast lookup?
          │         │
         No        Yes
          │         │
          ▼         ▼
 Continue     Seen before?
                  │      │
                 No     Yes
                  │      │
                  ▼      ▼
            Continue   Hash Map
                          │
                          ▼
              Count / Lookup / Mapping?
                          │
                          ▼
                    Use Hash Map
```

---

# 📌 Summary

## Definition

Stores data as **key → value** pairs with average **O(1)** lookup.

---

## Strengths

- Fast lookup
- Fast insertion
- Fast deletion
- Frequency counting
- Mapping values
- Duplicate detection
- Memoization

---

## Weaknesses

- Extra memory usage
- No automatic sorting
- Worst-case O(n) with many collisions

---

## Complexity

| Operation | Complexity |
|-----------|------------|
| Insert | O(1) average |
| Search | O(1) average |
| Update | O(1) average |
| Delete | O(1) average |
| Space | O(n) |

---

## Remember

> **Hash Maps trade memory for speed.**

If the first idea that comes to mind is:

> *"I need to know if I've already seen this value..."*

A **Hash Map** (or **Hash Set**) is very likely the correct data structure.
