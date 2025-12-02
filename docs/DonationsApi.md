# dolibarr_api.DonationsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_donations**](DonationsApi.md#create_donations) | **POST** /donations | Create donation object 🔐
[**donations_validate**](DonationsApi.md#donations_validate) | **POST** /donations/{id}/validate | Validate an donation 🔐
[**list_donations**](DonationsApi.md#list_donations) | **GET** /donations | List donations 🔐
[**remove_donations**](DonationsApi.md#remove_donations) | **DELETE** /donations/{id} | Delete donation 🔐
[**retrieve_donations**](DonationsApi.md#retrieve_donations) | **GET** /donations/{id} | Get properties of an donation object 🔐
[**update_donations**](DonationsApi.md#update_donations) | **PUT** /donations/{id} | Update order general fields (won&#39;t touch lines of order) 🔐


# **create_donations**
> int create_donations(create_donations_model=create_donations_model)

Create donation object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_donations_model import CreateDonationsModel
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
    api_instance = dolibarr_api.DonationsApi(api_client)
    create_donations_model = dolibarr_api.CreateDonationsModel() # CreateDonationsModel | request_data    (optional)

    try:
        # Create donation object 🔐
        api_response = api_instance.create_donations(create_donations_model=create_donations_model)
        print("The response of DonationsApi->create_donations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationsApi->create_donations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_donations_model** | [**CreateDonationsModel**](CreateDonationsModel.md)| request_data    | [optional] 

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

# **donations_validate**
> str donations_validate(id, donations_validate_model=donations_validate_model)

Validate an donation 🔐

If you get a bad value for param notrigger check, provide this in body { "idwarehouse": 0, "notrigger": 0 }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.donations_validate_model import DonationsValidateModel
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
    api_instance = dolibarr_api.DonationsApi(api_client)
    id = 56 # int | Order ID
    donations_validate_model = dolibarr_api.DonationsValidateModel() # DonationsValidateModel | idwarehouse   notrigger    (optional)

    try:
        # Validate an donation 🔐
        api_response = api_instance.donations_validate(id, donations_validate_model=donations_validate_model)
        print("The response of DonationsApi->donations_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationsApi->donations_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **donations_validate_model** | [**DonationsValidateModel**](DonationsValidateModel.md)| idwarehouse   notrigger    | [optional] 

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
**304** | Not Modified |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_donations**
> List[str] list_donations(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

List donations 🔐

Get a list of donations

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
    api_instance = dolibarr_api.DonationsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter orders of (example '1' or '1,2,3') (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List donations 🔐
        api_response = api_instance.list_donations(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of DonationsApi->list_donations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationsApi->list_donations: %s\n" % e)
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

# **remove_donations**
> List[str] remove_donations(id)

Delete donation 🔐

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
    api_instance = dolibarr_api.DonationsApi(api_client)
    id = 56 # int | Order ID

    try:
        # Delete donation 🔐
        api_response = api_instance.remove_donations(id)
        print("The response of DonationsApi->remove_donations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationsApi->remove_donations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 

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

# **retrieve_donations**
> Dict[str, object] retrieve_donations(id)

Get properties of an donation object 🔐

Return an array with donation information

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
    api_instance = dolibarr_api.DonationsApi(api_client)
    id = 56 # int | ID of order

    try:
        # Get properties of an donation object 🔐
        api_response = api_instance.retrieve_donations(id)
        print("The response of DonationsApi->retrieve_donations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationsApi->retrieve_donations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of order | 

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

# **update_donations**
> Dict[str, object] update_donations(id, update_donations_model=update_donations_model)

Update order general fields (won't touch lines of order) 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_donations_model import UpdateDonationsModel
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
    api_instance = dolibarr_api.DonationsApi(api_client)
    id = 56 # int | Id of order to update
    update_donations_model = dolibarr_api.UpdateDonationsModel() # UpdateDonationsModel | request_data    (optional)

    try:
        # Update order general fields (won't touch lines of order) 🔐
        api_response = api_instance.update_donations(id, update_donations_model=update_donations_model)
        print("The response of DonationsApi->update_donations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationsApi->update_donations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **update_donations_model** | [**UpdateDonationsModel**](UpdateDonationsModel.md)| request_data    | [optional] 

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

