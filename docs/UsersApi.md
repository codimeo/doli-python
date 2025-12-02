# dolibarr_api.UsersApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_users**](UsersApi.md#create_users) | **POST** /users | Create a user 🔐
[**list_users**](UsersApi.md#list_users) | **GET** /users | List users 🔐
[**remove_users**](UsersApi.md#remove_users) | **DELETE** /users/{id} | Delete a user 🔐
[**retrieve_users**](UsersApi.md#retrieve_users) | **GET** /users/{id} | Get a user 🔐
[**update_users**](UsersApi.md#update_users) | **PUT** /users/{id} | Update a user 🔐
[**users_create_user_notification**](UsersApi.md#users_create_user_notification) | **POST** /users/{id}/notifications | Create a notification for a user 🔐
[**users_create_user_notification_by_code**](UsersApi.md#users_create_user_notification_by_code) | **POST** /users/{id}/notificationsbycode/{code} | Create a notification for a user using action trigger code 🔐
[**users_info_groups**](UsersApi.md#users_info_groups) | **GET** /users/groups/{group} | Get properties of a user group 🔐
[**users_list_groups**](UsersApi.md#users_list_groups) | **GET** /users/groups | List groups 🔐
[**users_remove_user_notification**](UsersApi.md#users_remove_user_notification) | **DELETE** /users/{id}/notifications/{notification_id} | Delete a notification attached to a user 🔐
[**users_retrieve_by_email**](UsersApi.md#users_retrieve_by_email) | **GET** /users/email/{email} | Get a user by email 🔐
[**users_retrieve_by_login**](UsersApi.md#users_retrieve_by_login) | **GET** /users/login/{login} | Get a user by login 🔐
[**users_retrieve_groups**](UsersApi.md#users_retrieve_groups) | **GET** /users/{id}/groups | List the groups of a user 🔐
[**users_retrieve_info**](UsersApi.md#users_retrieve_info) | **GET** /users/info | Get more properties of a user 🔐
[**users_retrieve_user_notification**](UsersApi.md#users_retrieve_user_notification) | **GET** /users/{id}/notifications | Get notifications for a user 🔐
[**users_set_group**](UsersApi.md#users_set_group) | **GET** /users/{id}/setGroup/{group} | Add a user to a group 🔐
[**users_set_password**](UsersApi.md#users_set_password) | **GET** /users/{id}/setPassword | Update a user password 🔐
[**users_update_user_notification**](UsersApi.md#users_update_user_notification) | **PUT** /users/{id}/notifications/{notification_id} | Update a notification for a user 🔐


# **create_users**
> int create_users(create_users_model=create_users_model)

Create a user 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_users_model import CreateUsersModel
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
    api_instance = dolibarr_api.UsersApi(api_client)
    create_users_model = dolibarr_api.CreateUsersModel() # CreateUsersModel | request_data    (optional)

    try:
        # Create a user 🔐
        api_response = api_instance.create_users(create_users_model=create_users_model)
        print("The response of UsersApi->create_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_users_model** | [**CreateUsersModel**](CreateUsersModel.md)| request_data    | [optional] 

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
**401** | Not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> List[str] list_users(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, category=category, sqlfilters=sqlfilters, properties=properties)

List users 🔐

Get a list of Users

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
    api_instance = dolibarr_api.UsersApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    user_ids = 'user_ids_example' # str | User ids filter field. Example: '1' or '1,2,3' (optional)
    category = 56 # int | Use this param to filter list by category (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # List users 🔐
        api_response = api_instance.list_users(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, category=category, sqlfilters=sqlfilters, properties=properties)
        print("The response of UsersApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **user_ids** | **str**| User ids filter field. Example: &#39;1&#39; or &#39;1,2,3&#39; | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
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

# **remove_users**
> List[str] remove_users(id)

Delete a user 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | Account ID

    try:
        # Delete a user 🔐
        api_response = api_instance.remove_users(id)
        print("The response of UsersApi->remove_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->remove_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Account ID | 

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
**403** | Not allowed |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_users**
> str retrieve_users(id, includepermissions=includepermissions)

Get a user 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | ID of user
    includepermissions = 56 # int | Set this to 1 to have the array of permissions loaded (not done by default for performance purpose) (optional)

    try:
        # Get a user 🔐
        api_response = api_instance.retrieve_users(id, includepermissions=includepermissions)
        print("The response of UsersApi->retrieve_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->retrieve_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of user | 
 **includepermissions** | **int**| Set this to 1 to have the array of permissions loaded (not done by default for performance purpose) | [optional] 

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

# **update_users**
> Dict[str, object] update_users(id, update_users_model=update_users_model)

Update a user 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_users_model import UpdateUsersModel
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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | Id of account to update
    update_users_model = dolibarr_api.UpdateUsersModel() # UpdateUsersModel | request_data    (optional)

    try:
        # Update a user 🔐
        api_response = api_instance.update_users(id, update_users_model=update_users_model)
        print("The response of UsersApi->update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of account to update | 
 **update_users_model** | [**UpdateUsersModel**](UpdateUsersModel.md)| request_data    | [optional] 

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
**403** | Not allowed |  -  |
**404** | Not found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create_user_notification**
> str users_create_user_notification(id, users_create_user_notification_model=users_create_user_notification_model)

Create a notification for a user 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.users_create_user_notification_model import UsersCreateUserNotificationModel
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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | ID of the user
    users_create_user_notification_model = dolibarr_api.UsersCreateUserNotificationModel() # UsersCreateUserNotificationModel | request_data    (optional)

    try:
        # Create a notification for a user 🔐
        api_response = api_instance.users_create_user_notification(id, users_create_user_notification_model=users_create_user_notification_model)
        print("The response of UsersApi->users_create_user_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_user_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the user | 
 **users_create_user_notification_model** | [**UsersCreateUserNotificationModel**](UsersCreateUserNotificationModel.md)| request_data    | [optional] 

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

# **users_create_user_notification_by_code**
> str users_create_user_notification_by_code(id, code, users_create_user_notification_by_code_model=users_create_user_notification_by_code_model)

Create a notification for a user using action trigger code 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.users_create_user_notification_by_code_model import UsersCreateUserNotificationByCodeModel
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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | ID of the user
    code = 'code_example' # str | Action Trigger code
    users_create_user_notification_by_code_model = dolibarr_api.UsersCreateUserNotificationByCodeModel() # UsersCreateUserNotificationByCodeModel | request_data    (optional)

    try:
        # Create a notification for a user using action trigger code 🔐
        api_response = api_instance.users_create_user_notification_by_code(id, code, users_create_user_notification_by_code_model=users_create_user_notification_by_code_model)
        print("The response of UsersApi->users_create_user_notification_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_user_notification_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the user | 
 **code** | **str**| Action Trigger code | 
 **users_create_user_notification_by_code_model** | [**UsersCreateUserNotificationByCodeModel**](UsersCreateUserNotificationByCodeModel.md)| request_data    | [optional] 

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

# **users_info_groups**
> Dict[str, object] users_info_groups(group, load_members=load_members)

Get properties of a user group 🔐

Return an array with group information

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
    api_instance = dolibarr_api.UsersApi(api_client)
    group = 56 # int | ID of group
    load_members = 56 # int | Load members list or not (optional)

    try:
        # Get properties of a user group 🔐
        api_response = api_instance.users_info_groups(group, load_members=load_members)
        print("The response of UsersApi->users_info_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_info_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **int**| ID of group | 
 **load_members** | **int**| Load members list or not | [optional] 

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
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_groups**
> List[str] users_list_groups(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, group_ids=group_ids, sqlfilters=sqlfilters, properties=properties)

List groups 🔐

Return an array with a list of Groups

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
    api_instance = dolibarr_api.UsersApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    group_ids = 'group_ids_example' # str | Groups ids filter field. Example: '1' or '1,2,3' (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # List groups 🔐
        api_response = api_instance.users_list_groups(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, group_ids=group_ids, sqlfilters=sqlfilters, properties=properties)
        print("The response of UsersApi->users_list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **group_ids** | **str**| Groups ids filter field. Example: &#39;1&#39; or &#39;1,2,3&#39; | [optional] 
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
**403** | Not allowed |  -  |
**404** | User not found |  -  |
**503** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_remove_user_notification**
> int users_remove_user_notification(id, notification_id)

Delete a notification attached to a user 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | ID of the user
    notification_id = 56 # int | ID of UserNotification

    try:
        # Delete a notification attached to a user 🔐
        api_response = api_instance.users_remove_user_notification(id, notification_id)
        print("The response of UsersApi->users_remove_user_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_remove_user_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the user | 
 **notification_id** | **int**| ID of UserNotification | 

### Return type

**int**

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

# **users_retrieve_by_email**
> str users_retrieve_by_email(email, includepermissions=includepermissions)

Get a user by email 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    email = 'email_example' # str | Email of user
    includepermissions = 56 # int | Set this to 1 to have the array of permissions loaded (not done by default for performance purpose) (optional)

    try:
        # Get a user by email 🔐
        api_response = api_instance.users_retrieve_by_email(email, includepermissions=includepermissions)
        print("The response of UsersApi->users_retrieve_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_retrieve_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of user | 
 **includepermissions** | **int**| Set this to 1 to have the array of permissions loaded (not done by default for performance purpose) | [optional] 

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
**400** | Bad request |  -  |
**401** | Insufficient rights |  -  |
**404** | User or group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_retrieve_by_login**
> str users_retrieve_by_login(login, includepermissions=includepermissions)

Get a user by login 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    login = 'login_example' # str | Login of user
    includepermissions = 56 # int | Set this to 1 to have the array of permissions loaded (not done by default for performance purpose) (optional)

    try:
        # Get a user by login 🔐
        api_response = api_instance.users_retrieve_by_login(login, includepermissions=includepermissions)
        print("The response of UsersApi->users_retrieve_by_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_retrieve_by_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| Login of user | 
 **includepermissions** | **int**| Set this to 1 to have the array of permissions loaded (not done by default for performance purpose) | [optional] 

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
**400** | Bad request |  -  |
**401** | Insufficient rights |  -  |
**404** | User or group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_retrieve_groups**
> List[str] users_retrieve_groups(id)

List the groups of a user 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | Id of user

    try:
        # List the groups of a user 🔐
        api_response = api_instance.users_retrieve_groups(id)
        print("The response of UsersApi->users_retrieve_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_retrieve_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of user | 

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
**403** | Not allowed |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_retrieve_info**
> str users_retrieve_info(includepermissions=includepermissions)

Get more properties of a user 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    includepermissions = 56 # int | Set this to 1 to have the array of permissions loaded (not done by default for performance purpose) (optional)

    try:
        # Get more properties of a user 🔐
        api_response = api_instance.users_retrieve_info(includepermissions=includepermissions)
        print("The response of UsersApi->users_retrieve_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_retrieve_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includepermissions** | **int**| Set this to 1 to have the array of permissions loaded (not done by default for performance purpose) | [optional] 

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

# **users_retrieve_user_notification**
> List[str] users_retrieve_user_notification(id)

Get notifications for a user 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | ID of the user

    try:
        # Get notifications for a user 🔐
        api_response = api_instance.users_retrieve_user_notification(id)
        print("The response of UsersApi->users_retrieve_user_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_retrieve_user_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the user | 

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

# **users_set_group**
> int users_set_group(id, group, entity=entity)

Add a user to a group 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | User ID
    group = 56 # int | Group ID
    entity = 56 # int | Entity ID (valid only for superadmin in multicompany transverse mode) (optional)

    try:
        # Add a user to a group 🔐
        api_response = api_instance.users_set_group(id, group, entity=entity)
        print("The response of UsersApi->users_set_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_set_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **group** | **int**| Group ID | 
 **entity** | **int**| Entity ID (valid only for superadmin in multicompany transverse mode) | [optional] 

### Return type

**int**

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
**404** | User not found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_set_password**
> int users_set_password(id, send_password=send_password)

Update a user password 🔐

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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | User ID
    send_password = True # bool | Only if set to true, the new password will send to the user (optional)

    try:
        # Update a user password 🔐
        api_response = api_instance.users_set_password(id, send_password=send_password)
        print("The response of UsersApi->users_set_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_set_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **send_password** | **bool**| Only if set to true, the new password will send to the user | [optional] 

### Return type

**int**

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
**404** | User not found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_user_notification**
> str users_update_user_notification(id, notification_id, users_update_user_notification_model=users_update_user_notification_model)

Update a notification for a user 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.users_update_user_notification_model import UsersUpdateUserNotificationModel
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
    api_instance = dolibarr_api.UsersApi(api_client)
    id = 56 # int | ID of the User
    notification_id = 56 # int | ID of UserNotification
    users_update_user_notification_model = dolibarr_api.UsersUpdateUserNotificationModel() # UsersUpdateUserNotificationModel | request_data    (optional)

    try:
        # Update a notification for a user 🔐
        api_response = api_instance.users_update_user_notification(id, notification_id, users_update_user_notification_model=users_update_user_notification_model)
        print("The response of UsersApi->users_update_user_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_update_user_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the User | 
 **notification_id** | **int**| ID of UserNotification | 
 **users_update_user_notification_model** | [**UsersUpdateUserNotificationModel**](UsersUpdateUserNotificationModel.md)| request_data    | [optional] 

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

