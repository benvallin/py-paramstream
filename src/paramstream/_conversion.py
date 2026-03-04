# %% Set up ----

# Import required libraries
from typing import Union, TypeAlias
import pandas as pd
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import StrVector, BoolVector, FloatVector, IntVector, ListVector
from rpy2.robjects import NULL
from rpy2.robjects import RObject
from rpy2.rinterface import NULLType

# %% _get_paramstream_r() ----

def _get_paramstream_r():
  
  try:
    
    return importr('paramstream')
  
  except Exception as e:
    
    raise ImportError(
      "R package 'paramstream' is not installed or R is not available."
      ) from e
    
        
# %% _py_to_r() ----

PyScalar: TypeAlias = Union[str, int, float, bool]
PyValue: TypeAlias = Union[
    None,
    PyScalar,
    list['PyValue'],
    dict[str, 'PyValue'],
]

def _py_to_r(obj: PyValue) -> Union[RObject, NULLType]:
  
  """Convert a supported Python object into the corresponding rpy2 R object
  
  Supported conversions:
    None            -> R NULL
    bool            -> logical vector (length 1)
    str             -> character vector (length 1)
    int             -> integer vector (length 1)
    float           -> numeric vector (length 1)
    list[str]       -> character vector
    list[bool]      -> logical vector
    list[int]       -> integer vector
    list[float]     -> numeric vector
    list[mixed]     -> R list (recursive conversion)
    dict            -> named R list (recursive conversion)

  Lists and dictionaries are converted recursively.

  Parameters
  ----------
  obj : Any 
      Python object to convert.

  Returns
  -------
  rpy2.robjects.RObject or rpy2.robjects.NULL
      Equivalent R representation.

  Raises
  ------
  TypeError
      If the object type is not supported.
      
  """
  
  if obj is None:
    
    return NULL
  
  if isinstance(obj, bool):
    
    return BoolVector([obj])

  if isinstance(obj, str):      
    
    return StrVector([obj])
  
  if isinstance(obj, int):
    
    return IntVector([obj])
  
  if isinstance(obj, float):
    
    return FloatVector([obj])
  
  if isinstance(obj, list):
    
    if len(obj) == 0:
      
      return ListVector({})
    
    if all(isinstance(x, str) for x in obj):
      
      return StrVector(obj)
    
    if all(isinstance(x, bool) for x in obj):
      
      return BoolVector(obj)
    
    if all(isinstance(x, int) for x in obj):
      
      return IntVector(obj)
    
    if all(isinstance(x, float) for x in obj):
      
      return FloatVector(obj)
    
    return ListVector({str(i): _py_to_r(v) for i, v in enumerate(obj)})
  
  if isinstance(obj, dict):
    
    return ListVector({k: _py_to_r(v) for k, v in obj.items()})
  
  raise TypeError(f'Unsupported type: {type(obj)}')
