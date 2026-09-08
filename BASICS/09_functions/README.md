# FUNCTIONS

YOU HAVE ALREADY BEEN USING FUNCTIONS.

```python
print()
input()
int()
len()
```

Those are functions somebody else made.

NOW YOU MAKE YOUR OWN.

```python
def say_hello():
    print("hello")
```

That CREATES the function.

It does not run yet.

Run it like this:

```python
say_hello()
```

## PARAMETERS

Functions can receive information:

```python
def say_hello(name):
    print("Hello", name)

say_hello("Bramity")
say_hello("Foxz")
```

`name` is a parameter.

## RETURN

A function can also SEND a value back:

```python
def add(x, y):
    return x + y

answer = add(5, 10)
print(answer)
```

Think of it like:

```text
add(5, 10)
-> does work
-> returns 15
```

# TRY IT

Make a function called `double`.

It receives one number and returns that number multiplied by 2.

Example:

```python
answer = double(5)
print(answer)
```

Should print:

```text
10
```
