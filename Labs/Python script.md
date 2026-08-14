
# 1. Conditions

### Exercise 1 — Positive, Negative, Zero

```python
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**Output:**

```text
Negative
```

### Exercise 2 — Even or Odd

```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Output:**

```text
Even
```

### Exercise 3 — Adult or Minor

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

**Output:**

```text
Minor
```

---

# 2. Loops

### Exercise 1 — For Loop

```python
for i in range(1, 11):
    print(i)
```

**Output:**

```text
1
2
3
4
5
6
7
8
9
10
```

### Exercise 2 — While Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

**Output:**

```text
1
2
3
4
5
```

### Exercise 3 — Break

```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```

**Output:**

```text
1
2
3
4
5
```

---

# 3. Functions

### Exercise 1 — Greeting

```python
def greet():
    return "Hello Hamida"

print(greet())
```

**Output:**

```text
Hello Hamida
```

### Exercise 2 — Addition

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

**Output:**

```text
8
```

### Exercise 3 — Even or Odd Function

```python
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(6))
```
**Output:**

```text
Even
```

