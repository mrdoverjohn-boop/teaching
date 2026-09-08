import random
from pathlib import Path

base = Path(__file__).parent

folders = [
    folder for folder in base.iterdir()
    if folder.is_dir() and folder.name[:2].isdigit()
]

picked = random.choice(folders)

print("\nYOUR CHALLENGE IS:\n")
print(picked.name)
print()
print((picked / "README.md").read_text())
