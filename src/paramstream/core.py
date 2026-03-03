# %% Set up ----

# Import required libraries
from typing import Optional
import pandas as pd
from rpy2.robjects.conversion import localconverter, rpy2py
from rpy2.robjects.pandas2ri import converter
from ._conversion import _get_paramstream_r, _py_to_r

# %% get_params_log_id_from_dict() ----

def get_params_log_id_from_dict(params_dict: dict, in_dir_path: str) -> str:
  
  """Get log ID from parameters dict
  
  This function is a Python wrapper around param.stream::get_params_log_id_from_list().
  It converts Python objects to their R equivalents before calling the underlying R function.

  Parameters
  ----------
  params_dict: dict
      Dictionary mapping parameter names to values. Values must be scalars (str, int, float, bool), lists of homogeneous scalars, or None.
  in_dir_path: str
      Path to the directory containing the params.log file.

  Returns
  -------
  str
      The log ID matching <params_list> in the params.log file at <in_dir_path>.
  
  Raises
  ------
  TypeError
      If <params_dict> contains unsupported value types.
  rpy2.rinterface_lib.embedded.RRuntimeError
      If the underlying R function raises an error.
      
  """
  
  _paramstream_r = _get_paramstream_r()
  
  params_list_r = _py_to_r(params_dict)
  in_dir_path_r = _py_to_r(in_dir_path)
  
  output_r = _paramstream_r.get_params_log_id_from_list(
    params_list=params_list_r, 
    in_dir_path=in_dir_path_r
    )
    
  return output_r[0]

# %% write_params_log_from_dict() ----

def write_params_log_from_dict(params_dict: dict, out_dir_path: str, params_log_table: bool = True) -> Optional[pd.DataFrame]:
  
  """Write parameters log file from parameters dict
  
  This function is a Python wrapper around param.stream::write_params_log_from_list().
  It converts Python objects to their R equivalents before calling the underlying R function.

  Parameters
  ----------
  params_dict: dict
      Dictionary mapping parameter names to values. Values must be scalars (str, int, float, bool), lists of homogeneous scalars, or None.
  out_dir_path: str
      Path to the directory where the params.log file should be written.
  params_log_table: bool, default=True
      If True, return the params log table as a pandas DataFrame.
      If False, no value is returned.

  Returns
  -------
  pd.DataFrame or None
      The params log table if <params_log_table> is True.
  
  Raises
  ------
  TypeError
      If <params_dict> contains unsupported value types.
  rpy2.rinterface_lib.embedded.RRuntimeError
      If the underlying R function raises an error.
      
  """
  _paramstream_r = _get_paramstream_r()
  
  params_list_r = _py_to_r(params_dict)
  out_dir_path_r = _py_to_r(out_dir_path)
  params_log_table_r = _py_to_r(params_log_table)
  
  output_r = _paramstream_r.write_params_log_from_list(
    params_list=params_list_r, 
    out_dir_path=out_dir_path_r,
    params_log_table=params_log_table_r
    )
  
  if params_log_table is False:
    
    return
  
  else:
    
    with localconverter(converter):
      
      return rpy2py(output_r)

# %% get_params_log_table() ----

def get_params_log_table(log_id: str, in_dir_path: str) -> pd.DataFrame:
  
  """Get parameters log table from log ID
  
  This function is a Python wrapper around param.stream::get_params_log_table().
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
  
  output_r = _paramstream_r.get_params_log_table(
    log_id=log_id_r, 
    in_dir_path=in_dir_path_r
    )
  
  with localconverter(converter):
    
    return rpy2py(output_r)

