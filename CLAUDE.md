# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a collection of Python utility scripts for business tasks, organized by domain:
- `archive/` - Archive handling utilities (tar.gz extraction)
- `excel/` - Excel data processing tools (column comparison and sorting)
- `sql/` - SQL utilities (placeholder replacement)

## Dependencies

Install dependencies with:
```bash
pip install -r requirements.txt
```

Key dependencies include pandas, openpyxl, and xlrd for Excel processing.

## Script Usage

Each script is designed to be run independently:

### Archive Tools
```bash
python archive/extract_targz.py <path_to_targz_dir>
```
Extracts all tar.gz files in a directory to `_extracted/<filename>/` subdirectories.

### Excel Tools
```bash
python excel/sort_pairs.py
```
Interactive script that compares two Excel columns (A and B), finding common values and unique values in each column.

### SQL Tools
```bash
python sql/replace_query_params.py
```
Interactive script that replaces SQL placeholders (?) with provided parameters.

## Code Architecture

- Scripts follow a common pattern: utility function + interactive `__main__` block
- Use pathlib.Path for file operations where applicable
- Functions are designed to be importable and reusable
- Input validation and error handling included in command-line interfaces

## Testing

The `test/` directory contains test data and extraction examples. No formal test framework is currently in use.