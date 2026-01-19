# dolibarr_api.KnowledgemanagementApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_knowledgemanagement**](KnowledgemanagementApi.md#create_knowledgemanagement) | **POST** /knowledgemanagement/knowledgerecords | Create knowledgerecord object 🔐
[**knowledgemanagement_cancel**](KnowledgemanagementApi.md#knowledgemanagement_cancel) | **POST** /knowledgemanagement/{id}/cancel | Cancel a knowledge 🔐
[**knowledgemanagement_retrieve_categories**](KnowledgemanagementApi.md#knowledgemanagement_retrieve_categories) | **GET** /knowledgemanagement/knowledgerecords/{id}/categories | Get categories for a knowledgerecord object 🔐
[**knowledgemanagement_validate**](KnowledgemanagementApi.md#knowledgemanagement_validate) | **POST** /knowledgemanagement/{id}/validate | Validate a knowledge 🔐
[**list_knowledgemanagement**](KnowledgemanagementApi.md#list_knowledgemanagement) | **GET** /knowledgemanagement/knowledgerecords | List knowledgerecords 🔐
[**remove_knowledgemanagement**](KnowledgemanagementApi.md#remove_knowledgemanagement) | **DELETE** /knowledgemanagement/knowledgerecords/{id} | Delete knowledgerecord 🔐
[**retrieve_knowledgemanagement**](KnowledgemanagementApi.md#retrieve_knowledgemanagement) | **GET** /knowledgemanagement/knowledgerecords/{id} | Get properties of a knowledgerecord object 🔐
[**update_knowledgemanagement**](KnowledgemanagementApi.md#update_knowledgemanagement) | **PUT** /knowledgemanagement/knowledgerecords/{id} | Update knowledgerecord 🔐


# **create_knowledgemanagement**
> int create_knowledgemanagement(create_knowledgemanagement_model=create_knowledgemanagement_model)

Create knowledgerecord object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_knowledgemanagement_model import CreateKnowledgemanagementModel
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
    api_instance = dolibarr_api.KnowledgemanagementApi(api_client)
    create_knowledgemanagement_model = dolibarr_api.CreateKnowledgemanagementModel() # CreateKnowledgemanagementModel | request_data    (optional)

    try:
        # Create knowledgerecord object 🔐
        api_response = api_instance.create_knowledgemanagement(create_knowledgemanagement_model=create_knowledgemanagement_model)
        print("The response of KnowledgemanagementApi->create_knowledgemanagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgemanagementApi->create_knowledgemanagement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_knowledgemanagement_model** | [**CreateKnowledgemanagementModel**](CreateKnowledgemanagementModel.md)| request_data    | [optional] 

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

# **knowledgemanagement_cancel**
> Dict[str, object] knowledgemanagement_cancel(id, knowledgemanagement_cancel_model=knowledgemanagement_cancel_model)

Cancel a knowledge 🔐

If you get a bad value for param notrigger check, provide this in body { "notrigger": 0 }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.knowledgemanagement_cancel_model import KnowledgemanagementCancelModel
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
    api_instance = dolibarr_api.KnowledgemanagementApi(api_client)
    id = 56 # int | knowledge ID
    knowledgemanagement_cancel_model = dolibarr_api.KnowledgemanagementCancelModel() # KnowledgemanagementCancelModel | notrigger    (optional)

    try:
        # Cancel a knowledge 🔐
        api_response = api_instance.knowledgemanagement_cancel(id, knowledgemanagement_cancel_model=knowledgemanagement_cancel_model)
        print("The response of KnowledgemanagementApi->knowledgemanagement_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgemanagementApi->knowledgemanagement_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledge ID | 
 **knowledgemanagement_cancel_model** | [**KnowledgemanagementCancelModel**](KnowledgemanagementCancelModel.md)| notrigger    | [optional] 

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

# **knowledgemanagement_retrieve_categories**
> str knowledgemanagement_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get categories for a knowledgerecord object 🔐

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
    api_instance = dolibarr_api.KnowledgemanagementApi(api_client)
    id = 56 # int | ID of knowledgerecord object
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)

    try:
        # Get categories for a knowledgerecord object 🔐
        api_response = api_instance.knowledgemanagement_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
        print("The response of KnowledgemanagementApi->knowledgemanagement_retrieve_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgemanagementApi->knowledgemanagement_retrieve_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of knowledgerecord object | 
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledgemanagement_validate**
> Dict[str, object] knowledgemanagement_validate(id, knowledgemanagement_validate_model=knowledgemanagement_validate_model)

Validate a knowledge 🔐

If you get a bad value for param notrigger check, provide this in body { "notrigger": 0 }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.knowledgemanagement_validate_model import KnowledgemanagementValidateModel
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
    api_instance = dolibarr_api.KnowledgemanagementApi(api_client)
    id = 56 # int | knowledge ID
    knowledgemanagement_validate_model = dolibarr_api.KnowledgemanagementValidateModel() # KnowledgemanagementValidateModel | notrigger    (optional)

    try:
        # Validate a knowledge 🔐
        api_response = api_instance.knowledgemanagement_validate(id, knowledgemanagement_validate_model=knowledgemanagement_validate_model)
        print("The response of KnowledgemanagementApi->knowledgemanagement_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgemanagementApi->knowledgemanagement_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledge ID | 
 **knowledgemanagement_validate_model** | [**KnowledgemanagementValidateModel**](KnowledgemanagementValidateModel.md)| notrigger    | [optional] 

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

# **list_knowledgemanagement**
> List[str] list_knowledgemanagement(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, category=category, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

List knowledgerecords 🔐

Get a list of knowledgerecords

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
    api_instance = dolibarr_api.KnowledgemanagementApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    category = 56 # int | Use this param to filter list by category (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List knowledgerecords 🔐
        api_response = api_instance.list_knowledgemanagement(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, category=category, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of KnowledgemanagementApi->list_knowledgemanagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgemanagementApi->list_knowledgemanagement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
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
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_knowledgemanagement**
> List[str] remove_knowledgemanagement(id)

Delete knowledgerecord 🔐

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
    api_instance = dolibarr_api.KnowledgemanagementApi(api_client)
    id = 56 # int | KnowledgeRecord ID

    try:
        # Delete knowledgerecord 🔐
        api_response = api_instance.remove_knowledgemanagement(id)
        print("The response of KnowledgemanagementApi->remove_knowledgemanagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgemanagementApi->remove_knowledgemanagement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| KnowledgeRecord ID | 

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

# **retrieve_knowledgemanagement**
> Dict[str, object] retrieve_knowledgemanagement(id)

Get properties of a knowledgerecord object 🔐

Return an array with knowledgerecord information

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
    api_instance = dolibarr_api.KnowledgemanagementApi(api_client)
    id = 56 # int | ID of knowledgerecord

    try:
        # Get properties of a knowledgerecord object 🔐
        api_response = api_instance.retrieve_knowledgemanagement(id)
        print("The response of KnowledgemanagementApi->retrieve_knowledgemanagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgemanagementApi->retrieve_knowledgemanagement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of knowledgerecord | 

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
**403** | Not allowed |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_knowledgemanagement**
> Dict[str, object] update_knowledgemanagement(id, update_knowledgemanagement_model=update_knowledgemanagement_model)

Update knowledgerecord 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_knowledgemanagement_model import UpdateKnowledgemanagementModel
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
    api_instance = dolibarr_api.KnowledgemanagementApi(api_client)
    id = 56 # int | Id of knowledgerecord to update
    update_knowledgemanagement_model = dolibarr_api.UpdateKnowledgemanagementModel() # UpdateKnowledgemanagementModel | request_data    (optional)

    try:
        # Update knowledgerecord 🔐
        api_response = api_instance.update_knowledgemanagement(id, update_knowledgemanagement_model=update_knowledgemanagement_model)
        print("The response of KnowledgemanagementApi->update_knowledgemanagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgemanagementApi->update_knowledgemanagement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of knowledgerecord to update | 
 **update_knowledgemanagement_model** | [**UpdateKnowledgemanagementModel**](UpdateKnowledgemanagementModel.md)| request_data    | [optional] 

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

