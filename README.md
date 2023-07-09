# dataclass_codec

dataclass_codec is a Python library that provides encoding and decoding functions for dictionaries. It allows you to easily convert Python dictionaries to JSON-compatible data structures and vice versa.

## Installation

You can install dataclass_codec using pip:

```
pip install dataclass-codec
```

## Usage

dataclass_codec is designed to work with dictionaries, which are a common way to represent structured data in Python. You can use dataclass_codec to decode dictionaries into Python dataclasses.

Here is an example of how to use dataclass_codec with dataclasses:

```python
from dataclasses import dataclass
from dataclass_codec import decode

# Define a dataclass
@dataclass
class Person:
    name: str
    age: int
    city: str

# Define a dictionary representing a person
person_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Decode the dictionary into a Person object
person = decode(person_dict, Person)

# Access the attributes of the Person object
print(person.name)  # Output: John
print(person.age)   # Output: 30
print(person.city)  # Output: New York
```

In the above example, we define a dataclass `Person` using the `@dataclass` decorator. The `Person` dataclass has three attributes: `name`, `age`, and `city`. We then have a dictionary `person_dict` representing a person. By using the `decode` function from dataclass_codec, we can easily convert the dictionary into a Person object. Finally, we access the attributes of the Person object and print their values.

## Advanced Features

### Nested Dictionaries

You can use dataclass_codec to decode dictionaries that have nested dictionaries as values. The nested dictionaries will be decoded into nested dataclass objects.

```python
from dataclasses import dataclass
from dataclass_codec import decode

# Define a nested dataclass
@dataclass
class Address:
    street: str
    city: str
    zip_code: str

# Define a dataclass with a nested dataclass
@dataclass
class Person:
    name: str
    age: int
    address: Address

# Define a dictionary with a nested address dictionary
person_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip_code": "10001"
    }
}

# Decode the dictionary into a Person object
person = decode(person_dict, Person)

# Access the attributes of the Person object and its nested Address object
print(person.name)                      # Output: John
print(person.age)                       # Output: 30
print(person.address.street)            # Output: 123 Main St
print(person.address.city)              # Output: New York
print(person.address.zip_code)          # Output: 10001
```

In this example, we define a dataclass `Address` representing an address with attributes `street`, `city`, and `zip_code`. We also define a dataclass `Person` with attributes `name`, `age`, and `address`, where `address` is an instance of the `Address` dataclass. The dictionary `person_dict` contains a nested dictionary for the address. By using the `decode` function, we can easily convert the dictionary into a Person object with a nested Address object. Finally, we access the attributes of the Person object and its nested Address object and print their values.

Remember to define all your dataclasses using the `@dataclass` decorator for dataclass_codec to work correctly.

### Decoding a Dictionary with Generic List

```python
from dataclasses import dataclass
from dataclass_codec import decode
from typing import List, TypeVar

# Define a TypeVar
T = TypeVar('T')

# Define a generic dataclass
@dataclass
class Container:
    items: List[T]

# Define a dictionary with a list of items
container_dict = {
    "items": [1, 2, 3, 4, 5]
}

# Decode the dictionary into a Container object
container = decode(container_dict, Container[int])

# Access the attributes of the Container object
print(container.items)  # Output: [1, 2, 3, 4, 5]
```

In this example, we showcase how to decode a dictionary containing a list of generic types. We define a generic dataclass `Container` with a single attribute `items`, which is a list of generic type `T`. The dictionary `container_dict` contains a list of items `[1, 2, 3, 4, 5]`. By using the `decode` function with the type `Container[int]`, we can convert the dictionary into a `Container` object, where the list of items is preserved.

Feel free to include this example in your readme to demonstrate how to decode a dictionary with a generic list into a corresponding dataclass object.

## Conclusion

dataclass_codec is a powerful library for decoding dictionaries into dataclasses in Python. It provides an easy and efficient way to convert data between Python objects and JSON-compatible formats. Whether you need to deserialize data for processing or manipulation purposes, dataclass_codec can simplify the process and save you time. Give it a try and see how it can enhance your data manipulation workflow.
