# swe-testing-assignment

## Project Description

Quick-Calc is a simple calculator application developed as part of the **Applied System Software** course assignment.
The application performs the four basic arithmetic operations: **addition, subtraction, multiplication, and division**, and includes a **clear function** to reset the result.

The main goal of this project is not the user interface, but to demonstrate **clean code, testing strategies, and proper use of Git and GitHub**. The project implements **unit testing and integration testing** using the Pytest framework.

---

## Features

* Addition of two numbers
* Subtraction of two numbers
* Multiplication of two numbers
* Division of two numbers
* Division-by-zero handling
* Clear function to reset result

---

## Project Structure

```
swe-testing-assignment
│
├── quick_calc
│   ├── __init__.py
│   └── calculator.py
│
├── tests
│   ├── test_unit.py
│   └── test_integration.py
│
├── requirements.txt
├── pytest.ini
├── README.md
└── TESTING.md
```

---

## Setup Instructions

1. Clone the repository:

```
git clone https://github.com/Ilaha-Habibova/swe-testing-assignment.git
```

2. Navigate into the project folder:

```
cd swe-testing-assignment
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Tests

Run all tests using Pytest:

```
pytest
```

Pytest will automatically discover all tests in the **tests/** directory and display the results.

---

## Testing Framework Research

### Pytest

Pytest is a modern Python testing framework known for its simplicity and powerful features. It allows developers to write concise test functions using simple `assert` statements. Pytest also provides helpful error messages, automatic test discovery, and support for fixtures and plugins.

### Unittest

Unittest is Python’s built-in testing framework and follows a structure similar to Java’s JUnit. Tests are written using classes that inherit from `unittest.TestCase`. While it is reliable and widely used, it often requires more boilerplate code compared to Pytest.

### Why Pytest Was Chosen

Pytest was selected for this project because it provides a **simpler syntax**, **better readability**, and **automatic test discovery**. These features make it especially suitable for small projects and educational assignments where clarity and ease of use are important.
