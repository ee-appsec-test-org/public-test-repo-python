# public-test-repo-python

A simple dummy Python application that greets users.

## Features

- Simple greeting function
- Interactive user input
- Basic unit tests

## Requirements

- Python 3.6 or higher

## Usage

Run the application:

```bash
python app.py
```

Run the tests:

```bash
python test_app.py
```

Or run tests with verbose output:

```bash
python -m unittest test_app.py -v
```

## Example

```python
from app import greet

# Greet with default name
print(greet())  # Output: Hello, World!

# Greet with custom name
print(greet("Alice"))  # Output: Hello, Alice!
```