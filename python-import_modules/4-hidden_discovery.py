#!/usr/bin/python3
import dis
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)  # Get all names defined in the module
    for name in sorted(names):  # Sort names alphabetically
        if not name.startswith("__"):  # Filter out names that start with '__'
            print(name)
