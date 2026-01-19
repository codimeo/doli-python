# dolibarr_api.ObjectlinksApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**objectlinks_create**](ObjectlinksApi.md#objectlinks_create) | **POST** /objectlinks | Create object link 🔐
[**objectlinks_remove_by_id**](ObjectlinksApi.md#objectlinks_remove_by_id) | **DELETE** /objectlinks/{id} | Delete an object link 🔐
[**objectlinks_remove_by_values**](ObjectlinksApi.md#objectlinks_remove_by_values) | **DELETE** /objectlinks | Delete object link By Values, not id 🔐
[**objectlinks_retrieve_by_id**](ObjectlinksApi.md#objectlinks_retrieve_by_id) | **GET** /objectlinks/{id} | Get properties of a ObjectLink object 🔐
[**objectlinks_retrieve_by_values**](ObjectlinksApi.md#objectlinks_retrieve_by_values) | **GET** /objectlinks | GET object link(s) By Values, not id 🔐


# **objectlinks_create**
> List[str] objectlinks_create(objectlinks_create_model=objectlinks_create_model)

Create object link 🔐

Examples: Only set "notrigger": 1 because 0 is the default value. Linking subscriptions for when you sell membership as part of another sale {"fk_source":"1679","sourcetype":"propal","fk_target":"1233","targettype":"commande"} {"fk_source":"167","sourcetype":"facture","fk_target":"123","targettype":"subscription"}

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.objectlinks_create_model import ObjectlinksCreateModel
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
    api_instance = dolibarr_api.ObjectlinksApi(api_client)
    objectlinks_create_model = dolibarr_api.ObjectlinksCreateModel() # ObjectlinksCreateModel | request_data    (optional)

    try:
        # Create object link 🔐
        api_response = api_instance.objectlinks_create(objectlinks_create_model=objectlinks_create_model)
        print("The response of ObjectlinksApi->objectlinks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectlinksApi->objectlinks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **objectlinks_create_model** | [**ObjectlinksCreateModel**](ObjectlinksCreateModel.md)| request_data    | [optional] 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **objectlinks_remove_by_id**
> List[str] objectlinks_remove_by_id(id)

Delete an object link 🔐

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
    api_instance = dolibarr_api.ObjectlinksApi(api_client)
    id = 56 # int | object link ID

    try:
        # Delete an object link 🔐
        api_response = api_instance.objectlinks_remove_by_id(id)
        print("The response of ObjectlinksApi->objectlinks_remove_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectlinksApi->objectlinks_remove_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| object link ID | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **objectlinks_remove_by_values**
> List[str] objectlinks_remove_by_values(fk_source, sourcetype, fk_target, targettype, relationtype=relationtype, notrigger=notrigger)

Delete object link By Values, not id 🔐

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
    api_instance = dolibarr_api.ObjectlinksApi(api_client)
    fk_source = 56 # int | source id of object we link from
    sourcetype = 'sourcetype_example' # str | type of the source object
    fk_target = 56 # int | target id of object we link to
    targettype = 'targettype_example' # str | type of the target object
    relationtype = 'relationtype_example' # str | type of the relation, usually null (optional)
    notrigger = 56 # int | 1=Does not execute triggers, 0=execute triggers (optional)

    try:
        # Delete object link By Values, not id 🔐
        api_response = api_instance.objectlinks_remove_by_values(fk_source, sourcetype, fk_target, targettype, relationtype=relationtype, notrigger=notrigger)
        print("The response of ObjectlinksApi->objectlinks_remove_by_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectlinksApi->objectlinks_remove_by_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fk_source** | **int**| source id of object we link from | 
 **sourcetype** | **str**| type of the source object | 
 **fk_target** | **int**| target id of object we link to | 
 **targettype** | **str**| type of the target object | 
 **relationtype** | **str**| type of the relation, usually null | [optional] 
 **notrigger** | **int**| 1&#x3D;Does not execute triggers, 0&#x3D;execute triggers | [optional] 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **objectlinks_retrieve_by_id**
> Dict[str, object] objectlinks_retrieve_by_id(id)

Get properties of a ObjectLink object 🔐

Return an array with object link information

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
    api_instance = dolibarr_api.ObjectlinksApi(api_client)
    id = 56 # int | ID of objectlink

    try:
        # Get properties of a ObjectLink object 🔐
        api_response = api_instance.objectlinks_retrieve_by_id(id)
        print("The response of ObjectlinksApi->objectlinks_retrieve_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectlinksApi->objectlinks_retrieve_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of objectlink | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **objectlinks_retrieve_by_values**
> Dict[str, object] objectlinks_retrieve_by_values(fk_source, sourcetype, fk_target, targettype, relationtype=relationtype)

GET object link(s) By Values, not id 🔐

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
    api_instance = dolibarr_api.ObjectlinksApi(api_client)
    fk_source = 56 # int | source id of object we link from
    sourcetype = 'sourcetype_example' # str | type of the source object
    fk_target = 56 # int | target id of object we link to
    targettype = 'targettype_example' # str | type of the target object
    relationtype = 'relationtype_example' # str | type of the relation, usually null (optional)

    try:
        # GET object link(s) By Values, not id 🔐
        api_response = api_instance.objectlinks_retrieve_by_values(fk_source, sourcetype, fk_target, targettype, relationtype=relationtype)
        print("The response of ObjectlinksApi->objectlinks_retrieve_by_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectlinksApi->objectlinks_retrieve_by_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fk_source** | **int**| source id of object we link from | 
 **sourcetype** | **str**| type of the source object | 
 **fk_target** | **int**| target id of object we link to | 
 **targettype** | **str**| type of the target object | 
 **relationtype** | **str**| type of the relation, usually null | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

