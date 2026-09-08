# RANDOM NUMBERS

Games LOVE randomness.

Python has a module called `random`.

```python
import random
```

Now you can do:

```python
number = random.randint(1, 10)
print(number)
```

That chooses a random whole number from 1 through 10.

## RANDOM CHOICE

```python
enemies = ["zombie", "skeleton", "gremlin"]

enemy = random.choice(enemies)

print(enemy)
```

It chooses one thing from the list.

## MINI PROJECT: NUMBER GUESSER

Make the computer choose:

```python
secret_number = random.randint(1, 10)
```

Then repeatedly ask the player to guess.

Tell them if they are:

- too high
- too low
- correct

Once they guess correctly, end the game.

If you can do that WITHOUT copying a finished solution:

YOU ARE READY FOR THE 30 MINUTE GAME CHALLENGE.
