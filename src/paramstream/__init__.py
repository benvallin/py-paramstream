"""

Python wrapper for the R package `paramstream`.

"""

from .core import (
  get_param_log_id,
  write_param_log,
  get_param_log_table
  )

__all__ = [
  'get_param_log_id',
  'write_param_log',
  'get_param_log_table'
  ]

from importlib.metadata import version, PackageNotFoundError

try:
  
  __version__ = version('paramstream')
  
except PackageNotFoundError:
  
  __version__ = 'unknown'