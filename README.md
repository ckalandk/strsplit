# strsplit

![Test & Publish](https://github.com/ckalandk/strsplit/actions/workflows/test-and-publish.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/strsplit)
![Python Version](https://img.shields.io/pypi/pyversions/strsplit)

A flexible string splitting utility for Python that allows splitting by different strategies and filtering the results using predicates.
This package is inspired by the abseil StrSplit library.

## Features

- Split by a delimiter string (`SplitByStr`)
- Split by fixed length chunks (`SplitByLength`)
- Split by any character in a set (`SplitByAnyChar`)
- Control maximum splits with `maxsplit` parameter (default `-1` = no limit)
- Filter out substrings via a predicate function in the main `split` function

## Installation

```bash
pip install strsplit
