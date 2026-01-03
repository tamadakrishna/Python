"""
Python performs these steps internally:

    1. Searches for my_module
    2. Loads the module into memory
    3. Compiles it into bytecode (if needed)
    4. Executes the module’s top-level code
    5. Stores it in sys.modules
    6. Creates __pycache__ for faster future imports
A module is loaded only once, even if imported multiple times.


sys.modules – Module Cache in Memory
    1. Dictionary of module names → module objects
    2. Prevents duplicate loading
    3. Improves performance


Module Search Order (Very Important)

When importing a module, Python searches in this order:

    1. Current directory (root project folder)
    2. PYTHONPATH
    3. Standard library
    4. Site-packages (installed modules)

Check search paths:
    import sys
    print(sys.path)

"""