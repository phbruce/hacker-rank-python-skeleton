# HackerRank Python Skeleton

This repository contains Python solution templates for HackerRank problems. It's designed to streamline the problem-solving process by providing a basic structure which can be easily adapted for different questions.

## How to Use

To use this repository for solving HackerRank problems, follow these steps:

1. **Select a HackerRank Problem**: Choose a problem from HackerRank that you wish to solve.

2. **Copy the Test Code**: In each HackerRank problem, there's a testing section usually within the `if __name__ == '__main__':` block. Copy this test code.

3. **Adapt the Code**: In the repository, you will find a template function in `script.py` that you need to complete. Replace this function with your solution. Also, ensure to adapt the function names as necessary to match those in the HackerRank test code.

4. **Input File**: An `input` file is expected at the root of the directory. Each line in this file represents an input that will be used when executing the specified script.

5. **Running the Script**: After implementing your solution, use the provided Makefile to test your solution locally. The Makefile is configured to use the `input` file for input data and allows you to specify the script file to be executed.

## Example

Here is an example of how you might adapt the `script.py` template for a specific question:

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'yourFunctionName' function below.
# The function is expected to return a RETURN_TYPE.
# The function accepts the following parameters:
#  1. PARAMETER_1
#  2. PARAMETER_2
#

def yourFunctionName(parameter1, parameter2):
    # Your logic goes here
    pass

if __name__ == '__main__':
    # HackerRank test code
```

## Makefile Usage

The `Makefile` in this repository is configured to automate the setup and execution of your solution scripts:

- It creates a Python virtual environment in the current directory.
- Activates the virtual environment.
- By default, runs `script.py` using the input from the `input` file.

To execute your script, simply run:

```bash
make
```

To execute a different script, specify the script name by running:

```bash
make SCRIPT_NAME=your_script_name.py
```

This command will compile and test your solution using the inputs provided in the `input` file and the specified script.

## Cleaning Up

To clean up the virtual environment files created by the Makefile, run:

```bash
make clean
```

## Contribution

Feel free to contribute to this repository by adding new solution templates or improving existing ones.
