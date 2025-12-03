#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example: Search for a supplier by name and display its ID and official name

This example demonstrates how to:
1. Configure the Dolibarr API client
2. Search for suppliers using SQL filters
3. Display supplier information (ref_id and name)

Requirements:
- Create a .env file with DOLIBARR_API_KEY (see .env.example)
- Optionally set DOLIBARR_HOST in .env (defaults to http://dolibarr.codimeo.com/api/index.php)
"""

import os
import sys
import ast
from pathlib import Path

from dotenv import load_dotenv

import dolibarr_api
from dolibarr_api.api.thirdparties_api import ThirdpartiesApi
from dolibarr_api.rest import ApiException

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)


def search_supplier(supplier_name: str):
    # pylint: disable=too-many-locals,too-many-statements
    """
    Search for a supplier by name and display its details.

    Args:
        supplier_name: The name (or partial name) of the supplier to search for
    """
    # Get configuration from environment variables
    api_key = os.environ.get('DOLIBARR_API_KEY')
    if not api_key:
        print("Error: DOLIBARR_API_KEY is not set")
        print("Please create a .env file in the examples/ folder with:")
        print("  DOLIBARR_API_KEY=your-api-key")
        print("(See .env.example for a template)")
        sys.exit(1)

    host = os.environ.get('DOLIBARR_HOST', 'http://dolibarr.codimeo.com/api/index.php')

    # Configure API client
    configuration = dolibarr_api.Configuration(
        host=host
    )
    configuration.api_key['api_key'] = api_key

    # Create API client and instance
    with dolibarr_api.ApiClient(configuration) as api_client:
        api_instance = ThirdpartiesApi(api_client)

        try:
            # Search for suppliers (mode=4) with name matching the search term
            # Using SQL filters to search by name or alias
            sql_filter = (
                f"((t.nom:like:'%{supplier_name}%') or "
                f"(t.name_alias:like:'%{supplier_name}%'))"
            )

            print(f"Searching for supplier: '{supplier_name}'...")
            print(f"Using SQL filter: {sql_filter}\n")

            # Call the API to list third parties filtered by supplier mode and name
            api_response = api_instance.list_thirdparties(
                mode=4,  # 4 = suppliers only
                sqlfilters=sql_filter,
                sortfield='t.nom',
                sortorder='ASC'
            )

            # Process and display results
            if not api_response or len(api_response) == 0:
                print(f"No suppliers found matching '{supplier_name}'")
                return

            print(f"Found {len(api_response)} supplier(s):\n")
            print("-" * 80)

            for idx, supplier_data in enumerate(api_response, 1):
                # The API returns Python dict strings (not JSON), so we need to parse them
                if isinstance(supplier_data, str):
                    supplier = ast.literal_eval(supplier_data)
                else:
                    supplier = supplier_data

                # Get detailed information for each supplier
                supplier_id = supplier.get('id')
                supplier_ref = supplier.get('ref', 'N/A')
                supplier_name_full = supplier.get('name', supplier.get('nom', 'N/A'))
                supplier_alias = supplier.get('name_alias', '')
                supplier_type = supplier.get('client', 'N/A')

                print(f"{idx}. Supplier Information:")
                print(f"   ID (ref_id):      {supplier_id}")
                print(f"   Reference:        {supplier_ref}")
                print(f"   Official Name:    {supplier_name_full}")
                if supplier_alias:
                    print(f"   Alias:            {supplier_alias}")
                print(f"   Type Code:        {supplier_type}")
                print("-" * 80)

        except ApiException as e:
            print(f"Exception when calling ThirdpartiesApi->list_thirdparties: {e}")
            print(f"Status: {e.status}")
            print(f"Reason: {e.reason}")
            if e.body:
                print(f"Body: {e.body}")
            sys.exit(1)
        except (ValueError, KeyError) as e:
            print(f"Error processing response data: {e}")
            sys.exit(1)


def main():
    """Main function to run the example."""
    # Default supplier name to search for
    supplier_name = "Orange"

    # Allow command line argument to override default
    if len(sys.argv) > 1:
        supplier_name = sys.argv[1]

    print("=" * 80)
    print("Dolibarr API - Search Supplier by Name")
    print("=" * 80)
    print()

    search_supplier(supplier_name)

    print()
    print("Example completed successfully!")


if __name__ == "__main__":
    main()
