# Spliit Client

[![PyPI version](https://badge.fury.io/py/spliit_client.svg)](https://badge.fury.io/py/spliit_client)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python client for the [Spliit API](https://spliit.app) - a group expense sharing platform. Easily create groups, manage participants, and add or retrieve expenses programmatically.

## Features

- ✅ Create and manage expense groups
- ✅ Add participants to groups
- ✅ Create, retrieve, and delete expenses
- ✅ Support for multiple split modes (evenly, by shares, by percentage, by amount)
- ✅ Comprehensive expense categories
- ✅ Command-line interface
- ✅ Type hints and comprehensive documentation
- ✅ Error handling and validation

## Installation

### From PyPI (Recommended)

```bash
pip install spliit_client
```

### From Source

```bash
git clone https://github.com/yourusername/spliit_client.git
cd spliit_client
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/yourusername/spliit_client.git
cd spliit_client
pip install -e ".[dev]"
```

## Quick Start

### Basic Usage

```python
from spliit_client import Spliit, SplitMode

# Create a new group
group = Spliit.create_group(
    name="Trip to Paris",
    currency="$",
    participants=[
        {"name": "Alice"},
        {"name": "Bob"},
        {"name": "Charlie"}
    ]
)

# Get participant IDs
participants = group.get_participants()
alice_id = participants["Alice"]

# Add an expense
expense_id = group.add_expense(
    title="Dinner",
    amount=6000,  # Amount in cents ($60.00)
    paid_by=alice_id,
    paid_for=[
        (alice_id, 1),
        (participants["Bob"], 1),
        (participants["Charlie"], 1)
    ],
    split_mode=SplitMode.EVENLY,
    notes="Dinner at a restaurant",
    category=8  # Dining Out
)

# Retrieve all expenses
expenses = group.get_expenses()
for expense in expenses:
    print(f"{expense['title']}: ${expense['amount']/100:.2f}")
```

### Command Line Interface

The package includes a CLI for common operations:

```bash
# Create a new group
spliit create-group "Trip to Paris" --currency "$" --participants Alice Bob Charlie

# List all available categories
spliit list-categories

# Show version
spliit version
```

## API Reference

### Spliit Class

The main client class for interacting with the Spliit API.

#### Class Methods

##### `create_group(name, currency="$", server_url=OFFICIAL_INSTANCE, participants=None)`

Create a new group and return a client instance for it.

**Parameters:**
- `name` (str): Name of the group
- `currency` (str): Currency symbol (default: "$")
- `server_url` (str): Spliit server URL (default: official instance)
- `participants` (List[Dict[str, str]]): List of participant dictionaries with "name" key

**Returns:**
- `Spliit`: Client instance for the created group

**Example:**
```python
group = Spliit.create_group(
    name="Weekend Trip",
    currency="€",
    participants=[{"name": "Alice"}, {"name": "Bob"}]
)
```

#### Instance Methods

##### `get_group()`

Get group details.

**Returns:**
- `Dict`: Group information including name, currency, and participants

##### `get_participants()`

Get all participants with their IDs.

**Returns:**
- `Dict[str, str]`: Mapping of participant names to their IDs

##### `get_username_id(name)`

Get participant ID by name.

**Parameters:**
- `name` (str): Participant name

**Returns:**
- `Optional[str]`: Participant ID or None if not found

##### `get_expenses()`

Get all expenses in the group.

**Returns:**
- `List[Dict]`: List of expense dictionaries

##### `get_expense(expense_id)`

Get details of a specific expense.

**Parameters:**
- `expense_id` (str): The ID of the expense to retrieve

**Returns:**
- `Dict`: Expense details

##### `add_expense(title, amount, paid_by, paid_for, split_mode=SplitMode.EVENLY, expense_date=None, notes="", category=0)`

Add a new expense to the group.

**Parameters:**
- `title` (str): Title of the expense
- `amount` (int): Amount in cents (e.g., 1350 for $13.50)
- `paid_by` (str): ID of the participant who paid
- `paid_for` (List[Tuple[str, int]]): List of (participant_id, shares) tuples
- `split_mode` (SplitMode): How to split the expense
- `expense_date` (Optional[datetime]): Date of the expense (defaults to current UTC time)
- `notes` (str): Optional notes for the expense
- `category` (int): Expense category ID

**Returns:**
- `str`: The expense ID

**Example:**
```python
expense_id = group.add_expense(
    title="Gas",
    amount=4500,  # $45.00
    paid_by=alice_id,
    paid_for=[(alice_id, 1), (bob_id, 1)],
    split_mode=SplitMode.EVENLY,
    category=31  # Gas/Fuel
)
```

##### `remove_expense(expense_id)`

Remove an expense from the group.

**Parameters:**
- `expense_id` (str): The ID of the expense to remove

**Returns:**
- `Dict`: Response data from the API

### SplitMode Enum

Available split modes for expenses:

- `SplitMode.EVENLY`: Split the expense evenly among participants
- `SplitMode.BY_SHARES`: Split by number of shares per participant
- `SplitMode.BY_PERCENTAGE`: Split by percentage
- `SplitMode.BY_AMOUNT`: Split by specific amounts

### CATEGORIES Dictionary

Predefined expense categories organized by group:

```python
CATEGORIES = {
    "Uncategorized": {"General": 0, "Payment": 1},
    "Entertainment": {"Entertainment": 2, "Games": 3, "Movies": 4, "Music": 5, "Sports": 6},
    "Food and Drink": {"Food and Drink": 7, "Dining Out": 8, "Groceries": 9, "Liquor": 10},
    "Home": {"Home": 11, "Electronics": 12, "Furniture": 13, "Household Supplies": 14, "Maintenance": 15, "Mortgage": 16, "Pets": 17, "Rent": 18, "Services": 19},
    "Life": {"Childcare": 20, "Clothing": 21, "Education": 22, "Gifts": 23, "Insurance": 24, "Medical Expenses": 25, "Taxes": 26},
    "Transportation": {"Transportation": 27, "Bicycle": 28, "Bus/Train": 29, "Car": 30, "Gas/Fuel": 31, "Hotel": 32, "Parking": 33, "Plane": 34, "Taxi": 35},
    "Utilities": {"Utilities": 36, "Cleaning": 37, "Electricity": 38, "Heat/Gas": 39, "Trash": 40, "TV/Phone/Internet": 41, "Water": 42}
}
```

## Examples

### Complete Example: Trip Expense Management

```python
from spliit_client import Spliit, SplitMode

# Create a group for a weekend trip
group = Spliit.create_group(
    name="Weekend Trip to Mountains",
    currency="$",
    participants=[
        {"name": "Alice"},
        {"name": "Bob"},
        {"name": "Charlie"},
        {"name": "Diana"}
    ]
)

# Get participant IDs
participants = group.get_participants()
alice_id = participants["Alice"]
bob_id = participants["Bob"]
charlie_id = participants["Charlie"]
diana_id = participants["Diana"]

# Add various expenses
expenses = []

# Gas for the trip (split evenly)
gas_expense = group.add_expense(
    title="Gas for the trip",
    amount=8000,  # $80.00
    paid_by=alice_id,
    paid_for=[(alice_id, 1), (bob_id, 1), (charlie_id, 1), (diana_id, 1)],
    split_mode=SplitMode.EVENLY,
    category=31  # Gas/Fuel
)
expenses.append(gas_expense)

# Hotel (split evenly)
hotel_expense = group.add_expense(
    title="Hotel room",
    amount=20000,  # $200.00
    paid_by=bob_id,
    paid_for=[(alice_id, 1), (bob_id, 1), (charlie_id, 1), (diana_id, 1)],
    split_mode=SplitMode.EVENLY,
    category=32  # Hotel
)
expenses.append(hotel_expense)

# Dinner (Alice and Bob paid, Charlie and Diana didn't eat)
dinner_expense = group.add_expense(
    title="Dinner at restaurant",
    amount=12000,  # $120.00
    paid_by=alice_id,
    paid_for=[(alice_id, 1), (bob_id, 1)],  # Only Alice and Bob
    split_mode=SplitMode.EVENLY,
    category=8  # Dining Out
)
expenses.append(dinner_expense)

# Get all expenses
all_expenses = group.get_expenses()
print(f"Total expenses: {len(all_expenses)}")
for expense in all_expenses:
    print(f"- {expense['title']}: ${expense['amount']/100:.2f}")
```

### Error Handling

```python
from spliit_client import Spliit
import requests

try:
    group = Spliit.create_group("Test Group")
    expenses = group.get_expenses()
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Development

### Setting up Development Environment

```bash
git clone https://github.com/yourusername/spliit_client.git
cd spliit_client
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=spliit_client

# Run specific test file
pytest tests/test_client.py
```

### Code Formatting

```bash
# Format code with black
black spliit_client tests

# Check code style
flake8 spliit_client tests

# Type checking
mypy spliit_client
```

### Building and Publishing

```bash
# Build package
python -m build

# Upload to PyPI (test)
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Spliit](https://spliit.app) for providing the expense sharing platform
- The Python community for excellent tools and libraries

## Support

If you encounter any issues or have questions:

1. Check the [documentation](https://github.com/yourusername/spliit_client#readme)
2. Search [existing issues](https://github.com/yourusername/spliit_client/issues)
3. Create a [new issue](https://github.com/yourusername/spliit_client/issues/new)

---

**Note:** This is an unofficial client for the Spliit API. It is not affiliated with or endorsed by Spliit. 