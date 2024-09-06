from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        "dtw_module",                         
        sources=["dtw_module.pyx", "dtw.cpp", "algoritmos.cpp"],  
        language="c++",                       
        include_dirs=[numpy.get_include()],   
    )
]

setup(
    name="dtw_module",
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
)

