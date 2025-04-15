#!/usr/bin/env python3
"""
Test API Service

This script tests the API service by making requests to various APIs.
It can be run from the command line to test the API service without
having to run the Jupyter notebooks.
"""

import os
import sys
import argparse
import pandas as pd
from api_service import APIService, IBGEService

def test_ibge_api(verbose=True):
    """
    Test the IBGE API service.
    
    Args:
        verbose: Whether to print verbose output
    
    Returns:
        True if all tests pass, False otherwise
    """
    if verbose:
        print("Testing IBGE API Service...")
    
    # Create an instance of the IBGE service
    ibge_service = IBGEService(cache_enabled=True)
    
    # Test getting agricultural production data for Nova Friburgo
    if verbose:
        print("\nTesting agricultural production data for Nova Friburgo (3303401)...")
    nf_data = ibge_service.get_agricultural_production("3303401", 2000, 2023)
    if nf_data is not None:
        if verbose:
            print("Success! Got data for Nova Friburgo:")
            print(nf_data.head())
    else:
        if verbose:
            print("Failed to get data for Nova Friburgo.")
        return False
    
    # Test getting agricultural production data for Teresópolis
    if verbose:
        print("\nTesting agricultural production data for Teresópolis (3305802)...")
    t_data = ibge_service.get_agricultural_production("3305802", 2000, 2023)
    if t_data is not None:
        if verbose:
            print("Success! Got data for Teresópolis:")
            print(t_data.head())
    else:
        if verbose:
            print("Failed to get data for Teresópolis.")
        return False
    
    # Test getting census data for Nova Friburgo
    if verbose:
        print("\nTesting census data for Nova Friburgo (3303401)...")
    nf_census = ibge_service.get_census_data("3303401", 2006)
    if nf_census is not None:
        if verbose:
            print("Success! Got census data for Nova Friburgo:")
            print(nf_census)
    else:
        if verbose:
            print("Failed to get census data for Nova Friburgo.")
        return False
    
    if verbose:
        print("\nAll IBGE API tests passed!")
    
    return True

def test_direct_api_request(url, verbose=True):
    """
    Test a direct API request.
    
    Args:
        url: The URL to request
        verbose: Whether to print verbose output
    
    Returns:
        True if the request succeeds, False otherwise
    """
    if verbose:
        print(f"Testing direct API request to {url}...")
    
    # Create an instance of the API service
    api_service = APIService(base_url="", cache_enabled=False)
    
    # Make the request
    response = api_service.get(url)
    
    if response:
        if verbose:
            print("Success! Got response:")
            print(response)
        return True
    else:
        if verbose:
            print("Failed to get response.")
        return False

def main():
    """
    Main function.
    """
    parser = argparse.ArgumentParser(description="Test API Service")
    parser.add_argument("--ibge", action="store_true", help="Test IBGE API")
    parser.add_argument("--url", type=str, help="Test a direct API request to the specified URL")
    parser.add_argument("--quiet", action="store_true", help="Suppress verbose output")
    
    args = parser.parse_args()
    
    # If no arguments are provided, test all APIs
    if not args.ibge and not args.url:
        args.ibge = True
    
    # Test IBGE API
    if args.ibge:
        test_ibge_api(verbose=not args.quiet)
    
    # Test direct API request
    if args.url:
        test_direct_api_request(args.url, verbose=not args.quiet)

if __name__ == "__main__":
    main()
