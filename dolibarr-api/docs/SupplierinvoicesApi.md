# dolibarr_api.SupplierinvoicesApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplierinvoices**](SupplierinvoicesApi.md#create_supplierinvoices) | **POST** /supplierinvoices | Create supplier invoice object 🔐
[**list_supplierinvoices**](SupplierinvoicesApi.md#list_supplierinvoices) | **GET** /supplierinvoices | List invoices 🔐
[**remove_supplierinvoices**](SupplierinvoicesApi.md#remove_supplierinvoices) | **DELETE** /supplierinvoices/{id} | Delete supplier invoice 🔐
[**retrieve_supplierinvoices**](SupplierinvoicesApi.md#retrieve_supplierinvoices) | **GET** /supplierinvoices/{id} | Get properties of a supplier invoice object 🔐
[**supplierinvoices_add_payment**](SupplierinvoicesApi.md#supplierinvoices_add_payment) | **POST** /supplierinvoices/{id}/payments | Add payment line to a specific supplier invoice with the remain to pay as amount. 🔐
[**supplierinvoices_create_line**](SupplierinvoicesApi.md#supplierinvoices_create_line) | **POST** /supplierinvoices/{id}/lines | Add a line to given supplier invoice 🔐
[**supplierinvoices_remove_line**](SupplierinvoicesApi.md#supplierinvoices_remove_line) | **DELETE** /supplierinvoices/{id}/lines/{lineid} | Deletes a line of a given supplier invoice 🔐
[**supplierinvoices_retrieve_lines**](SupplierinvoicesApi.md#supplierinvoices_retrieve_lines) | **GET** /supplierinvoices/{id}/lines | Get lines of a supplier invoice 🔐
[**supplierinvoices_retrieve_payments**](SupplierinvoicesApi.md#supplierinvoices_retrieve_payments) | **GET** /supplierinvoices/{id}/payments | Get list of payments of a given supplier invoice 🔐
[**supplierinvoices_settodraft**](SupplierinvoicesApi.md#supplierinvoices_settodraft) | **POST** /supplierinvoices/{id}/settodraft | Sets an invoice as draft 🔐
[**supplierinvoices_update_line**](SupplierinvoicesApi.md#supplierinvoices_update_line) | **PUT** /supplierinvoices/{id}/lines/{lineid} | Update a line to a given supplier invoice 🔐
[**supplierinvoices_validate**](SupplierinvoicesApi.md#supplierinvoices_validate) | **POST** /supplierinvoices/{id}/validate | Validate an invoice 🔐
[**update_supplierinvoices**](SupplierinvoicesApi.md#update_supplierinvoices) | **PUT** /supplierinvoices/{id} | Update supplier invoice 🔐


# **create_supplierinvoices**
> int create_supplierinvoices(create_supplierinvoices_model=create_supplierinvoices_model)

Create supplier invoice object 🔐

Note: soc_id = dolibarr_order_id Example: {'ref': 'auto', 'ref_supplier': '7985630', 'socid': 1, 'note': 'Inserted with Python', 'order_supplier': 1, 'date': '2021-07-28'}

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_supplierinvoices_model import CreateSupplierinvoicesModel
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    create_supplierinvoices_model = dolibarr_api.CreateSupplierinvoicesModel() # CreateSupplierinvoicesModel | request_data    (optional)

    try:
        # Create supplier invoice object 🔐
        api_response = api_instance.create_supplierinvoices(create_supplierinvoices_model=create_supplierinvoices_model)
        print("The response of SupplierinvoicesApi->create_supplierinvoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->create_supplierinvoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_supplierinvoices_model** | [**CreateSupplierinvoicesModel**](CreateSupplierinvoicesModel.md)| request_data    | [optional] 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supplierinvoices**
> List[str] list_supplierinvoices(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, status=status, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

List invoices 🔐

Get a list of supplier invoices

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter invoices of (example '1' or '1,2,3') (optional)
    status = 'status_example' # str | Filter by invoice status : draft | unpaid | paid | cancelled (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List invoices 🔐
        api_response = api_instance.list_supplierinvoices(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, status=status, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of SupplierinvoicesApi->list_supplierinvoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->list_supplierinvoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter invoices of (example &#39;1&#39; or &#39;1,2,3&#39;) | [optional] 
 **status** | **str**| Filter by invoice status : draft | unpaid | paid | cancelled | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.datec:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
 **properties** | **str**| Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names | [optional] 
 **pagination_data** | **bool**| If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* | [optional] 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_supplierinvoices**
> List[str] remove_supplierinvoices(id)

Delete supplier invoice 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Supplier invoice ID

    try:
        # Delete supplier invoice 🔐
        api_response = api_instance.remove_supplierinvoices(id)
        print("The response of SupplierinvoicesApi->remove_supplierinvoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->remove_supplierinvoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Supplier invoice ID | 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_supplierinvoices**
> Dict[str, object] retrieve_supplierinvoices(id)

Get properties of a supplier invoice object 🔐

Return an array with supplier invoice information

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | ID of supplier invoice

    try:
        # Get properties of a supplier invoice object 🔐
        api_response = api_instance.retrieve_supplierinvoices(id)
        print("The response of SupplierinvoicesApi->retrieve_supplierinvoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->retrieve_supplierinvoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of supplier invoice | 

### Return type

**Dict[str, object]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | 404 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_add_payment**
> int supplierinvoices_add_payment(id, supplierinvoices_add_payment_model)

Add payment line to a specific supplier invoice with the remain to pay as amount. 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.supplierinvoices_add_payment_model import SupplierinvoicesAddPaymentModel
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Id of invoice
    supplierinvoices_add_payment_model = dolibarr_api.SupplierinvoicesAddPaymentModel() # SupplierinvoicesAddPaymentModel | **datepaye** (required)   **payment_mode_id** (required)   **closepaidinvoices** (required)   **accountid** (required)   num_payment   comment   chqemetteur   chqbank   amount   

    try:
        # Add payment line to a specific supplier invoice with the remain to pay as amount. 🔐
        api_response = api_instance.supplierinvoices_add_payment(id, supplierinvoices_add_payment_model)
        print("The response of SupplierinvoicesApi->supplierinvoices_add_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->supplierinvoices_add_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of invoice | 
 **supplierinvoices_add_payment_model** | [**SupplierinvoicesAddPaymentModel**](SupplierinvoicesAddPaymentModel.md)| **datepaye** (required)   **payment_mode_id** (required)   **closepaidinvoices** (required)   **accountid** (required)   num_payment   comment   chqemetteur   chqbank   amount    | 

### Return type

**int**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_create_line**
> str supplierinvoices_create_line(id, supplierinvoices_create_line_model=supplierinvoices_create_line_model)

Add a line to given supplier invoice 🔐

Note: socid = dolibarr_order_id, pu_ht = net price, remise = discount Example: {'socid': 1, 'qty': 1, 'pu_ht': 21.0, 'tva_tx': 25.0, 'fk_product': '1189', 'product_type': 0, 'remise_percent': 1.0, 'vat_src_code': None}

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.supplierinvoices_create_line_model import SupplierinvoicesCreateLineModel
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Id of supplier invoice to update
    supplierinvoices_create_line_model = dolibarr_api.SupplierinvoicesCreateLineModel() # SupplierinvoicesCreateLineModel | request_data    (optional)

    try:
        # Add a line to given supplier invoice 🔐
        api_response = api_instance.supplierinvoices_create_line(id, supplierinvoices_create_line_model=supplierinvoices_create_line_model)
        print("The response of SupplierinvoicesApi->supplierinvoices_create_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->supplierinvoices_create_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice to update | 
 **supplierinvoices_create_line_model** | [**SupplierinvoicesCreateLineModel**](SupplierinvoicesCreateLineModel.md)| request_data    | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_remove_line**
> List[str] supplierinvoices_remove_line(id, lineid)

Deletes a line of a given supplier invoice 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Id of supplier invoice
    lineid = 56 # int | Id of the line to delete

    try:
        # Deletes a line of a given supplier invoice 🔐
        api_response = api_instance.supplierinvoices_remove_line(id, lineid)
        print("The response of SupplierinvoicesApi->supplierinvoices_remove_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->supplierinvoices_remove_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice | 
 **lineid** | **int**| Id of the line to delete | 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad parameters |  -  |
**403** | Not allowed |  -  |
**404** | Not found |  -  |
**405** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_retrieve_lines**
> List[str] supplierinvoices_retrieve_lines(id)

Get lines of a supplier invoice 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Id of supplier invoice

    try:
        # Get lines of a supplier invoice 🔐
        api_response = api_instance.supplierinvoices_retrieve_lines(id)
        print("The response of SupplierinvoicesApi->supplierinvoices_retrieve_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->supplierinvoices_retrieve_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice | 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_retrieve_payments**
> List[str] supplierinvoices_retrieve_payments(id)

Get list of payments of a given supplier invoice 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Id of SupplierInvoice

    try:
        # Get list of payments of a given supplier invoice 🔐
        api_response = api_instance.supplierinvoices_retrieve_payments(id)
        print("The response of SupplierinvoicesApi->supplierinvoices_retrieve_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->supplierinvoices_retrieve_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of SupplierInvoice | 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_settodraft**
> Dict[str, object] supplierinvoices_settodraft(id, supplierinvoices_settodraft_model=supplierinvoices_settodraft_model)

Sets an invoice as draft 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.supplierinvoices_settodraft_model import SupplierinvoicesSettodraftModel
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Id of supplier invoice
    supplierinvoices_settodraft_model = dolibarr_api.SupplierinvoicesSettodraftModel() # SupplierinvoicesSettodraftModel | idwarehouse   notrigger    (optional)

    try:
        # Sets an invoice as draft 🔐
        api_response = api_instance.supplierinvoices_settodraft(id, supplierinvoices_settodraft_model=supplierinvoices_settodraft_model)
        print("The response of SupplierinvoicesApi->supplierinvoices_settodraft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->supplierinvoices_settodraft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice | 
 **supplierinvoices_settodraft_model** | [**SupplierinvoicesSettodraftModel**](SupplierinvoicesSettodraftModel.md)| idwarehouse   notrigger    | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_update_line**
> str supplierinvoices_update_line(id, lineid, supplierinvoices_update_line_model=supplierinvoices_update_line_model)

Update a line to a given supplier invoice 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.supplierinvoices_update_line_model import SupplierinvoicesUpdateLineModel
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Id of supplier invoice to update
    lineid = 56 # int | Id of line to update
    supplierinvoices_update_line_model = dolibarr_api.SupplierinvoicesUpdateLineModel() # SupplierinvoicesUpdateLineModel | request_data    (optional)

    try:
        # Update a line to a given supplier invoice 🔐
        api_response = api_instance.supplierinvoices_update_line(id, lineid, supplierinvoices_update_line_model=supplierinvoices_update_line_model)
        print("The response of SupplierinvoicesApi->supplierinvoices_update_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->supplierinvoices_update_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice to update | 
 **lineid** | **int**| Id of line to update | 
 **supplierinvoices_update_line_model** | [**SupplierinvoicesUpdateLineModel**](SupplierinvoicesUpdateLineModel.md)| request_data    | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Not allowed |  -  |
**404** | Not found |  -  |
**304** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierinvoices_validate**
> List[str] supplierinvoices_validate(id, supplierinvoices_validate_model=supplierinvoices_validate_model)

Validate an invoice 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.supplierinvoices_validate_model import SupplierinvoicesValidateModel
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Invoice ID
    supplierinvoices_validate_model = dolibarr_api.SupplierinvoicesValidateModel() # SupplierinvoicesValidateModel | idwarehouse   notrigger    (optional)

    try:
        # Validate an invoice 🔐
        api_response = api_instance.supplierinvoices_validate(id, supplierinvoices_validate_model=supplierinvoices_validate_model)
        print("The response of SupplierinvoicesApi->supplierinvoices_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->supplierinvoices_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invoice ID | 
 **supplierinvoices_validate_model** | [**SupplierinvoicesValidateModel**](SupplierinvoicesValidateModel.md)| idwarehouse   notrigger    | [optional] 

### Return type

**List[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supplierinvoices**
> str update_supplierinvoices(id, update_supplierinvoices_model=update_supplierinvoices_model)

Update supplier invoice 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_supplierinvoices_model import UpdateSupplierinvoicesModel
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.SupplierinvoicesApi(api_client)
    id = 56 # int | Id of supplier invoice to update
    update_supplierinvoices_model = dolibarr_api.UpdateSupplierinvoicesModel() # UpdateSupplierinvoicesModel | request_data    (optional)

    try:
        # Update supplier invoice 🔐
        api_response = api_instance.update_supplierinvoices(id, update_supplierinvoices_model=update_supplierinvoices_model)
        print("The response of SupplierinvoicesApi->update_supplierinvoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierinvoicesApi->update_supplierinvoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier invoice to update | 
 **update_supplierinvoices_model** | [**UpdateSupplierinvoicesModel**](UpdateSupplierinvoicesModel.md)| request_data    | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

