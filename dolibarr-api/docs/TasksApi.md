# dolibarr_api.TasksApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tasks**](TasksApi.md#create_tasks) | **POST** /tasks | Create task object 🔐
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /tasks | List tasks 🔐
[**remove_tasks**](TasksApi.md#remove_tasks) | **DELETE** /tasks/{id} | Delete task 🔐
[**retrieve_tasks**](TasksApi.md#retrieve_tasks) | **GET** /tasks/{id} | Get properties of a task object 🔐
[**tasks_add_time_spent**](TasksApi.md#tasks_add_time_spent) | **POST** /tasks/{id}/addtimespent | Add time spent to a task of a project. 🔐
[**tasks_remove_time_spent**](TasksApi.md#tasks_remove_time_spent) | **DELETE** /tasks/{id}/timespent/{timespent_id} | Delete time spent for a task of a project. 🔐
[**tasks_retrieve_roles**](TasksApi.md#tasks_retrieve_roles) | **GET** /tasks/{id}/roles | Get roles a user is assigned to a task with 🔐
[**tasks_timespent_record_checks**](TasksApi.md#tasks_timespent_record_checks) | **GET** /tasks/timespentrecordchecks/{id} | Validate task &amp; timespent IDs for timespent API methods. 🔐
[**tasks_update_time_spent**](TasksApi.md#tasks_update_time_spent) | **PUT** /tasks/{id}/timespent/{timespent_id} | Update time spent for a task of a project. 🔐
[**update_tasks**](TasksApi.md#update_tasks) | **PUT** /tasks/{id} | Update task general fields (won&#39;t touch time spent of task) 🔐


# **create_tasks**
> int create_tasks(create_tasks_model=create_tasks_model)

Create task object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_tasks_model import CreateTasksModel
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
    api_instance = dolibarr_api.TasksApi(api_client)
    create_tasks_model = dolibarr_api.CreateTasksModel() # CreateTasksModel | request_data    (optional)

    try:
        # Create task object 🔐
        api_response = api_instance.create_tasks(create_tasks_model=create_tasks_model)
        print("The response of TasksApi->create_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tasks_model** | [**CreateTasksModel**](CreateTasksModel.md)| request_data    | [optional] 

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

# **list_tasks**
> List[str] list_tasks(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties)

List tasks 🔐

Get a list of tasks

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
    api_instance = dolibarr_api.TasksApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # List tasks 🔐
        api_response = api_instance.list_tasks(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties)
        print("The response of TasksApi->list_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tasks**
> List[str] remove_tasks(id)

Delete task 🔐

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
    api_instance = dolibarr_api.TasksApi(api_client)
    id = 56 # int | Task ID

    try:
        # Delete task 🔐
        api_response = api_instance.remove_tasks(id)
        print("The response of TasksApi->remove_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->remove_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID | 

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

# **retrieve_tasks**
> str retrieve_tasks(id, includetimespent=includetimespent)

Get properties of a task object 🔐

Return an array with task information

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
    api_instance = dolibarr_api.TasksApi(api_client)
    id = 56 # int | ID of task
    includetimespent = 56 # int | 0=Return only task. 1=Include a summary of time spent, 2=Include details of time spent lines (optional)

    try:
        # Get properties of a task object 🔐
        api_response = api_instance.retrieve_tasks(id, includetimespent=includetimespent)
        print("The response of TasksApi->retrieve_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->retrieve_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of task | 
 **includetimespent** | **int**| 0&#x3D;Return only task. 1&#x3D;Include a summary of time spent, 2&#x3D;Include details of time spent lines | [optional] 

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

# **tasks_add_time_spent**
> List[str] tasks_add_time_spent(id, tasks_add_time_spent_model)

Add time spent to a task of a project. 🔐

You can test this API with the following input message { "date": "2016-12-31 23:15:00", "duration": 1800, "user_id": 1, "note": "My time test" }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.tasks_add_time_spent_model import TasksAddTimeSpentModel
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
    api_instance = dolibarr_api.TasksApi(api_client)
    id = 56 # int | Task ID
    tasks_add_time_spent_model = dolibarr_api.TasksAddTimeSpentModel() # TasksAddTimeSpentModel | **date** (required)   **duration** (required)   user_id   note   

    try:
        # Add time spent to a task of a project. 🔐
        api_response = api_instance.tasks_add_time_spent(id, tasks_add_time_spent_model)
        print("The response of TasksApi->tasks_add_time_spent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_add_time_spent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID | 
 **tasks_add_time_spent_model** | [**TasksAddTimeSpentModel**](TasksAddTimeSpentModel.md)| **date** (required)   **duration** (required)   user_id   note    | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_remove_time_spent**
> List[str] tasks_remove_time_spent(id, timespent_id)

Delete time spent for a task of a project. 🔐

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
    api_instance = dolibarr_api.TasksApi(api_client)
    id = 56 # int | Task ID
    timespent_id = 56 # int | Time spent ID (llx_element_time.rowid)

    try:
        # Delete time spent for a task of a project. 🔐
        api_response = api_instance.tasks_remove_time_spent(id, timespent_id)
        print("The response of TasksApi->tasks_remove_time_spent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_remove_time_spent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID | 
 **timespent_id** | **int**| Time spent ID (llx_element_time.rowid) | 

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

# **tasks_retrieve_roles**
> List[str] tasks_retrieve_roles(id, userid=userid)

Get roles a user is assigned to a task with 🔐

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
    api_instance = dolibarr_api.TasksApi(api_client)
    id = 56 # int | Id of task
    userid = 56 # int | Id of user (0 = connected user) (optional)

    try:
        # Get roles a user is assigned to a task with 🔐
        api_response = api_instance.tasks_retrieve_roles(id, userid=userid)
        print("The response of TasksApi->tasks_retrieve_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_retrieve_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of task | 
 **userid** | **int**| Id of user (0 &#x3D; connected user) | [optional] 

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

# **tasks_timespent_record_checks**
> str tasks_timespent_record_checks(id, timespent_id)

Validate task & timespent IDs for timespent API methods. 🔐

Loads the selected task & timespent records.

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
    api_instance = dolibarr_api.TasksApi(api_client)
    id = 56 # int | Task ID
    timespent_id = 56 # int | Time spent ID (llx_element_time.rowid)

    try:
        # Validate task & timespent IDs for timespent API methods. 🔐
        api_response = api_instance.tasks_timespent_record_checks(id, timespent_id)
        print("The response of TasksApi->tasks_timespent_record_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_timespent_record_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID | 
 **timespent_id** | **int**| Time spent ID (llx_element_time.rowid) | 

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

# **tasks_update_time_spent**
> List[str] tasks_update_time_spent(id, timespent_id, tasks_update_time_spent_model)

Update time spent for a task of a project. 🔐

You can test this API with the following input message { "date": "2016-12-31 23:15:00", "duration": 1800, "user_id": 1, "note": "My time test" }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.tasks_update_time_spent_model import TasksUpdateTimeSpentModel
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
    api_instance = dolibarr_api.TasksApi(api_client)
    id = 56 # int | Task ID
    timespent_id = 56 # int | Time spent ID (llx_element_time.rowid)
    tasks_update_time_spent_model = dolibarr_api.TasksUpdateTimeSpentModel() # TasksUpdateTimeSpentModel | **date** (required)   **duration** (required)   user_id   note   

    try:
        # Update time spent for a task of a project. 🔐
        api_response = api_instance.tasks_update_time_spent(id, timespent_id, tasks_update_time_spent_model)
        print("The response of TasksApi->tasks_update_time_spent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_update_time_spent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Task ID | 
 **timespent_id** | **int**| Time spent ID (llx_element_time.rowid) | 
 **tasks_update_time_spent_model** | [**TasksUpdateTimeSpentModel**](TasksUpdateTimeSpentModel.md)| **date** (required)   **duration** (required)   user_id   note    | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tasks**
> Dict[str, object] update_tasks(id, update_tasks_model=update_tasks_model)

Update task general fields (won't touch time spent of task) 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_tasks_model import UpdateTasksModel
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
    api_instance = dolibarr_api.TasksApi(api_client)
    id = 56 # int | Id of task to update
    update_tasks_model = dolibarr_api.UpdateTasksModel() # UpdateTasksModel | request_data    (optional)

    try:
        # Update task general fields (won't touch time spent of task) 🔐
        api_response = api_instance.update_tasks(id, update_tasks_model=update_tasks_model)
        print("The response of TasksApi->update_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->update_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of task to update | 
 **update_tasks_model** | [**UpdateTasksModel**](UpdateTasksModel.md)| request_data    | [optional] 

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

