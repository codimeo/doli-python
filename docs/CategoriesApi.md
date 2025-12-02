# dolibarr_api.CategoriesApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_link_object_by_id**](CategoriesApi.md#categories_link_object_by_id) | **POST** /categories/{id}/objects/{type}/{object_id} | Link an object to a category by id 🔐
[**categories_link_object_by_ref**](CategoriesApi.md#categories_link_object_by_ref) | **POST** /categories/{id}/objects/{type}/ref/{object_ref} | Link an object to a category by ref 🔐
[**categories_retrieve_list_for_object**](CategoriesApi.md#categories_retrieve_list_for_object) | **GET** /categories/object/{type}/{id} | List categories of an object 🔐
[**categories_retrieve_objects**](CategoriesApi.md#categories_retrieve_objects) | **GET** /categories/{id}/objects | Get the list of objects in a category. 🔐
[**categories_unlink_object_by_id**](CategoriesApi.md#categories_unlink_object_by_id) | **DELETE** /categories/{id}/objects/{type}/{object_id} | Unlink an object from a category by id 🔐
[**categories_unlink_object_by_ref**](CategoriesApi.md#categories_unlink_object_by_ref) | **DELETE** /categories/{id}/objects/{type}/ref/{object_ref} | Unlink an object from a category by ref 🔐
[**create_categories**](CategoriesApi.md#create_categories) | **POST** /categories | Create category object 🔐
[**list_categories**](CategoriesApi.md#list_categories) | **GET** /categories | List categories 🔐
[**remove_categories**](CategoriesApi.md#remove_categories) | **DELETE** /categories/{id} | Delete category 🔐
[**retrieve_categories**](CategoriesApi.md#retrieve_categories) | **GET** /categories/{id} | Get properties of a category object 🔐
[**update_categories**](CategoriesApi.md#update_categories) | **PUT** /categories/{id} | Update category 🔐


# **categories_link_object_by_id**
> List[str] categories_link_object_by_id(id, type, object_id)

Link an object to a category by id 🔐

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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    id = 56 # int | ID of category
    type = 'type_example' # str | Type of category ('member', 'customer', 'supplier', 'product', 'contact', 'actioncomm')
    object_id = 56 # int | ID of object

    try:
        # Link an object to a category by id 🔐
        api_response = api_instance.categories_link_object_by_id(id, type, object_id)
        print("The response of CategoriesApi->categories_link_object_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->categories_link_object_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of category | 
 **type** | **str**| Type of category (&#39;member&#39;, &#39;customer&#39;, &#39;supplier&#39;, &#39;product&#39;, &#39;contact&#39;, &#39;actioncomm&#39;) | 
 **object_id** | **int**| ID of object | 

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

# **categories_link_object_by_ref**
> List[str] categories_link_object_by_ref(id, type, object_ref)

Link an object to a category by ref 🔐

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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    id = 56 # int | ID of category
    type = 'type_example' # str | Type of category ('member', 'customer', 'supplier', 'product', 'contact')
    object_ref = 'object_ref_example' # str | Reference of object (product, thirdparty, member, ...)

    try:
        # Link an object to a category by ref 🔐
        api_response = api_instance.categories_link_object_by_ref(id, type, object_ref)
        print("The response of CategoriesApi->categories_link_object_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->categories_link_object_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of category | 
 **type** | **str**| Type of category (&#39;member&#39;, &#39;customer&#39;, &#39;supplier&#39;, &#39;product&#39;, &#39;contact&#39;) | 
 **object_ref** | **str**| Reference of object (product, thirdparty, member, ...) | 

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

# **categories_retrieve_list_for_object**
> List[str] categories_retrieve_list_for_object(id, type, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

List categories of an object 🔐

Get the list of categories linked to an object

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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    id = 56 # int | Object ID
    type = 'type_example' # str | Type of category ('member', 'customer', 'supplier', 'product', 'contact', 'project', 'actioncomm')
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)

    try:
        # List categories of an object 🔐
        api_response = api_instance.categories_retrieve_list_for_object(id, type, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
        print("The response of CategoriesApi->categories_retrieve_list_for_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->categories_retrieve_list_for_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Object ID | 
 **type** | **str**| Type of category (&#39;member&#39;, &#39;customer&#39;, &#39;supplier&#39;, &#39;product&#39;, &#39;contact&#39;, &#39;project&#39;, &#39;actioncomm&#39;) | 
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 

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

# **categories_retrieve_objects**
> str categories_retrieve_objects(id, type, onlyids=onlyids)

Get the list of objects in a category. 🔐

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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    id = 56 # int | ID of category
    type = 'type_example' # str | Type of category ('member', 'customer', 'supplier', 'product', 'contact', 'project')
    onlyids = 56 # int | Return only ids of objects (consume less memory) (optional)

    try:
        # Get the list of objects in a category. 🔐
        api_response = api_instance.categories_retrieve_objects(id, type, onlyids=onlyids)
        print("The response of CategoriesApi->categories_retrieve_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->categories_retrieve_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of category | 
 **type** | **str**| Type of category (&#39;member&#39;, &#39;customer&#39;, &#39;supplier&#39;, &#39;product&#39;, &#39;contact&#39;, &#39;project&#39;) | 
 **onlyids** | **int**| Return only ids of objects (consume less memory) | [optional] 

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

# **categories_unlink_object_by_id**
> List[str] categories_unlink_object_by_id(id, type, object_id)

Unlink an object from a category by id 🔐

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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    id = 56 # int | ID of category
    type = 'type_example' # str | Type of category ('member', 'customer', 'supplier', 'product', 'contact', 'actioncomm')
    object_id = 56 # int | ID of the object

    try:
        # Unlink an object from a category by id 🔐
        api_response = api_instance.categories_unlink_object_by_id(id, type, object_id)
        print("The response of CategoriesApi->categories_unlink_object_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->categories_unlink_object_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of category | 
 **type** | **str**| Type of category (&#39;member&#39;, &#39;customer&#39;, &#39;supplier&#39;, &#39;product&#39;, &#39;contact&#39;, &#39;actioncomm&#39;) | 
 **object_id** | **int**| ID of the object | 

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

# **categories_unlink_object_by_ref**
> List[str] categories_unlink_object_by_ref(id, type, object_ref)

Unlink an object from a category by ref 🔐

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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    id = 56 # int | ID of category
    type = 'type_example' # str | Type of category ('member', 'customer', 'supplier', 'product', 'contact', 'actioncomm')
    object_ref = 'object_ref_example' # str | Reference of the object (product, thirdparty, member, ...)

    try:
        # Unlink an object from a category by ref 🔐
        api_response = api_instance.categories_unlink_object_by_ref(id, type, object_ref)
        print("The response of CategoriesApi->categories_unlink_object_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->categories_unlink_object_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of category | 
 **type** | **str**| Type of category (&#39;member&#39;, &#39;customer&#39;, &#39;supplier&#39;, &#39;product&#39;, &#39;contact&#39;, &#39;actioncomm&#39;) | 
 **object_ref** | **str**| Reference of the object (product, thirdparty, member, ...) | 

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

# **create_categories**
> int create_categories(create_categories_model=create_categories_model)

Create category object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_categories_model import CreateCategoriesModel
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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    create_categories_model = dolibarr_api.CreateCategoriesModel() # CreateCategoriesModel | request_data    (optional)

    try:
        # Create category object 🔐
        api_response = api_instance.create_categories(create_categories_model=create_categories_model)
        print("The response of CategoriesApi->create_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->create_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_categories_model** | [**CreateCategoriesModel**](CreateCategoriesModel.md)| request_data    | [optional] 

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

# **list_categories**
> List[str] list_categories(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, sqlfilters=sqlfilters, properties=properties)

List categories 🔐

Get a list of categories according to filters

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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    type = 'type_example' # str | Type of category ('member', 'customer', 'supplier', 'product', 'contact', 'actioncomm') (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # List categories 🔐
        api_response = api_instance.list_categories(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, sqlfilters=sqlfilters, properties=properties)
        print("The response of CategoriesApi->list_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->list_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **type** | **str**| Type of category (&#39;member&#39;, &#39;customer&#39;, &#39;supplier&#39;, &#39;product&#39;, &#39;contact&#39;, &#39;actioncomm&#39;) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.date_creation:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
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

# **remove_categories**
> List[str] remove_categories(id)

Delete category 🔐

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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    id = 56 # int | Category ID

    try:
        # Delete category 🔐
        api_response = api_instance.remove_categories(id)
        print("The response of CategoriesApi->remove_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->remove_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Category ID | 

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

# **retrieve_categories**
> List[str] retrieve_categories(id, include_childs=include_childs)

Get properties of a category object 🔐

Return an array with category information

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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    id = 56 # int | ID of category
    include_childs = True # bool | Include child categories list (true or false) (optional)

    try:
        # Get properties of a category object 🔐
        api_response = api_instance.retrieve_categories(id, include_childs=include_childs)
        print("The response of CategoriesApi->retrieve_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->retrieve_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of category | 
 **include_childs** | **bool**| Include child categories list (true or false) | [optional] 

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

# **update_categories**
> Dict[str, object] update_categories(id, update_categories_model=update_categories_model)

Update category 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_categories_model import UpdateCategoriesModel
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
    api_instance = dolibarr_api.CategoriesApi(api_client)
    id = 56 # int | Id of category to update
    update_categories_model = dolibarr_api.UpdateCategoriesModel() # UpdateCategoriesModel | request_data    (optional)

    try:
        # Update category 🔐
        api_response = api_instance.update_categories(id, update_categories_model=update_categories_model)
        print("The response of CategoriesApi->update_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->update_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of category to update | 
 **update_categories_model** | [**UpdateCategoriesModel**](UpdateCategoriesModel.md)| request_data    | [optional] 

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

