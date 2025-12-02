# dolibarr_api.OrdersApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_orders**](OrdersApi.md#create_orders) | **POST** /orders | Create a sale order 🔐
[**list_orders**](OrdersApi.md#list_orders) | **GET** /orders | List orders 🔐
[**orders_close**](OrdersApi.md#orders_close) | **POST** /orders/{id}/close | Close an order (Classify it as \&quot;Delivered\&quot;) 🔐
[**orders_create_contact**](OrdersApi.md#orders_create_contact) | **POST** /orders/{id}/contact/{contactid}/{type} | Add a contact type of given order 🔐
[**orders_create_line**](OrdersApi.md#orders_create_line) | **POST** /orders/{id}/lines | Add a line to given order 🔐
[**orders_create_order_from_proposal**](OrdersApi.md#orders_create_order_from_proposal) | **POST** /orders/createfromproposal/{proposalid} | Create an order using an existing proposal. 🔐
[**orders_create_order_shipment**](OrdersApi.md#orders_create_order_shipment) | **POST** /orders/{id}/shipment/{warehouse_id} | Create the shipment of an order 🔐
[**orders_remove_contact**](OrdersApi.md#orders_remove_contact) | **DELETE** /orders/{id}/contact/{contactid}/{type} | Unlink a contact type of given order 🔐
[**orders_remove_line**](OrdersApi.md#orders_remove_line) | **DELETE** /orders/{id}/lines/{lineid} | Delete a line of a given order 🔐
[**orders_reopen**](OrdersApi.md#orders_reopen) | **POST** /orders/{id}/reopen | Tag the order as validated (opened) 🔐
[**orders_retrieve_by_ref**](OrdersApi.md#orders_retrieve_by_ref) | **GET** /orders/ref/{ref} | Get properties of an order object by ref 🔐
[**orders_retrieve_by_ref_ext**](OrdersApi.md#orders_retrieve_by_ref_ext) | **GET** /orders/ref_ext/{ref_ext} | Get properties of an order object by ref_ext 🔐
[**orders_retrieve_contacts**](OrdersApi.md#orders_retrieve_contacts) | **GET** /orders/{id}/contacts | Get contacts of given order 🔐
[**orders_retrieve_line**](OrdersApi.md#orders_retrieve_line) | **GET** /orders/{id}/lines/{lineid} | Get properties of a line of an order object by id 🔐
[**orders_retrieve_lines**](OrdersApi.md#orders_retrieve_lines) | **GET** /orders/{id}/lines | Get lines of an order 🔐
[**orders_retrieve_order_shipments**](OrdersApi.md#orders_retrieve_order_shipments) | **GET** /orders/{id}/shipment | Get the shipments of an order 🔐
[**orders_setinvoiced**](OrdersApi.md#orders_setinvoiced) | **POST** /orders/{id}/setinvoiced | Classify the order as invoiced. Could be also called setbilled 🔐
[**orders_settodraft**](OrdersApi.md#orders_settodraft) | **POST** /orders/{id}/settodraft | Set an order to draft 🔐
[**orders_update_line**](OrdersApi.md#orders_update_line) | **PUT** /orders/{id}/lines/{lineid} | Update a line to given order 🔐
[**orders_validate**](OrdersApi.md#orders_validate) | **POST** /orders/{id}/validate | Validate an order 🔐
[**remove_orders**](OrdersApi.md#remove_orders) | **DELETE** /orders/{id} | Delete order 🔐
[**retrieve_orders**](OrdersApi.md#retrieve_orders) | **GET** /orders/{id} | Get properties of an order object by id 🔐
[**update_orders**](OrdersApi.md#update_orders) | **PUT** /orders/{id} | Update order general fields (won&#39;t touch lines of order) 🔐


# **create_orders**
> int create_orders(create_orders_model=create_orders_model)

Create a sale order 🔐

Example: { "socid": 2, "date": 1595196000, "type": 0, "lines": [{ "fk_product": 2, "qty": 1 }] }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_orders_model import CreateOrdersModel
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
    api_instance = dolibarr_api.OrdersApi(api_client)
    create_orders_model = dolibarr_api.CreateOrdersModel() # CreateOrdersModel | request_data    (optional)

    try:
        # Create a sale order 🔐
        api_response = api_instance.create_orders(create_orders_model=create_orders_model)
        print("The response of OrdersApi->create_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_orders_model** | [**CreateOrdersModel**](CreateOrdersModel.md)| request_data    | [optional] 

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

# **list_orders**
> List[str] list_orders(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, sqlfilterlines=sqlfilterlines, properties=properties, pagination_data=pagination_data, loadlinkedobjects=loadlinkedobjects)

List orders 🔐

Get a list of orders

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    thirdparty_ids = 'thirdparty_ids_example' # str | Thirdparty ids to filter orders of (example '1' or '1,2,3') (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\" (optional)
    sqlfilterlines = 'sqlfilterlines_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(tl.fk_product:=:'17') and (tl.price:<:'250')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)
    loadlinkedobjects = 56 # int | Load also linked object (optional)

    try:
        # List orders 🔐
        api_response = api_instance.list_orders(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, thirdparty_ids=thirdparty_ids, sqlfilters=sqlfilters, sqlfilterlines=sqlfilterlines, properties=properties, pagination_data=pagination_data, loadlinkedobjects=loadlinkedobjects)
        print("The response of OrdersApi->list_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->list_orders: %s\n" % e)
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
 **sqlfilterlines** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(tl.fk_product:&#x3D;:&#39;17&#39;) and (tl.price:&lt;:&#39;250&#39;)\&quot; | [optional] 
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
**404** | Not found |  -  |
**503** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_close**
> Dict[str, object] orders_close(id, orders_close_model=orders_close_model)

Close an order (Classify it as \"Delivered\") 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.orders_close_model import OrdersCloseModel
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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Order ID
    orders_close_model = dolibarr_api.OrdersCloseModel() # OrdersCloseModel | notrigger    (optional)

    try:
        # Close an order (Classify it as \"Delivered\") 🔐
        api_response = api_instance.orders_close(id, orders_close_model=orders_close_model)
        print("The response of OrdersApi->orders_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **orders_close_model** | [**OrdersCloseModel**](OrdersCloseModel.md)| notrigger    | [optional] 

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

# **orders_create_contact**
> List[str] orders_create_contact(id, contactid, type)

Add a contact type of given order 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of order to update
    contactid = 56 # int | Id of contact to add
    type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER)

    try:
        # Add a contact type of given order 🔐
        api_response = api_instance.orders_create_contact(id, contactid, type)
        print("The response of OrdersApi->orders_create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **contactid** | **int**| Id of contact to add | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER) | 

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

# **orders_create_line**
> int orders_create_line(id, orders_create_line_model=orders_create_line_model)

Add a line to given order 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.orders_create_line_model import OrdersCreateLineModel
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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of order to update
    orders_create_line_model = dolibarr_api.OrdersCreateLineModel() # OrdersCreateLineModel | request_data    (optional)

    try:
        # Add a line to given order 🔐
        api_response = api_instance.orders_create_line(id, orders_create_line_model=orders_create_line_model)
        print("The response of OrdersApi->orders_create_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_create_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **orders_create_line_model** | [**OrdersCreateLineModel**](OrdersCreateLineModel.md)| request_data    | [optional] 

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

# **orders_create_order_from_proposal**
> Dict[str, object] orders_create_order_from_proposal(proposalid)

Create an order using an existing proposal. 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    proposalid = 56 # int | Id of the proposal

    try:
        # Create an order using an existing proposal. 🔐
        api_response = api_instance.orders_create_order_from_proposal(proposalid)
        print("The response of OrdersApi->orders_create_order_from_proposal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_create_order_from_proposal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposalid** | **int**| Id of the proposal | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_create_order_shipment**
> int orders_create_order_shipment(id, warehouse_id)

Create the shipment of an order 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of the order
    warehouse_id = 56 # int | Id of a warehouse

    try:
        # Create the shipment of an order 🔐
        api_response = api_instance.orders_create_order_shipment(id, warehouse_id)
        print("The response of OrdersApi->orders_create_order_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_create_order_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the order | 
 **warehouse_id** | **int**| Id of a warehouse | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_remove_contact**
> List[str] orders_remove_contact(id, contactid, type)

Unlink a contact type of given order 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of order to update
    contactid = 56 # int | Id of contact
    type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER).

    try:
        # Unlink a contact type of given order 🔐
        api_response = api_instance.orders_remove_contact(id, contactid, type)
        print("The response of OrdersApi->orders_remove_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_remove_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **contactid** | **int**| Id of contact | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER). | 

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

# **orders_remove_line**
> Dict[str, object] orders_remove_line(id, lineid)

Delete a line of a given order 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of order to update
    lineid = 56 # int | Id of line to delete

    try:
        # Delete a line of a given order 🔐
        api_response = api_instance.orders_remove_line(id, lineid)
        print("The response of OrdersApi->orders_remove_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_remove_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **lineid** | **int**| Id of line to delete | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_reopen**
> int orders_reopen(id)

Tag the order as validated (opened) 🔐

Function used when order is reopend after being closed.

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of the order

    try:
        # Tag the order as validated (opened) 🔐
        api_response = api_instance.orders_reopen(id)
        print("The response of OrdersApi->orders_reopen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_reopen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the order | 

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
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_retrieve_by_ref**
> str orders_retrieve_by_ref(ref, contact_list=contact_list)

Get properties of an order object by ref 🔐

Return an array with order information

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    ref = 'ref_example' # str | Ref of object
    contact_list = 56 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id, -1: Do not return contacts/adddesses (optional)

    try:
        # Get properties of an order object by ref 🔐
        api_response = api_instance.orders_retrieve_by_ref(ref, contact_list=contact_list)
        print("The response of OrdersApi->orders_retrieve_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_retrieve_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of object | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id, -1: Do not return contacts/adddesses | [optional] 

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

# **orders_retrieve_by_ref_ext**
> str orders_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)

Get properties of an order object by ref_ext 🔐

Return an array with order information

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    ref_ext = 'ref_ext_example' # str | External reference of object
    contact_list = 56 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id, -1: Do not return contacts/adddesses (optional)

    try:
        # Get properties of an order object by ref_ext 🔐
        api_response = api_instance.orders_retrieve_by_ref_ext(ref_ext, contact_list=contact_list)
        print("The response of OrdersApi->orders_retrieve_by_ref_ext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_retrieve_by_ref_ext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_ext** | **str**| External reference of object | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id, -1: Do not return contacts/adddesses | [optional] 

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

# **orders_retrieve_contacts**
> Dict[str, object] orders_retrieve_contacts(id, type=type)

Get contacts of given order 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | ID of order
    type = 'type_example' # str | Type of the contact (BILLING, SHIPPING, CUSTOMER) (optional)

    try:
        # Get contacts of given order 🔐
        api_response = api_instance.orders_retrieve_contacts(id, type=type)
        print("The response of OrdersApi->orders_retrieve_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_retrieve_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of order | 
 **type** | **str**| Type of the contact (BILLING, SHIPPING, CUSTOMER) | [optional] 

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

# **orders_retrieve_line**
> Dict[str, object] orders_retrieve_line(id, lineid, properties=properties)

Get properties of a line of an order object by id 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of order
    lineid = 56 # int | Id of line
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # Get properties of a line of an order object by id 🔐
        api_response = api_instance.orders_retrieve_line(id, lineid, properties=properties)
        print("The response of OrdersApi->orders_retrieve_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_retrieve_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order | 
 **lineid** | **int**| Id of line | 
 **properties** | **str**| Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_retrieve_lines**
> List[str] orders_retrieve_lines(id)

Get lines of an order 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of order

    try:
        # Get lines of an order 🔐
        api_response = api_instance.orders_retrieve_lines(id)
        print("The response of OrdersApi->orders_retrieve_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_retrieve_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order | 

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

# **orders_retrieve_order_shipments**
> List[str] orders_retrieve_order_shipments(id)

Get the shipments of an order 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of the order

    try:
        # Get the shipments of an order 🔐
        api_response = api_instance.orders_retrieve_order_shipments(id)
        print("The response of OrdersApi->orders_retrieve_order_shipments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_retrieve_order_shipments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the order | 

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

# **orders_setinvoiced**
> Dict[str, object] orders_setinvoiced(id)

Classify the order as invoiced. Could be also called setbilled 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of the order

    try:
        # Classify the order as invoiced. Could be also called setbilled 🔐
        api_response = api_instance.orders_setinvoiced(id)
        print("The response of OrdersApi->orders_setinvoiced:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_setinvoiced: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the order | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_settodraft**
> Dict[str, object] orders_settodraft(id, orders_settodraft_model=orders_settodraft_model)

Set an order to draft 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.orders_settodraft_model import OrdersSettodraftModel
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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Order ID
    orders_settodraft_model = dolibarr_api.OrdersSettodraftModel() # OrdersSettodraftModel | idwarehouse    (optional)

    try:
        # Set an order to draft 🔐
        api_response = api_instance.orders_settodraft(id, orders_settodraft_model=orders_settodraft_model)
        print("The response of OrdersApi->orders_settodraft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_settodraft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **orders_settodraft_model** | [**OrdersSettodraftModel**](OrdersSettodraftModel.md)| idwarehouse    | [optional] 

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

# **orders_update_line**
> str orders_update_line(id, lineid, orders_update_line_model=orders_update_line_model)

Update a line to given order 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.orders_update_line_model import OrdersUpdateLineModel
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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of order to update
    lineid = 56 # int | Id of line to update
    orders_update_line_model = dolibarr_api.OrdersUpdateLineModel() # OrdersUpdateLineModel | request_data    (optional)

    try:
        # Update a line to given order 🔐
        api_response = api_instance.orders_update_line(id, lineid, orders_update_line_model=orders_update_line_model)
        print("The response of OrdersApi->orders_update_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_update_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **lineid** | **int**| Id of line to update | 
 **orders_update_line_model** | [**OrdersUpdateLineModel**](OrdersUpdateLineModel.md)| request_data    | [optional] 

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

# **orders_validate**
> Dict[str, object] orders_validate(id, orders_validate_model=orders_validate_model)

Validate an order 🔐

If you get a bad value for param notrigger check, provide this in body { "idwarehouse": 0, "notrigger": 0 }

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.orders_validate_model import OrdersValidateModel
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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Order ID
    orders_validate_model = dolibarr_api.OrdersValidateModel() # OrdersValidateModel | idwarehouse   notrigger    (optional)

    try:
        # Validate an order 🔐
        api_response = api_instance.orders_validate(id, orders_validate_model=orders_validate_model)
        print("The response of OrdersApi->orders_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **orders_validate_model** | [**OrdersValidateModel**](OrdersValidateModel.md)| idwarehouse   notrigger    | [optional] 

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

# **remove_orders**
> List[str] remove_orders(id)

Delete order 🔐

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Order ID

    try:
        # Delete order 🔐
        api_response = api_instance.remove_orders(id)
        print("The response of OrdersApi->remove_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->remove_orders: %s\n" % e)
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

# **retrieve_orders**
> str retrieve_orders(id, contact_list=contact_list)

Get properties of an order object by id 🔐

Return an array with order information

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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | ID of order
    contact_list = 56 # int | 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id, -1: Do not return contacts/adddesses (optional)

    try:
        # Get properties of an order object by id 🔐
        api_response = api_instance.retrieve_orders(id, contact_list=contact_list)
        print("The response of OrdersApi->retrieve_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->retrieve_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of order | 
 **contact_list** | **int**| 0: Returned array of contacts/addresses contains all properties, 1: Return array contains just id, -1: Do not return contacts/adddesses | [optional] 

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

# **update_orders**
> Dict[str, object] update_orders(id, update_orders_model=update_orders_model)

Update order general fields (won't touch lines of order) 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_orders_model import UpdateOrdersModel
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
    api_instance = dolibarr_api.OrdersApi(api_client)
    id = 56 # int | Id of order to update
    update_orders_model = dolibarr_api.UpdateOrdersModel() # UpdateOrdersModel | request_data    (optional)

    try:
        # Update order general fields (won't touch lines of order) 🔐
        api_response = api_instance.update_orders(id, update_orders_model=update_orders_model)
        print("The response of OrdersApi->update_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->update_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of order to update | 
 **update_orders_model** | [**UpdateOrdersModel**](UpdateOrdersModel.md)| request_data    | [optional] 

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

