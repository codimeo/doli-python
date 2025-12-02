# dolibarr_api.SupplierproposalsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplierproposals**](SupplierproposalsApi.md#create_supplierproposals) | **POST** /supplierproposals | Create supplier proposal (price request) object 🔐
[**list_supplierproposals**](SupplierproposalsApi.md#list_supplierproposals) | **GET** /supplierproposals | List supplier proposals 🔐
[**remove_supplierproposals**](SupplierproposalsApi.md#remove_supplierproposals) | **DELETE** /supplierproposals/{id} | Delete commercial proposal 🔐
[**retrieve_supplierproposals**](SupplierproposalsApi.md#retrieve_supplierproposals) | **GET** /supplierproposals/{id} | Get properties of a supplier proposal (price request) object 🔐
[**update_supplierproposals**](SupplierproposalsApi.md#update_supplierproposals) | **PUT** /supplierproposals/{id} | Update supplier proposal general fields (won&#39;t touch lines of supplier proposal) 🔐


# **create_supplierproposals**
> int create_supplierproposals(create_supplierproposals_model=create_supplierproposals_model)

Create supplier proposal (price request) object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_supplierproposals_model import CreateSupplierproposalsModel
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
    api_instance = dolibarr_api.SupplierproposalsApi(api_client)
    create_supplierproposals_model = dolibarr_api.CreateSupplierproposalsModel() # CreateSupplierproposalsModel | request_data    (optional)

    try:
        # Create supplier proposal (price request) object 🔐
        api_response = api_instance.create_supplierproposals(create_supplierproposals_model=create_supplierproposals_model)
        print("The response of SupplierproposalsApi->create_supplierproposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierproposalsApi->create_supplierproposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_supplierproposals_model** | [**CreateSupplierproposalsModel**](CreateSupplierproposalsModel.md)| request_data    | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supplierproposals**
> List[str] list_supplierproposals(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

List supplier proposals 🔐

Get a list of supplier proposals

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
    api_instance = dolibarr_api.SupplierproposalsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter supplier proposals (example '1' or '1,2,3') (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List supplier proposals 🔐
        api_response = api_instance.list_supplierproposals(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of SupplierproposalsApi->list_supplierproposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierproposalsApi->list_supplierproposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter supplier proposals (example &#39;1&#39; or &#39;1,2,3&#39;) | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_supplierproposals**
> List[str] remove_supplierproposals(id)

Delete commercial proposal 🔐

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
    api_instance = dolibarr_api.SupplierproposalsApi(api_client)
    id = 56 # int | Supplier proposal ID

    try:
        # Delete commercial proposal 🔐
        api_response = api_instance.remove_supplierproposals(id)
        print("The response of SupplierproposalsApi->remove_supplierproposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierproposalsApi->remove_supplierproposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Supplier proposal ID | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_supplierproposals**
> Dict[str, object] retrieve_supplierproposals(id)

Get properties of a supplier proposal (price request) object 🔐

Return an array with supplier proposal information

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
    api_instance = dolibarr_api.SupplierproposalsApi(api_client)
    id = 56 # int | ID of supplier proposal

    try:
        # Get properties of a supplier proposal (price request) object 🔐
        api_response = api_instance.retrieve_supplierproposals(id)
        print("The response of SupplierproposalsApi->retrieve_supplierproposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierproposalsApi->retrieve_supplierproposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of supplier proposal | 

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
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supplierproposals**
> Dict[str, object] update_supplierproposals(id, update_supplierproposals_model=update_supplierproposals_model)

Update supplier proposal general fields (won't touch lines of supplier proposal) 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_supplierproposals_model import UpdateSupplierproposalsModel
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
    api_instance = dolibarr_api.SupplierproposalsApi(api_client)
    id = 56 # int | Id of supplier proposal to update
    update_supplierproposals_model = dolibarr_api.UpdateSupplierproposalsModel() # UpdateSupplierproposalsModel | request_data    (optional)

    try:
        # Update supplier proposal general fields (won't touch lines of supplier proposal) 🔐
        api_response = api_instance.update_supplierproposals(id, update_supplierproposals_model=update_supplierproposals_model)
        print("The response of SupplierproposalsApi->update_supplierproposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierproposalsApi->update_supplierproposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier proposal to update | 
 **update_supplierproposals_model** | [**UpdateSupplierproposalsModel**](UpdateSupplierproposalsModel.md)| request_data    | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

