# data-engineering-assignment-python
Data engineering assignment to analyse and cleanse data quality issues in a dataset

=====
Parse njson File
=====

This is short guide to setup the system and environment/dependencies to run the njson parse function.

Project Structure
-----------------
The util function that parses the njson file is present in ``util_func`` folder.

Environment
-----------------
The virtual environment needed to install the dependencies is included in this project.
The folder ``venv`` has the venv environment.

To activate environment

.. code-block:: sh

  # enter venv folder
  cd venv

  # activate the environment by running activate
  # this may differ based on the os
  # on MAC

  . venv/bin/activate

Python Library Dependencies
-----------------------
The requirements file in the project has list of dependencies that are used by ``util_func``.

.. code-block:: sh

  pip install -r requirements.txt

Running the Application
-----------------------
Running the main application calls the ``parse_njson_file`` function  that has default file name configured as an input.

.. code-block:: sh

  python run.py


Running Jupyter Notebook
-----------------------
Run Jupyter Notebook
.. code-block:: sh

  jupyter notebook


Jupyter Notebook
-----------------------
Jupyter notebook has all the code that can be executed cell by cell to see the transformation as the data is processed.

Jupyter notebook is located in ``notebook`` folder.


Running the application with new njson file
-----------------------
The function can be run with a new nsjon file by copying the njson file to the root folder.
Rename the file name ``discoveries.njson`` in the main function.
Similarly, copy the new file to ``notebook`` folder and modify the name in the notebook.


Data Profile
-----------------------
The data is profiled using the ``pandas-profiling`` library that provides stats relating to the data.

Based on the profiled data, data is cleansed and transformed.

The stats relating to discoveries.njson can be found in the jupyter notebook.
