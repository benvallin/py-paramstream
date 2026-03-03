"""
Python wrapper for the R package `param.stream`.
"""

from .core import (
  get_params_log_id_from_dict,
  write_params_log_from_dict,
  get_params_log_table
  )

__all__ = [
  'get_params_log_id_from_dict',
  'write_params_log_from_dict',
  'get_params_log_table'
  ]

from importlib.metadata import version, PackageNotFoundError

try:
  
  __version__ = version('paramstream')
  
except PackageNotFoundError:
  
  __version__ = 'unknown'