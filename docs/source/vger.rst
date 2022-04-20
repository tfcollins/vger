Vger Doc Tools
--------------

Library API for vger doc generation tools.

.. raw:: html

   <hr>

Command-Line Interface
^^^^^^^^^^^^^^^^^^^^^^

The vger library is primarily designed to be used through a CLI interface. Each source project (hdl,no-os,linux, ...) will have its own command to parse and generate doc pages for Sphinx. 

To get the CLI run:

.. code:: bash
   
   git clone https://github.com/tfcollins/vger.git
   cd vger
   pip install .

Now you will have access to the base CLI command **vger**. **vger** as the following sub-commands per source project:

.. click:: vger.cli:cli
   :prog: vger
   :nested: full


HDL Source
^^^^^^^^^^

.. automodule:: vger.hdl
    :members:

.. raw:: html

   <hr>

Linux Source
^^^^^^^^^^^^
