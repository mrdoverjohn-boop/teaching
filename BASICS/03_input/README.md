# Python Basics

## INPUT

Another REALLY important part of Python is:

# `input()`

`input()` pauses the program and waits for the user to type something.

For example:

```python
input()
```

This DOES work by itself.

The problem is that if you do this, Python receives what the user typed and then immediately throws it away because you never saved it.

So most of the time you want:

```python
user_input = input()
```

Now the process is basically:

```text
input()
-> wait for the user
-> user types something
-> input() RETURNS that text
-> save the returned text inside user_input
```

Then you can do:

```python
print(user_input)
```

## YOU CAN ALSO PUT TEXT INSIDE INPUT

```python
name = input("What is your name? ")
print(name)
```

The text inside `input()` is called a **prompt**.

## IMPORTANT WEIRD THING

`input()` ALWAYS gives you a string.

So:

```python
age = input("How old are you? ")
```

Even if someone types:

```text
16
```

Python currently sees it as `"16"` — TEXT.

We will fix that in the next lesson.

# TRY IT

Ask the user for:
1. their name
2. their favorite game

Then print both answers back to them.

Good luck gng 🥶
