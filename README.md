# Asymptotic Complexity Analysis -- CS415 Project 1

![Asymptotic Complexity Graph](images/ASYMPT_COMP.jpeg)

## Contributers: 
- Alejandro Madrigal
- [Owen Mastropietro](https://github.com/OwenMastropietro)

## Instructions To Run:
***CLI***
1. `$ python3 project01a.py`
2. Follow the prompts for entering significant data.

***PyCharm***
1. Under "configurations", set script path to the python "project01a" file.
2. Select "run" located in the upper-right corner of the application.
3. Follow the prompts for entering significant data.

## Algorithms Reviewed
1. Euclid's Algorithm for finding the Greatest Common Divisor, GCD.
2. Iterative and Recursive Functions to return the n'th number in the Fibonacci sequence.
3. Three techniques for an exponentiation function to compute a<sup>n</sup>.
4. Selection Sort.
5. Insertion Sort.

## Project Description
For this project, we were tasked with exploring the upper bounds of Euclid's Algorithm for computing the Greatest Common Divisor, GCD, exploring three different techniques for computing a<sup>2</sup>, and exploring two common sorting algorithms, insertion sort and selection sort.

### Task 1:
**Implement an algorithm for computing the Greatest Common Divisor of two integers**
```python
def euclid_GCD(m, n):
    if n == 0: return m, 0
    if n == 1: return 1, 0
    else:
        val, basic_operation_count = euclidGCD(n, m % n)
        return val, basic_operation_count + 1
```
- ***Time Complexity:*** *Θ(n) --> Θ(2^b)*

**Implement an algorithm, that returns the k'th number in the fibonacci sequence**
```python
def fib(k):
    if k == 0: return 0, 0
    if k == 1: return 1, 0
    else:
        val_1, basic_ops_1 = fib(k-1)   # where val_1 = fib(k-1)[0] and basic_ops_1 = fib(k-1)[1]
        val_2, basic_ops_2 = fib(k-2)
        return val_1 + val_2, basic_ops_1 + basic_ops_2 + 1
```
- ***Time Complexity:*** *Θ(phi^k) or Θ(phi^2^b)*

**Explore GCD(fib(k+1), fib(k))**
- Add Description / What did I find?

### Task 2:
**Exponentiation Algorithms for computing a<sup>x</sup>.**

***Technique 1: Decrease by One***
```python
def exp1(a, n):
    if n == 0: return 1, 0     # Note: a^0 = 1 for all values of a.
    if n == 1: return a, 0     # Note: a^1 = a for all values of a.
    else:
        val, basic_operation_count = exp1(a, n-1)
        return a * val, basic_operation_count + 1
```
- ***Recurrence Relation:*** *M(n) = M(n-1) + 1*
    - *M(n-1) represents the number of basic operations in computing exp1(a, n-1)*
    - *+ 1 represents the additional basic operation in computing exp1(a, n-1) x a*
- ***Time Complexity:*** *Θ(n) ==> Θ(2<sup>b</sup>)*

***Technique 2: Decrease by Constant Factor***
```python
def exp2(a, n):
    if n == 0: return 1, 0      # Note: a^0 = 1 for all values of a.
    if n == 1: return a, 0      # Note: a^1 = a for all values of a.
    elif n % 2 == 0:            # If n is even:
        val, basic_operation_count = exp2(a, n/2)
        return val ** 2, basic_operation_count + 1     # Increment basic_operation_count by one due to squaring.
    else:                       # If n is odd:
        val, basic_operation_count = exp2(a, (n-1) / 2)
        return a * val ** 2, basic_operation_count + 2 # Increment basic_operation_count by two due to squaring and multiplying.
```
- *As per the textbook, on page 133, we are reducing the problem size by about half at the expense of one or two multiplications.*
- ***Recurrenc Relation:*** *M(n) = M(n/2) + 1?*
- ***Time Complexity:*** *Θ(log n)*

***Technique 3: Divide and Conquer***
```python
def exp3(a, n):
    if n == 0: return 1, 0              # Note: a^0 = 1 for all values of a.
    if n == 1: return a, 0              # Note: a^1 = a for all values of a.
    elif n % 2 == 0:    # If n is even:
        val, basic_operation_count = exp3(a, n/2)
        return val * val, basic_operation_count + 1       # Increment basic_operation_count by one due to single multiplication of val * val
    else:               # If n is odd:
        val, basic_operation_count = exp3(a, (n-1)/2)         # According to the project page, (n-1)/2. However, everywhere online uses n/2 and it does not seem to effect the result.
        return a * val * val, basic_operation_count + 2   # Increment basic_operation_count by two due to two multiplications of a * val * val.
```
- ***Recurrence Relation:*** *M(n) = M(n/2) + 1*
- ***Time Complexity:*** *Θ(log n) ==> Θ(n log n)?*

### Task 3:
**Insertion Sort**
```python
def insertion_sort(arr_in, n):
    basic_operation_count = 0
    arr = arr_in.copy()
    i = 0
    while i < n:
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            basic_operation_count += 1
            j = j - 1
        basic_operation_count += 1
        i = i + 1
    return arr, basic_operation_count
```
- ***Recurrence Relation:***
    - *Best: C(n) = n - 1*
    - *Average: C(n) = {n(n - 1) \over 2}*
    - *Worst: C(n) = {n(n-1) \over 2}*
- ***Time Complexity:***
    - *Best: O(n)*
    - *Average: O(n<sup>2</sup>)*
    - *Worst: O(n<sup>2</sup>)*

**Selection Sort**
```python
def selection_sort(arr_in, n):
    basic_operation_count = 0
    arr = arr_in.copy()
    i = 0
    while i < n-1:
        bigIdx = 0
        j = 1
        while j < n-i:
            if arr[j] > arr[bigIdx]:
                bigIdx = j
            basic_operation_count += 1
            j = j + 1
        arr[bigIdx], arr[n-i-1] = arr[n-i-1], arr[bigIdx]   # swap(arr, bigIdx, n-i-1)
        i = i + 1
    return arr, basic_operation_count
```
- ***Recurrence Relation:*** *here*
- ***Time Complexity:*** *here*

## Useful Resources
- [alt text](link)
- [alt text](link)