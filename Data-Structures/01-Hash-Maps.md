# 🗂️ Hash Maps

## 📖 What is it?

Stores **key → value** pairs for **O(1)** average lookup.

```
key ─────► value
```

---

## 🎯 Use when

- Previous values matter
- Fast lookup
- Count frequencies
- Find duplicates
- Associate two values
- Cache results

---

## ❌ Don't use when

- Order matters
- Need sorted traversal
- Sequential processing is enough

---

## ⚙️ Complexity

| Operation | Time |
|-----------|------|
| Lookup | O(1) |
| Insert | O(1) |
| Delete | O(1) |
| Space | O(n) |

---

## ⚠️ Collision

```
cat ─┐
     ├──► Bucket 5
dog ─┘
```

Solutions

- Chaining
- Open Addressing

---

## 🧠 Recognition

Problem says...

- seen before
- duplicates
- frequencies
- mapping
- lookup

↓

Think **Hash Map**

---

## 💻 Template

```python
d = {}

# insert
d[key] = value

# lookup
d[key]

# safe lookup
d.get(key)

# update
d[key] += 1
```

---

## 📈 Frequency

```python
freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

---

## 🏆 Common Problems

- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements

---

## 💡 Remember

> Fast lookup = Hash Map
