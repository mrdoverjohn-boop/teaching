# IF STATEMENTS

RIGHT NOW your programs basically do everything in order.

But games need to make decisions.

Like:

> IF health is 0, die.

> IF password is correct, let them in.

That is what an `if` statement does.

```python
age = 16

if age >= 16:
    print("You are at least 16")
```

## THE INDENTATION MATTERS

This:

```python
if age >= 16:
    print("this only happens if the condition is true")
```

is different from:

```python
if age >= 16:
    print("inside the if")

print("this happens no matter what")
```

## COMPARISONS

```python
x == 5   # equal to
x != 5   # NOT equal to
x > 5    # greater than
x < 5    # less than
x >= 5   # greater than OR equal to
x <= 5   # less than OR equal to
```

IMPORTANT:

```python
x = 5
```

means:

> PUT 5 INTO x

But:

```python
x == 5
```

means:

> IS x equal to 5?

## ELSE

```python
password = input("Password: ")

if password == "beans":
    print("correct")
else:
    print("WRONG BOZO")
```

## ELIF

Use `elif` if there are multiple possibilities:

```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("below C")
```

# TRY IT

Ask the user for a number.

If it is greater than 10, say so.

If it is exactly 10, say so.

Otherwise tell them it is below 10.
