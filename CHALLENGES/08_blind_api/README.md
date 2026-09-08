# BLIND API CHALLENGE

You are given helper code.

You are NOT allowed to edit it.

You have to figure out how to use it.

---

# SETUP

Create a helper file like:

```python
# game_tools.py

import random

def random_damage():
    return random.randint(1, 10)

def heal(health, amount):
    return health + amount

def enemy_name():
    enemies = ["Goblin", "Skeleton", "Gremlin"]
    return random.choice(enemies)
```

The students get the file.

They can READ IT.

They may NOT MODIFY IT.

---

# GOAL

Make a game that uses every required helper function.

Example requirement:

Use:

- `random_damage()`
- `heal()`
- `enemy_name()`

at least once in a meaningful way.

---

# TIME

Recommended:

30 minutes.

---

# HARDER VERSION

Instead of giving them the source code:

only give them documentation like:

```text
random_damage()
Returns a random integer damage value.

heal(health, amount)
Returns updated health.

enemy_name()
Returns a random enemy name.
```

Now they have to treat the helper code like a real library.

---

# SCORING

0–5 each:

- Correct API Use
- Fun
- Creativity
- Completeness
- Code Organization

---

# SECRET LESSON

This is basically baby API/library programming.

You do not always need to know HOW a function works.

Sometimes you only need to know:

- what you give it
- what it gives back
- what it is supposed to do
