Command-Line Interface (CLI)
==========================

Spliit Client provides a convenient CLI for common operations.

Usage
-----

.. code-block:: bash

   spliit [COMMAND] [OPTIONS]

Available Commands
------------------

- ``create-group``: Create a new group
- ``list-categories``: List all available categories
- ``version``: Show version information

Examples
--------

Create a new group:

.. code-block:: bash

   spliit create-group "Trip to Paris" --currency "$" --participants Alice Bob Charlie

List all categories:

.. code-block:: bash

   spliit list-categories

Show version:

.. code-block:: bash

   spliit version

For more details, run ``spliit [COMMAND] --help``. 