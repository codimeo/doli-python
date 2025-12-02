# dolibarr_api.InterventionsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_interventions**](InterventionsApi.md#create_interventions) | **POST** /interventions | Create an intervention 🔐
[**interventions_close_fichinter**](InterventionsApi.md#interventions_close_fichinter) | **POST** /interventions/{id}/close | Close an intervention 🔐
[**interventions_create_line**](InterventionsApi.md#interventions_create_line) | **POST** /interventions/{id}/lines | Add a line to an intervention 🔐
[**interventions_reopen**](InterventionsApi.md#interventions_reopen) | **POST** /interventions/{id}/reopen | Reopen an intervention 🔐
[**interventions_validate**](InterventionsApi.md#interventions_validate) | **POST** /interventions/{id}/validate | Validate an intervention 🔐
[**list_interventions**](InterventionsApi.md#list_interventions) | **GET** /interventions | List interventions 🔐
[**remove_interventions**](InterventionsApi.md#remove_interventions) | **DELETE** /interventions/{id} | Delete an intervention 🔐
[**retrieve_interventions**](InterventionsApi.md#retrieve_interventions) | **GET** /interventions/{id} | Get an intervention Return an array with intervention information 🔐
[**update_interventions**](InterventionsApi.md#update_interventions) | **PUT** /interventions/{id} | Update intervention general fields (won&#39;t touch lines of fichinter) 🔐


# **create_interventions**
> int create_interventions(create_interventions_model=create_interventions_model)

Create an intervention 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_interventions_model import CreateInterventionsModel
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
    api_instance = dolibarr_api.InterventionsApi(api_client)
    create_interventions_model = dolibarr_api.CreateInterventionsModel() # CreateInterventionsModel | request_data    (optional)

    try:
        # Create an intervention 🔐
        api_response = api_instance.create_interventions(create_interventions_model=create_interventions_model)
        print("The response of InterventionsApi->create_interventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterventionsApi->create_interventions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_interventions_model** | [**CreateInterventionsModel**](CreateInterventionsModel.md)| request_data    | [optional] 

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

# **interventions_close_fichinter**
> Dict[str, object] interventions_close_fichinter(id)

Close an intervention 🔐

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
    api_instance = dolibarr_api.InterventionsApi(api_client)
    id = 56 # int | Intervention ID

    try:
        # Close an intervention 🔐
        api_response = api_instance.interventions_close_fichinter(id)
        print("The response of InterventionsApi->interventions_close_fichinter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterventionsApi->interventions_close_fichinter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Intervention ID | 

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

# **interventions_create_line**
> int interventions_create_line(id, interventions_create_line_model=interventions_create_line_model)

Add a line to an intervention 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.interventions_create_line_model import InterventionsCreateLineModel
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
    api_instance = dolibarr_api.InterventionsApi(api_client)
    id = 56 # int | ID of intervention to update
    interventions_create_line_model = dolibarr_api.InterventionsCreateLineModel() # InterventionsCreateLineModel | request_data    (optional)

    try:
        # Add a line to an intervention 🔐
        api_response = api_instance.interventions_create_line(id, interventions_create_line_model=interventions_create_line_model)
        print("The response of InterventionsApi->interventions_create_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterventionsApi->interventions_create_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of intervention to update | 
 **interventions_create_line_model** | [**InterventionsCreateLineModel**](InterventionsCreateLineModel.md)| request_data    | [optional] 

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

# **interventions_reopen**
> Dict[str, object] interventions_reopen(id)

Reopen an intervention 🔐

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
    api_instance = dolibarr_api.InterventionsApi(api_client)
    id = 56 # int | Intervention ID

    try:
        # Reopen an intervention 🔐
        api_response = api_instance.interventions_reopen(id)
        print("The response of InterventionsApi->interventions_reopen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterventionsApi->interventions_reopen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Intervention ID | 

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

# **interventions_validate**
> Dict[str, object] interventions_validate(id, interventions_validate_model=interventions_validate_model)

Validate an intervention 🔐

If you get a bad value for param notrigger check, provide this in body { "notrigger": 0 }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.interventions_validate_model import InterventionsValidateModel
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
    api_instance = dolibarr_api.InterventionsApi(api_client)
    id = 56 # int | Intervention ID
    interventions_validate_model = dolibarr_api.InterventionsValidateModel() # InterventionsValidateModel | notrigger    (optional)

    try:
        # Validate an intervention 🔐
        api_response = api_instance.interventions_validate(id, interventions_validate_model=interventions_validate_model)
        print("The response of InterventionsApi->interventions_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterventionsApi->interventions_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Intervention ID | 
 **interventions_validate_model** | [**InterventionsValidateModel**](InterventionsValidateModel.md)| notrigger    | [optional] 

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

# **list_interventions**
> List[str] list_interventions(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, contact_type=contact_type, pagination_data=pagination_data)

List interventions 🔐

Get a list of interventions

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
    api_instance = dolibarr_api.InterventionsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter orders of (example '1' or '1,2,3') (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of property names (optional)
    contact_type = 'contact_type_example' # str | Type of contacts: thirdparty, internal or external (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List interventions 🔐
        api_response = api_instance.list_interventions(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, contact_type=contact_type, pagination_data=pagination_data)
        print("The response of InterventionsApi->list_interventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterventionsApi->list_interventions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter orders of (example &#39;1&#39; or &#39;1,2,3&#39;) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.date_creation:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
 **properties** | **str**| Restrict the data returned to these properties. Ignored if empty. Comma separated list of property names | [optional] 
 **contact_type** | **str**| Type of contacts: thirdparty, internal or external | [optional] 
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

# **remove_interventions**
> List[str] remove_interventions(id)

Delete an intervention 🔐

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
    api_instance = dolibarr_api.InterventionsApi(api_client)
    id = 56 # int | Intervention ID

    try:
        # Delete an intervention 🔐
        api_response = api_instance.remove_interventions(id)
        print("The response of InterventionsApi->remove_interventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterventionsApi->remove_interventions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Intervention ID | 

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

# **retrieve_interventions**
> Dict[str, object] retrieve_interventions(id, ref=ref, ref_ext=ref_ext, contact_list=contact_list)

Get an intervention Return an array with intervention information 🔐

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
    api_instance = dolibarr_api.InterventionsApi(api_client)
    id = 56 # int | ID of intervention
    ref = 'ref_example' # str | Ref of object (optional)
    ref_ext = 'ref_ext_example' # str | External reference of object (optional)
    contact_list = 56 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id, -1: Do not return contacts/adddesses (optional)

    try:
        # Get an intervention Return an array with intervention information 🔐
        api_response = api_instance.retrieve_interventions(id, ref=ref, ref_ext=ref_ext, contact_list=contact_list)
        print("The response of InterventionsApi->retrieve_interventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterventionsApi->retrieve_interventions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of intervention | 
 **ref** | **str**| Ref of object | [optional] 
 **ref_ext** | **str**| External reference of object | [optional] 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id, -1: Do not return contacts/adddesses | [optional] 

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

# **update_interventions**
> Dict[str, object] update_interventions(id, update_interventions_model=update_interventions_model)

Update intervention general fields (won't touch lines of fichinter) 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_interventions_model import UpdateInterventionsModel
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
    api_instance = dolibarr_api.InterventionsApi(api_client)
    id = 56 # int | ID of fichinter to update
    update_interventions_model = dolibarr_api.UpdateInterventionsModel() # UpdateInterventionsModel | request_data    (optional)

    try:
        # Update intervention general fields (won't touch lines of fichinter) 🔐
        api_response = api_instance.update_interventions(id, update_interventions_model=update_interventions_model)
        print("The response of InterventionsApi->update_interventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InterventionsApi->update_interventions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of fichinter to update | 
 **update_interventions_model** | [**UpdateInterventionsModel**](UpdateInterventionsModel.md)| request_data    | [optional] 

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

