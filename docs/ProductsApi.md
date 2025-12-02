# dolibarr_api.ProductsApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_products**](ProductsApi.md#create_products) | **POST** /products | Create a product 🔐
[**list_products**](ProductsApi.md#list_products) | **GET** /products | List products 🔐
[**products_add_attribute_value**](ProductsApi.md#products_add_attribute_value) | **POST** /products/attributes/{id}/values | Add attribute value 🔐
[**products_add_attributes**](ProductsApi.md#products_add_attributes) | **POST** /products/attributes | Add attributes 🔐
[**products_add_purchase_price**](ProductsApi.md#products_add_purchase_price) | **POST** /products/{id}/purchase_prices | Add/Update purchase prices for a product 🔐
[**products_add_subproducts**](ProductsApi.md#products_add_subproducts) | **POST** /products/{id}/subproducts/add | Add a subproduct 🔐
[**products_add_variant**](ProductsApi.md#products_add_variant) | **POST** /products/{id}/variants | Add variant 🔐
[**products_add_variant_by_product_ref**](ProductsApi.md#products_add_variant_by_product_ref) | **POST** /products/ref/{ref}/variants | Add variant by product ref 🔐
[**products_del_subproducts**](ProductsApi.md#products_del_subproducts) | **DELETE** /products/{id}/subproducts/remove/{subproduct_id} | Remove a subproduct 🔐
[**products_remove_attribute_value_by_id**](ProductsApi.md#products_remove_attribute_value_by_id) | **DELETE** /products/attributes/values/{id} | Delete attribute value by ID 🔐
[**products_remove_attribute_value_by_ref**](ProductsApi.md#products_remove_attribute_value_by_ref) | **DELETE** /products/attributes/{id}/values/ref/{ref} | Delete attribute value by ref 🔐
[**products_remove_attributes**](ProductsApi.md#products_remove_attributes) | **DELETE** /products/attributes/{id} | Delete attributes by ID 🔐
[**products_remove_purchase_price**](ProductsApi.md#products_remove_purchase_price) | **DELETE** /products/{id}/purchase_prices/{priceid} | Delete a purchase price for a product 🔐
[**products_remove_variant**](ProductsApi.md#products_remove_variant) | **DELETE** /products/variants/{id} | Delete product variants 🔐
[**products_retrieve_attribute_by_id**](ProductsApi.md#products_retrieve_attribute_by_id) | **GET** /products/attributes/{id} | Get attribute by ID 🔐
[**products_retrieve_attribute_value_by_id**](ProductsApi.md#products_retrieve_attribute_value_by_id) | **GET** /products/attributes/values/{id} | Get attribute value by ID 🔐
[**products_retrieve_attribute_value_by_ref**](ProductsApi.md#products_retrieve_attribute_value_by_ref) | **GET** /products/attributes/{id}/values/ref/{ref} | Get attribute value by ref 🔐
[**products_retrieve_attribute_values**](ProductsApi.md#products_retrieve_attribute_values) | **GET** /products/attributes/{id}/values | Get all values for an attribute ID 🔐
[**products_retrieve_attribute_values_by_ref**](ProductsApi.md#products_retrieve_attribute_values_by_ref) | **GET** /products/attributes/ref/{ref}/values | Get all values for an attribute ref 🔐
[**products_retrieve_attributes**](ProductsApi.md#products_retrieve_attributes) | **GET** /products/attributes | Get attributes 🔐
[**products_retrieve_attributes_by_ref**](ProductsApi.md#products_retrieve_attributes_by_ref) | **GET** /products/attributes/ref/{ref} | Get attributes by ref 🔐
[**products_retrieve_attributes_by_ref_ext**](ProductsApi.md#products_retrieve_attributes_by_ref_ext) | **GET** /products/attributes/ref_ext/{ref_ext} | Get attributes by ref_ext 🔐
[**products_retrieve_by_barcode**](ProductsApi.md#products_retrieve_by_barcode) | **GET** /products/barcode/{barcode} | Get product by barcode 🔐
[**products_retrieve_by_ref**](ProductsApi.md#products_retrieve_by_ref) | **GET** /products/ref/{ref} | Get product by ref 🔐
[**products_retrieve_by_ref_ext**](ProductsApi.md#products_retrieve_by_ref_ext) | **GET** /products/ref_ext/{ref_ext} | Get product by ref_ext 🔐
[**products_retrieve_categories**](ProductsApi.md#products_retrieve_categories) | **GET** /products/{id}/categories | Get categories for a product 🔐
[**products_retrieve_customer_prices_per_customer**](ProductsApi.md#products_retrieve_customer_prices_per_customer) | **GET** /products/{id}/selling_multiprices/per_customer | Get prices per customer for a product 🔐
[**products_retrieve_customer_prices_per_quantity**](ProductsApi.md#products_retrieve_customer_prices_per_quantity) | **GET** /products/{id}/selling_multiprices/per_quantity | Get prices per quantity for a product 🔐
[**products_retrieve_customer_prices_per_segment**](ProductsApi.md#products_retrieve_customer_prices_per_segment) | **GET** /products/{id}/selling_multiprices/per_segment | Get prices per segment for a product 🔐
[**products_retrieve_purchase_prices**](ProductsApi.md#products_retrieve_purchase_prices) | **GET** /products/{id}/purchase_prices | Get purchase prices for a product 🔐
[**products_retrieve_stock**](ProductsApi.md#products_retrieve_stock) | **GET** /products/{id}/stock | Get stock data for a product 🔐
[**products_retrieve_subproducts**](ProductsApi.md#products_retrieve_subproducts) | **GET** /products/{id}/subproducts | Get the list of subproducts of a product 🔐
[**products_retrieve_supplier_products**](ProductsApi.md#products_retrieve_supplier_products) | **GET** /products/purchase_prices | Get a list of all purchase prices of products 🔐
[**products_retrieve_variants**](ProductsApi.md#products_retrieve_variants) | **GET** /products/{id}/variants | Get product variants 🔐
[**products_retrieve_variants_by_prod_ref**](ProductsApi.md#products_retrieve_variants_by_prod_ref) | **GET** /products/ref/{ref}/variants | Get product variants by Product ref 🔐
[**products_update_attribute_value**](ProductsApi.md#products_update_attribute_value) | **PUT** /products/attributes/values/{id} | Update attribute value 🔐
[**products_update_attributes**](ProductsApi.md#products_update_attributes) | **PUT** /products/attributes/{id} | Update attributes by ID 🔐
[**products_update_variant**](ProductsApi.md#products_update_variant) | **PUT** /products/variants/{id} | Update product variants 🔐
[**remove_products**](ProductsApi.md#remove_products) | **DELETE** /products/{id} | Delete a product 🔐
[**retrieve_products**](ProductsApi.md#retrieve_products) | **GET** /products/{id} | Get a product 🔐
[**update_products**](ProductsApi.md#update_products) | **PUT** /products/{id} | Update a product 🔐


# **create_products**
> int create_products(create_products_model=create_products_model)

Create a product 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_products_model import CreateProductsModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    create_products_model = dolibarr_api.CreateProductsModel() # CreateProductsModel | request_data    (optional)

    try:
        # Create a product 🔐
        api_response = api_instance.create_products(create_products_model=create_products_model)
        print("The response of ProductsApi->create_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->create_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_products_model** | [**CreateProductsModel**](CreateProductsModel.md)| request_data    | [optional] 

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

# **list_products**
> List[str] list_products(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, sqlfilters=sqlfilters, ids_only=ids_only, variant_filter=variant_filter, pagination_data=pagination_data, includestockdata=includestockdata, properties=properties)

List products 🔐

Get a list of products

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    mode = 56 # int | Use this param to filter list (0 for all, 1 for only product, 2 for only service) (optional)
    category = 56 # int | Use this param to filter list by category (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.tobuy:=:0) and (t.tosell:=:1)\" (optional)
    ids_only = True # bool | Return only IDs of product instead of all properties (faster, above all if list is long) (optional)
    variant_filter = 56 # int | Use this param to filter list (0 = all, 1=products without variants, 2=parent of variants, 3=variants only) (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0 (optional)
    includestockdata = 56 # int | Load also information about stock (slower) (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # List products 🔐
        api_response = api_instance.list_products(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, sqlfilters=sqlfilters, ids_only=ids_only, variant_filter=variant_filter, pagination_data=pagination_data, includestockdata=includestockdata, properties=properties)
        print("The response of ProductsApi->list_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->list_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **mode** | **int**| Use this param to filter list (0 for all, 1 for only product, 2 for only service) | [optional] 
 **category** | **int**| Use this param to filter list by category | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.tobuy:&#x3D;:0) and (t.tosell:&#x3D;:1)\&quot; | [optional] 
 **ids_only** | **bool**| Return only IDs of product instead of all properties (faster, above all if list is long) | [optional] 
 **variant_filter** | **int**| Use this param to filter list (0 &#x3D; all, 1&#x3D;products without variants, 2&#x3D;parent of variants, 3&#x3D;variants only) | [optional] 
 **pagination_data** | **bool**| If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0 | [optional] 
 **includestockdata** | **int**| Load also information about stock (slower) | [optional] 
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

# **products_add_attribute_value**
> int products_add_attribute_value(id, products_add_attribute_value_model)

Add attribute value 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.products_add_attribute_value_model import ProductsAddAttributeValueModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Attribute
    products_add_attribute_value_model = dolibarr_api.ProductsAddAttributeValueModel() # ProductsAddAttributeValueModel | **ref** (required)   **value** (required)   

    try:
        # Add attribute value 🔐
        api_response = api_instance.products_add_attribute_value(id, products_add_attribute_value_model)
        print("The response of ProductsApi->products_add_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_add_attribute_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 
 **products_add_attribute_value_model** | [**ProductsAddAttributeValueModel**](ProductsAddAttributeValueModel.md)| **ref** (required)   **value** (required)    | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_attributes**
> int products_add_attributes(products_add_attributes_model)

Add attributes 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.products_add_attributes_model import ProductsAddAttributesModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    products_add_attributes_model = dolibarr_api.ProductsAddAttributesModel() # ProductsAddAttributesModel | **ref** (required)   **label** (required)   ref_ext   

    try:
        # Add attributes 🔐
        api_response = api_instance.products_add_attributes(products_add_attributes_model)
        print("The response of ProductsApi->products_add_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_add_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **products_add_attributes_model** | [**ProductsAddAttributesModel**](ProductsAddAttributesModel.md)| **ref** (required)   **label** (required)   ref_ext    | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_purchase_price**
> int products_add_purchase_price(id, products_add_purchase_price_model)

Add/Update purchase prices for a product 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.products_add_purchase_price_model import ProductsAddPurchasePriceModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Product
    products_add_purchase_price_model = dolibarr_api.ProductsAddPurchasePriceModel() # ProductsAddPurchasePriceModel | **qty** (required)   **buyprice** (required)   **price_base_type** (required)   **fourn_id** (required)   **availability** (required)   **ref_fourn** (required)   **tva_tx** (required)   charges   remise_percent   remise   newnpr   delivery_time_days   supplier_reputation   localtaxes_array   newdefaultvatcode   multicurrency_buyprice   multicurrency_price_base_type   multicurrency_tx   multicurrency_code   desc_fourn   barcode   fk_barcode_type   

    try:
        # Add/Update purchase prices for a product 🔐
        api_response = api_instance.products_add_purchase_price(id, products_add_purchase_price_model)
        print("The response of ProductsApi->products_add_purchase_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_add_purchase_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Product | 
 **products_add_purchase_price_model** | [**ProductsAddPurchasePriceModel**](ProductsAddPurchasePriceModel.md)| **qty** (required)   **buyprice** (required)   **price_base_type** (required)   **fourn_id** (required)   **availability** (required)   **ref_fourn** (required)   **tva_tx** (required)   charges   remise_percent   remise   newnpr   delivery_time_days   supplier_reputation   localtaxes_array   newdefaultvatcode   multicurrency_buyprice   multicurrency_price_base_type   multicurrency_tx   multicurrency_code   desc_fourn   barcode   fk_barcode_type    | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_subproducts**
> int products_add_subproducts(id, products_add_subproducts_model)

Add a subproduct 🔐

Link a product/service to a parent product/service

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.products_add_subproducts_model import ProductsAddSubproductsModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of parent product/service
    products_add_subproducts_model = dolibarr_api.ProductsAddSubproductsModel() # ProductsAddSubproductsModel | **subproduct_id** (required)   **qty** (required)   incdec   

    try:
        # Add a subproduct 🔐
        api_response = api_instance.products_add_subproducts(id, products_add_subproducts_model)
        print("The response of ProductsApi->products_add_subproducts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_add_subproducts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of parent product/service | 
 **products_add_subproducts_model** | [**ProductsAddSubproductsModel**](ProductsAddSubproductsModel.md)| **subproduct_id** (required)   **qty** (required)   incdec    | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_variant**
> int products_add_variant(id, products_add_variant_model)

Add variant 🔐

"features" is a list of attributes pairs id_attribute=>id_value. Example: array(id_color=>id_Blue, id_size=>id_small, id_option=>id_val_a, ...)

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.products_add_variant_model import ProductsAddVariantModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Product
    products_add_variant_model = dolibarr_api.ProductsAddVariantModel() # ProductsAddVariantModel | **weight_impact** (required)   **price_impact** (required)   **price_impact_is_percent** (required)   **features** (required)   reference   ref_ext   

    try:
        # Add variant 🔐
        api_response = api_instance.products_add_variant(id, products_add_variant_model)
        print("The response of ProductsApi->products_add_variant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_add_variant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Product | 
 **products_add_variant_model** | [**ProductsAddVariantModel**](ProductsAddVariantModel.md)| **weight_impact** (required)   **price_impact** (required)   **price_impact_is_percent** (required)   **features** (required)   reference   ref_ext    | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_add_variant_by_product_ref**
> int products_add_variant_by_product_ref(ref, products_add_variant_by_product_ref_model)

Add variant by product ref 🔐

"features" is a list of attributes pairs id_attribute=>id_value. Example: array(id_color=>id_Blue, id_size=>id_small, id_option=>id_val_a, ...)

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.products_add_variant_by_product_ref_model import ProductsAddVariantByProductRefModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    ref = 'ref_example' # str | Ref of Product
    products_add_variant_by_product_ref_model = dolibarr_api.ProductsAddVariantByProductRefModel() # ProductsAddVariantByProductRefModel | **weight_impact** (required)   **price_impact** (required)   **price_impact_is_percent** (required)   **features** (required)   

    try:
        # Add variant by product ref 🔐
        api_response = api_instance.products_add_variant_by_product_ref(ref, products_add_variant_by_product_ref_model)
        print("The response of ProductsApi->products_add_variant_by_product_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_add_variant_by_product_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of Product | 
 **products_add_variant_by_product_ref_model** | [**ProductsAddVariantByProductRefModel**](ProductsAddVariantByProductRefModel.md)| **weight_impact** (required)   **price_impact** (required)   **price_impact_is_percent** (required)   **features** (required)    | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_del_subproducts**
> int products_del_subproducts(id, subproduct_id)

Remove a subproduct 🔐

Unlink a product/service from a parent product/service

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of parent product/service
    subproduct_id = 56 # int | ID of child product/service

    try:
        # Remove a subproduct 🔐
        api_response = api_instance.products_del_subproducts(id, subproduct_id)
        print("The response of ProductsApi->products_del_subproducts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_del_subproducts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of parent product/service | 
 **subproduct_id** | **int**| ID of child product/service | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_attribute_value_by_id**
> int products_remove_attribute_value_by_id(id)

Delete attribute value by ID 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Attribute value

    try:
        # Delete attribute value by ID 🔐
        api_response = api_instance.products_remove_attribute_value_by_id(id)
        print("The response of ProductsApi->products_remove_attribute_value_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_remove_attribute_value_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute value | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_attribute_value_by_ref**
> int products_remove_attribute_value_by_ref(id, ref)

Delete attribute value by ref 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Attribute
    ref = 'ref_example' # str | Ref of Attribute value

    try:
        # Delete attribute value by ref 🔐
        api_response = api_instance.products_remove_attribute_value_by_ref(id, ref)
        print("The response of ProductsApi->products_remove_attribute_value_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_remove_attribute_value_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 
 **ref** | **str**| Ref of Attribute value | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_attributes**
> int products_remove_attributes(id)

Delete attributes by ID 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Attribute

    try:
        # Delete attributes by ID 🔐
        api_response = api_instance.products_remove_attributes(id)
        print("The response of ProductsApi->products_remove_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_remove_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_purchase_price**
> int products_remove_purchase_price(id, priceid)

Delete a purchase price for a product 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | Product ID
    priceid = 56 # int | purchase price ID

    try:
        # Delete a purchase price for a product 🔐
        api_response = api_instance.products_remove_purchase_price(id, priceid)
        print("The response of ProductsApi->products_remove_purchase_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_remove_purchase_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Product ID | 
 **priceid** | **int**| purchase price ID | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_remove_variant**
> int products_remove_variant(id)

Delete product variants 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Variant

    try:
        # Delete product variants 🔐
        api_response = api_instance.products_remove_variant(id)
        print("The response of ProductsApi->products_remove_variant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_remove_variant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Variant | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attribute_by_id**
> Dict[str, object] products_retrieve_attribute_by_id(id)

Get attribute by ID 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Attribute

    try:
        # Get attribute by ID 🔐
        api_response = api_instance.products_retrieve_attribute_by_id(id)
        print("The response of ProductsApi->products_retrieve_attribute_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_attribute_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 

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

# **products_retrieve_attribute_value_by_id**
> List[str] products_retrieve_attribute_value_by_id(id)

Get attribute value by ID 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Attribute value

    try:
        # Get attribute value by ID 🔐
        api_response = api_instance.products_retrieve_attribute_value_by_id(id)
        print("The response of ProductsApi->products_retrieve_attribute_value_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_attribute_value_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute value | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attribute_value_by_ref**
> List[str] products_retrieve_attribute_value_by_ref(id, ref)

Get attribute value by ref 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Attribute value
    ref = 'ref_example' # str | Ref of Attribute value

    try:
        # Get attribute value by ref 🔐
        api_response = api_instance.products_retrieve_attribute_value_by_ref(id, ref)
        print("The response of ProductsApi->products_retrieve_attribute_value_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_attribute_value_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute value | 
 **ref** | **str**| Ref of Attribute value | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attribute_values**
> List[str] products_retrieve_attribute_values(id)

Get all values for an attribute ID 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of an Attribute

    try:
        # Get all values for an attribute ID 🔐
        api_response = api_instance.products_retrieve_attribute_values(id)
        print("The response of ProductsApi->products_retrieve_attribute_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_attribute_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of an Attribute | 

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
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attribute_values_by_ref**
> List[str] products_retrieve_attribute_values_by_ref(ref)

Get all values for an attribute ref 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    ref = 'ref_example' # str | Ref of an Attribute

    try:
        # Get all values for an attribute ref 🔐
        api_response = api_instance.products_retrieve_attribute_values_by_ref(ref)
        print("The response of ProductsApi->products_retrieve_attribute_values_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_attribute_values_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of an Attribute | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attributes**
> List[str] products_retrieve_attributes(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties)

Get attributes 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:color)\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)

    try:
        # Get attributes 🔐
        api_response = api_instance.products_retrieve_attributes(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, sqlfilters=sqlfilters, properties=properties)
        print("The response of ProductsApi->products_retrieve_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.ref:like:color)\&quot; | [optional] 
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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_attributes_by_ref**
> List[str] products_retrieve_attributes_by_ref(ref)

Get attributes by ref 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    ref = 'ref_example' # str | Reference of Attribute

    try:
        # Get attributes by ref 🔐
        api_response = api_instance.products_retrieve_attributes_by_ref(ref)
        print("The response of ProductsApi->products_retrieve_attributes_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_attributes_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Reference of Attribute | 

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

# **products_retrieve_attributes_by_ref_ext**
> List[str] products_retrieve_attributes_by_ref_ext(ref_ext)

Get attributes by ref_ext 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    ref_ext = 'ref_ext_example' # str | External reference of Attribute

    try:
        # Get attributes by ref_ext 🔐
        api_response = api_instance.products_retrieve_attributes_by_ref_ext(ref_ext)
        print("The response of ProductsApi->products_retrieve_attributes_by_ref_ext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_attributes_by_ref_ext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_ext** | **str**| External reference of Attribute | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_by_barcode**
> str products_retrieve_by_barcode(barcode, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)

Get product by barcode 🔐

Return an array with product information

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    barcode = 'barcode_example' # str | Barcode of element
    includestockdata = 56 # int | Load also information about stock (slower) (optional)
    includesubproducts = True # bool | Load information about subproducts (optional)
    includeparentid = True # bool | Load also ID of parent product (if product is a variant of a parent product) (optional)
    includetrans = True # bool | Load also the translations of product label and description (optional)

    try:
        # Get product by barcode 🔐
        api_response = api_instance.products_retrieve_by_barcode(barcode, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)
        print("The response of ProductsApi->products_retrieve_by_barcode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_by_barcode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode of element | 
 **includestockdata** | **int**| Load also information about stock (slower) | [optional] 
 **includesubproducts** | **bool**| Load information about subproducts | [optional] 
 **includeparentid** | **bool**| Load also ID of parent product (if product is a variant of a parent product) | [optional] 
 **includetrans** | **bool**| Load also the translations of product label and description | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_by_ref**
> str products_retrieve_by_ref(ref, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)

Get product by ref 🔐

Return an array with product information

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    ref = 'ref_example' # str | Ref of element
    includestockdata = 56 # int | Load also information about stock (slower) (optional)
    includesubproducts = True # bool | Load information about subproducts (optional)
    includeparentid = True # bool | Load also ID of parent product (if product is a variant of a parent product) (optional)
    includetrans = True # bool | Load also the translations of product label and description (optional)

    try:
        # Get product by ref 🔐
        api_response = api_instance.products_retrieve_by_ref(ref, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)
        print("The response of ProductsApi->products_retrieve_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of element | 
 **includestockdata** | **int**| Load also information about stock (slower) | [optional] 
 **includesubproducts** | **bool**| Load information about subproducts | [optional] 
 **includeparentid** | **bool**| Load also ID of parent product (if product is a variant of a parent product) | [optional] 
 **includetrans** | **bool**| Load also the translations of product label and description | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_by_ref_ext**
> str products_retrieve_by_ref_ext(ref_ext, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)

Get product by ref_ext 🔐

Return an array with product information

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    ref_ext = 'ref_ext_example' # str | Ref_ext of element
    includestockdata = 56 # int | Load also information about stock (slower) (optional)
    includesubproducts = True # bool | Load information about subproducts (optional)
    includeparentid = True # bool | Load also ID of parent product (if product is a variant of a parent product) (optional)
    includetrans = True # bool | Load also the translations of product label and description (optional)

    try:
        # Get product by ref_ext 🔐
        api_response = api_instance.products_retrieve_by_ref_ext(ref_ext, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)
        print("The response of ProductsApi->products_retrieve_by_ref_ext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_by_ref_ext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_ext** | **str**| Ref_ext of element | 
 **includestockdata** | **int**| Load also information about stock (slower) | [optional] 
 **includesubproducts** | **bool**| Load information about subproducts | [optional] 
 **includeparentid** | **bool**| Load also ID of parent product (if product is a variant of a parent product) | [optional] 
 **includetrans** | **bool**| Load also the translations of product label and description | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_categories**
> str products_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get categories for a product 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of product
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)

    try:
        # Get categories for a product 🔐
        api_response = api_instance.products_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
        print("The response of ProductsApi->products_retrieve_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 
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
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_customer_prices_per_customer**
> str products_retrieve_customer_prices_per_customer(id, thirdparty_id=thirdparty_id)

Get prices per customer for a product 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of product
    thirdparty_id = 'thirdparty_id_example' # str | Thirdparty id to filter orders of (example '1') (optional)

    try:
        # Get prices per customer for a product 🔐
        api_response = api_instance.products_retrieve_customer_prices_per_customer(id, thirdparty_id=thirdparty_id)
        print("The response of ProductsApi->products_retrieve_customer_prices_per_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_customer_prices_per_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 
 **thirdparty_id** | **str**| Thirdparty id to filter orders of (example &#39;1&#39;) | [optional] 

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

# **products_retrieve_customer_prices_per_quantity**
> str products_retrieve_customer_prices_per_quantity(id)

Get prices per quantity for a product 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of product

    try:
        # Get prices per quantity for a product 🔐
        api_response = api_instance.products_retrieve_customer_prices_per_quantity(id)
        print("The response of ProductsApi->products_retrieve_customer_prices_per_quantity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_customer_prices_per_quantity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 

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

# **products_retrieve_customer_prices_per_segment**
> str products_retrieve_customer_prices_per_segment(id)

Get prices per segment for a product 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of product

    try:
        # Get prices per segment for a product 🔐
        api_response = api_instance.products_retrieve_customer_prices_per_segment(id)
        print("The response of ProductsApi->products_retrieve_customer_prices_per_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_customer_prices_per_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 

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

# **products_retrieve_purchase_prices**
> List[str] products_retrieve_purchase_prices(id, ref=ref, ref_ext=ref_ext, barcode=barcode)

Get purchase prices for a product 🔐

Return an array with product information. TODO implement getting a product by ref or by $ref_ext

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of product
    ref = 'ref_example' # str | Ref of element (optional)
    ref_ext = 'ref_ext_example' # str | Ref ext of element (optional)
    barcode = 'barcode_example' # str | Barcode of element (optional)

    try:
        # Get purchase prices for a product 🔐
        api_response = api_instance.products_retrieve_purchase_prices(id, ref=ref, ref_ext=ref_ext, barcode=barcode)
        print("The response of ProductsApi->products_retrieve_purchase_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_purchase_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 
 **ref** | **str**| Ref of element | [optional] 
 **ref_ext** | **str**| Ref ext of element | [optional] 
 **barcode** | **str**| Barcode of element | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_stock**
> str products_retrieve_stock(id, selected_warehouse_id=selected_warehouse_id)

Get stock data for a product 🔐

Optionally with $selected_warehouse_id parameter user can get stock of a specific warehouse

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Product
    selected_warehouse_id = 56 # int | ID of warehouse (optional)

    try:
        # Get stock data for a product 🔐
        api_response = api_instance.products_retrieve_stock(id, selected_warehouse_id=selected_warehouse_id)
        print("The response of ProductsApi->products_retrieve_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Product | 
 **selected_warehouse_id** | **int**| ID of warehouse | [optional] 

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
**500** | System error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_subproducts**
> List[str] products_retrieve_subproducts(id)

Get the list of subproducts of a product 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of parent product/service

    try:
        # Get the list of subproducts of a product 🔐
        api_response = api_instance.products_retrieve_subproducts(id)
        print("The response of ProductsApi->products_retrieve_subproducts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_subproducts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of parent product/service | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_supplier_products**
> List[str] products_retrieve_supplier_products(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, supplier=supplier, sqlfilters=sqlfilters)

Get a list of all purchase prices of products 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Limit for list (optional)
    page = 56 # int | Page number (optional)
    mode = 56 # int | Use this param to filter list (0 for all, 1 for only product, 2 for only service) (optional)
    category = 56 # int | Use this param to filter list by category of product (optional)
    supplier = 56 # int | Use this param to filter list by supplier (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.tobuy:=:0) and (t.tosell:=:1)\" (optional)

    try:
        # Get a list of all purchase prices of products 🔐
        api_response = api_instance.products_retrieve_supplier_products(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, supplier=supplier, sqlfilters=sqlfilters)
        print("The response of ProductsApi->products_retrieve_supplier_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_supplier_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Limit for list | [optional] 
 **page** | **int**| Page number | [optional] 
 **mode** | **int**| Use this param to filter list (0 for all, 1 for only product, 2 for only service) | [optional] 
 **category** | **int**| Use this param to filter list by category of product | [optional] 
 **supplier** | **int**| Use this param to filter list by supplier | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.tobuy:&#x3D;:0) and (t.tosell:&#x3D;:1)\&quot; | [optional] 

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

# **products_retrieve_variants**
> List[str] products_retrieve_variants(id, includestock=includestock)

Get product variants 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Product
    includestock = 56 # int | Default value 0. If parameter is set to 1 the response will contain stock data of each variant (optional)

    try:
        # Get product variants 🔐
        api_response = api_instance.products_retrieve_variants(id, includestock=includestock)
        print("The response of ProductsApi->products_retrieve_variants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_variants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Product | 
 **includestock** | **int**| Default value 0. If parameter is set to 1 the response will contain stock data of each variant | [optional] 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_retrieve_variants_by_prod_ref**
> List[str] products_retrieve_variants_by_prod_ref(ref)

Get product variants by Product ref 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    ref = 'ref_example' # str | Ref of Product

    try:
        # Get product variants by Product ref 🔐
        api_response = api_instance.products_retrieve_variants_by_prod_ref(ref)
        print("The response of ProductsApi->products_retrieve_variants_by_prod_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve_variants_by_prod_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| Ref of Product | 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update_attribute_value**
> Dict[str, object] products_update_attribute_value(id, products_update_attribute_value_model)

Update attribute value 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.products_update_attribute_value_model import ProductsUpdateAttributeValueModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Attribute
    products_update_attribute_value_model = dolibarr_api.ProductsUpdateAttributeValueModel() # ProductsUpdateAttributeValueModel | **request_data** (required)   

    try:
        # Update attribute value 🔐
        api_response = api_instance.products_update_attribute_value(id, products_update_attribute_value_model)
        print("The response of ProductsApi->products_update_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_update_attribute_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 
 **products_update_attribute_value_model** | [**ProductsUpdateAttributeValueModel**](ProductsUpdateAttributeValueModel.md)| **request_data** (required)    | 

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
**401** | Unauthorized |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update_attributes**
> Dict[str, object] products_update_attributes(id, products_update_attributes_model=products_update_attributes_model)

Update attributes by ID 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.products_update_attributes_model import ProductsUpdateAttributesModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Attribute
    products_update_attributes_model = dolibarr_api.ProductsUpdateAttributesModel() # ProductsUpdateAttributesModel | request_data    (optional)

    try:
        # Update attributes by ID 🔐
        api_response = api_instance.products_update_attributes(id, products_update_attributes_model=products_update_attributes_model)
        print("The response of ProductsApi->products_update_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_update_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attribute | 
 **products_update_attributes_model** | [**ProductsUpdateAttributesModel**](ProductsUpdateAttributesModel.md)| request_data    | [optional] 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update_variant**
> int products_update_variant(id, products_update_variant_model=products_update_variant_model)

Update product variants 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.products_update_variant_model import ProductsUpdateVariantModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of Variant
    products_update_variant_model = dolibarr_api.ProductsUpdateVariantModel() # ProductsUpdateVariantModel | request_data    (optional)

    try:
        # Update product variants 🔐
        api_response = api_instance.products_update_variant(id, products_update_variant_model=products_update_variant_model)
        print("The response of ProductsApi->products_update_variant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_update_variant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Variant | 
 **products_update_variant_model** | [**ProductsUpdateVariantModel**](ProductsUpdateVariantModel.md)| request_data    | [optional] 

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
**500** | System error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_products**
> List[str] remove_products(id)

Delete a product 🔐

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | Product ID

    try:
        # Delete a product 🔐
        api_response = api_instance.remove_products(id)
        print("The response of ProductsApi->remove_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->remove_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Product ID | 

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

# **retrieve_products**
> str retrieve_products(id, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)

Get a product 🔐

Return an array with product information

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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | ID of product
    includestockdata = 56 # int | Load also information about stock (slower) (optional)
    includesubproducts = True # bool | Load information about subproducts (optional)
    includeparentid = True # bool | Load also ID of parent product (if product is a variant of a parent product) (optional)
    includetrans = True # bool | Load also the translations of product label and description (optional)

    try:
        # Get a product 🔐
        api_response = api_instance.retrieve_products(id, includestockdata=includestockdata, includesubproducts=includesubproducts, includeparentid=includeparentid, includetrans=includetrans)
        print("The response of ProductsApi->retrieve_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->retrieve_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of product | 
 **includestockdata** | **int**| Load also information about stock (slower) | [optional] 
 **includesubproducts** | **bool**| Load information about subproducts | [optional] 
 **includeparentid** | **bool**| Load also ID of parent product (if product is a variant of a parent product) | [optional] 
 **includetrans** | **bool**| Load also the translations of product label and description | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_products**
> Dict[str, object] update_products(id, update_products_model=update_products_model)

Update a product 🔐

Price will be updated by this API only if option is set on "One price per product" or if PRODUIT_MULTIPRICES is set (1 price per segment) See other APIs for other price modes.

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_products_model import UpdateProductsModel
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
    api_instance = dolibarr_api.ProductsApi(api_client)
    id = 56 # int | Id of product to update
    update_products_model = dolibarr_api.UpdateProductsModel() # UpdateProductsModel | request_data    (optional)

    try:
        # Update a product 🔐
        api_response = api_instance.update_products(id, update_products_model=update_products_model)
        print("The response of ProductsApi->update_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->update_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of product to update | 
 **update_products_model** | [**UpdateProductsModel**](UpdateProductsModel.md)| request_data    | [optional] 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

