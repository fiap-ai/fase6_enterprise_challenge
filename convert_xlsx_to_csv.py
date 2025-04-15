#!/usr/bin/env python3
"""
Convert XLSX files to CSV

This script converts Excel (XLSX) files to CSV format.
It can be used to convert a single file or all files in a directory.
"""

import os
import sys
import pandas as pd
import argparse
from pathlib import Path

def convert_xlsx_to_csv(input_file, output_file=None, sheet_name=0, index=False, verbose=True):
    """
    Convert an Excel file to CSV.
    
    Parameters:
    -----------
    input_file : str
        Path to the input Excel file.
    output_file : str, optional
        Path to the output CSV file. If None, the output file will have the same name as the input file but with a .csv extension.
    sheet_name : str or int, optional
        Name or index of the sheet to convert. Default is 0 (first sheet).
    index : bool, optional
        Whether to include the index in the CSV file. Default is False.
    verbose : bool, optional
        Whether to print information about the conversion. Default is True.
    
    Returns:
    --------
    str
        Path to the output CSV file.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.csv'
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read Excel file
    if verbose:
        print(f"Reading Excel file: {input_file}")
    
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    
    # Write CSV file
    if verbose:
        print(f"Writing CSV file: {output_file}")
    
    df.to_csv(output_file, index=index)
    
    if verbose:
        print(f"Conversion complete: {input_file} -> {output_file}")
        print(f"Number of rows: {df.shape[0]}")
        print(f"Number of columns: {df.shape[1]}")
    
    return output_file

def convert_directory(input_dir, output_dir=None, sheet_name=0, index=False, verbose=True):
    """
    Convert all Excel files in a directory to CSV.
    
    Parameters:
    -----------
    input_dir : str
        Path to the input directory.
    output_dir : str, optional
        Path to the output directory. If None, the output files will be in the same directory as the input files.
    sheet_name : str or int, optional
        Name or index of the sheet to convert. Default is 0 (first sheet).
    index : bool, optional
        Whether to include the index in the CSV files. Default is False.
    verbose : bool, optional
        Whether to print information about the conversion. Default is True.
    
    Returns:
    --------
    list
        List of paths to the output CSV files.
    """
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    
    if output_dir is None:
        output_dir = input_dir
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get all Excel files in the input directory
    xlsx_files = [f for f in os.listdir(input_dir) if f.endswith('.xlsx')]
    
    if not xlsx_files:
        print(f"No Excel files found in {input_dir}")
        return []
    
    if verbose:
        print(f"Found {len(xlsx_files)} Excel files in {input_dir}")
    
    # Convert each Excel file to CSV
    output_files = []
    for xlsx_file in xlsx_files:
        input_file = os.path.join(input_dir, xlsx_file)
        output_file = os.path.join(output_dir, os.path.splitext(xlsx_file)[0] + '.csv')
        
        try:
            output_file = convert_xlsx_to_csv(input_file, output_file, sheet_name, index, verbose)
            output_files.append(output_file)
        except Exception as e:
            print(f"Error converting {input_file}: {e}")
    
    if verbose:
        print(f"Converted {len(output_files)} Excel files to CSV")
    
    return output_files

def main():
    """
    Main function.
    """
    parser = argparse.ArgumentParser(description='Convert Excel (XLSX) files to CSV format.')
    parser.add_argument('input', help='Input file or directory')
    parser.add_argument('-o', '--output', help='Output file or directory')
    parser.add_argument('-s', '--sheet', default=0, help='Sheet name or index (default: 0)')
    parser.add_argument('-i', '--index', action='store_true', help='Include index in CSV file')
    parser.add_argument('-q', '--quiet', action='store_true', help='Suppress output')
    
    args = parser.parse_args()
    
    verbose = not args.quiet
    
    if os.path.isdir(args.input):
        # Convert all Excel files in the directory
        convert_directory(args.input, args.output, args.sheet, args.index, verbose)
    else:
        # Convert a single Excel file
        convert_xlsx_to_csv(args.input, args.output, args.sheet, args.index, verbose)

if __name__ == '__main__':
    main()
