# Algorithms for trajectory similarity measures
This repo contains some algorithms retrieved from literature and implemented in C++ and Python, with the idea of performing analysis and benchmarking in order to help us gain insights to build a Python library that will work with trajectories (in GeoJSON format) to mainly find similarity measures between them.

## Usage
For building the C++ libraries that the `src` directory will contain the `Makefile` needs to be modified and executed:

```
make
```

Notice that this should compile an object file and then link this to a dynamic library that will be used by the Python library `cppyy`.

```sh
g++ -fPIC -Wall <C++ file> -o <Object file> # Compiles object file
g++ -shared -o <Dynamic library> <Object file> # Links dynamic library
```

`make clean` will clean compiled files.

> For future development we should consider using `cmake`.

### Python integration
To integrate with python, `requirements.txt` should be installed via pip:

```sh
pip install -r requirements.txt
```

Having done this now you can import `cppyy` into your code:

```sh
import cppyy
cppyy.include('src/your_header_file.h') # Enables calls
cppyy.load_library('build/your_dynamic_lib.so') # Executes calls
lib = cppyy.gbl # To shorten library calls, i.e.: lib.your_function()
```

## Tests

Run the tests contained in the `test` directory and you should get the following output if everything was set up correctly:

```sh
7.280109889280518 # For trajectories with different length
2.8284271247461903 # For trajectories with same length
```

## Directory structure

    .
    ├── build                   # Compiled files (not included in GitHub)
    ├── examples                # More elaborated examples
    ├── src                     # C++ source code
    └── tests                   # Tests (C++/Python) to ensure expected outcomes
