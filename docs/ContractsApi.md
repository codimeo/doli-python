# dolibarr_api.ContractsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_activate_line**](ContractsApi.md#contracts_activate_line) | **PUT** /contracts/{id}/lines/{lineid}/activate | Activate a service line of a given contract 🔐
[**contracts_close**](ContractsApi.md#contracts_close) | **POST** /contracts/{id}/close | Close all services of a contract 🔐
[**contracts_create_line**](ContractsApi.md#contracts_create_line) | **POST** /contracts/{id}/lines | Add a line to given contract 🔐
[**contracts_remove_line**](ContractsApi.md#contracts_remove_line) | **DELETE** /contracts/{id}/lines/{lineid} | Delete a line to given contract 🔐
[**contracts_retrieve_lines**](ContractsApi.md#contracts_retrieve_lines) | **GET** /contracts/{id}/lines | Get lines of a contract 🔐
[**contracts_unactivate_line**](ContractsApi.md#contracts_unactivate_line) | **PUT** /contracts/{id}/lines/{lineid}/unactivate | Unactivate a service line of a given contract 🔐
[**contracts_update_line**](ContractsApi.md#contracts_update_line) | **PUT** /contracts/{id}/lines/{lineid} | Update a line to given contract 🔐
[**contracts_validate**](ContractsApi.md#contracts_validate) | **POST** /contracts/{id}/validate | Validate a contract 🔐
[**create_contracts**](ContractsApi.md#create_contracts) | **POST** /contracts | Create contract object 🔐
[**list_contracts**](ContractsApi.md#list_contracts) | **GET** /contracts | List contracts 🔐
[**remove_contracts**](ContractsApi.md#remove_contracts) | **DELETE** /contracts/{id} | Delete contract 🔐
[**retrieve_contracts**](ContractsApi.md#retrieve_contracts) | **GET** /contracts/{id} | Get properties of a contract object 🔐
[**update_contracts**](ContractsApi.md#update_contracts) | **PUT** /contracts/{id} | Update contract general fields (won&#39;t touch lines of contract) 🔐


# **contracts_activate_line**
> str contracts_activate_line(id, lineid, contracts_activate_line_model)

Activate a service line of a given contract 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.contracts_activate_line_model import ContractsActivateLineModel
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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Id of contract to activate
    lineid = 56 # int | Id of line to activate
    contracts_activate_line_model = dolibarr_api.ContractsActivateLineModel() # ContractsActivateLineModel | **datestart** (required)   dateend   comment   

    try:
        # Activate a service line of a given contract 🔐
        api_response = api_instance.contracts_activate_line(id, lineid, contracts_activate_line_model)
        print("The response of ContractsApi->contracts_activate_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->contracts_activate_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contract to activate | 
 **lineid** | **int**| Id of line to activate | 
 **contracts_activate_line_model** | [**ContractsActivateLineModel**](ContractsActivateLineModel.md)| **datestart** (required)   dateend   comment    | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_close**
> List[str] contracts_close(id, contracts_close_model=contracts_close_model)

Close all services of a contract 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.contracts_close_model import ContractsCloseModel
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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Contract ID
    contracts_close_model = dolibarr_api.ContractsCloseModel() # ContractsCloseModel | notrigger    (optional)

    try:
        # Close all services of a contract 🔐
        api_response = api_instance.contracts_close(id, contracts_close_model=contracts_close_model)
        print("The response of ContractsApi->contracts_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->contracts_close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Contract ID | 
 **contracts_close_model** | [**ContractsCloseModel**](ContractsCloseModel.md)| notrigger    | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_create_line**
> str contracts_create_line(id, contracts_create_line_model=contracts_create_line_model)

Add a line to given contract 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.contracts_create_line_model import ContractsCreateLineModel
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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Id of contrat to update
    contracts_create_line_model = dolibarr_api.ContractsCreateLineModel() # ContractsCreateLineModel | request_data    (optional)

    try:
        # Add a line to given contract 🔐
        api_response = api_instance.contracts_create_line(id, contracts_create_line_model=contracts_create_line_model)
        print("The response of ContractsApi->contracts_create_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->contracts_create_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contrat to update | 
 **contracts_create_line_model** | [**ContractsCreateLineModel**](ContractsCreateLineModel.md)| request_data    | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_remove_line**
> str contracts_remove_line(id, lineid)

Delete a line to given contract 🔐

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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Id of contract to update
    lineid = 56 # int | Id of line to delete

    try:
        # Delete a line to given contract 🔐
        api_response = api_instance.contracts_remove_line(id, lineid)
        print("The response of ContractsApi->contracts_remove_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->contracts_remove_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contract to update | 
 **lineid** | **int**| Id of line to delete | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_retrieve_lines**
> List[str] contracts_retrieve_lines(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

Get lines of a contract 🔐

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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Id of contract
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # Get lines of a contract 🔐
        api_response = api_instance.contracts_retrieve_lines(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of ContractsApi->contracts_retrieve_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->contracts_retrieve_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contract | 
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.date_creation:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
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
**404** | Not Found |  -  |
**503** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_unactivate_line**
> str contracts_unactivate_line(id, lineid, contracts_unactivate_line_model)

Unactivate a service line of a given contract 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.contracts_unactivate_line_model import ContractsUnactivateLineModel
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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Id of contract to activate
    lineid = 56 # int | Id of line to activate
    contracts_unactivate_line_model = dolibarr_api.ContractsUnactivateLineModel() # ContractsUnactivateLineModel | **datestart** (required)   comment   

    try:
        # Unactivate a service line of a given contract 🔐
        api_response = api_instance.contracts_unactivate_line(id, lineid, contracts_unactivate_line_model)
        print("The response of ContractsApi->contracts_unactivate_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->contracts_unactivate_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contract to activate | 
 **lineid** | **int**| Id of line to activate | 
 **contracts_unactivate_line_model** | [**ContractsUnactivateLineModel**](ContractsUnactivateLineModel.md)| **datestart** (required)   comment    | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_update_line**
> str contracts_update_line(id, lineid, contracts_update_line_model=contracts_update_line_model)

Update a line to given contract 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.contracts_update_line_model import ContractsUpdateLineModel
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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Id of contrat to update
    lineid = 56 # int | Id of line to update
    contracts_update_line_model = dolibarr_api.ContractsUpdateLineModel() # ContractsUpdateLineModel | request_data    (optional)

    try:
        # Update a line to given contract 🔐
        api_response = api_instance.contracts_update_line(id, lineid, contracts_update_line_model=contracts_update_line_model)
        print("The response of ContractsApi->contracts_update_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->contracts_update_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contrat to update | 
 **lineid** | **int**| Id of line to update | 
 **contracts_update_line_model** | [**ContractsUpdateLineModel**](ContractsUpdateLineModel.md)| request_data    | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_validate**
> List[str] contracts_validate(id, contracts_validate_model=contracts_validate_model)

Validate a contract 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.contracts_validate_model import ContractsValidateModel
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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Contract ID
    contracts_validate_model = dolibarr_api.ContractsValidateModel() # ContractsValidateModel | notrigger    (optional)

    try:
        # Validate a contract 🔐
        api_response = api_instance.contracts_validate(id, contracts_validate_model=contracts_validate_model)
        print("The response of ContractsApi->contracts_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->contracts_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Contract ID | 
 **contracts_validate_model** | [**ContractsValidateModel**](ContractsValidateModel.md)| notrigger    | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contracts**
> int create_contracts(create_contracts_model=create_contracts_model)

Create contract object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_contracts_model import CreateContractsModel
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
    api_instance = dolibarr_api.ContractsApi(api_client)
    create_contracts_model = dolibarr_api.CreateContractsModel() # CreateContractsModel | request_data    (optional)

    try:
        # Create contract object 🔐
        api_response = api_instance.create_contracts(create_contracts_model=create_contracts_model)
        print("The response of ContractsApi->create_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->create_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contracts_model** | [**CreateContractsModel**](CreateContractsModel.md)| request_data    | [optional] 

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

# **list_contracts**
> List[str] list_contracts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

List contracts 🔐

Get a list of contracts

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
    api_instance = dolibarr_api.ContractsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter contracts of (example '1' or '1,2,3') (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List contracts 🔐
        api_response = api_instance.list_contracts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of ContractsApi->list_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->list_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter contracts of (example &#39;1&#39; or &#39;1,2,3&#39;) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.date_creation:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
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
**404** | Not found |  -  |
**503** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_contracts**
> List[str] remove_contracts(id)

Delete contract 🔐

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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Contract ID

    try:
        # Delete contract 🔐
        api_response = api_instance.remove_contracts(id)
        print("The response of ContractsApi->remove_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->remove_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Contract ID | 

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

# **retrieve_contracts**
> Dict[str, object] retrieve_contracts(id)

Get properties of a contract object 🔐

Return an array with contract information

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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | ID of contract

    try:
        # Get properties of a contract object 🔐
        api_response = api_instance.retrieve_contracts(id)
        print("The response of ContractsApi->retrieve_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->retrieve_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of contract | 

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

# **update_contracts**
> Dict[str, object] update_contracts(id, update_contracts_model=update_contracts_model)

Update contract general fields (won't touch lines of contract) 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_contracts_model import UpdateContractsModel
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
    api_instance = dolibarr_api.ContractsApi(api_client)
    id = 56 # int | Id of contract to update
    update_contracts_model = dolibarr_api.UpdateContractsModel() # UpdateContractsModel | request_data    (optional)

    try:
        # Update contract general fields (won't touch lines of contract) 🔐
        api_response = api_instance.update_contracts(id, update_contracts_model=update_contracts_model)
        print("The response of ContractsApi->update_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->update_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of contract to update | 
 **update_contracts_model** | [**UpdateContractsModel**](UpdateContractsModel.md)| request_data    | [optional] 

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

