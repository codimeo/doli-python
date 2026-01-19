# dolibarr_api.StockmovementsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stockmovements**](StockmovementsApi.md#create_stockmovements) | **POST** /stockmovements | Create stock movement object. 🔐
[**list_stockmovements**](StockmovementsApi.md#list_stockmovements) | **GET** /stockmovements | Get a list of stock movement 🔐


# **create_stockmovements**
> int create_stockmovements(create_stockmovements_model)

Create stock movement object. 🔐

You can use the following message to test this RES API: { "product_id": 1, "warehouse_id": 1, "qty": 1, "lot": "", "movementcode": "INV123", "movementlabel": "Inventory 123", "price": 0 } $price Can be set to update AWP (Average Weighted Price) when you make a stock increase $dlc Eat-by date. Will be used if lot does not exists yet and will be created. $dluo Sell-by date. Will be used if lot does not exists yet and will be created.

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_stockmovements_model import CreateStockmovementsModel
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
    api_instance = dolibarr_api.StockmovementsApi(api_client)
    create_stockmovements_model = dolibarr_api.CreateStockmovementsModel() # CreateStockmovementsModel | **product_id** (required)   **warehouse_id** (required)   **qty** (required)   type   lot   movementcode   movementlabel   price   datem   dlc   dluo   origin_type   origin_id   

    try:
        # Create stock movement object. 🔐
        api_response = api_instance.create_stockmovements(create_stockmovements_model)
        print("The response of StockmovementsApi->create_stockmovements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockmovementsApi->create_stockmovements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stockmovements_model** | [**CreateStockmovementsModel**](CreateStockmovementsModel.md)| **product_id** (required)   **warehouse_id** (required)   **qty** (required)   type   lot   movementcode   movementlabel   price   datem   dlc   dluo   origin_type   origin_id    | 

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

# **list_stockmovements**
> List[str] list_stockmovements(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties)

Get a list of stock movement 🔐

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
    api_instance = dolibarr_api.StockmovementsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.fk_product:=:1) and (t.date_creation:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # Get a list of stock movement 🔐
        api_response = api_instance.list_stockmovements(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties)
        print("The response of StockmovementsApi->list_stockmovements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StockmovementsApi->list_stockmovements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.fk_product:&#x3D;:1) and (t.date_creation:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
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

