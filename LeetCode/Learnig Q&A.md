# 📙💡​​ LeetCode Learning Questions & Answers
This page is designed for all the small questions I've had while solving LeetCode problems. Most of them are language-related (Python) or about the algorithms themselves.

### Q1: What is the `self` parameter in fuctions used for?

**Answer:**
The `self` parameter is used for **Object-Oriented Programming (OOP)**. It represents the specific instance of the class that's being created. `self` allows functions inside the class to access or modify that specific object's data.

In Python, `self` is a convention and is **necessary** when defining instance methods within a class—it's how the method knows which object's data to work with.

---

### Q2: Why use a class `Solution`?

**Answer:**
Using a class wrapper serves several important purposes:

1. **Testing Framework Compatibility**: LeetCode and similar platforms run your function against hundreds of test cases. By wrapping your solution in a class, the platform can easily spin up a fresh, isolated instance of your code for each test case.

2. **Data Isolation**: This ensures that leftover data from Test Case #1 doesn't accidentally interfere with Test Case #2. Each instance is independent and clean.

3. **Standard Convention**: Most coding interview platforms expect solutions to follow this class-based structure, making it a standard practice in competitive programming.
