# Algorithms for trajectory similarity measures
This repo contains some algorithms retrieved from literature and implemented
in C++ and Python, with the idea of performing analysis and benchmarking in
order to help us gain insights to build a Python library that will work with
trajectories (in GeoJSON format) to mainly find similarity measures between
them.

## Usage
For building the C++ libraries that the `src` directory will contain the
`Makefile` needs to be modified and executed:

```
make
```

Notice that this should create the dynamic library that will be used by the
Python library `cppyy`.

```sh
g++ -fPIC -Wall -o <Dynamic library with .so extension> <C++ file>
```

`make clean` will clean compiled files.

> For future development we should consider using `cmake`.

### Python integration
To integrate with python, `requirements.txt` should be installed via pip:

```sh
pip install -r requirements.txt
```

Having done this now you can import `cppyy` into your code:

```python
import cppyy
cppyy.include('src/your_header_file.h') # Enables calls
cppyy.load_library('your_dynamic_lib.so') # Executes calls
lib = cppyy.gbl # To shorten library calls, i.e.: lib.your_function()
```

> `cppyy` will meant to be used only for testing!

### Jupyter notebooks
Install `requirements-jupyter.txt` dependencies:

```sh
pip install -r requirements-jupyter.txt
```

This will contain `requirements.txt` dependencies. Make sure to match same
dependencies versions! In order not to get versions conflicts.

#### Hosting jupyter lab
In order to view, modify or work with the notebooks you only need to run:

```sh
jupyter lab
```

This will open the jupyter host in your default browser.

## Directory structure

Below find the proposed structure for this repository:

    .
    ├── .github/workflows       # Github Actions
    ├── docs                    # Sphinx documentation generator directory
    ├── examples                # Some useful examples
    ├── notebooks               # Jupyter notebooks
    ├── similarity_measures_b106# The python test module (library)
    ├── src                     # C++ source code
    └── tests                   # Tests (C++/Python) to ensure expected outcomes
