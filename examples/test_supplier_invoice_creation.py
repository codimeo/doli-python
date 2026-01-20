#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example: Test Supplier Invoice Creation

This example demonstrates how to:
1. Configure the Dolibarr API client
2. Attempt to create a supplier invoice
3. Handle errors and display results

Requirements:
- Create a .env file with DOLIBARR_API_KEY (see .env.example)
- Optionally set DOLIBARR_HOST in .env (defaults to http://dolibarr.codimeo.com/api/index.php)
"""

import os
from random import randint
import sys
from pathlib import Path

from dotenv import load_dotenv

import dolibarr_api
from dolibarr_api.api.supplierinvoices_api import SupplierinvoicesApi
from dolibarr_api.models.create_supplierinvoices_model import (
    CreateSupplierinvoicesModel,
)
from dolibarr_api.rest import ApiException

# Load environment variables from .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


def test_create_supplier_invoice():
    """
    Test creating a supplier invoice.
    """
    # Get configuration from environment variables
    api_key = os.environ.get("DOLIBARR_API_KEY")
    if not api_key:
        print("Error: DOLIBARR_API_KEY is not set")
        print("Please create a .env file in the examples/ folder with:")
        print("  DOLIBARR_API_KEY=your-api-key")
        print("(See .env.example for a template)")
        sys.exit(1)

    host = os.environ.get("DOLIBARR_HOST", "http://dolibarr.codimeo.com/api/index.php")

    # Configure API client
    configuration = dolibarr_api.Configuration(host=host)
    configuration.api_key["api_key"] = api_key

    # Create API client and instance
    with dolibarr_api.ApiClient(configuration) as api_client:
        api_instance = SupplierinvoicesApi(api_client)
        
        random_ref = "TEST" + str(randint(1000, 9999))

        try:
            print("Attempting to create a supplier invoice...")
            print(
                "Using test data: ref=auto, ref_supplier=" + random_ref + ", socid=397, note=Test supplier invoice, date=2023-12-03"
            )
            print()

            # The API expects a JSON dict, not the generated model format
            # Based on the doc example: {'ref': 'auto', 'ref_supplier': '7985630', 'socid': 1, 'note': 'Inserted with Python', 'order_supplier': 1, 'date': '2021-07-28'}
            invoice_data = {
                "ref": "auto",
                "ref_supplier": random_ref, # Generate a unique ref and pad it with zeros
                "socid": 397,
                "note": "Test supplier invoice from API",
                "date": "2023-12-03",
            }

            # Call the API to create supplier invoice, passing the dict directly as the model
            # The generated serialize method sets _body_params = create_supplierinvoices_model
            # So passing the dict directly should work if the API accepts JSON
            api_response = api_instance.create_supplierinvoices(
                create_supplierinvoices_model=invoice_data  # Pass dict instead of model
            )

            print("SUCCESS: Supplier invoice created!")
            print(f"Invoice ID: {api_response}")
            print(
                "Note: This is a test invoice - you may want to delete it manually in Dolibarr"
            )

        except ApiException as e:
            print("API Exception occurred:")
            print(f"Status: {e.status}")
            print(f"Reason: {e.reason}")
            if e.body:
                print(f"Body: {e.body}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)


def main():
    """Main function to run the example."""
    print("=" * 80)
    print("Dolibarr API - Test Supplier Invoice Creation")
    print("=" * 80)
    print()

    test_create_supplier_invoice()

    print()
    print("Test completed!")


if __name__ == "__main__":
    main()
