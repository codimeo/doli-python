# dolibarr_api.ContactsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contacts_add_category**](ContactsApi.md#contacts_add_category) | **PUT** /contacts/{id}/categories/{category_id} | Add a category to a contact 🔐
[**contacts_create_user**](ContactsApi.md#contacts_create_user) | **POST** /contacts/{id}/createUser | Create a user account object from contact (external user) 🔐
[**contacts_remove_category**](ContactsApi.md#contacts_remove_category) | **DELETE** /contacts/{id}/categories/{category_id} | Remove the link between a category and a contact 🔐
[**contacts_retrieve_by_email**](ContactsApi.md#contacts_retrieve_by_email) | **GET** /contacts/email/{email} | Get a contact by Email 🔐
[**contacts_retrieve_categories**](ContactsApi.md#contacts_retrieve_categories) | **GET** /contacts/{id}/categories | Get categories of a contact 🔐
[**create_contacts**](ContactsApi.md#create_contacts) | **POST** /contacts | Create a contact 🔐
[**list_contacts**](ContactsApi.md#list_contacts) | **GET** /contacts | List contacts 🔐
[**remove_contacts**](ContactsApi.md#remove_contacts) | **DELETE** /contacts/{id} | Delete a contact 🔐
[**retrieve_contacts**](ContactsApi.md#retrieve_contacts) | **GET** /contacts/{id} | Get a contact 🔐
[**update_contacts**](ContactsApi.md#update_contacts) | **PUT** /contacts/{id} | Update a contact 🔐


# **contacts_add_category**
> str contacts_add_category(id, category_id)

Add a category to a contact 🔐

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
    api_instance = dolibarr_api.ContactsApi(api_client)
    id = 56 # int | ID of contact
    category_id = 56 # int | ID of category

    try:
        # Add a category to a contact 🔐
        api_response = api_instance.contacts_add_category(id, category_id)
        print("The response of ContactsApi->contacts_add_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_add_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of contact | 
 **category_id** | **int**| ID of category | 

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
**401** | Insufficient rights |  -  |
**404** | Category or contact not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_create_user**
> int contacts_create_user(id, contacts_create_user_model=contacts_create_user_model)

Create a user account object from contact (external user) 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.contacts_create_user_model import ContactsCreateUserModel
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
    api_instance = dolibarr_api.ContactsApi(api_client)
    id = 56 # int | ID of contact
    contacts_create_user_model = dolibarr_api.ContactsCreateUserModel() # ContactsCreateUserModel | request_data    (optional)

    try:
        # Create a user account object from contact (external user) 🔐
        api_response = api_instance.contacts_create_user(id, contacts_create_user_model=contacts_create_user_model)
        print("The response of ContactsApi->contacts_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of contact | 
 **contacts_create_user_model** | [**ContactsCreateUserModel**](ContactsCreateUserModel.md)| request_data    | [optional] 

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

# **contacts_remove_category**
> str contacts_remove_category(id, category_id)

Remove the link between a category and a contact 🔐

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
    api_instance = dolibarr_api.ContactsApi(api_client)
    id = 56 # int | ID of contact
    category_id = 56 # int | ID of category

    try:
        # Remove the link between a category and a contact 🔐
        api_response = api_instance.contacts_remove_category(id, category_id)
        print("The response of ContactsApi->contacts_remove_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_remove_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of contact | 
 **category_id** | **int**| ID of category | 

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
**401** | Insufficient rights |  -  |
**404** | Category or contact not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_retrieve_by_email**
> str contacts_retrieve_by_email(email, includecount=includecount, includeroles=includeroles)

Get a contact by Email 🔐

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
    api_instance = dolibarr_api.ContactsApi(api_client)
    email = 'email_example' # str | Email of contact
    includecount = 56 # int | Include count of elements the contact is used as a link for (optional)
    includeroles = 56 # int | Includes roles of the contact (optional)

    try:
        # Get a contact by Email 🔐
        api_response = api_instance.contacts_retrieve_by_email(email, includecount=includecount, includeroles=includeroles)
        print("The response of ContactsApi->contacts_retrieve_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_retrieve_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of contact | 
 **includecount** | **int**| Include count of elements the contact is used as a link for | [optional] 
 **includeroles** | **int**| Includes roles of the contact | [optional] 

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
**401** | Insufficient rights |  -  |
**404** | User or group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_retrieve_categories**
> str contacts_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get categories of a contact 🔐

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
    api_instance = dolibarr_api.ContactsApi(api_client)
    id = 56 # int | ID of contact
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)

    try:
        # Get categories of a contact 🔐
        api_response = api_instance.contacts_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
        print("The response of ContactsApi->contacts_retrieve_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->contacts_retrieve_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of contact | 
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

# **create_contacts**
> int create_contacts(create_contacts_model=create_contacts_model)

Create a contact 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_contacts_model import CreateContactsModel
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
    api_instance = dolibarr_api.ContactsApi(api_client)
    create_contacts_model = dolibarr_api.CreateContactsModel() # CreateContactsModel | request_data    (optional)

    try:
        # Create a contact 🔐
        api_response = api_instance.create_contacts(create_contacts_model=create_contacts_model)
        print("The response of ContactsApi->create_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->create_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contacts_model** | [**CreateContactsModel**](CreateContactsModel.md)| request_data    | [optional] 

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

# **list_contacts**
> str list_contacts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, category=category, sqlfilters=sqlfilters, includecount=includecount, includeroles=includeroles, properties=properties, pagination_data=pagination_data)

List contacts 🔐

Get a list of contacts

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
    api_instance = dolibarr_api.ContactsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    thirdparty_ids = 'thirdparty_ids_example' # str | Third party ids to filter contacts of (example '1' or '1,2,3') (optional)
    category = 56 # int | Use this param to filter list by category (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    includecount = 56 # int | Include count of elements the contact is used as a link for (optional)
    includeroles = 56 # int | Includes roles of the contact (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true, the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List contacts 🔐
        api_response = api_instance.list_contacts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, category=category, sqlfilters=sqlfilters, includecount=includecount, includeroles=includeroles, properties=properties, pagination_data=pagination_data)
        print("The response of ContactsApi->list_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->list_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Third party ids to filter contacts of (example &#39;1&#39; or &#39;1,2,3&#39;) | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.date_creation:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
 **includecount** | **int**| Include count of elements the contact is used as a link for | [optional] 
 **includeroles** | **int**| Includes roles of the contact | [optional] 
 **properties** | **str**| Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names | [optional] 
 **pagination_data** | **bool**| If this parameter is set to true, the response will include pagination data. Default value is false. Page starts from 0* | [optional] 

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

# **remove_contacts**
> str remove_contacts(id)

Delete a contact 🔐

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
    api_instance = dolibarr_api.ContactsApi(api_client)
    id = 56 # int | Contact ID

    try:
        # Delete a contact 🔐
        api_response = api_instance.remove_contacts(id)
        print("The response of ContactsApi->remove_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->remove_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Contact ID | 

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

# **retrieve_contacts**
> str retrieve_contacts(id, includecount=includecount, includeroles=includeroles)

Get a contact 🔐

Return an array with contact information

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
    api_instance = dolibarr_api.ContactsApi(api_client)
    id = 56 # int | ID of contact
    includecount = 56 # int | Include count of elements the contact is used as a link for (optional)
    includeroles = 56 # int | Includes roles of the contact (optional)

    try:
        # Get a contact 🔐
        api_response = api_instance.retrieve_contacts(id, includecount=includecount, includeroles=includeroles)
        print("The response of ContactsApi->retrieve_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->retrieve_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of contact | 
 **includecount** | **int**| Include count of elements the contact is used as a link for | [optional] 
 **includeroles** | **int**| Includes roles of the contact | [optional] 

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

# **update_contacts**
> str update_contacts(id, update_contacts_model=update_contacts_model)

Update a contact 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_contacts_model import UpdateContactsModel
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
    api_instance = dolibarr_api.ContactsApi(api_client)
    id = 56 # int | ID of contact to update
    update_contacts_model = dolibarr_api.UpdateContactsModel() # UpdateContactsModel | request_data    (optional)

    try:
        # Update a contact 🔐
        api_response = api_instance.update_contacts(id, update_contacts_model=update_contacts_model)
        print("The response of ContactsApi->update_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->update_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of contact to update | 
 **update_contacts_model** | [**UpdateContactsModel**](UpdateContactsModel.md)| request_data    | [optional] 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

