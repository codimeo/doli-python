# Dolibarr API Examples

This folder contains example scripts demonstrating how to use the Dolibarr Python API client.

## Prerequisites

1. **Install the package:**

   ```bash
   pip install -e ..
   ```

2. **Set up environment variables:**

   ```bash
   export DOLIBARR_API_KEY='your-api-key-here'
   export DOLIBARR_HOST='http://your-dolibarr-instance.com/api/index.php'  # Optional
   ```

   You can get your API key from Dolibarr:
   - Go to: Home > Setup > Modules/Applications
   - Enable the "REST API" module
   - Go to your user settings to generate an API key

## Available Examples

### 1. Search Supplier by Name

**File:** `search_supplier_by_name.py`

Search for a supplier by name and display its ID and official name.

**Usage:**

```bash
# Search for "Orange"
python search_supplier_by_name.py

# Search for a different supplier
python search_supplier_by_name.py "CompanyName"
```

**Features:**

- Search by supplier name or alias
- Filter to show only suppliers (not customers or prospects)
- Display supplier ID, reference, and official name
- Handle API exceptions gracefully

## Running the Examples

### Option 1: Direct execution

```bash
cd examples
python search_supplier_by_name.py
```

### Option 2: Make scripts executable (Unix/Linux/macOS)

```bash
chmod +x examples/*.py
./examples/search_supplier_by_name.py
```

### Option 3: Using the virtual environment

```bash
source .venv/bin/activate
python examples/search_supplier_by_name.py
```

## Common Configuration

All examples use these common configuration patterns:

```python
import os
import dolibarr_api
from dolibarr_api.rest import ApiException

# Configure API client
configuration = dolibarr_api.Configuration(
    host=os.environ.get('DOLIBARR_HOST', 'http://dolibarr.codimeo.com/api/index.php')
)
configuration.api_key['api_key'] = os.environ['DOLIBARR_API_KEY']

# Use the API
with dolibarr_api.ApiClient(configuration) as api_client:
    api_instance = dolibarr_api.SomeApi(api_client)
    result = api_instance.some_method()
```

## Error Handling

All examples include proper error handling for:

- Missing API key
- API exceptions (404, 403, 500, etc.)
- Network errors
- Invalid responses

## Tips

1. **Testing:** Use a development/test Dolibarr instance for testing
2. **API Key Security:** Never commit your API key to version control
3. **Rate Limiting:** Be mindful of API rate limits in production
4. **Debugging:** Set `configuration.debug = True` for detailed logging

## Support

For issues or questions:

- Check the [Dolibarr API documentation](https://www.dolibarr.org/documentation-home/250-developer-documentation/api-rest)
- Review the generated API docs in the `docs/` folder
- Open an issue on the project repository

## License

These examples are provided as-is for educational purposes.
