#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1  # Subtract 1 for the script name
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print(f"{arg_count} arguments:")

    for i in range(1, arg_count + 1):
        print(f"{i}: {sys.argv[i]}")
