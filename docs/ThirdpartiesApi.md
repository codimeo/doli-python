# dolibarr_api.ThirdpartiesApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_thirdparties**](ThirdpartiesApi.md#create_thirdparties) | **POST** /thirdparties | Create a third party 🔐
[**list_thirdparties**](ThirdpartiesApi.md#list_thirdparties) | **GET** /thirdparties | List third parties 🔐
[**remove_thirdparties**](ThirdpartiesApi.md#remove_thirdparties) | **DELETE** /thirdparties/{id} | Delete a third party 🔐
[**retrieve_thirdparties**](ThirdpartiesApi.md#retrieve_thirdparties) | **GET** /thirdparties/{id} | Get a third party 🔐
[**thirdparties_add_category**](ThirdpartiesApi.md#thirdparties_add_category) | **PUT** /thirdparties/{id}/categories/{category_id} | Add a customer category to a third party 🔐
[**thirdparties_add_representative**](ThirdpartiesApi.md#thirdparties_add_representative) | **POST** /thirdparties/{id}/representative/{representative_id} | Add a customer representative to a third party 🔐
[**thirdparties_add_supplier_category**](ThirdpartiesApi.md#thirdparties_add_supplier_category) | **PUT** /thirdparties/{id}/supplier_categories/{category_id} | Add a supplier category to a third party 🔐
[**thirdparties_create_company_bank_account**](ThirdpartiesApi.md#thirdparties_create_company_bank_account) | **POST** /thirdparties/{id}/bankaccounts | Create a company bank account for a third party 🔐
[**thirdparties_create_company_notification**](ThirdpartiesApi.md#thirdparties_create_company_notification) | **POST** /thirdparties/{id}/notifications | Create a company notification for a third party 🔐
[**thirdparties_create_company_notification_by_code**](ThirdpartiesApi.md#thirdparties_create_company_notification_by_code) | **POST** /thirdparties/{id}/notificationsbycode/{code} | Create a company notification for a third party using action trigger code 🔐
[**thirdparties_create_societe_account**](ThirdpartiesApi.md#thirdparties_create_societe_account) | **POST** /thirdparties/{id}/accounts | Create and attach a new account to an existing third party 🔐
[**thirdparties_create_societe_account_0**](ThirdpartiesApi.md#thirdparties_create_societe_account_0) | **POST** /thirdparties/{id}/accounts/{site} | Create and attach a new (or replace an existing) specific site account for a third party 🔐
[**thirdparties_generate_bank_account_document**](ThirdpartiesApi.md#thirdparties_generate_bank_account_document) | **GET** /thirdparties/{id}/generateBankAccountDocument/{companybankid}/{model} | Generate a document from a bank account record 🔐
[**thirdparties_merge**](ThirdpartiesApi.md#thirdparties_merge) | **PUT** /thirdparties/{id}/merge/{idtodelete} | Merge a third party into another third party 🔐
[**thirdparties_remove_category**](ThirdpartiesApi.md#thirdparties_remove_category) | **DELETE** /thirdparties/{id}/categories/{category_id} | Remove the link between a customer category and the third party 🔐
[**thirdparties_remove_company_bank_account**](ThirdpartiesApi.md#thirdparties_remove_company_bank_account) | **DELETE** /thirdparties/{id}/bankaccounts/{bankaccount_id} | Delete a bank account attached to a third party 🔐
[**thirdparties_remove_company_notification**](ThirdpartiesApi.md#thirdparties_remove_company_notification) | **DELETE** /thirdparties/{id}/notifications/{notification_id} | Delete a company notification attached to a third party 🔐
[**thirdparties_remove_representative**](ThirdpartiesApi.md#thirdparties_remove_representative) | **DELETE** /thirdparties/{id}/representative/{representative_id} | Remove the link between a customer representative and a third party 🔐
[**thirdparties_remove_societe_account**](ThirdpartiesApi.md#thirdparties_remove_societe_account) | **DELETE** /thirdparties/{id}/accounts/{site} | Delete a specific site account attached to a third party 🔐
[**thirdparties_remove_societe_accounts**](ThirdpartiesApi.md#thirdparties_remove_societe_accounts) | **DELETE** /thirdparties/{id}/accounts | Delete all accounts attached to a third party 🔐
[**thirdparties_remove_supplier_category**](ThirdpartiesApi.md#thirdparties_remove_supplier_category) | **DELETE** /thirdparties/{id}/supplier_categories/{category_id} | Remove the link between a category and the third party 🔐
[**thirdparties_retrieve_by_barcode**](ThirdpartiesApi.md#thirdparties_retrieve_by_barcode) | **GET** /thirdparties/barcode/{barcode} | Get a third party by barcode. 🔐
[**thirdparties_retrieve_by_email**](ThirdpartiesApi.md#thirdparties_retrieve_by_email) | **GET** /thirdparties/email/{email} | Get properties of a third party by email. 🔐
[**thirdparties_retrieve_categories**](ThirdpartiesApi.md#thirdparties_retrieve_categories) | **GET** /thirdparties/{id}/categories | Get customer categories for a third party 🔐
[**thirdparties_retrieve_company_bank_account**](ThirdpartiesApi.md#thirdparties_retrieve_company_bank_account) | **GET** /thirdparties/{id}/bankaccounts | Get company bank accounts of a third party 🔐
[**thirdparties_retrieve_company_notification**](ThirdpartiesApi.md#thirdparties_retrieve_company_notification) | **GET** /thirdparties/{id}/notifications | Get company notifications for a third party 🔐
[**thirdparties_retrieve_fixed_amount_discounts**](ThirdpartiesApi.md#thirdparties_retrieve_fixed_amount_discounts) | **GET** /thirdparties/{id}/fixedamountdiscounts | Get fixed amount discount of a third party 🔐
[**thirdparties_retrieve_invoices_qualified_for_credit_note**](ThirdpartiesApi.md#thirdparties_retrieve_invoices_qualified_for_credit_note) | **GET** /thirdparties/{id}/getinvoicesqualifiedforcreditnote | Return invoices qualified to be corrected by a credit note 🔐
[**thirdparties_retrieve_invoices_qualified_for_replacement**](ThirdpartiesApi.md#thirdparties_retrieve_invoices_qualified_for_replacement) | **GET** /thirdparties/{id}/getinvoicesqualifiedforreplacement | Return invoices qualified to be replaced by another invoice 🔐
[**thirdparties_retrieve_out_standing_invoices**](ThirdpartiesApi.md#thirdparties_retrieve_out_standing_invoices) | **GET** /thirdparties/{id}/outstandinginvoices | Get outstanding invoices for a third party 🔐
[**thirdparties_retrieve_out_standing_order**](ThirdpartiesApi.md#thirdparties_retrieve_out_standing_order) | **GET** /thirdparties/{id}/outstandingorders | Get outstanding orders for a third party 🔐
[**thirdparties_retrieve_out_standing_proposals**](ThirdpartiesApi.md#thirdparties_retrieve_out_standing_proposals) | **GET** /thirdparties/{id}/outstandingproposals | Get outstanding proposals for a third party 🔐
[**thirdparties_retrieve_sales_representatives**](ThirdpartiesApi.md#thirdparties_retrieve_sales_representatives) | **GET** /thirdparties/{id}/representatives | Get representatives of a third party 🔐
[**thirdparties_retrieve_societe_accounts**](ThirdpartiesApi.md#thirdparties_retrieve_societe_accounts) | **GET** /thirdparties/{id}/accounts | Get a specific account attached to a third party 🔐
[**thirdparties_retrieve_societe_by_accounts**](ThirdpartiesApi.md#thirdparties_retrieve_societe_by_accounts) | **GET** /thirdparties/accounts/{site}/{key_account} | Get a specific third party by account 🔐
[**thirdparties_retrieve_supplier_categories**](ThirdpartiesApi.md#thirdparties_retrieve_supplier_categories) | **GET** /thirdparties/{id}/supplier_categories | Get supplier categories for a third party 🔐
[**thirdparties_set_thirdparty_price_level**](ThirdpartiesApi.md#thirdparties_set_thirdparty_price_level) | **PUT** /thirdparties/{id}/setpricelevel/{priceLevel} | Set a new price level for the given third party 🔐
[**thirdparties_update_company_bank_account**](ThirdpartiesApi.md#thirdparties_update_company_bank_account) | **PUT** /thirdparties/{id}/bankaccounts/{bankaccount_id} | Update a company bank account of a third party 🔐
[**thirdparties_update_company_notification**](ThirdpartiesApi.md#thirdparties_update_company_notification) | **PUT** /thirdparties/{id}/notifications/{notification_id} | Update a company notification for a third party 🔐
[**thirdparties_update_societe_account**](ThirdpartiesApi.md#thirdparties_update_societe_account) | **PUT** /thirdparties/{id}/accounts/{site} | Update specified values of a specific account attached to a third party 🔐
[**update_thirdparties**](ThirdpartiesApi.md#update_thirdparties) | **PUT** /thirdparties/{id} | Update third party 🔐


# **create_thirdparties**
> int create_thirdparties(create_thirdparties_model=create_thirdparties_model)

Create a third party 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.create_thirdparties_model import CreateThirdpartiesModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    create_thirdparties_model = dolibarr_api.CreateThirdpartiesModel() # CreateThirdpartiesModel | request_data    (optional)

    try:
        # Create a third party 🔐
        api_response = api_instance.create_thirdparties(create_thirdparties_model=create_thirdparties_model)
        print("The response of ThirdpartiesApi->create_thirdparties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->create_thirdparties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_thirdparties_model** | [**CreateThirdpartiesModel**](CreateThirdpartiesModel.md)| request_data    | [optional] 

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

# **list_thirdparties**
> List[str] list_thirdparties(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)

List third parties 🔐

Get a list of third parties

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    sortfield = 'sortfield_example' # str | S ort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | List limit (optional)
    page = 56 # int | Page number (optional)
    mode = 56 # int | Set to 0 to show all third parties, Set to 1 to show only customers, 2 for prospects, 3 for neither customer or prospect, 4 for suppliers (optional)
    category = 56 # int | Use this param to filter the list by category (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"((t.nom:like:'TheCompany%') or (t.name_alias:like:'TheCompany%')) and (t.datec:<:'20160101')\" (optional)
    properties = 'properties_example' # str | Restrict the data returned to these properties. Ignored if empty. Comma separated list of properties names (optional)
    pagination_data = True # bool | If this parameter is set to true the response will include pagination data. Default value is false. Page starts from 0* (optional)

    try:
        # List third parties 🔐
        api_response = api_instance.list_thirdparties(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, mode=mode, category=category, sqlfilters=sqlfilters, properties=properties, pagination_data=pagination_data)
        print("The response of ThirdpartiesApi->list_thirdparties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->list_thirdparties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| S ort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| List limit | [optional] 
 **page** | **int**| Page number | [optional] 
 **mode** | **int**| Set to 0 to show all third parties, Set to 1 to show only customers, 2 for prospects, 3 for neither customer or prospect, 4 for suppliers | [optional] 
 **category** | **int**| Use this param to filter the list by category | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;((t.nom:like:&#39;TheCompany%&#39;) or (t.name_alias:like:&#39;TheCompany%&#39;)) and (t.datec:&lt;:&#39;20160101&#39;)\&quot; | [optional] 
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

# **remove_thirdparties**
> List[str] remove_thirdparties(id)

Delete a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party

    try:
        # Delete a third party 🔐
        api_response = api_instance.remove_thirdparties(id)
        print("The response of ThirdpartiesApi->remove_thirdparties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->remove_thirdparties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 

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

# **retrieve_thirdparties**
> Dict[str, object] retrieve_thirdparties(id)

Get a third party 🔐

Return the third party object

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party to load

    try:
        # Get a third party 🔐
        api_response = api_instance.retrieve_thirdparties(id)
        print("The response of ThirdpartiesApi->retrieve_thirdparties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->retrieve_thirdparties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party to load | 

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

# **thirdparties_add_category**
> Dict[str, object] thirdparties_add_category(id, category_id)

Add a customer category to a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    category_id = 56 # int | ID of category

    try:
        # Add a customer category to a third party 🔐
        api_response = api_instance.thirdparties_add_category(id, category_id)
        print("The response of ThirdpartiesApi->thirdparties_add_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_add_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **category_id** | **int**| ID of category | 

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

# **thirdparties_add_representative**
> int thirdparties_add_representative(id, representative_id)

Add a customer representative to a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    representative_id = 56 # int | ID of representative

    try:
        # Add a customer representative to a third party 🔐
        api_response = api_instance.thirdparties_add_representative(id, representative_id)
        print("The response of ThirdpartiesApi->thirdparties_add_representative:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_add_representative: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **representative_id** | **int**| ID of representative | 

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
**401** | Access not allowed for your login |  -  |
**404** | User or Third party not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_add_supplier_category**
> str thirdparties_add_supplier_category(id, category_id)

Add a supplier category to a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    category_id = 56 # int | ID of category

    try:
        # Add a supplier category to a third party 🔐
        api_response = api_instance.thirdparties_add_supplier_category(id, category_id)
        print("The response of ThirdpartiesApi->thirdparties_add_supplier_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_add_supplier_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **category_id** | **int**| ID of category | 

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

# **thirdparties_create_company_bank_account**
> str thirdparties_create_company_bank_account(id, thirdparties_create_company_bank_account_model=thirdparties_create_company_bank_account_model)

Create a company bank account for a third party 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.thirdparties_create_company_bank_account_model import ThirdpartiesCreateCompanyBankAccountModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    thirdparties_create_company_bank_account_model = dolibarr_api.ThirdpartiesCreateCompanyBankAccountModel() # ThirdpartiesCreateCompanyBankAccountModel | request_data    (optional)

    try:
        # Create a company bank account for a third party 🔐
        api_response = api_instance.thirdparties_create_company_bank_account(id, thirdparties_create_company_bank_account_model=thirdparties_create_company_bank_account_model)
        print("The response of ThirdpartiesApi->thirdparties_create_company_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_create_company_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **thirdparties_create_company_bank_account_model** | [**ThirdpartiesCreateCompanyBankAccountModel**](ThirdpartiesCreateCompanyBankAccountModel.md)| request_data    | [optional] 

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

# **thirdparties_create_company_notification**
> str thirdparties_create_company_notification(id, thirdparties_create_company_notification_model=thirdparties_create_company_notification_model)

Create a company notification for a third party 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.thirdparties_create_company_notification_model import ThirdpartiesCreateCompanyNotificationModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    thirdparties_create_company_notification_model = dolibarr_api.ThirdpartiesCreateCompanyNotificationModel() # ThirdpartiesCreateCompanyNotificationModel | request_data    (optional)

    try:
        # Create a company notification for a third party 🔐
        api_response = api_instance.thirdparties_create_company_notification(id, thirdparties_create_company_notification_model=thirdparties_create_company_notification_model)
        print("The response of ThirdpartiesApi->thirdparties_create_company_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_create_company_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **thirdparties_create_company_notification_model** | [**ThirdpartiesCreateCompanyNotificationModel**](ThirdpartiesCreateCompanyNotificationModel.md)| request_data    | [optional] 

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

# **thirdparties_create_company_notification_by_code**
> str thirdparties_create_company_notification_by_code(id, code, thirdparties_create_company_notification_by_code_model=thirdparties_create_company_notification_by_code_model)

Create a company notification for a third party using action trigger code 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.thirdparties_create_company_notification_by_code_model import ThirdpartiesCreateCompanyNotificationByCodeModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    code = 'code_example' # str | Action Trigger code
    thirdparties_create_company_notification_by_code_model = dolibarr_api.ThirdpartiesCreateCompanyNotificationByCodeModel() # ThirdpartiesCreateCompanyNotificationByCodeModel | request_data    (optional)

    try:
        # Create a company notification for a third party using action trigger code 🔐
        api_response = api_instance.thirdparties_create_company_notification_by_code(id, code, thirdparties_create_company_notification_by_code_model=thirdparties_create_company_notification_by_code_model)
        print("The response of ThirdpartiesApi->thirdparties_create_company_notification_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_create_company_notification_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **code** | **str**| Action Trigger code | 
 **thirdparties_create_company_notification_by_code_model** | [**ThirdpartiesCreateCompanyNotificationByCodeModel**](ThirdpartiesCreateCompanyNotificationByCodeModel.md)| request_data    | [optional] 

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

# **thirdparties_create_societe_account**
> str thirdparties_create_societe_account(id, thirdparties_create_societe_account_model=thirdparties_create_societe_account_model)

Create and attach a new account to an existing third party 🔐

Possible fields for request_data (request body) are specified in <code>llx_societe_account</code> table.<br> See <a href="https://wiki.dolibarr.org/index.php/Table_llx_societe_account">Table llx_societe_account</a> wiki page for more information<br><br> <u>Example body payload :</u> <pre>{"key_account": "cus_DAVkLSs1LYyYI", "site": "stripe"}</pre>

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.thirdparties_create_societe_account_model import ThirdpartiesCreateSocieteAccountModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    thirdparties_create_societe_account_model = dolibarr_api.ThirdpartiesCreateSocieteAccountModel() # ThirdpartiesCreateSocieteAccountModel | request_data    (optional)

    try:
        # Create and attach a new account to an existing third party 🔐
        api_response = api_instance.thirdparties_create_societe_account(id, thirdparties_create_societe_account_model=thirdparties_create_societe_account_model)
        print("The response of ThirdpartiesApi->thirdparties_create_societe_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_create_societe_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **thirdparties_create_societe_account_model** | [**ThirdpartiesCreateSocieteAccountModel**](ThirdpartiesCreateSocieteAccountModel.md)| request_data    | [optional] 

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
**401** | Unauthorized: User does not have permission to read thirdparties |  -  |
**409** | Conflict: An Account already exists for this company and site. |  -  |
**500** | Internal Server Error: Error creating SocieteAccount account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_create_societe_account_0**
> str thirdparties_create_societe_account_0(id, site, thirdparties_create_societe_account_model=thirdparties_create_societe_account_model)

Create and attach a new (or replace an existing) specific site account for a third party 🔐

You <strong>MUST</strong> pass all values to keep (otherwise, they will be deleted) !<br> If you just need to update specific fields prefer <code>PUT /thirdparties/{id}/accounts/{site}</code> endpoint.<br><br> When a <strong>SocieteAccount</strong> entity does not exist for the <code>id</code> and <code>site</code> supplied, a new one will be created. In that case <code>fk_soc</code> and <code>site</code> members form request body payload will be ignored and <code>id</code> and <code>site</code> query strings parameters will be used instead.

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.thirdparties_create_societe_account_model import ThirdpartiesCreateSocieteAccountModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    site = 'site_example' # str | Site key
    thirdparties_create_societe_account_model = dolibarr_api.ThirdpartiesCreateSocieteAccountModel() # ThirdpartiesCreateSocieteAccountModel | request_data    (optional)

    try:
        # Create and attach a new (or replace an existing) specific site account for a third party 🔐
        api_response = api_instance.thirdparties_create_societe_account_0(id, site, thirdparties_create_societe_account_model=thirdparties_create_societe_account_model)
        print("The response of ThirdpartiesApi->thirdparties_create_societe_account_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_create_societe_account_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **site** | **str**| Site key | 
 **thirdparties_create_societe_account_model** | [**ThirdpartiesCreateSocieteAccountModel**](ThirdpartiesCreateSocieteAccountModel.md)| request_data    | [optional] 

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
**401** | Unauthorized: User does not have permission to read thirdparties |  -  |
**500** | Internal Server Error: Error updating SocieteAccount entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_generate_bank_account_document**
> List[str] thirdparties_generate_bank_account_document(id, companybankid, model)

Generate a document from a bank account record 🔐

Like SEPA mandate

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    companybankid = 56 # int | ID of company bank
    model = 'model_example' # str | Model of document to generate

    try:
        # Generate a document from a bank account record 🔐
        api_response = api_instance.thirdparties_generate_bank_account_document(id, companybankid, model)
        print("The response of ThirdpartiesApi->thirdparties_generate_bank_account_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_generate_bank_account_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **companybankid** | **int**| ID of company bank | 
 **model** | **str**| Model of document to generate | 

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

# **thirdparties_merge**
> Dict[str, object] thirdparties_merge(id, idtodelete)

Merge a third party into another third party 🔐

Merge content (properties, notes) and objects (like invoices, events, orders, proposals, ...) of a third party into a target third party, then delete the merged third party. If a property has a defined value both in the third party to delete and the third party to keep, the value of the third party to delete will be ignored, the value of the target third party will remain, except for notes (content is concatenated).

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of thirdparty to keep (the target third party)
    idtodelete = 56 # int | ID of thirdparty to remove (the third party to delete), once data has been merged into the target third party.

    try:
        # Merge a third party into another third party 🔐
        api_response = api_instance.thirdparties_merge(id, idtodelete)
        print("The response of ThirdpartiesApi->thirdparties_merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty to keep (the target third party) | 
 **idtodelete** | **int**| ID of thirdparty to remove (the third party to delete), once data has been merged into the target third party. | 

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

# **thirdparties_remove_category**
> Dict[str, object] thirdparties_remove_category(id, category_id)

Remove the link between a customer category and the third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    category_id = 56 # int | ID of category

    try:
        # Remove the link between a customer category and the third party 🔐
        api_response = api_instance.thirdparties_remove_category(id, category_id)
        print("The response of ThirdpartiesApi->thirdparties_remove_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_remove_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **category_id** | **int**| ID of category | 

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

# **thirdparties_remove_company_bank_account**
> int thirdparties_remove_company_bank_account(id, bankaccount_id)

Delete a bank account attached to a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    bankaccount_id = 56 # int | ID of CompanyBankAccount

    try:
        # Delete a bank account attached to a third party 🔐
        api_response = api_instance.thirdparties_remove_company_bank_account(id, bankaccount_id)
        print("The response of ThirdpartiesApi->thirdparties_remove_company_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_remove_company_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **bankaccount_id** | **int**| ID of CompanyBankAccount | 

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

# **thirdparties_remove_company_notification**
> int thirdparties_remove_company_notification(id, notification_id)

Delete a company notification attached to a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    notification_id = 56 # int | ID of CompanyNotification

    try:
        # Delete a company notification attached to a third party 🔐
        api_response = api_instance.thirdparties_remove_company_notification(id, notification_id)
        print("The response of ThirdpartiesApi->thirdparties_remove_company_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_remove_company_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **notification_id** | **int**| ID of CompanyNotification | 

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

# **thirdparties_remove_representative**
> int thirdparties_remove_representative(id, representative_id)

Remove the link between a customer representative and a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    representative_id = 56 # int | ID of representative

    try:
        # Remove the link between a customer representative and a third party 🔐
        api_response = api_instance.thirdparties_remove_representative(id, representative_id)
        print("The response of ThirdpartiesApi->thirdparties_remove_representative:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_remove_representative: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **representative_id** | **int**| ID of representative | 

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
**401** | Access not allowed for your login |  -  |
**404** | User or Third party not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_remove_societe_account**
> str thirdparties_remove_societe_account(id, site)

Delete a specific site account attached to a third party 🔐

by account id

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    site = 'site_example' # str | Site key

    try:
        # Delete a specific site account attached to a third party 🔐
        api_response = api_instance.thirdparties_remove_societe_account(id, site)
        print("The response of ThirdpartiesApi->thirdparties_remove_societe_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_remove_societe_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **site** | **str**| Site key | 

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
**401** | Unauthorized: User does not have permission to delete thirdparties accounts |  -  |
**404** | Not Found: Specified thirdparty ID does not belongs to an existing thirdparty |  -  |
**500** | Internal Server Error: Error deleting SocieteAccount entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_remove_societe_accounts**
> str thirdparties_remove_societe_accounts(id)

Delete all accounts attached to a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party

    try:
        # Delete all accounts attached to a third party 🔐
        api_response = api_instance.thirdparties_remove_societe_accounts(id)
        print("The response of ThirdpartiesApi->thirdparties_remove_societe_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_remove_societe_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 

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
**401** | Unauthorized: User does not have permission to delete thirdparties accounts |  -  |
**404** | Not Found: Specified thirdparty ID does not belongs to an existing thirdparty |  -  |
**500** | Internal Server Error: Error deleting SocieteAccount entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_remove_supplier_category**
> str thirdparties_remove_supplier_category(id, category_id)

Remove the link between a category and the third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    category_id = 56 # int | ID of category

    try:
        # Remove the link between a category and the third party 🔐
        api_response = api_instance.thirdparties_remove_supplier_category(id, category_id)
        print("The response of ThirdpartiesApi->thirdparties_remove_supplier_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_remove_supplier_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **category_id** | **int**| ID of category | 

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

# **thirdparties_retrieve_by_barcode**
> str thirdparties_retrieve_by_barcode(barcode)

Get a third party by barcode. 🔐

 Return an array with third party information

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    barcode = 'barcode_example' # str | Barcode of the third party

    try:
        # Get a third party by barcode. 🔐
        api_response = api_instance.thirdparties_retrieve_by_barcode(barcode)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_by_barcode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_by_barcode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Barcode of the third party | 

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

# **thirdparties_retrieve_by_email**
> str thirdparties_retrieve_by_email(email)

Get properties of a third party by email. 🔐

 Return an array with third party information

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    email = 'email_example' # str | Email of the third party to load

    try:
        # Get properties of a third party by email. 🔐
        api_response = api_instance.thirdparties_retrieve_by_email(email)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of the third party to load | 

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

# **thirdparties_retrieve_categories**
> List[str] thirdparties_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get customer categories for a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | List limit (optional)
    page = 56 # int | Page number (optional)

    try:
        # Get customer categories for a third party 🔐
        api_response = api_instance.thirdparties_retrieve_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
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

# **thirdparties_retrieve_company_bank_account**
> List[str] thirdparties_retrieve_company_bank_account(id)

Get company bank accounts of a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party

    try:
        # Get company bank accounts of a third party 🔐
        api_response = api_instance.thirdparties_retrieve_company_bank_account(id)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_company_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_company_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 

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

# **thirdparties_retrieve_company_notification**
> List[str] thirdparties_retrieve_company_notification(id)

Get company notifications for a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party

    try:
        # Get company notifications for a third party 🔐
        api_response = api_instance.thirdparties_retrieve_company_notification(id)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_company_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_company_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 

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

# **thirdparties_retrieve_fixed_amount_discounts**
> List[str] thirdparties_retrieve_fixed_amount_discounts(id, filter=filter, sortfield=sortfield, sortorder=sortorder)

Get fixed amount discount of a third party 🔐

all sources: deposit, credit note, commercial offers, etc.

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    filter = 'filter_example' # str | Filter exceptional discount. \"none\" will return every discount, \"available\" returns unapplied discounts, \"used\" returns applied discounts (optional)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)

    try:
        # Get fixed amount discount of a third party 🔐
        api_response = api_instance.thirdparties_retrieve_fixed_amount_discounts(id, filter=filter, sortfield=sortfield, sortorder=sortorder)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_fixed_amount_discounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_fixed_amount_discounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **filter** | **str**| Filter exceptional discount. \&quot;none\&quot; will return every discount, \&quot;available\&quot; returns unapplied discounts, \&quot;used\&quot; returns applied discounts | [optional] 
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_invoices_qualified_for_credit_note**
> List[str] thirdparties_retrieve_invoices_qualified_for_credit_note(id)

Return invoices qualified to be corrected by a credit note 🔐

Invoices matching the following rules are returned (validated + payment on process) or classified (paid completely or paid partially) + not already replaced + not already a credit note

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of a third party

    try:
        # Return invoices qualified to be corrected by a credit note 🔐
        api_response = api_instance.thirdparties_retrieve_invoices_qualified_for_credit_note(id)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_invoices_qualified_for_credit_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_invoices_qualified_for_credit_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of a third party | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_invoices_qualified_for_replacement**
> List[str] thirdparties_retrieve_invoices_qualified_for_replacement(id)

Return invoices qualified to be replaced by another invoice 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of a third party

    try:
        # Return invoices qualified to be replaced by another invoice 🔐
        api_response = api_instance.thirdparties_retrieve_invoices_qualified_for_replacement(id)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_invoices_qualified_for_replacement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_invoices_qualified_for_replacement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of a third party | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_out_standing_invoices**
> List[str] thirdparties_retrieve_out_standing_invoices(id, mode=mode)

Get outstanding invoices for a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    mode = 'mode_example' # str | 'customer' or 'supplier' (optional)

    try:
        # Get outstanding invoices for a third party 🔐
        api_response = api_instance.thirdparties_retrieve_out_standing_invoices(id, mode=mode)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_out_standing_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_out_standing_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **mode** | **str**| &#39;customer&#39; or &#39;supplier&#39; | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_out_standing_order**
> List[str] thirdparties_retrieve_out_standing_order(id, mode=mode)

Get outstanding orders for a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    mode = 'mode_example' # str | 'customer' or 'supplier' (optional)

    try:
        # Get outstanding orders for a third party 🔐
        api_response = api_instance.thirdparties_retrieve_out_standing_order(id, mode=mode)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_out_standing_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_out_standing_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **mode** | **str**| &#39;customer&#39; or &#39;supplier&#39; | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_out_standing_proposals**
> List[str] thirdparties_retrieve_out_standing_proposals(id, mode=mode)

Get outstanding proposals for a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    mode = 'mode_example' # str | 'customer' or 'supplier' (optional)

    try:
        # Get outstanding proposals for a third party 🔐
        api_response = api_instance.thirdparties_retrieve_out_standing_proposals(id, mode=mode)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_out_standing_proposals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_out_standing_proposals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **mode** | **str**| &#39;customer&#39; or &#39;supplier&#39; | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_sales_representatives**
> List[str] thirdparties_retrieve_sales_representatives(id, mode=mode)

Get representatives of a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    mode = 56 # int | 0=Array with properties, 1=Array of id. (optional)

    try:
        # Get representatives of a third party 🔐
        api_response = api_instance.thirdparties_retrieve_sales_representatives(id, mode=mode)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_sales_representatives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_sales_representatives: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **mode** | **int**| 0&#x3D;Array with properties, 1&#x3D;Array of id. | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_societe_accounts**
> str thirdparties_retrieve_societe_accounts(id, site=site)

Get a specific account attached to a third party 🔐

Specify the site key

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    site = 'site_example' # str | Site key (optional)

    try:
        # Get a specific account attached to a third party 🔐
        api_response = api_instance.thirdparties_retrieve_societe_accounts(id, site=site)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_societe_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_societe_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **site** | **str**| Site key | [optional] 

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
**401** | Unauthorized: User does not have permission to read thirdparties |  -  |
**404** | Not Found: Specified thirdparty ID does not belongs to an existing thirdparty |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_societe_by_accounts**
> str thirdparties_retrieve_societe_by_accounts(site, key_account)

Get a specific third party by account 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    site = 'site_example' # str | Site key
    key_account = 'key_account_example' # str | Key of the account

    try:
        # Get a specific third party by account 🔐
        api_response = api_instance.thirdparties_retrieve_societe_by_accounts(site, key_account)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_societe_by_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_societe_by_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**| Site key | 
 **key_account** | **str**| Key of the account | 

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
**401** | Unauthorized: User does not have permission to read thirdparties |  -  |
**404** | Not Found: Specified thirdparty ID does not belongs to an existing thirdparty |  -  |
**500** | RestException |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_retrieve_supplier_categories**
> List[str] thirdparties_retrieve_supplier_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)

Get supplier categories for a third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | List limit (optional)
    page = 56 # int | Page number (optional)

    try:
        # Get supplier categories for a third party 🔐
        api_response = api_instance.thirdparties_retrieve_supplier_categories(id, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page)
        print("The response of ThirdpartiesApi->thirdparties_retrieve_supplier_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_retrieve_supplier_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
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

# **thirdparties_set_thirdparty_price_level**
> Dict[str, object] thirdparties_set_thirdparty_price_level(id, price_level)

Set a new price level for the given third party 🔐

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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of thirdparty
    price_level = 56 # int | Price level to apply to thirdparty

    try:
        # Set a new price level for the given third party 🔐
        api_response = api_instance.thirdparties_set_thirdparty_price_level(id, price_level)
        print("The response of ThirdpartiesApi->thirdparties_set_thirdparty_price_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_set_thirdparty_price_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty | 
 **price_level** | **int**| Price level to apply to thirdparty | 

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
**400** | Price level out of bounds |  -  |
**401** | Access not allowed for your login |  -  |
**404** | Third party not found |  -  |
**500** | Error fetching/setting price level |  -  |
**501** | Request needs modules \&quot;Thirdparties\&quot; and \&quot;Products\&quot; and setting Multiprices activated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thirdparties_update_company_bank_account**
> str thirdparties_update_company_bank_account(id, bankaccount_id, thirdparties_update_company_bank_account_model=thirdparties_update_company_bank_account_model)

Update a company bank account of a third party 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.thirdparties_update_company_bank_account_model import ThirdpartiesUpdateCompanyBankAccountModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    bankaccount_id = 56 # int | ID of CompanyBankAccount
    thirdparties_update_company_bank_account_model = dolibarr_api.ThirdpartiesUpdateCompanyBankAccountModel() # ThirdpartiesUpdateCompanyBankAccountModel | request_data    (optional)

    try:
        # Update a company bank account of a third party 🔐
        api_response = api_instance.thirdparties_update_company_bank_account(id, bankaccount_id, thirdparties_update_company_bank_account_model=thirdparties_update_company_bank_account_model)
        print("The response of ThirdpartiesApi->thirdparties_update_company_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_update_company_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **bankaccount_id** | **int**| ID of CompanyBankAccount | 
 **thirdparties_update_company_bank_account_model** | [**ThirdpartiesUpdateCompanyBankAccountModel**](ThirdpartiesUpdateCompanyBankAccountModel.md)| request_data    | [optional] 

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

# **thirdparties_update_company_notification**
> str thirdparties_update_company_notification(id, notification_id, thirdparties_update_company_notification_model=thirdparties_update_company_notification_model)

Update a company notification for a third party 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.thirdparties_update_company_notification_model import ThirdpartiesUpdateCompanyNotificationModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    notification_id = 56 # int | ID of CompanyNotification
    thirdparties_update_company_notification_model = dolibarr_api.ThirdpartiesUpdateCompanyNotificationModel() # ThirdpartiesUpdateCompanyNotificationModel | request_data    (optional)

    try:
        # Update a company notification for a third party 🔐
        api_response = api_instance.thirdparties_update_company_notification(id, notification_id, thirdparties_update_company_notification_model=thirdparties_update_company_notification_model)
        print("The response of ThirdpartiesApi->thirdparties_update_company_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_update_company_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **notification_id** | **int**| ID of CompanyNotification | 
 **thirdparties_update_company_notification_model** | [**ThirdpartiesUpdateCompanyNotificationModel**](ThirdpartiesUpdateCompanyNotificationModel.md)| request_data    | [optional] 

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

# **thirdparties_update_societe_account**
> str thirdparties_update_societe_account(id, site, thirdparties_update_societe_account_model=thirdparties_update_societe_account_model)

Update specified values of a specific account attached to a third party 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.thirdparties_update_societe_account_model import ThirdpartiesUpdateSocieteAccountModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of the third party
    site = 'site_example' # str | Site key
    thirdparties_update_societe_account_model = dolibarr_api.ThirdpartiesUpdateSocieteAccountModel() # ThirdpartiesUpdateSocieteAccountModel | request_data    (optional)

    try:
        # Update specified values of a specific account attached to a third party 🔐
        api_response = api_instance.thirdparties_update_societe_account(id, site, thirdparties_update_societe_account_model=thirdparties_update_societe_account_model)
        print("The response of ThirdpartiesApi->thirdparties_update_societe_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->thirdparties_update_societe_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the third party | 
 **site** | **str**| Site key | 
 **thirdparties_update_societe_account_model** | [**ThirdpartiesUpdateSocieteAccountModel**](ThirdpartiesUpdateSocieteAccountModel.md)| request_data    | [optional] 

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
**401** | Unauthorized: User does not have permission to read thirdparties |  -  |
**404** | Not Found: Specified thirdparty ID does not belongs to an existing thirdparty |  -  |
**409** | Conflict: Another SocieteAccount entity already exists for this thirdparty with this site key. |  -  |
**500** | Internal Server Error: Error updating SocieteAccount entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_thirdparties**
> Dict[str, object] update_thirdparties(id, update_thirdparties_model=update_thirdparties_model)

Update third party 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.update_thirdparties_model import UpdateThirdpartiesModel
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
    api_instance = dolibarr_api.ThirdpartiesApi(api_client)
    id = 56 # int | ID of thirdparty to update
    update_thirdparties_model = dolibarr_api.UpdateThirdpartiesModel() # UpdateThirdpartiesModel | request_data    (optional)

    try:
        # Update third party 🔐
        api_response = api_instance.update_thirdparties(id, update_thirdparties_model=update_thirdparties_model)
        print("The response of ThirdpartiesApi->update_thirdparties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdpartiesApi->update_thirdparties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of thirdparty to update | 
 **update_thirdparties_model** | [**UpdateThirdpartiesModel**](UpdateThirdpartiesModel.md)| request_data    | [optional] 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

