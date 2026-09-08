# WHILE LOOPS

A loop repeats code.

A `while` loop repeats code WHILE something is true.

```python
number = 0

while number < 5:
    print(number)
    number = number + 1
```

That prints:

```text
0
1
2
3
4
```

## WHY THIS IS HUGE FOR GAMES

You can make a game loop:

```python
playing = True

while playing:
    choice = input("What do you want to do? ")

    if choice == "quit":
        playing = False
```

NOW your program can keep running instead of instantly ending.

## BE CAREFUL WITH INFINITE LOOPS

This:

```python
while True:
    print("AAAAAAAA")
```

never ends unless something stops it.

That is not always bad.

Games often basically ARE giant loops.

You just need a way to leave.

```python
while True:
    choice = input("> ")

    if choice == "quit":
        break
```

`break` immediately exits the loop.

# TRY IT

Make a menu that repeatedly asks:

```text
1. Say hello
2. Say goodbye
3. Quit
```

The menu should keep appearing until they choose Quit.
