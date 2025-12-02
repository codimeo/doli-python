# dolibarr_api.SupplierordersApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supplierorders**](SupplierordersApi.md#create_supplierorders) | **POST** /supplierorders | Create supplier order object 🔐
[**list_supplierorders**](SupplierordersApi.md#list_supplierorders) | **GET** /supplierorders | List orders 🔐
[**remove_supplierorders**](SupplierordersApi.md#remove_supplierorders) | **DELETE** /supplierorders/{id} | Delete supplier order 🔐
[**retrieve_supplierorders**](SupplierordersApi.md#retrieve_supplierorders) | **GET** /supplierorders/{id} | Get properties of a supplier order object 🔐
[**supplierorders_approve**](SupplierordersApi.md#supplierorders_approve) | **POST** /supplierorders/{id}/approve | Approve an order 🔐
[**supplierorders_create_contact**](SupplierordersApi.md#supplierorders_create_contact) | **POST** /supplierorders/{id}/contact/{contactid}/{type}/{source} | Add a contact type of given supplier order 🔐
[**supplierorders_make_order**](SupplierordersApi.md#supplierorders_make_order) | **POST** /supplierorders/{id}/makeorder | Sends an order to the vendor 🔐
[**supplierorders_receive_order**](SupplierordersApi.md#supplierorders_receive_order) | **POST** /supplierorders/{id}/receive | Receives the order, dispatches products. 🔐
[**supplierorders_remove_contact**](SupplierordersApi.md#supplierorders_remove_contact) | **DELETE** /supplierorders/{id}/contact/{contactid}/{type}/{source} | Unlink a contact type of given supplier order 🔐
[**supplierorders_retrieve_contacts**](SupplierordersApi.md#supplierorders_retrieve_contacts) | **GET** /supplierorders/{id}/contacts | Get contacts of given supplier order 🔐
[**supplierorders_validate**](SupplierordersApi.md#supplierorders_validate) | **POST** /supplierorders/{id}/validate | Validate an order 🔐
[**update_supplierorders**](SupplierordersApi.md#update_supplierorders) | **PUT** /supplierorders/{id} | Update supplier order 🔐


# **create_supplierorders**
> int create_supplierorders(create_supplierorders_model=create_supplierorders_model)

Create supplier order object 🔐

Example: {"ref": "auto", "ref_supplier": "1234", "socid": "1", "multicurrency_code": "SEK", "multicurrency_tx": 1, "tva_tx": 25, "note": "Imported via the REST API"}

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_supplierorders_model import CreateSupplierordersModel
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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    create_supplierorders_model = dolibarr_api.CreateSupplierordersModel() # CreateSupplierordersModel | request_data    (optional)

    try:
        # Create supplier order object 🔐
        api_response = api_instance.create_supplierorders(create_supplierorders_model=create_supplierorders_model)
        print("The response of SupplierordersApi->create_supplierorders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->create_supplierorders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_supplierorders_model** | [**CreateSupplierordersModel**](CreateSupplierordersModel.md)| request_data    | [optional] 

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

# **list_supplierorders**
> List[str] list_supplierorders(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, product_ids=product_ids, status=status, sqlfilters=sqlfilters, sqlfilterlines=sqlfilterlines, properties=properties, pagination_data=pagination_data)

List orders 🔐

Get a list of supplier orders

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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter orders of (example '1' or '1,2,3') (optional)
    product_ids = 'product_ids_example' # str | Product ids to filter orders of (example '1' or '1,2,3') (optional)
    status = 'status_example' # str | Filter by order status : draft | validated | approved | running | received_start | received_end | cancelled | refused (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'20160101')\" (optional)
    sqlfilterlines = 'sqlfilterlines_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(tl.fk_product:=:'17') and (tl.price:<:'250')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List orders 🔐
        api_response = api_instance.list_supplierorders(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, product_ids=product_ids, status=status, sqlfilters=sqlfilters, sqlfilterlines=sqlfilterlines, properties=properties, pagination_data=pagination_data)
        print("The response of SupplierordersApi->list_supplierorders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->list_supplierorders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **thirdparty_ids** | **str**| Thirdparty ids to filter orders of (example &#39;1&#39; or &#39;1,2,3&#39;) | [optional] 
 **product_ids** | **str**| Product ids to filter orders of (example &#39;1&#39; or &#39;1,2,3&#39;) | [optional] 
 **status** | **str**| Filter by order status : draft | validated | approved | running | received_start | received_end | cancelled | refused | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:&#39;SO-%&#39;) and (t.datec:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
 **sqlfilterlines** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(tl.fk_product:&#x3D;:&#39;17&#39;) and (tl.price:&lt;:&#39;250&#39;)\&quot; | [optional] 
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

# **remove_supplierorders**
> List[str] remove_supplierorders(id)

Delete supplier order 🔐

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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | Supplier order ID

    try:
        # Delete supplier order 🔐
        api_response = api_instance.remove_supplierorders(id)
        print("The response of SupplierordersApi->remove_supplierorders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->remove_supplierorders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Supplier order ID | 

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

# **retrieve_supplierorders**
> str retrieve_supplierorders(id)

Get properties of a supplier order object 🔐

Return an array with supplier order information

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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | ID of supplier order

    try:
        # Get properties of a supplier order object 🔐
        api_response = api_instance.retrieve_supplierorders(id)
        print("The response of SupplierordersApi->retrieve_supplierorders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->retrieve_supplierorders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of supplier order | 

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

# **supplierorders_approve**
> List[str] supplierorders_approve(id, supplierorders_approve_model=supplierorders_approve_model)

Approve an order 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.supplierorders_approve_model import SupplierordersApproveModel
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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | Order ID
    supplierorders_approve_model = dolibarr_api.SupplierordersApproveModel() # SupplierordersApproveModel | idwarehouse   secondlevel    (optional)

    try:
        # Approve an order 🔐
        api_response = api_instance.supplierorders_approve(id, supplierorders_approve_model=supplierorders_approve_model)
        print("The response of SupplierordersApi->supplierorders_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->supplierorders_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **supplierorders_approve_model** | [**SupplierordersApproveModel**](SupplierordersApproveModel.md)| idwarehouse   secondlevel    | [optional] 

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

# **supplierorders_create_contact**
> List[str] supplierorders_create_contact(id, contactid, type, source)

Add a contact type of given supplier order 🔐

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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | Id of supplier order to update
    contactid = 56 # int | Id of contact/user to add
    type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER, SALESREPFOLL, ...)
    source = 'source_example' # str | Source of the contact (external, internal)

    try:
        # Add a contact type of given supplier order 🔐
        api_response = api_instance.supplierorders_create_contact(id, contactid, type, source)
        print("The response of SupplierordersApi->supplierorders_create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->supplierorders_create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier order to update | 
 **contactid** | **int**| Id of contact/user to add | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER, SALESREPFOLL, ...) | 
 **source** | **str**| Source of the contact (external, internal) | 

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

# **supplierorders_make_order**
> List[str] supplierorders_make_order(id, supplierorders_make_order_model)

Sends an order to the vendor 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.supplierorders_make_order_model import SupplierordersMakeOrderModel
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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | Order ID
    supplierorders_make_order_model = dolibarr_api.SupplierordersMakeOrderModel() # SupplierordersMakeOrderModel | **date** (required)   **method** (required)   comment   

    try:
        # Sends an order to the vendor 🔐
        api_response = api_instance.supplierorders_make_order(id, supplierorders_make_order_model)
        print("The response of SupplierordersApi->supplierorders_make_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->supplierorders_make_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **supplierorders_make_order_model** | [**SupplierordersMakeOrderModel**](SupplierordersMakeOrderModel.md)| **date** (required)   **method** (required)   comment    | 

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

# **supplierorders_receive_order**
> List[str] supplierorders_receive_order(id, supplierorders_receive_order_model)

Receives the order, dispatches products. 🔐

 Example: <code> { "closeopenorder": 1, "comment": "", "lines": [{ "id": 14, "fk_product": 112, "qty": 18, "warehouse": 1, "price": 114, "comment": "", "eatby": 0, "sellby": 0, "batch": 0, "notrigger": 0 }] }</code>

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.supplierorders_receive_order_model import SupplierordersReceiveOrderModel
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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | Order ID
    supplierorders_receive_order_model = dolibarr_api.SupplierordersReceiveOrderModel() # SupplierordersReceiveOrderModel | **closeopenorder** (required)   **comment** (required)   **lines** (required)   

    try:
        # Receives the order, dispatches products. 🔐
        api_response = api_instance.supplierorders_receive_order(id, supplierorders_receive_order_model)
        print("The response of SupplierordersApi->supplierorders_receive_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->supplierorders_receive_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **supplierorders_receive_order_model** | [**SupplierordersReceiveOrderModel**](SupplierordersReceiveOrderModel.md)| **closeopenorder** (required)   **comment** (required)   **lines** (required)    | 

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

# **supplierorders_remove_contact**
> List[str] supplierorders_remove_contact(id, contactid, type, source)

Unlink a contact type of given supplier order 🔐

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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | Id of supplier order to update
    contactid = 56 # int | Id of contact/user to add
    type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER, SALESREPFOLL, ...).
    source = 'source_example' # str | Source of the contact (internal, external).

    try:
        # Unlink a contact type of given supplier order 🔐
        api_response = api_instance.supplierorders_remove_contact(id, contactid, type, source)
        print("The response of SupplierordersApi->supplierorders_remove_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->supplierorders_remove_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier order to update | 
 **contactid** | **int**| Id of contact/user to add | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER, SALESREPFOLL, ...). | 
 **source** | **str**| Source of the contact (internal, external). | 

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
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supplierorders_retrieve_contacts**
> Dict[str, object] supplierorders_retrieve_contacts(id, source, type=type)

Get contacts of given supplier order 🔐

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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | ID of supplier order
    source = 'source_example' # str | Source of the contact (internal, external, all).
    type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER, SALESREPFOLL, ...) (optional)

    try:
        # Get contacts of given supplier order 🔐
        api_response = api_instance.supplierorders_retrieve_contacts(id, source, type=type)
        print("The response of SupplierordersApi->supplierorders_retrieve_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->supplierorders_retrieve_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of supplier order | 
 **source** | **str**| Source of the contact (internal, external, all). | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER, SALESREPFOLL, ...) | [optional] 

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

# **supplierorders_validate**
> List[str] supplierorders_validate(id, supplierorders_validate_model=supplierorders_validate_model)

Validate an order 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.supplierorders_validate_model import SupplierordersValidateModel
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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | Order ID
    supplierorders_validate_model = dolibarr_api.SupplierordersValidateModel() # SupplierordersValidateModel | idwarehouse   notrigger    (optional)

    try:
        # Validate an order 🔐
        api_response = api_instance.supplierorders_validate(id, supplierorders_validate_model=supplierorders_validate_model)
        print("The response of SupplierordersApi->supplierorders_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->supplierorders_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **supplierorders_validate_model** | [**SupplierordersValidateModel**](SupplierordersValidateModel.md)| idwarehouse   notrigger    | [optional] 

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

# **update_supplierorders**
> str update_supplierorders(id, update_supplierorders_model=update_supplierorders_model)

Update supplier order 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_supplierorders_model import UpdateSupplierordersModel
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
    api_instance = dolibarr_api.SupplierordersApi(api_client)
    id = 56 # int | Id of supplier order to update
    update_supplierorders_model = dolibarr_api.UpdateSupplierordersModel() # UpdateSupplierordersModel | request_data    (optional)

    try:
        # Update supplier order 🔐
        api_response = api_instance.update_supplierorders(id, update_supplierorders_model=update_supplierorders_model)
        print("The response of SupplierordersApi->update_supplierorders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupplierordersApi->update_supplierorders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of supplier order to update | 
 **update_supplierorders_model** | [**UpdateSupplierordersModel**](UpdateSupplierordersModel.md)| request_data    | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

