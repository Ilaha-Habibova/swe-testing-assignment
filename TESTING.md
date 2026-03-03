# Testing Strategy – Quick-Calc

## Overview

Software testing is an important part of the software development process.
According to the course lecture, testing helps ensure that software meets requirements, works correctly, and reduces errors throughout the Software Development Life Cycle (SDLC).

The Quick-Calc project applies testing to verify that the calculator operations behave correctly and produce accurate results.

Testing in this project was implemented using the **Pytest** framework.

---

# Testing Strategy

## What Was Tested

The tests focus on verifying the correctness of the calculator’s core functionality:

- Addition
- Subtraction
- Multiplication
- Division
- Division by zero handling
- Negative numbers
- Decimal numbers
- Large numbers
- Clear/reset functionality

Unit tests were used to test individual functions, while integration tests verify how the calculator behaves when operations are used together.

---

## What Was Not Tested

Some aspects were intentionally not tested in this project:

- Performance testing
- Graphical user interface testing
- Security testing

These were excluded because the goal of this project is to demonstrate **core testing concepts and functional correctness**, rather than full production-level testing.

---

# Lecture Concepts

## Testing Pyramid

The test suite follows the **Testing Pyramid principle**, where a project contains many unit tests and fewer integration tests.

In this project:

- **8 Unit Tests** verify individual calculator operations.
- **2 Integration Tests** verify interactions between different components.

This structure reflects the testing pyramid idea where small, fast unit tests form the base and larger integration tests are fewer.

---

## Black-Box vs White-Box Testing

### White-Box Testing

The **unit tests** represent white-box testing because they directly test the internal logic of the calculator functions.

For example, the addition and multiplication tests directly verify the behavior of specific functions.

### Black-Box Testing

The **integration tests** are closer to black-box testing because they simulate user behavior without focusing on the internal implementation of the functions.

---

## Functional vs Non-Functional Testing

### Functional Testing

This project focuses mainly on **functional testing**, which verifies that the calculator performs the correct operations and returns expected results.

Examples include:

- Correct addition and subtraction
- Correct multiplication and division
- Proper handling of division by zero

### Non-Functional Testing

Non-functional aspects such as performance, scalability, and usability were not tested because they are outside the scope of this assignment.

---

## Regression Testing

The test suite also supports **regression testing**.

If future changes are made to the calculator code, running the test suite again will ensure that existing functionality still works correctly.

For example, if a future update accidentally breaks the division logic, the corresponding test will fail and immediately alert the developer.

---

# Test Results Summary

| Test Name                  | Type        | Status |
| -------------------------- | ----------- | ------ |
| test_add                   | Unit        | Pass   |
| test_subtract              | Unit        | Pass   |
| test_multiply              | Unit        | Pass   |
| test_divide                | Unit        | Pass   |
| test_divide_by_zero        | Unit        | Pass   |
| test_negative_numbers      | Unit        | Pass   |
| test_decimal_numbers       | Unit        | Pass   |
| test_large_numbers         | Unit        | Pass   |
| test_full_addition_flow    | Integration | Pass   |
| test_clear_after_operation | Integration | Pass   |

All tests were executed using **Pytest**, and all tests passed successfully.
