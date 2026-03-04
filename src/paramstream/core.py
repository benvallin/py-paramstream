# %% Set up ----

# Import required libraries
from typing import Optional
import pandas as pd
from rpy2.robjects.conversion import localconverter, rpy2py
from rpy2.robjects.pandas2ri import converter
from ._conversion import _get_paramstream_r, _py_to_r

# %% get_param_log_id() ----

def get_param_log_id(param_dict: dict, in_dir_path: str) -> str:
  
  """Get log ID from parameter dict
  
  This function is a Python wrapper around paramstream::get_param_log_id().
  It converts Python objects to their R equivalents before calling the underlying R function.

  Parameters
  ----------
  param_dict: dict
      Dictionary mapping parameter names to values. Values must be scalars (str, int, float, bool), lists of homogeneous scalars, or None.
  in_dir_path: str
      Path to the directory containing the params.log file.

  Returns
  -------
  str
      The log ID matching <param_list> in the params.log file at <in_dir_path>.
  
  Raises
  ------
  TypeError
      If <param_dict> contains unsupported value types.
  rpy2.rinterface_lib.embedded.RRuntimeError
      If the underlying R function raises an error.
      
  """
  
  _paramstream_r = _get_paramstream_r()
  
  param_list_r = _py_to_r(param_dict)
  in_dir_path_r = _py_to_r(in_dir_path)
  
  output_r = _paramstream_r.get_param_log_id(
    param_list=param_list_r, 
    in_dir_path=in_dir_path_r
    )
    
  return output_r[0]

# %% write_param_log() ----

def write_param_log(param_dict: dict, out_dir_path: str, param_log_table: bool = True) -> Optional[pd.DataFrame]:
  
  """Write parameter log file from parameter dict
  
  This function is a Python wrapper around paramstream::write_param_log().
  It converts Python objects to their R equivalents before calling the underlying R function.

  Parameters
  ----------
  param_dict: dict
      Dictionary mapping parameter names to values. Values must be scalars (str, int, float, bool), lists of homogeneous scalars, or None.
  out_dir_path: str
      Path to the directory where the params.log file should be written.
  param_log_table: bool, default=True
      If True, return the params log table as a pandas DataFrame.
      If False, no value is returned.

  Returns
  -------
  pd.DataFrame or None
      The params log table if <param_log_table> is True.
  
  Raises
  ------
  TypeError
      If <param_dict> contains unsupported value types.
  rpy2.rinterface_lib.embedded.RRuntimeError
      If the underlying R function raises an error.
      
  """
  _paramstream_r = _get_paramstream_r()
  
  param_list_r = _py_to_r(param_dict)
  out_dir_path_r = _py_to_r(out_dir_path)
  param_log_table_r = _py_to_r(param_log_table)
  
  output_r = _paramstream_r.write_param_log(
    param_list=param_list_r, 
    out_dir_path=out_dir_path_r,
    param_log_table=param_log_table_r
    )
  
  if param_log_table is False:
    
    return
  
  else:
    
    with localconverter(converter):
      
      return rpy2py(output_r)

# %% get_param_log_table() ----

def get_param_log_table(log_id: str, in_dir_path: str) -> pd.DataFrame:
  
  """Get parameter log table from log ID
  
  This function is a Python wrapper around paramstream::get_param_log_table().
  It converts Python objects to their R equivalents before calling the underlying R function.

  Parameters
  ----------
  log_id: str
      log ID for which the log table should be returned.
  in_dir_path: str
      Path to the directory containing the params.log file.

  Returns
  -------
  pd.DataFrame
      The params log table matching the input <log_id>.
  
  Raises
  ------
  rpy2.rinterface_lib.embedded.RRuntimeError
      If the underlying R function raises an error.
      
  """
  
  _paramstream_r = _get_paramstream_r()
  
  log_id_r = _py_to_r(log_id)
  in_dir_path_r = _py_to_r(in_dir_path)
  
  output_r = _paramstream_r.get_param_log_table(
    log_id=log_id_r, 
    in_dir_path=in_dir_path_r
    )
  
  with localconverter(converter):
    
    return rpy2py(output_r)

