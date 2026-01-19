# dolibarr_api.DocumentsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_documents**](DocumentsApi.md#create_documents) | **POST** /documents/upload | Upload a document 🔐
[**documents_builddoc**](DocumentsApi.md#documents_builddoc) | **PUT** /documents/builddoc | Build a document 🔐
[**documents_retrieve_documents_list_by_element**](DocumentsApi.md#documents_retrieve_documents_list_by_element) | **GET** /documents | List documents of an element 🔐
[**list_documents**](DocumentsApi.md#list_documents) | **GET** /documents/download | Download a document 🔐
[**remove_documents**](DocumentsApi.md#remove_documents) | **DELETE** /documents | Delete a document 🔐


# **create_documents**
> str create_documents(create_documents_model)

Upload a document 🔐

Test sample for invoice: { "filename": "mynewfile.txt", "modulepart": "invoice", "ref": "FA1701-001", "subdir": "", "filecontent": "content text", "fileencoding": "", "overwriteifexists": "0" }. Test sample for supplier invoice: { "filename": "mynewfile.txt", "modulepart": "supplier_invoice", "ref": "FA1701-001", "subdir": "", "filecontent": "content text", "fileencoding": "", "overwriteifexists": "0" }. Test sample for medias file: { "filename": "mynewfile.txt", "modulepart": "medias", "ref": "", "subdir": "image/mywebsite", "filecontent": "Y29udGVudCB0ZXh0Cg==", "fileencoding": "base64", "overwriteifexists": "0" }. Supported modules: invoice, order, supplier_order, task/project_task, product/service, expensereport, fichinter, member, propale, agenda, contact

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_documents_model import CreateDocumentsModel
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
    api_instance = dolibarr_api.DocumentsApi(api_client)
    create_documents_model = dolibarr_api.CreateDocumentsModel() # CreateDocumentsModel | **filename** (required)   **modulepart** (required)   ref   subdir   filecontent   fileencoding   overwriteifexists   createdirifnotexists   position   cover   array_options   generateThumbs   

    try:
        # Upload a document 🔐
        api_response = api_instance.create_documents(create_documents_model)
        print("The response of DocumentsApi->create_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->create_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_documents_model** | [**CreateDocumentsModel**](CreateDocumentsModel.md)| **filename** (required)   **modulepart** (required)   ref   subdir   filecontent   fileencoding   overwriteifexists   createdirifnotexists   position   cover   array_options   generateThumbs    | 

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
**400** | Bad Request |  -  |
**403** | Access denied |  -  |
**404** | Object not found |  -  |
**500** | Error on file operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_builddoc**
> List[str] documents_builddoc(documents_builddoc_model)

Build a document 🔐

Test sample 1: { "modulepart": "invoice", "original_file": "FA1701-001/FA1701-001.pdf", "doctemplate": "crabe", "langcode": "fr_FR" }. Supported modules: invoice, order, proposal, contract, supplier invoice, shipment, mrp

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.documents_builddoc_model import DocumentsBuilddocModel
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
    api_instance = dolibarr_api.DocumentsApi(api_client)
    documents_builddoc_model = dolibarr_api.DocumentsBuilddocModel() # DocumentsBuilddocModel | **modulepart** (required)   original_file   doctemplate   langcode   

    try:
        # Build a document 🔐
        api_response = api_instance.documents_builddoc(documents_builddoc_model)
        print("The response of DocumentsApi->documents_builddoc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_builddoc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_builddoc_model** | [**DocumentsBuilddocModel**](DocumentsBuilddocModel.md)| **modulepart** (required)   original_file   doctemplate   langcode    | 

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
**400** | Bad value for parameter modulepart or original_file |  -  |
**403** | Access denied |  -  |
**404** | Invoice, Order, Proposal, Contract or Shipment not found |  -  |
**500** | Error generating document |  -  |
**501** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_retrieve_documents_list_by_element**
> List[str] documents_retrieve_documents_list_by_element(modulepart, id=id, ref=ref, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, content_type=content_type, pagination_data=pagination_data)

List documents of an element 🔐

Use element ID or Ref. Supported modules: thirdparty, user, member, proposal, order, supplier_order, shipment, invoice, supplier_invoice, product, event, expensereport, knowledgemanagement, category, contract

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
    api_instance = dolibarr_api.DocumentsApi(api_client)
    modulepart = 'modulepart_example' # str | Name of module or area concerned ('thirdparty', 'member', 'proposal', 'order', 'invoice', 'supplier_invoice', 'shipment', 'project', ...)
    id = 56 # int | ID of element (optional)
    ref = 'ref_example' # str | Ref of element (optional)
    sortfield = 'sortfield_example' # str | Sort criteria ('','fullname','relativename','name','date','size') (optional)
    sortorder = 'sortorder_example' # str | Sort order ('asc' or 'desc') (optional)
    limit = 56 # int | List limit (optional)
    page = 56 # int | Page number (optional)
    content_type = 'content_type_example' # str | Filter on content-type (example 'application/pdf' or 'application/pdf,image/jpeg')) (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List documents of an element 🔐
        api_response = api_instance.documents_retrieve_documents_list_by_element(modulepart, id=id, ref=ref, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, content_type=content_type, pagination_data=pagination_data)
        print("The response of DocumentsApi->documents_retrieve_documents_list_by_element:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_retrieve_documents_list_by_element: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modulepart** | **str**| Name of module or area concerned (&#39;thirdparty&#39;, &#39;member&#39;, &#39;proposal&#39;, &#39;order&#39;, &#39;invoice&#39;, &#39;supplier_invoice&#39;, &#39;shipment&#39;, &#39;project&#39;, ...) | 
 **id** | **int**| ID of element | [optional] 
 **ref** | **str**| Ref of element | [optional] 
 **sortfield** | **str**| Sort criteria (&#39;&#39;,&#39;fullname&#39;,&#39;relativename&#39;,&#39;name&#39;,&#39;date&#39;,&#39;size&#39;) | [optional] 
 **sortorder** | **str**| Sort order (&#39;asc&#39; or &#39;desc&#39;) | [optional] 
 **limit** | **int**| List limit | [optional] 
 **page** | **int**| Page number | [optional] 
 **content_type** | **str**| Filter on content-type (example &#39;application/pdf&#39; or &#39;application/pdf,image/jpeg&#39;)) | [optional] 
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
**400** | Bad value for parameter modulepart, id or ref |  -  |
**403** | Access denied |  -  |
**404** | Thirdparty, User, Member, Order, Invoice or Proposal not found |  -  |
**500** | Error while fetching object |  -  |
**503** | Error when retrieve ecm list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> List[str] list_documents(modulepart, original_file=original_file)

Download a document 🔐

Note that, this API is similar to using the wrapper link "documents.php" to download a file (used for internal HTML links of documents into application), but with no need to have a session cookie (the token is used instead).

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
    api_instance = dolibarr_api.DocumentsApi(api_client)
    modulepart = 'modulepart_example' # str | Name of module or area concerned by file download ('facture', ...)
    original_file = 'original_file_example' # str | Relative path with filename, relative to modulepart (for example: IN201701-999/IN201701-999.pdf) (optional)

    try:
        # Download a document 🔐
        api_response = api_instance.list_documents(modulepart, original_file=original_file)
        print("The response of DocumentsApi->list_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->list_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modulepart** | **str**| Name of module or area concerned by file download (&#39;facture&#39;, ...) | 
 **original_file** | **str**| Relative path with filename, relative to modulepart (for example: IN201701-999/IN201701-999.pdf) | [optional] 

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
**400** | Bad value for parameter modulepart or original_file |  -  |
**403** | Access denied |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_documents**
> List[str] remove_documents(modulepart, original_file)

Delete a document 🔐

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
    api_instance = dolibarr_api.DocumentsApi(api_client)
    modulepart = 'modulepart_example' # str | Name of module or area concerned by file download ('product', ...)
    original_file = 'original_file_example' # str | Relative path with filename, relative to modulepart (for example: PRODUCT-REF-999/IMAGE-999.jpg)

    try:
        # Delete a document 🔐
        api_response = api_instance.remove_documents(modulepart, original_file)
        print("The response of DocumentsApi->remove_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->remove_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modulepart** | **str**| Name of module or area concerned by file download (&#39;product&#39;, ...) | 
 **original_file** | **str**| Relative path with filename, relative to modulepart (for example: PRODUCT-REF-999/IMAGE-999.jpg) | 

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
**400** | Bad value for parameter original_file |  -  |
**403** | Access denied |  -  |
**404** | File not found |  -  |
**500** | Error on file operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

