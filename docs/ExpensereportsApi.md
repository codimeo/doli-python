# dolibarr_api.ExpensereportsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_expensereports**](ExpensereportsApi.md#create_expensereports) | **POST** /expensereports | Create an expense report 🔐
[**expensereports_add_payment**](ExpensereportsApi.md#expensereports_add_payment) | **POST** /expensereports/{id}/payments | Create a payment for an expense report 🔐
[**expensereports_approve**](ExpensereportsApi.md#expensereports_approve) | **POST** /expensereports/{id}/approve | Approve an expense report 🔐
[**expensereports_deny**](ExpensereportsApi.md#expensereports_deny) | **POST** /expensereports/{id}/deny | Deny an expense report 🔐
[**expensereports_retrieve_all_payments**](ExpensereportsApi.md#expensereports_retrieve_all_payments) | **GET** /expensereports/payments | Get the list of payments of an expense report 🔐
[**expensereports_retrieve_payments**](ExpensereportsApi.md#expensereports_retrieve_payments) | **GET** /expensereports/payments/{pid} | Get an expense report payment 🔐
[**expensereports_update_payment**](ExpensereportsApi.md#expensereports_update_payment) | **PUT** /expensereports/{id}/payments | Update a payment of an expense report 🔐
[**expensereports_validate**](ExpensereportsApi.md#expensereports_validate) | **POST** /expensereports/{id}/validate | Validate an expense report 🔐
[**list_expensereports**](ExpensereportsApi.md#list_expensereports) | **GET** /expensereports | List expense reports 🔐
[**remove_expensereports**](ExpensereportsApi.md#remove_expensereports) | **DELETE** /expensereports/{id} | Delete expense report 🔐
[**retrieve_expensereports**](ExpensereportsApi.md#retrieve_expensereports) | **GET** /expensereports/{id} | Get an expense report 🔐
[**update_expensereports**](ExpensereportsApi.md#update_expensereports) | **PUT** /expensereports/{id} | Update expense report general fields 🔐


# **create_expensereports**
> int create_expensereports(create_expensereports_model=create_expensereports_model)

Create an expense report 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_expensereports_model import CreateExpensereportsModel
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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    create_expensereports_model = dolibarr_api.CreateExpensereportsModel() # CreateExpensereportsModel | request_data    (optional)

    try:
        # Create an expense report 🔐
        api_response = api_instance.create_expensereports(create_expensereports_model=create_expensereports_model)
        print("The response of ExpensereportsApi->create_expensereports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->create_expensereports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_expensereports_model** | [**CreateExpensereportsModel**](CreateExpensereportsModel.md)| request_data    | [optional] 

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

# **expensereports_add_payment**
> int expensereports_add_payment(id, expensereports_add_payment_model=expensereports_add_payment_model)

Create a payment for an expense report 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.expensereports_add_payment_model import ExpensereportsAddPaymentModel
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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    id = 56 # int | ID of an expense report
    expensereports_add_payment_model = dolibarr_api.ExpensereportsAddPaymentModel() # ExpensereportsAddPaymentModel | request_data    (optional)

    try:
        # Create a payment for an expense report 🔐
        api_response = api_instance.expensereports_add_payment(id, expensereports_add_payment_model=expensereports_add_payment_model)
        print("The response of ExpensereportsApi->expensereports_add_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->expensereports_add_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of an expense report | 
 **expensereports_add_payment_model** | [**ExpensereportsAddPaymentModel**](ExpensereportsAddPaymentModel.md)| request_data    | [optional] 

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

# **expensereports_approve**
> Dict[str, object] expensereports_approve(id, expensereports_approve_model=expensereports_approve_model)

Approve an expense report 🔐

If you get a bad value for param notrigger check, provide this in body { "notrigger": 0 }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.expensereports_approve_model import ExpensereportsApproveModel
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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    id = 56 # int | Expense report ID
    expensereports_approve_model = dolibarr_api.ExpensereportsApproveModel() # ExpensereportsApproveModel | notrigger    (optional)

    try:
        # Approve an expense report 🔐
        api_response = api_instance.expensereports_approve(id, expensereports_approve_model=expensereports_approve_model)
        print("The response of ExpensereportsApi->expensereports_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->expensereports_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense report ID | 
 **expensereports_approve_model** | [**ExpensereportsApproveModel**](ExpensereportsApproveModel.md)| notrigger    | [optional] 

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

# **expensereports_deny**
> Dict[str, object] expensereports_deny(id, expensereports_deny_model)

Deny an expense report 🔐

If you get a bad value for param notrigger check, provide this in body { "notrigger": 0 }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.expensereports_deny_model import ExpensereportsDenyModel
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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    id = 56 # int | Expense report ID
    expensereports_deny_model = dolibarr_api.ExpensereportsDenyModel() # ExpensereportsDenyModel | **details** (required)   notrigger   

    try:
        # Deny an expense report 🔐
        api_response = api_instance.expensereports_deny(id, expensereports_deny_model)
        print("The response of ExpensereportsApi->expensereports_deny:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->expensereports_deny: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense report ID | 
 **expensereports_deny_model** | [**ExpensereportsDenyModel**](ExpensereportsDenyModel.md)| **details** (required)   notrigger    | 

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

# **expensereports_retrieve_all_payments**
> List[str] expensereports_retrieve_all_payments(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get the list of payments of an expense report 🔐

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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | List limit (optional)
    page = 56 # int | Page number (optional)

    try:
        # Get the list of payments of an expense report 🔐
        api_response = api_instance.expensereports_retrieve_all_payments(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
        print("The response of ExpensereportsApi->expensereports_retrieve_all_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->expensereports_retrieve_all_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| List limit | [optional] 
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

# **expensereports_retrieve_payments**
> str expensereports_retrieve_payments(pid)

Get an expense report payment 🔐

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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    pid = 56 # int | Payment ID

    try:
        # Get an expense report payment 🔐
        api_response = api_instance.expensereports_retrieve_payments(pid)
        print("The response of ExpensereportsApi->expensereports_retrieve_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->expensereports_retrieve_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **int**| Payment ID | 

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

# **expensereports_update_payment**
> str expensereports_update_payment(id, expensereports_update_payment_model=expensereports_update_payment_model)

Update a payment of an expense report 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.expensereports_update_payment_model import ExpensereportsUpdatePaymentModel
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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    id = 56 # int | ID of paymentExpenseReport
    expensereports_update_payment_model = dolibarr_api.ExpensereportsUpdatePaymentModel() # ExpensereportsUpdatePaymentModel | request_data    (optional)

    try:
        # Update a payment of an expense report 🔐
        api_response = api_instance.expensereports_update_payment(id, expensereports_update_payment_model=expensereports_update_payment_model)
        print("The response of ExpensereportsApi->expensereports_update_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->expensereports_update_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of paymentExpenseReport | 
 **expensereports_update_payment_model** | [**ExpensereportsUpdatePaymentModel**](ExpensereportsUpdatePaymentModel.md)| request_data    | [optional] 

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

# **expensereports_validate**
> Dict[str, object] expensereports_validate(id, expensereports_validate_model=expensereports_validate_model)

Validate an expense report 🔐

If you get a bad value for param notrigger check, provide this in body { "notrigger": 0 }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.expensereports_validate_model import ExpensereportsValidateModel
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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    id = 56 # int | Expense report ID
    expensereports_validate_model = dolibarr_api.ExpensereportsValidateModel() # ExpensereportsValidateModel | notrigger    (optional)

    try:
        # Validate an expense report 🔐
        api_response = api_instance.expensereports_validate(id, expensereports_validate_model=expensereports_validate_model)
        print("The response of ExpensereportsApi->expensereports_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->expensereports_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense report ID | 
 **expensereports_validate_model** | [**ExpensereportsValidateModel**](ExpensereportsValidateModel.md)| notrigger    | [optional] 

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

# **list_expensereports**
> List[str] list_expensereports(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

List expense reports 🔐

Get a list of Expense Reports

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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | List limit (optional)
    page = 56 # int | Page number (optional)
    user_ids = 'user_ids_example' # str | User ids filter field. Example: '1' or '1,2,3' (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List expense reports 🔐
        api_response = api_instance.list_expensereports(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, user_ids=user_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of ExpensereportsApi->list_expensereports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->list_expensereports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| List limit | [optional] 
 **page** | **int**| Page number | [optional] 
 **user_ids** | **str**| User ids filter field. Example: &#39;1&#39; or &#39;1,2,3&#39; | [optional] 
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

# **remove_expensereports**
> List[str] remove_expensereports(id)

Delete expense report 🔐

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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    id = 56 # int | Expense Report ID

    try:
        # Delete expense report 🔐
        api_response = api_instance.remove_expensereports(id)
        print("The response of ExpensereportsApi->remove_expensereports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->remove_expensereports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Expense Report ID | 

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

# **retrieve_expensereports**
> Dict[str, object] retrieve_expensereports(id)

Get an expense report 🔐

Return an array with Expense Report information

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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    id = 56 # int | ID of Expense Report

    try:
        # Get an expense report 🔐
        api_response = api_instance.retrieve_expensereports(id)
        print("The response of ExpensereportsApi->retrieve_expensereports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->retrieve_expensereports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Expense Report | 

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

# **update_expensereports**
> Dict[str, object] update_expensereports(id, update_expensereports_model=update_expensereports_model)

Update expense report general fields 🔐

Does not touch lines of the expense report

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_expensereports_model import UpdateExpensereportsModel
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
    api_instance = dolibarr_api.ExpensereportsApi(api_client)
    id = 56 # int | ID of Expense Report to update
    update_expensereports_model = dolibarr_api.UpdateExpensereportsModel() # UpdateExpensereportsModel | request_data    (optional)

    try:
        # Update expense report general fields 🔐
        api_response = api_instance.update_expensereports(id, update_expensereports_model=update_expensereports_model)
        print("The response of ExpensereportsApi->update_expensereports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensereportsApi->update_expensereports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Expense Report to update | 
 **update_expensereports_model** | [**UpdateExpensereportsModel**](UpdateExpensereportsModel.md)| request_data    | [optional] 

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
**401** | Not allowed |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

