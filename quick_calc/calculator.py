class Calculator:
    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the division of two numbers.
        Raises ValueError if division by zero is attempted.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def clear(self):
        """Reset value to zero."""
        return 0