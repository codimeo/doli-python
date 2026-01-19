# dolibarr_api.AgendaeventsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agendaevents**](AgendaeventsApi.md#create_agendaevents) | **POST** /agendaevents | Create an agenda event 🔐
[**list_agendaevents**](AgendaeventsApi.md#list_agendaevents) | **GET** /agendaevents | List agenda events 🔐
[**remove_agendaevents**](AgendaeventsApi.md#remove_agendaevents) | **DELETE** /agendaevents/{id} | Delete an agenda event 🔐
[**retrieve_agendaevents**](AgendaeventsApi.md#retrieve_agendaevents) | **GET** /agendaevents/{id} | Get agenda event 🔐
[**update_agendaevents**](AgendaeventsApi.md#update_agendaevents) | **PUT** /agendaevents/{id} | Update an agenda event 🔐


# **create_agendaevents**
> int create_agendaevents(create_agendaevents_model=create_agendaevents_model)

Create an agenda event 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_agendaevents_model import CreateAgendaeventsModel
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
    api_instance = dolibarr_api.AgendaeventsApi(api_client)
    create_agendaevents_model = dolibarr_api.CreateAgendaeventsModel() # CreateAgendaeventsModel | request_data    (optional)

    try:
        # Create an agenda event 🔐
        api_response = api_instance.create_agendaevents(create_agendaevents_model=create_agendaevents_model)
        print("The response of AgendaeventsApi->create_agendaevents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgendaeventsApi->create_agendaevents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_agendaevents_model** | [**CreateAgendaeventsModel**](CreateAgendaeventsModel.md)| request_data    | [optional] 

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

# **list_agendaevents**
> List[str] list_agendaevents(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

List agenda events 🔐

Get a list of agenda events

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
    api_instance = dolibarr_api.AgendaeventsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    user_ids = 'user_ids_example' # str | User ids filter field (owners of event). Example: '1' or '1,2,3' (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.label:like:'%dol%') and (t.datec:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List agenda events 🔐
        api_response = api_instance.list_agendaevents(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of AgendaeventsApi->list_agendaevents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgendaeventsApi->list_agendaevents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **user_ids** | **str**| User ids filter field (owners of event). Example: &#39;1&#39; or &#39;1,2,3&#39; | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.label:like:&#39;%dol%&#39;) and (t.datec:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
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

# **remove_agendaevents**
> List[str] remove_agendaevents(id)

Delete an agenda event 🔐

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
    api_instance = dolibarr_api.AgendaeventsApi(api_client)
    id = 56 # int | ID of Agenda Event to delete

    try:
        # Delete an agenda event 🔐
        api_response = api_instance.remove_agendaevents(id)
        print("The response of AgendaeventsApi->remove_agendaevents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgendaeventsApi->remove_agendaevents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Agenda Event to delete | 

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

# **retrieve_agendaevents**
> Dict[str, object] retrieve_agendaevents(id)

Get agenda event 🔐

Return an array with agenda event information

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
    api_instance = dolibarr_api.AgendaeventsApi(api_client)
    id = 56 # int | ID of Agenda Event to get

    try:
        # Get agenda event 🔐
        api_response = api_instance.retrieve_agendaevents(id)
        print("The response of AgendaeventsApi->retrieve_agendaevents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgendaeventsApi->retrieve_agendaevents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Agenda Event to get | 

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

# **update_agendaevents**
> str update_agendaevents(id, update_agendaevents_model=update_agendaevents_model)

Update an agenda event 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_agendaevents_model import UpdateAgendaeventsModel
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
    api_instance = dolibarr_api.AgendaeventsApi(api_client)
    id = 56 # int | ID of Agenda Event to update
    update_agendaevents_model = dolibarr_api.UpdateAgendaeventsModel() # UpdateAgendaeventsModel | request_data    (optional)

    try:
        # Update an agenda event 🔐
        api_response = api_instance.update_agendaevents(id, update_agendaevents_model=update_agendaevents_model)
        print("The response of AgendaeventsApi->update_agendaevents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgendaeventsApi->update_agendaevents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Agenda Event to update | 
 **update_agendaevents_model** | [**UpdateAgendaeventsModel**](UpdateAgendaeventsModel.md)| request_data    | [optional] 

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

