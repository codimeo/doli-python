# dolibarr_api.BankaccountsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bankaccounts_add_line**](BankaccountsApi.md#bankaccounts_add_line) | **POST** /bankaccounts/{id}/lines | Add a line to an account 🔐
[**bankaccounts_add_link**](BankaccountsApi.md#bankaccounts_add_link) | **POST** /bankaccounts/{id}/lines/{line_id}/links | Add a link to an account line 🔐
[**bankaccounts_remove_line**](BankaccountsApi.md#bankaccounts_remove_line) | **DELETE** /bankaccounts/{id}/lines/{line_id} | Delete an account line 🔐
[**bankaccounts_retrieve_balance**](BankaccountsApi.md#bankaccounts_retrieve_balance) | **GET** /bankaccounts/{id}/balance | Get current account balance by ID 🔐
[**bankaccounts_retrieve_lines**](BankaccountsApi.md#bankaccounts_retrieve_lines) | **GET** /bankaccounts/{id}/lines | Get the list of lines of the account. 🔐
[**bankaccounts_retrieve_links**](BankaccountsApi.md#bankaccounts_retrieve_links) | **GET** /bankaccounts/{id}/lines/{line_id}/links | Get the list of links for a line of the account. 🔐
[**bankaccounts_transfer**](BankaccountsApi.md#bankaccounts_transfer) | **POST** /bankaccounts/transfer | Create an internal wire transfer between two bank accounts 🔐
[**bankaccounts_update_line**](BankaccountsApi.md#bankaccounts_update_line) | **PUT** /bankaccounts/{id}/lines/{line_id} | Update an account line 🔐
[**create_bankaccounts**](BankaccountsApi.md#create_bankaccounts) | **POST** /bankaccounts | Create account object 🔐
[**list_bankaccounts**](BankaccountsApi.md#list_bankaccounts) | **GET** /bankaccounts | Get the list of accounts. 🔐
[**remove_bankaccounts**](BankaccountsApi.md#remove_bankaccounts) | **DELETE** /bankaccounts/{id} | Delete account 🔐
[**retrieve_bankaccounts**](BankaccountsApi.md#retrieve_bankaccounts) | **GET** /bankaccounts/{id} | Get account by ID. 🔐
[**update_bankaccounts**](BankaccountsApi.md#update_bankaccounts) | **PUT** /bankaccounts/{id} | Update account 🔐


# **bankaccounts_add_line**
> int bankaccounts_add_line(id, bankaccounts_add_line_model)

Add a line to an account 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.bankaccounts_add_line_model import BankaccountsAddLineModel
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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account
    bankaccounts_add_line_model = dolibarr_api.BankaccountsAddLineModel() # BankaccountsAddLineModel | **date** (required)   **type** (required)   **label** (required)   **amount** (required)   category   cheque_number   cheque_writer   cheque_bank   accountancycode   datev   num_releve   

    try:
        # Add a line to an account 🔐
        api_response = api_instance.bankaccounts_add_line(id, bankaccounts_add_line_model)
        print("The response of BankaccountsApi->bankaccounts_add_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->bankaccounts_add_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 
 **bankaccounts_add_line_model** | [**BankaccountsAddLineModel**](BankaccountsAddLineModel.md)| **date** (required)   **type** (required)   **label** (required)   **amount** (required)   category   cheque_number   cheque_writer   cheque_bank   accountancycode   datev   num_releve    | 

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

# **bankaccounts_add_link**
> int bankaccounts_add_link(id, line_id, bankaccounts_add_link_model)

Add a link to an account line 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.bankaccounts_add_link_model import BankaccountsAddLinkModel
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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account
    line_id = 56 # int | ID of account line
    bankaccounts_add_link_model = dolibarr_api.BankaccountsAddLinkModel() # BankaccountsAddLinkModel | **url_id** (required)   **url** (required)   **label** (required)   **type** (required)   

    try:
        # Add a link to an account line 🔐
        api_response = api_instance.bankaccounts_add_link(id, line_id, bankaccounts_add_link_model)
        print("The response of BankaccountsApi->bankaccounts_add_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->bankaccounts_add_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 
 **line_id** | **int**| ID of account line | 
 **bankaccounts_add_link_model** | [**BankaccountsAddLinkModel**](BankaccountsAddLinkModel.md)| **url_id** (required)   **url** (required)   **label** (required)   **type** (required)    | 

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

# **bankaccounts_remove_line**
> List[str] bankaccounts_remove_line(id, line_id)

Delete an account line 🔐

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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account
    line_id = 56 # int | ID of account line

    try:
        # Delete an account line 🔐
        api_response = api_instance.bankaccounts_remove_line(id, line_id)
        print("The response of BankaccountsApi->bankaccounts_remove_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->bankaccounts_remove_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 
 **line_id** | **int**| ID of account line | 

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

# **bankaccounts_retrieve_balance**
> float bankaccounts_retrieve_balance(id)

Get current account balance by ID 🔐

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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account

    try:
        # Get current account balance by ID 🔐
        api_response = api_instance.bankaccounts_retrieve_balance(id)
        print("The response of BankaccountsApi->bankaccounts_retrieve_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->bankaccounts_retrieve_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 

### Return type

**float**

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

# **bankaccounts_retrieve_lines**
> List[str] bankaccounts_retrieve_lines(id, sqlfilters=sqlfilters)

Get the list of lines of the account. 🔐

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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.import_key:<:'20160101')\" (optional)

    try:
        # Get the list of lines of the account. 🔐
        api_response = api_instance.bankaccounts_retrieve_lines(id, sqlfilters=sqlfilters)
        print("The response of BankaccountsApi->bankaccounts_retrieve_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->bankaccounts_retrieve_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.import_key:&lt;:&#39;20160101&#39;)\&quot; | [optional] 

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

# **bankaccounts_retrieve_links**
> List[str] bankaccounts_retrieve_links(id, line_id)

Get the list of links for a line of the account. 🔐

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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account
    line_id = 56 # int | ID of account line

    try:
        # Get the list of links for a line of the account. 🔐
        api_response = api_instance.bankaccounts_retrieve_links(id, line_id)
        print("The response of BankaccountsApi->bankaccounts_retrieve_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->bankaccounts_retrieve_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 
 **line_id** | **int**| ID of account line | 

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

# **bankaccounts_transfer**
> List[str] bankaccounts_transfer(bankaccounts_transfer_model)

Create an internal wire transfer between two bank accounts 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.bankaccounts_transfer_model import BankaccountsTransferModel
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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    bankaccounts_transfer_model = dolibarr_api.BankaccountsTransferModel() # BankaccountsTransferModel | bankaccount_from_id   bankaccount_to_id   date   description   amount   amount_to   cheque_number   

    try:
        # Create an internal wire transfer between two bank accounts 🔐
        api_response = api_instance.bankaccounts_transfer(bankaccounts_transfer_model)
        print("The response of BankaccountsApi->bankaccounts_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->bankaccounts_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankaccounts_transfer_model** | [**BankaccountsTransferModel**](BankaccountsTransferModel.md)| bankaccount_from_id   bankaccount_to_id   date   description   amount   amount_to   cheque_number    | 

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
**401** | Unauthorized: User does not have permission to configure bank accounts |  -  |
**404** | Not Found: Either the source or the destination bankaccount for the provided id does not exist |  -  |
**500** | Internal Server Error: Error(s) returned by the RDBMS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bankaccounts_update_line**
> int bankaccounts_update_line(id, line_id, bankaccounts_update_line_model)

Update an account line 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.bankaccounts_update_line_model import BankaccountsUpdateLineModel
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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account
    line_id = 56 # int | ID of account line
    bankaccounts_update_line_model = dolibarr_api.BankaccountsUpdateLineModel() # BankaccountsUpdateLineModel | **label** (required)   

    try:
        # Update an account line 🔐
        api_response = api_instance.bankaccounts_update_line(id, line_id, bankaccounts_update_line_model)
        print("The response of BankaccountsApi->bankaccounts_update_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->bankaccounts_update_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 
 **line_id** | **int**| ID of account line | 
 **bankaccounts_update_line_model** | [**BankaccountsUpdateLineModel**](BankaccountsUpdateLineModel.md)| **label** (required)    | 

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

# **create_bankaccounts**
> int create_bankaccounts(create_bankaccounts_model=create_bankaccounts_model)

Create account object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_bankaccounts_model import CreateBankaccountsModel
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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    create_bankaccounts_model = dolibarr_api.CreateBankaccountsModel() # CreateBankaccountsModel | request_data    (optional)

    try:
        # Create account object 🔐
        api_response = api_instance.create_bankaccounts(create_bankaccounts_model=create_bankaccounts_model)
        print("The response of BankaccountsApi->create_bankaccounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->create_bankaccounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bankaccounts_model** | [**CreateBankaccountsModel**](CreateBankaccountsModel.md)| request_data    | [optional] 

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

# **list_bankaccounts**
> List[str] list_bankaccounts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, category=category, sqlfilters=sqlfilters, properties=properties)

Get the list of accounts. 🔐

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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    category = 56 # int | Use this param to filter list by category (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.import_key:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # Get the list of accounts. 🔐
        api_response = api_instance.list_bankaccounts(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, category=category, sqlfilters=sqlfilters, properties=properties)
        print("The response of BankaccountsApi->list_bankaccounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->list_bankaccounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.import_key:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
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

# **remove_bankaccounts**
> List[str] remove_bankaccounts(id)

Delete account 🔐

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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account

    try:
        # Delete account 🔐
        api_response = api_instance.remove_bankaccounts(id)
        print("The response of BankaccountsApi->remove_bankaccounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->remove_bankaccounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 

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

# **retrieve_bankaccounts**
> Dict[str, object] retrieve_bankaccounts(id)

Get account by ID. 🔐

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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account

    try:
        # Get account by ID. 🔐
        api_response = api_instance.retrieve_bankaccounts(id)
        print("The response of BankaccountsApi->retrieve_bankaccounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->retrieve_bankaccounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 

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

# **update_bankaccounts**
> Dict[str, object] update_bankaccounts(id, update_bankaccounts_model=update_bankaccounts_model)

Update account 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_bankaccounts_model import UpdateBankaccountsModel
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
    api_instance = dolibarr_api.BankaccountsApi(api_client)
    id = 56 # int | ID of account
    update_bankaccounts_model = dolibarr_api.UpdateBankaccountsModel() # UpdateBankaccountsModel | request_data    (optional)

    try:
        # Update account 🔐
        api_response = api_instance.update_bankaccounts(id, update_bankaccounts_model=update_bankaccounts_model)
        print("The response of BankaccountsApi->update_bankaccounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankaccountsApi->update_bankaccounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of account | 
 **update_bankaccounts_model** | [**UpdateBankaccountsModel**](UpdateBankaccountsModel.md)| request_data    | [optional] 

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

