.. image:: https://raw.githubusercontent.com/abg0148/spliit_client/main/docs/_static/logo.png
   :alt: Spliit Client Logo
   :align: center
   :width: 200px

Spliit Client Documentation
==========================

Welcome to the **Spliit Client** documentation!

A professional Python client for the Spliit API, enabling seamless group expense sharing and management. Open source, MIT licensed, and production-ready.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   cli
   api
   contributing

Quickstart
----------

Install from PyPI:

.. code-block:: bash

   pip install spliit-client

Create a group and add an expense:

.. code-block:: python

   from spliit_client import Spliit, SplitMode

   group = Spliit.create_group(
       name="Trip to Paris",
       currency="$",
       participants=[{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
   )
   participants = group.get_participants()
   alice_id = participants["Alice"]
   group.add_expense(
       title="Dinner",
       amount=6000,
       paid_by=alice_id,
       paid_for=[(alice_id, 1), (participants["Bob"], 1), (participants["Charlie"], 1)],
       split_mode=SplitMode.EVENLY,
       notes="Dinner at a restaurant",
       category=8
   )

For more, see :doc:`usage` and :doc:`cli`.

.. automodule:: spliit_client
   :members:
   :undoc-members:
   :show-inheritance: 