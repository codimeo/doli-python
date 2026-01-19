# dolibarr_api.MulticurrenciesApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_multicurrencies**](MulticurrenciesApi.md#create_multicurrencies) | **POST** /multicurrencies | Create Currency object 🔐
[**list_multicurrencies**](MulticurrenciesApi.md#list_multicurrencies) | **GET** /multicurrencies | List Currencies 🔐
[**multicurrencies_retrieve_by_code**](MulticurrenciesApi.md#multicurrencies_retrieve_by_code) | **GET** /multicurrencies/bycode/{code} | Get properties of a Currency object by code 🔐
[**multicurrencies_retrieve_rates**](MulticurrenciesApi.md#multicurrencies_retrieve_rates) | **GET** /multicurrencies/{id}/rates | List Currency rates 🔐
[**multicurrencies_update_rate**](MulticurrenciesApi.md#multicurrencies_update_rate) | **PUT** /multicurrencies/{id}/rates | Update Currency rate 🔐
[**remove_multicurrencies**](MulticurrenciesApi.md#remove_multicurrencies) | **DELETE** /multicurrencies/{id} | Delete Currency 🔐
[**retrieve_multicurrencies**](MulticurrenciesApi.md#retrieve_multicurrencies) | **GET** /multicurrencies/{id} | Get properties of a Currency object 🔐
[**update_multicurrencies**](MulticurrenciesApi.md#update_multicurrencies) | **PUT** /multicurrencies/{id} | Update Currency 🔐


# **create_multicurrencies**
> int create_multicurrencies(create_multicurrencies_model=create_multicurrencies_model)

Create Currency object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_multicurrencies_model import CreateMulticurrenciesModel
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
    api_instance = dolibarr_api.MulticurrenciesApi(api_client)
    create_multicurrencies_model = dolibarr_api.CreateMulticurrenciesModel() # CreateMulticurrenciesModel | request_data    (optional)

    try:
        # Create Currency object 🔐
        api_response = api_instance.create_multicurrencies(create_multicurrencies_model=create_multicurrencies_model)
        print("The response of MulticurrenciesApi->create_multicurrencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticurrenciesApi->create_multicurrencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_multicurrencies_model** | [**CreateMulticurrenciesModel**](CreateMulticurrenciesModel.md)| request_data    | [optional] 

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
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_multicurrencies**
> List[str] list_multicurrencies(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties)

List Currencies 🔐

Get a list of Currencies

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
    api_instance = dolibarr_api.MulticurrenciesApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.product_id:=:1) and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # List Currencies 🔐
        api_response = api_instance.list_multicurrencies(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties)
        print("The response of MulticurrenciesApi->list_multicurrencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticurrenciesApi->list_multicurrencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.product_id:&#x3D;:1) and (t.date_creation:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
 **properties** | **str**| Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names | [optional] 

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

# **multicurrencies_retrieve_by_code**
> str multicurrencies_retrieve_by_code(code)

Get properties of a Currency object by code 🔐

Return an array with Currency information

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
    api_instance = dolibarr_api.MulticurrenciesApi(api_client)
    code = 'code_example' # str | Code of Currency (ex: EUR)

    try:
        # Get properties of a Currency object by code 🔐
        api_response = api_instance.multicurrencies_retrieve_by_code(code)
        print("The response of MulticurrenciesApi->multicurrencies_retrieve_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticurrenciesApi->multicurrencies_retrieve_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of Currency (ex: EUR) | 

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
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multicurrencies_retrieve_rates**
> str multicurrencies_retrieve_rates(id)

List Currency rates 🔐

Get a list of Currency rates

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
    api_instance = dolibarr_api.MulticurrenciesApi(api_client)
    id = 56 # int | ID of Currency

    try:
        # List Currency rates 🔐
        api_response = api_instance.multicurrencies_retrieve_rates(id)
        print("The response of MulticurrenciesApi->multicurrencies_retrieve_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticurrenciesApi->multicurrencies_retrieve_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Currency | 

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
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multicurrencies_update_rate**
> str multicurrencies_update_rate(id, multicurrencies_update_rate_model=multicurrencies_update_rate_model)

Update Currency rate 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.multicurrencies_update_rate_model import MulticurrenciesUpdateRateModel
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
    api_instance = dolibarr_api.MulticurrenciesApi(api_client)
    id = 56 # int | Currency ID
    multicurrencies_update_rate_model = dolibarr_api.MulticurrenciesUpdateRateModel() # MulticurrenciesUpdateRateModel | request_data    (optional)

    try:
        # Update Currency rate 🔐
        api_response = api_instance.multicurrencies_update_rate(id, multicurrencies_update_rate_model=multicurrencies_update_rate_model)
        print("The response of MulticurrenciesApi->multicurrencies_update_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticurrenciesApi->multicurrencies_update_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Currency ID | 
 **multicurrencies_update_rate_model** | [**MulticurrenciesUpdateRateModel**](MulticurrenciesUpdateRateModel.md)| request_data    | [optional] 

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
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_multicurrencies**
> List[str] remove_multicurrencies(id)

Delete Currency 🔐

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
    api_instance = dolibarr_api.MulticurrenciesApi(api_client)
    id = 56 # int | Currency ID

    try:
        # Delete Currency 🔐
        api_response = api_instance.remove_multicurrencies(id)
        print("The response of MulticurrenciesApi->remove_multicurrencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticurrenciesApi->remove_multicurrencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Currency ID | 

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

# **retrieve_multicurrencies**
> Dict[str, object] retrieve_multicurrencies(id)

Get properties of a Currency object 🔐

Return an array with Currency information

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
    api_instance = dolibarr_api.MulticurrenciesApi(api_client)
    id = 56 # int | ID of Currency

    try:
        # Get properties of a Currency object 🔐
        api_response = api_instance.retrieve_multicurrencies(id)
        print("The response of MulticurrenciesApi->retrieve_multicurrencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticurrenciesApi->retrieve_multicurrencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Currency | 

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

# **update_multicurrencies**
> Dict[str, object] update_multicurrencies(id, update_multicurrencies_model=update_multicurrencies_model)

Update Currency 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_multicurrencies_model import UpdateMulticurrenciesModel
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
    api_instance = dolibarr_api.MulticurrenciesApi(api_client)
    id = 56 # int | Id of Currency to update
    update_multicurrencies_model = dolibarr_api.UpdateMulticurrenciesModel() # UpdateMulticurrenciesModel | request_data    (optional)

    try:
        # Update Currency 🔐
        api_response = api_instance.update_multicurrencies(id, update_multicurrencies_model=update_multicurrencies_model)
        print("The response of MulticurrenciesApi->update_multicurrencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MulticurrenciesApi->update_multicurrencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of Currency to update | 
 **update_multicurrencies_model** | [**UpdateMulticurrenciesModel**](UpdateMulticurrenciesModel.md)| request_data    | [optional] 

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
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

