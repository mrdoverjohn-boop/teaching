# MATH + DATA TYPE CONVERSION

You know variables.

You know input.

NOW WE MAKE THE COMPUTER DO MATH.

## BASIC OPERATORS

```python
5 + 2   # addition
5 - 2   # subtraction
5 * 2   # multiplication
5 / 2   # division
```

You can use variables too:

```python
x = 5
y = 2

print(x + y)
```

## BUT INPUT IS WEIRD

Remember:

```python
number = input("Give me a number: ")
```

`number` is a STRING.

So this:

```python
number + 5
```

will not work.

Python is basically looking at you like:

> mf you gave me TEXT and then asked me to add FIVE to it 😭

## CONVERT IT

Use `int()` for whole numbers:

```python
number = int(input("Give me a number: "))
```

Now if the user types `10`, `number` is the integer `10`.

For decimal numbers:

```python
number = float(input("Give me a decimal: "))
```

You can also convert existing variables:

```python
text = "50"
number = int(text)
```

## TRY IT

Make a calculator that:

1. asks for two numbers
2. adds them
3. prints the answer

BONUS:
Print subtraction, multiplication, and division too.
