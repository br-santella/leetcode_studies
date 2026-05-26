# 📙💡​​ Learning: Questions & Answers
All the small questions I've had while solving LeetCode problems.

### Q1: Why use a class `Solution`?

**Answer:**
Using a class wrapper serves several important purposes:

1. **Testing Framework Compatibility**: LeetCode and similar platforms run your function against hundreds of test cases. By wrapping your solution in a class, the platform can easily spin up a fresh, isolated instance of your code for each test case.

2. **Data Isolation**: This ensures that leftover data from Test Case #1 doesn't accidentally interfere with Test Case #2. Each instance is independent and clean.

3. **Standard Convention**: Most coding interview platforms expect solutions to follow this class-based structure, making it a standard practice in competitive programming.
