# dolibarr_api.EventattendeesApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eventattendees**](EventattendeesApi.md#create_eventattendees) | **POST** /eventattendees | Create an event attendee 🔐
[**eventattendees_remove_by_id**](EventattendeesApi.md#eventattendees_remove_by_id) | **DELETE** /eventattendees/{id} | Delete an event attendee 🔐
[**eventattendees_remove_by_ref**](EventattendeesApi.md#eventattendees_remove_by_ref) | **DELETE** /eventattendees/ref/{ref} | Delete an event attendee 🔐
[**eventattendees_retrieve_by_id**](EventattendeesApi.md#eventattendees_retrieve_by_id) | **GET** /eventattendees/{id} | Get properties of a event attendee by id 🔐
[**eventattendees_retrieve_by_ref**](EventattendeesApi.md#eventattendees_retrieve_by_ref) | **GET** /eventattendees/ref/{ref} | Get properties of an event attendee by ref 🔐
[**eventattendees_update_by_id**](EventattendeesApi.md#eventattendees_update_by_id) | **PUT** /eventattendees/{id} | Update an event attendee 🔐
[**eventattendees_update_by_ref**](EventattendeesApi.md#eventattendees_update_by_ref) | **PUT** /eventattendees/ref/{ref} | Update an event attendee 🔐
[**list_eventattendees**](EventattendeesApi.md#list_eventattendees) | **GET** /eventattendees | List Event attendees 🔐


# **create_eventattendees**
> int create_eventattendees(create_eventattendees_model=create_eventattendees_model)

Create an event attendee 🔐

Example: {"module":"adherent","type_template":"member","active": 1,"ref":"(SendingEmailOnAutoSubscription)","fk_user":0,"joinfiles": "0", ... } Required: {"ref":"myBestTemplate","topic":"myBestOffer","type_template":"propal_send"}

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_eventattendees_model import CreateEventattendeesModel
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
    api_instance = dolibarr_api.EventattendeesApi(api_client)
    create_eventattendees_model = dolibarr_api.CreateEventattendeesModel() # CreateEventattendeesModel | request_data    (optional)

    try:
        # Create an event attendee 🔐
        api_response = api_instance.create_eventattendees(create_eventattendees_model=create_eventattendees_model)
        print("The response of EventattendeesApi->create_eventattendees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventattendeesApi->create_eventattendees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_eventattendees_model** | [**CreateEventattendeesModel**](CreateEventattendeesModel.md)| request_data    | [optional] 

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
**304** | Not Modified |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eventattendees_remove_by_id**
> List[str] eventattendees_remove_by_id(id)

Delete an event attendee 🔐

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
    api_instance = dolibarr_api.EventattendeesApi(api_client)
    id = 56 # int | event attendee ID

    try:
        # Delete an event attendee 🔐
        api_response = api_instance.eventattendees_remove_by_id(id)
        print("The response of EventattendeesApi->eventattendees_remove_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventattendeesApi->eventattendees_remove_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| event attendee ID | 

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

# **eventattendees_remove_by_ref**
> List[str] eventattendees_remove_by_ref(ref)

Delete an event attendee 🔐

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
    api_instance = dolibarr_api.EventattendeesApi(api_client)
    ref = 'ref_example' # str | event attendee ref

    try:
        # Delete an event attendee 🔐
        api_response = api_instance.eventattendees_remove_by_ref(ref)
        print("The response of EventattendeesApi->eventattendees_remove_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventattendeesApi->eventattendees_remove_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| event attendee ref | 

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

# **eventattendees_retrieve_by_id**
> Dict[str, object] eventattendees_retrieve_by_id(id)

Get properties of a event attendee by id 🔐

Return an array with event attendee information

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
    api_instance = dolibarr_api.EventattendeesApi(api_client)
    id = 56 # int | ID of event attendee

    try:
        # Get properties of a event attendee by id 🔐
        api_response = api_instance.eventattendees_retrieve_by_id(id)
        print("The response of EventattendeesApi->eventattendees_retrieve_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventattendeesApi->eventattendees_retrieve_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of event attendee | 

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

# **eventattendees_retrieve_by_ref**
> Dict[str, object] eventattendees_retrieve_by_ref(ref)

Get properties of an event attendee by ref 🔐

Return an array with order information

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
    api_instance = dolibarr_api.EventattendeesApi(api_client)
    ref = 'ref_example' # str | Ref of object

    try:
        # Get properties of an event attendee by ref 🔐
        api_response = api_instance.eventattendees_retrieve_by_ref(ref)
        print("The response of EventattendeesApi->eventattendees_retrieve_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventattendeesApi->eventattendees_retrieve_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of object | 

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

# **eventattendees_update_by_id**
> Dict[str, object] eventattendees_update_by_id(id, eventattendees_update_by_id_model=eventattendees_update_by_id_model)

Update an event attendee 🔐

Example: {"module":"adherent","type_template":"member","active": 1,"ref":"(SendingEmailOnAutoSubscription)","fk_user":0,"joinfiles": "0", ... } Required: {"ref":"myBestTemplate","topic":"myBestOffer","type_template":"propal_send"}

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.eventattendees_update_by_id_model import EventattendeesUpdateByIdModel
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
    api_instance = dolibarr_api.EventattendeesApi(api_client)
    id = 56 # int | Id of order to update
    eventattendees_update_by_id_model = dolibarr_api.EventattendeesUpdateByIdModel() # EventattendeesUpdateByIdModel | request_data    (optional)

    try:
        # Update an event attendee 🔐
        api_response = api_instance.eventattendees_update_by_id(id, eventattendees_update_by_id_model=eventattendees_update_by_id_model)
        print("The response of EventattendeesApi->eventattendees_update_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventattendeesApi->eventattendees_update_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **eventattendees_update_by_id_model** | [**EventattendeesUpdateByIdModel**](EventattendeesUpdateByIdModel.md)| request_data    | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eventattendees_update_by_ref**
> Dict[str, object] eventattendees_update_by_ref(ref, eventattendees_update_by_ref_model=eventattendees_update_by_ref_model)

Update an event attendee 🔐

Example: {"module":"adherent","type_template":"member","active": 1,"ref":"(SendingEmailOnAutoSubscription)","fk_user":0,"joinfiles": "0", ... } Required: {"ref":"myBestTemplate","topic":"myBestOffer","type_template":"propal_send"}

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.eventattendees_update_by_ref_model import EventattendeesUpdateByRefModel
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
    api_instance = dolibarr_api.EventattendeesApi(api_client)
    ref = 'ref_example' # str | Ref of order to update
    eventattendees_update_by_ref_model = dolibarr_api.EventattendeesUpdateByRefModel() # EventattendeesUpdateByRefModel | request_data    (optional)

    try:
        # Update an event attendee 🔐
        api_response = api_instance.eventattendees_update_by_ref(ref, eventattendees_update_by_ref_model=eventattendees_update_by_ref_model)
        print("The response of EventattendeesApi->eventattendees_update_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventattendeesApi->eventattendees_update_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of order to update | 
 **eventattendees_update_by_ref_model** | [**EventattendeesUpdateByRefModel**](EventattendeesUpdateByRefModel.md)| request_data    | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_eventattendees**
> List[str] list_eventattendees(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

List Event attendees 🔐

Get a list of Event attendees

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
    api_instance = dolibarr_api.EventattendeesApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.status:=:1) and (t.email:=:'bad@example.com')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List Event attendees 🔐
        api_response = api_instance.list_eventattendees(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of EventattendeesApi->list_eventattendees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventattendeesApi->list_eventattendees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.status:&#x3D;:1) and (t.email:&#x3D;:&#39;bad@example.com&#39;)\&quot; | [optional] 
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
**403** | Access denied |  -  |
**503** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

