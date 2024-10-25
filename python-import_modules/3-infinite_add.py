#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:  # Skip the script name
        total += int(arg)  # Convert argument to integer and add to total
    print(total)
