# dolibarr_api.ProposalsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_proposals**](ProposalsApi.md#create_proposals) | **POST** /proposals | Create a commercial proposal 🔐
[**list_proposals**](ProposalsApi.md#list_proposals) | **GET** /proposals | List commercial proposals 🔐
[**proposals_close**](ProposalsApi.md#proposals_close) | **POST** /proposals/{id}/close | Close (accept or refuse) a commercial proposal 🔐
[**proposals_create_contact**](ProposalsApi.md#proposals_create_contact) | **POST** /proposals/{id}/contact/{contactid}/{type}/{source} | Add (link) a contact to a commercial proposal 🔐
[**proposals_create_line**](ProposalsApi.md#proposals_create_line) | **POST** /proposals/{id}/line | Add a line to a commercial proposal 🔐
[**proposals_create_lines**](ProposalsApi.md#proposals_create_lines) | **POST** /proposals/{id}/lines | Add lines to a commercial proposal 🔐
[**proposals_remove_contact**](ProposalsApi.md#proposals_remove_contact) | **DELETE** /proposals/{id}/contact/{contactid}/{type} | Remove (unlink) a contact from commercial proposal 🔐
[**proposals_remove_line**](ProposalsApi.md#proposals_remove_line) | **DELETE** /proposals/{id}/lines/{lineid} | Delete a line of a commercial proposal 🔐
[**proposals_retrieve_by_ref**](ProposalsApi.md#proposals_retrieve_by_ref) | **GET** /proposals/ref/{ref} | Get a commercial proposal by ref 🔐
[**proposals_retrieve_by_ref_ext**](ProposalsApi.md#proposals_retrieve_by_ref_ext) | **GET** /proposals/ref_ext/{ref_ext} | Get a commercial proposal by ref_ext 🔐
[**proposals_retrieve_lines**](ProposalsApi.md#proposals_retrieve_lines) | **GET** /proposals/{id}/lines | Get lines of a commercial proposal 🔐
[**proposals_setinvoiced**](ProposalsApi.md#proposals_setinvoiced) | **POST** /proposals/{id}/setinvoiced | Set a commercial proposal to billed 🔐
[**proposals_settodraft**](ProposalsApi.md#proposals_settodraft) | **POST** /proposals/{id}/settodraft | Set a commercial proposal to draft 🔐
[**proposals_update_line**](ProposalsApi.md#proposals_update_line) | **PUT** /proposals/{id}/lines/{lineid} | Update a line of a commercial proposal 🔐
[**proposals_validate**](ProposalsApi.md#proposals_validate) | **POST** /proposals/{id}/validate | Validate a commercial proposal 🔐
[**remove_proposals**](ProposalsApi.md#remove_proposals) | **DELETE** /proposals/{id} | Delete a commercial proposal 🔐
[**retrieve_proposals**](ProposalsApi.md#retrieve_proposals) | **GET** /proposals/{id} | Get a commercial proposal 🔐
[**update_proposals**](ProposalsApi.md#update_proposals) | **PUT** /proposals/{id} | Update a commercial proposal general fields (won&#39;t change lines of commercial proposal) 🔐


# **create_proposals**
> int create_proposals(create_proposals_model=create_proposals_model)

Create a commercial proposal 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_proposals_model import CreateProposalsModel
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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    create_proposals_model = dolibarr_api.CreateProposalsModel() # CreateProposalsModel | request_data    (optional)

    try:
        # Create a commercial proposal 🔐
        api_response = api_instance.create_proposals(create_proposals_model=create_proposals_model)
        print("The response of ProposalsApi->create_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->create_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_proposals_model** | [**CreateProposalsModel**](CreateProposalsModel.md)| request_data    | [optional] 

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

# **list_proposals**
> List[str] list_proposals(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data, loadlinkedobjects=loadlinkedobjects)

List commercial proposals 🔐

Get a list of commercial proposals

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter commercial proposals (example '1' or '1,2,3') (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'2016-01-01')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)
    loadlinkedobjects = 56 # int | Load also linked object (optional)

    try:
        # List commercial proposals 🔐
        api_response = api_instance.list_proposals(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data, loadlinkedobjects=loadlinkedobjects)
        print("The response of ProposalsApi->list_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->list_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter commercial proposals (example &#39;1&#39; or &#39;1,2,3&#39;) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.datec:&lt;:&#39;2016-01-01&#39;)\&quot; | [optional] 
 **properties** | **str**| Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names | [optional] 
 **pagination_data** | **bool**| If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* | [optional] 
 **loadlinkedobjects** | **int**| Load also linked object | [optional] 

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

# **proposals_close**
> Dict[str, object] proposals_close(id, proposals_close_model)

Close (accept or refuse) a commercial proposal 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.proposals_close_model import ProposalsCloseModel
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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Commercial proposal ID
    proposals_close_model = dolibarr_api.ProposalsCloseModel() # ProposalsCloseModel | **status** (required)   note_private   notrigger   note_public   

    try:
        # Close (accept or refuse) a commercial proposal 🔐
        api_response = api_instance.proposals_close(id, proposals_close_model)
        print("The response of ProposalsApi->proposals_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Commercial proposal ID | 
 **proposals_close_model** | [**ProposalsCloseModel**](ProposalsCloseModel.md)| **status** (required)   note_private   notrigger   note_public    | 

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

# **proposals_create_contact**
> List[str] proposals_create_contact(id, contactid, type, source)

Add (link) a contact to a commercial proposal 🔐

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Id of commercial proposal to update
    contactid = 56 # int | Id of external or internal contact to add
    type = 'type_example' # str | Type of the external contact (BILLING, SHIPPING, CUSTOMER), internal contact (SALESREPFOLL)
    source = 'source_example' # str | Source of the contact (internal, external)

    try:
        # Add (link) a contact to a commercial proposal 🔐
        api_response = api_instance.proposals_create_contact(id, contactid, type, source)
        print("The response of ProposalsApi->proposals_create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **contactid** | **int**| Id of external or internal contact to add | 
 **type** | **str**| Type of the external contact (BILLING, SHIPPING, CUSTOMER), internal contact (SALESREPFOLL) | 
 **source** | **str**| Source of the contact (internal, external) | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_create_line**
> int proposals_create_line(id, proposals_create_line_model=proposals_create_line_model)

Add a line to a commercial proposal 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.proposals_create_line_model import ProposalsCreateLineModel
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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Id of commercial proposal to update
    proposals_create_line_model = dolibarr_api.ProposalsCreateLineModel() # ProposalsCreateLineModel | request_data    (optional)

    try:
        # Add a line to a commercial proposal 🔐
        api_response = api_instance.proposals_create_line(id, proposals_create_line_model=proposals_create_line_model)
        print("The response of ProposalsApi->proposals_create_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_create_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **proposals_create_line_model** | [**ProposalsCreateLineModel**](ProposalsCreateLineModel.md)| request_data    | [optional] 

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

# **proposals_create_lines**
> int proposals_create_lines(id, proposals_create_lines_model=proposals_create_lines_model)

Add lines to a commercial proposal 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.proposals_create_lines_model import ProposalsCreateLinesModel
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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Id of commercial proposal to update
    proposals_create_lines_model = dolibarr_api.ProposalsCreateLinesModel() # ProposalsCreateLinesModel | request_data    (optional)

    try:
        # Add lines to a commercial proposal 🔐
        api_response = api_instance.proposals_create_lines(id, proposals_create_lines_model=proposals_create_lines_model)
        print("The response of ProposalsApi->proposals_create_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_create_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **proposals_create_lines_model** | [**ProposalsCreateLinesModel**](ProposalsCreateLinesModel.md)| request_data    | [optional] 

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

# **proposals_remove_contact**
> Dict[str, object] proposals_remove_contact(id, contactid, type)

Remove (unlink) a contact from commercial proposal 🔐

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Id of commercial proposal to update
    contactid = 56 # int | Row key of the contact in the array contact_ids.
    type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER).

    try:
        # Remove (unlink) a contact from commercial proposal 🔐
        api_response = api_instance.proposals_remove_contact(id, contactid, type)
        print("The response of ProposalsApi->proposals_remove_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_remove_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **contactid** | **int**| Row key of the contact in the array contact_ids. | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER). | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_remove_line**
> str proposals_remove_line(id, lineid)

Delete a line of a commercial proposal 🔐

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Id of commercial proposal to update
    lineid = 56 # int | Id of line to delete

    try:
        # Delete a line of a commercial proposal 🔐
        api_response = api_instance.proposals_remove_line(id, lineid)
        print("The response of ProposalsApi->proposals_remove_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_remove_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **lineid** | **int**| Id of line to delete | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposals_retrieve_by_ref**
> Dict[str, object] proposals_retrieve_by_ref(ref, contact_list=contact_list)

Get a commercial proposal by ref 🔐

Return an array with proposal information

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    ref = 'ref_example' # str | Ref of object
    contact_list = 56 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

    try:
        # Get a commercial proposal by ref 🔐
        api_response = api_instance.proposals_retrieve_by_ref(ref, contact_list=contact_list)
        print("The response of ProposalsApi->proposals_retrieve_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_retrieve_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of object | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id | [optional] 

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

# **proposals_retrieve_by_ref_ext**
> Dict[str, object] proposals_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)

Get a commercial proposal by ref_ext 🔐

Return an array with proposal information

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    ref_ext = 'ref_ext_example' # str | External reference of object
    contact_list = 56 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

    try:
        # Get a commercial proposal by ref_ext 🔐
        api_response = api_instance.proposals_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)
        print("The response of ProposalsApi->proposals_retrieve_by_ref_ext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_retrieve_by_ref_ext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_ext** | **str**| External reference of object | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id | [optional] 

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

# **proposals_retrieve_lines**
> List[str] proposals_retrieve_lines(id, sqlfilters=sqlfilters)

Get lines of a commercial proposal 🔐

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Id of commercial proposal
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. d is the alias for proposal lines table, p is the alias for product table. \"Syntax example \"(p.ref:like:'SO-%') AND (d.date_start:<:'20220101')\" (optional)

    try:
        # Get lines of a commercial proposal 🔐
        api_response = api_instance.proposals_retrieve_lines(id, sqlfilters=sqlfilters)
        print("The response of ProposalsApi->proposals_retrieve_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_retrieve_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal | 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. d is the alias for proposal lines table, p is the alias for product table. \&quot;Syntax example \&quot;(p.ref:like:&#39;SO-%&#39;) AND (d.date_start:&lt;:&#39;20220101&#39;)\&quot; | [optional] 

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

# **proposals_setinvoiced**
> Dict[str, object] proposals_setinvoiced(id)

Set a commercial proposal to billed 🔐

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Commercial proposal ID

    try:
        # Set a commercial proposal to billed 🔐
        api_response = api_instance.proposals_setinvoiced(id)
        print("The response of ProposalsApi->proposals_setinvoiced:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_setinvoiced: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Commercial proposal ID | 

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

# **proposals_settodraft**
> Dict[str, object] proposals_settodraft(id)

Set a commercial proposal to draft 🔐

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Order ID

    try:
        # Set a commercial proposal to draft 🔐
        api_response = api_instance.proposals_settodraft(id)
        print("The response of ProposalsApi->proposals_settodraft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_settodraft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 

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

# **proposals_update_line**
> str proposals_update_line(id, lineid, proposals_update_line_model=proposals_update_line_model)

Update a line of a commercial proposal 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.proposals_update_line_model import ProposalsUpdateLineModel
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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Id of commercial proposal to update
    lineid = 56 # int | Id of line to update
    proposals_update_line_model = dolibarr_api.ProposalsUpdateLineModel() # ProposalsUpdateLineModel | request_data    (optional)

    try:
        # Update a line of a commercial proposal 🔐
        api_response = api_instance.proposals_update_line(id, lineid, proposals_update_line_model=proposals_update_line_model)
        print("The response of ProposalsApi->proposals_update_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_update_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **lineid** | **int**| Id of line to update | 
 **proposals_update_line_model** | [**ProposalsUpdateLineModel**](ProposalsUpdateLineModel.md)| request_data    | [optional] 

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

# **proposals_validate**
> Dict[str, object] proposals_validate(id, proposals_validate_model=proposals_validate_model)

Validate a commercial proposal 🔐

If you get a bad value for param notrigger check that ou provide this in body { "notrigger": 0 }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.proposals_validate_model import ProposalsValidateModel
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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Commercial proposal ID
    proposals_validate_model = dolibarr_api.ProposalsValidateModel() # ProposalsValidateModel | notrigger    (optional)

    try:
        # Validate a commercial proposal 🔐
        api_response = api_instance.proposals_validate(id, proposals_validate_model=proposals_validate_model)
        print("The response of ProposalsApi->proposals_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->proposals_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Commercial proposal ID | 
 **proposals_validate_model** | [**ProposalsValidateModel**](ProposalsValidateModel.md)| notrigger    | [optional] 

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
**304** | Not Modified |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_proposals**
> List[str] remove_proposals(id)

Delete a commercial proposal 🔐

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Commercial proposal ID

    try:
        # Delete a commercial proposal 🔐
        api_response = api_instance.remove_proposals(id)
        print("The response of ProposalsApi->remove_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->remove_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Commercial proposal ID | 

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

# **retrieve_proposals**
> Dict[str, object] retrieve_proposals(id, contact_list=contact_list)

Get a commercial proposal 🔐

Return an array with commercial proposal information

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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | ID of commercial proposal
    contact_list = 56 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id (optional)

    try:
        # Get a commercial proposal 🔐
        api_response = api_instance.retrieve_proposals(id, contact_list=contact_list)
        print("The response of ProposalsApi->retrieve_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->retrieve_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of commercial proposal | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id | [optional] 

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

# **update_proposals**
> Dict[str, object] update_proposals(id, update_proposals_model=update_proposals_model)

Update a commercial proposal general fields (won't change lines of commercial proposal) 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_proposals_model import UpdateProposalsModel
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
    api_instance = dolibarr_api.ProposalsApi(api_client)
    id = 56 # int | Id of commercial proposal to update
    update_proposals_model = dolibarr_api.UpdateProposalsModel() # UpdateProposalsModel | request_data    (optional)

    try:
        # Update a commercial proposal general fields (won't change lines of commercial proposal) 🔐
        api_response = api_instance.update_proposals(id, update_proposals_model=update_proposals_model)
        print("The response of ProposalsApi->update_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProposalsApi->update_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of commercial proposal to update | 
 **update_proposals_model** | [**UpdateProposalsModel**](UpdateProposalsModel.md)| request_data    | [optional] 

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

