# Custom Array Implementation in Python

This folder contains a Python implementation of a custom array data structure. This custom array mimics the behavior of Python's built-in list but provides an insight into how dynamic arrays can be implemented and managed.

## Features

- **Dynamic Resizing**: Automatically resizes when capacity is reached, ensuring efficient space allocation.
- **Index-Based Access**: Allows for O(1) access and assignment operations via indices.
- **Boundary Checks**: Implements boundary checking to prevent out-of-bounds errors.
- **Iteration Support**: Compatible with Python's iteration protocols.

## Complexity Analysis

- **Space Complexity**: O(n), where n is the number of elements in the array.
- **Time Complexity**:
  - **Access**: O(1) - Direct access via index.
  - **Append**: Amortized O(1) - Constant time on average when appending elements.
  - **Remove**: O(n) - Requires shifting elements after the removal index.
  - **Resize**: O(n) - Involves creating a new array and copying elements.

## Usage

Here is a basic example of how to use the CustomArray class:

```python
custom_array = CustomArray()

# Append elements
custom_array.append(10)
custom_array.append(20)
custom_array.append(30)

# Access elements
print(f"Element at index 1: {custom_array[1]}")

# Modify elements
custom_array[1] = 25

# Remove elements
custom_array.remove(1)
