# LISTS

Sometimes you need MANY values.

Doing this sucks:

```python
enemy1 = "zombie"
enemy2 = "skeleton"
enemy3 = "gremlin"
```

Use a list:

```python
enemies = ["zombie", "skeleton", "gremlin"]
```

## GET SOMETHING FROM A LIST

```python
print(enemies[0])
```

IMPORTANT:

PROGRAMMERS START COUNTING AT ZERO 😭

```text
0 = zombie
1 = skeleton
2 = gremlin
```

## ADD SOMETHING

```python
enemies.append("evil cat")
```

## LOOP THROUGH A LIST

```python
for enemy in enemies:
    print(enemy)
```

## LENGTH

```python
print(len(enemies))
```

# TRY IT

Make a list of at least 3 games.

Then:

1. print the first game
2. add another game
3. loop through the entire list and print every game
