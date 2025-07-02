Usage Guide
===========

Installation
------------

Install the latest release from PyPI:

.. code-block:: bash

   pip install spliit-client

Or install the development version from source:

.. code-block:: bash

   git clone https://github.com/abg0148/spliit_client.git
   cd spliit_client
   pip install -e .

Basic Usage
-----------

.. code-block:: python

   from spliit_client import Spliit, SplitMode

   # Create a new group
   group = Spliit.create_group(
       name="Trip to Paris",
       currency="$",
       participants=[{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
   )

   # Get participant IDs
   participants = group.get_participants()
   alice_id = participants["Alice"]

   # Add an expense
   group.add_expense(
       title="Dinner",
       amount=6000,  # $60.00
       paid_by=alice_id,
       paid_for=[(alice_id, 1), (participants["Bob"], 1), (participants["Charlie"], 1)],
       split_mode=SplitMode.EVENLY,
       notes="Dinner at a restaurant",
       category=8  # Dining Out
   )

   # Retrieve all expenses
   expenses = group.get_expenses()
   for expense in expenses:
       print(f"{expense['title']}: ${expense['amount']/100:.2f}")

Advanced Examples
-----------------

Split by percentage:

.. code-block:: python

   group.add_expense(
       title="Groceries",
       amount=3000,  # $30.00
       paid_by=alice_id,
       paid_for=[(alice_id, 70), (participants["Bob"], 30)],
       split_mode=SplitMode.BY_PERCENTAGE,
       category=9  # Groceries
   )

Split by exact amounts:

.. code-block:: python

   group.add_expense(
       title="Movie tickets",
       amount=3000,  # $30.00
       paid_by=alice_id,
       paid_for=[(alice_id, 1500), (participants["Bob"], 1500)],
       split_mode=SplitMode.BY_AMOUNT,
       category=4  # Movies
   )

See :doc:`api` for the full API reference. 