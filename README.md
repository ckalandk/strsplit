# strsplit

A flexible string splitting utility for Python that allows splitting by different strategies and filtering the results using predicates.

## Features

- Split by a delimiter string (`SplitByStr`)
- Split by fixed length chunks (`SplitByLength`)
- Split by any character in a set (`SplitByAnyChar`)
- Control maximum splits with `maxsplit` parameter (default `-1` = no limit)
- Filter out substrings via a predicate function in the main `split` function

## Installation

```bash
pip install strsplit
