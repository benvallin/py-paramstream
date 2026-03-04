# ***paramstream***

**Parameter-Based Run Tracking for Reproducible Data Analysis Workflows**

A lightweight parameter-to-run identifier registry for deterministic result storage and retrieval in data analysis workflows.


---


## Description

`paramstream` provides utilities for recording analysis parameters and generating unique, parameter-derived run identifiers. Results can be stored using these identifiers and later retrieved by supplying the same parameter set. This enables lightweight reproducibility and consistent tracking of analysis outputs across workflow stages.

This package is a Python wrapper around the R package `paramstream`.


---


## Installation

You can install `py-paramstream` from PyPI with:

```bash
pip install py-paramstream
```


---


## System requirements

- Python >= 3.9
- R >= 4.0
- R package `paramstream` installed

You can install the R package `paramstream` from [GitHub](https://github.com/) with:

```r
remotes::install_github("benvallin/paramstream")
```


---
