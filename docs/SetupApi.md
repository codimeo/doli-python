# dolibarr_api.SetupApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setup_create_extrafields**](SetupApi.md#setup_create_extrafields) | **POST** /setup/extrafields/{elementtype}/{attrname} | Create Extrafield object 🔐
[**setup_remove_extrafields_from_names**](SetupApi.md#setup_remove_extrafields_from_names) | **DELETE** /setup/extrafields/{elementtype}/{attrname} | Delete extrafield 🔐
[**setup_retrieve_availability**](SetupApi.md#setup_retrieve_availability) | **GET** /setup/dictionary/availability | Get the list of delivery times. 🔐
[**setup_retrieve_check_integrity**](SetupApi.md#setup_retrieve_check_integrity) | **GET** /setup/checkintegrity | Do a test of integrity for files and setup. 🔐
[**setup_retrieve_company**](SetupApi.md#setup_retrieve_company) | **GET** /setup/company | Get properties of company 🔐
[**setup_retrieve_conf**](SetupApi.md#setup_retrieve_conf) | **GET** /setup/conf/{constantname} | Get value of a setup variables 🔐
[**setup_retrieve_confs**](SetupApi.md#setup_retrieve_confs) | **GET** /setup/conf | Get all setup variables 🔐
[**setup_retrieve_country_by_code**](SetupApi.md#setup_retrieve_country_by_code) | **GET** /setup/dictionary/countries/byCode/{code} | Get country by Code. 🔐
[**setup_retrieve_country_by_id**](SetupApi.md#setup_retrieve_country_by_id) | **GET** /setup/dictionary/countries/{id} | Get country by ID. 🔐
[**setup_retrieve_country_by_iso**](SetupApi.md#setup_retrieve_country_by_iso) | **GET** /setup/dictionary/countries/byISO/{iso} | Get country by Iso. 🔐
[**setup_retrieve_establishments**](SetupApi.md#setup_retrieve_establishments) | **GET** /setup/establishments | Get the list of establishments. 🔐
[**setup_retrieve_etablishment_by_id**](SetupApi.md#setup_retrieve_etablishment_by_id) | **GET** /setup/establishments/{id} | Get establishment by ID. 🔐
[**setup_retrieve_extrafields**](SetupApi.md#setup_retrieve_extrafields) | **GET** /setup/extrafields/{elementtype}/{attrname} |  🔐
[**setup_retrieve_list_of_action_triggers**](SetupApi.md#setup_retrieve_list_of_action_triggers) | **GET** /setup/actiontriggers | Get the list of Action Triggers. 🔐
[**setup_retrieve_list_of_civilities**](SetupApi.md#setup_retrieve_list_of_civilities) | **GET** /setup/dictionary/civilities | Get the list of civilities. 🔐
[**setup_retrieve_list_of_contact_types**](SetupApi.md#setup_retrieve_list_of_contact_types) | **GET** /setup/dictionary/contact_types | Get the list of contacts types. 🔐
[**setup_retrieve_list_of_countries**](SetupApi.md#setup_retrieve_list_of_countries) | **GET** /setup/dictionary/countries | Get the list of countries. 🔐
[**setup_retrieve_list_of_currencies**](SetupApi.md#setup_retrieve_list_of_currencies) | **GET** /setup/dictionary/currencies | Get the list of currencies. 🔐
[**setup_retrieve_list_of_event_types**](SetupApi.md#setup_retrieve_list_of_event_types) | **GET** /setup/dictionary/event_types | Get the list of events types. 🔐
[**setup_retrieve_list_of_expense_reports_types**](SetupApi.md#setup_retrieve_list_of_expense_reports_types) | **GET** /setup/dictionary/expensereport_types | Get the list of Expense Report types. 🔐
[**setup_retrieve_list_of_extrafields**](SetupApi.md#setup_retrieve_list_of_extrafields) | **GET** /setup/extrafields | Get the list of extra fields. 🔐
[**setup_retrieve_list_of_incoterms**](SetupApi.md#setup_retrieve_list_of_incoterms) | **GET** /setup/dictionary/incoterms | Get the list of incoterms. 🔐
[**setup_retrieve_list_of_legal_form**](SetupApi.md#setup_retrieve_list_of_legal_form) | **GET** /setup/dictionary/legal_form | Get the list of legal form of business. 🔐
[**setup_retrieve_list_of_measuring_units**](SetupApi.md#setup_retrieve_list_of_measuring_units) | **GET** /setup/dictionary/units | Get the list of measuring units. 🔐
[**setup_retrieve_list_of_regions**](SetupApi.md#setup_retrieve_list_of_regions) | **GET** /setup/dictionary/regions | Get the list of regions. 🔐
[**setup_retrieve_list_of_staff**](SetupApi.md#setup_retrieve_list_of_staff) | **GET** /setup/dictionary/staff | Get the list of staff. 🔐
[**setup_retrieve_list_of_states**](SetupApi.md#setup_retrieve_list_of_states) | **GET** /setup/dictionary/states | Get the list of states/provinces. 🔐
[**setup_retrieve_list_of_towns**](SetupApi.md#setup_retrieve_list_of_towns) | **GET** /setup/dictionary/towns | Get the list of towns. 🔐
[**setup_retrieve_list_ofsocial_networks**](SetupApi.md#setup_retrieve_list_ofsocial_networks) | **GET** /setup/dictionary/socialnetworks | Get the list of social networks. 🔐
[**setup_retrieve_modules**](SetupApi.md#setup_retrieve_modules) | **GET** /setup/modules | Get list of enabled modules 🔐
[**setup_retrieve_ordering_methods**](SetupApi.md#setup_retrieve_ordering_methods) | **GET** /setup/dictionary/ordering_methods | Get the list of ordering methods. 🔐
[**setup_retrieve_ordering_origins**](SetupApi.md#setup_retrieve_ordering_origins) | **GET** /setup/dictionary/ordering_origins | Get the list of ordering origins. 🔐
[**setup_retrieve_payment_terms**](SetupApi.md#setup_retrieve_payment_terms) | **GET** /setup/dictionary/payment_terms | Get the list of payments terms. 🔐
[**setup_retrieve_payment_types**](SetupApi.md#setup_retrieve_payment_types) | **GET** /setup/dictionary/payment_types | Get the list of payments types. 🔐
[**setup_retrieve_region_by_code**](SetupApi.md#setup_retrieve_region_by_code) | **GET** /setup/dictionary/regions/byCode/{code} | Get region by Code. 🔐
[**setup_retrieve_region_by_id**](SetupApi.md#setup_retrieve_region_by_id) | **GET** /setup/dictionary/regions/{id} | Get region by ID. 🔐
[**setup_retrieve_shipping_modes**](SetupApi.md#setup_retrieve_shipping_modes) | **GET** /setup/dictionary/shipping_methods | Get the list of shipping methods. 🔐
[**setup_retrieve_state_by_code**](SetupApi.md#setup_retrieve_state_by_code) | **GET** /setup/dictionary/states/byCode/{code} | Get state by Code. 🔐
[**setup_retrieve_state_by_id**](SetupApi.md#setup_retrieve_state_by_id) | **GET** /setup/dictionary/states/{id} | Get state by ID. 🔐
[**setup_retrieve_tickets_categories**](SetupApi.md#setup_retrieve_tickets_categories) | **GET** /setup/dictionary/ticket_categories | Get the list of tickets categories. 🔐
[**setup_retrieve_tickets_severities**](SetupApi.md#setup_retrieve_tickets_severities) | **GET** /setup/dictionary/ticket_severities | Get the list of tickets severity. 🔐
[**setup_retrieve_tickets_types**](SetupApi.md#setup_retrieve_tickets_types) | **GET** /setup/dictionary/ticket_types | Get the list of tickets types. 🔐
[**setup_update_extrafields**](SetupApi.md#setup_update_extrafields) | **PUT** /setup/extrafields/{elementtype}/{attrname} | Update Extrafield object 🔐


# **setup_create_extrafields**
> int setup_create_extrafields(attrname, elementtype, setup_create_extrafields_model=setup_create_extrafields_model)

Create Extrafield object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.setup_create_extrafields_model import SetupCreateExtrafieldsModel
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
    api_instance = dolibarr_api.SetupApi(api_client)
    attrname = 'attrname_example' # str | extrafield attrname
    elementtype = 'elementtype_example' # str | extrafield elementtype
    setup_create_extrafields_model = dolibarr_api.SetupCreateExtrafieldsModel() # SetupCreateExtrafieldsModel | request_data    (optional)

    try:
        # Create Extrafield object 🔐
        api_response = api_instance.setup_create_extrafields(attrname, elementtype, setup_create_extrafields_model=setup_create_extrafields_model)
        print("The response of SetupApi->setup_create_extrafields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_create_extrafields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attrname** | **str**| extrafield attrname | 
 **elementtype** | **str**| extrafield elementtype | 
 **setup_create_extrafields_model** | [**SetupCreateExtrafieldsModel**](SetupCreateExtrafieldsModel.md)| request_data    | [optional] 

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

# **setup_remove_extrafields_from_names**
> List[str] setup_remove_extrafields_from_names(attrname, elementtype)

Delete extrafield 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    attrname = 'attrname_example' # str | extrafield attrname
    elementtype = 'elementtype_example' # str | extrafield elementtype

    try:
        # Delete extrafield 🔐
        api_response = api_instance.setup_remove_extrafields_from_names(attrname, elementtype)
        print("The response of SetupApi->setup_remove_extrafields_from_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_remove_extrafields_from_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attrname** | **str**| extrafield attrname | 
 **elementtype** | **str**| extrafield elementtype | 

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

# **setup_retrieve_availability**
> List[str] setup_retrieve_availability(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of delivery times. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (optional)
    active = 56 # int | Delivery times is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter with. (optional)

    try:
        # Get the list of delivery times. 🔐
        api_response = api_instance.setup_retrieve_availability(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Delivery times is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter with. | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**403** | Access denied |  -  |
**503** | Error when retrieving list of availabilities |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_check_integrity**
> List[str] setup_retrieve_check_integrity(target)

Do a test of integrity for files and setup. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    target = 'target_example' # str | Can be 'local' or 'default' or Url of the signatures file to use for the test. Must be reachable by the tested Dolibarr.

    try:
        # Do a test of integrity for files and setup. 🔐
        api_response = api_instance.setup_retrieve_check_integrity(target)
        print("The response of SetupApi->setup_retrieve_check_integrity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_check_integrity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Can be &#39;local&#39; or &#39;default&#39; or Url of the signatures file to use for the test. Must be reachable by the tested Dolibarr. | 

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
**403** | Forbidden |  -  |
**404** | Signature file not found |  -  |
**500** | Technical error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_company**
> List[str] setup_retrieve_company()

Get properties of company 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)

    try:
        # Get properties of company 🔐
        api_response = api_instance.setup_retrieve_company()
        print("The response of SetupApi->setup_retrieve_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_company: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_conf**
> str setup_retrieve_conf(constantname)

Get value of a setup variables 🔐

Note that conf variables that stores security key or password hashes can't be loaded with API.

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
    api_instance = dolibarr_api.SetupApi(api_client)
    constantname = 'constantname_example' # str | Name of conf variable to get

    try:
        # Get value of a setup variables 🔐
        api_response = api_instance.setup_retrieve_conf(constantname)
        print("The response of SetupApi->setup_retrieve_conf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_conf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **constantname** | **str**| Name of conf variable to get | 

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
**400** | Error Bad or unknown value for constantname |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_confs**
> List[str] setup_retrieve_confs()

Get all setup variables 🔐

Note that conf variables that stores security key or password hashes can't be loaded with API.

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
    api_instance = dolibarr_api.SetupApi(api_client)

    try:
        # Get all setup variables 🔐
        api_response = api_instance.setup_retrieve_confs()
        print("The response of SetupApi->setup_retrieve_confs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_confs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**400** | Error Bad or unknown value for constantname |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_country_by_code**
> Dict[str, object] setup_retrieve_country_by_code(code, lang=lang)

Get country by Code. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    code = 'code_example' # str | Code of country (2 characters)
    lang = 'lang_example' # str | Code of the language the name of the country must be translated to (optional)

    try:
        # Get country by Code. 🔐
        api_response = api_instance.setup_retrieve_country_by_code(code, lang=lang)
        print("The response of SetupApi->setup_retrieve_country_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_country_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of country (2 characters) | 
 **lang** | **str**| Code of the language the name of the country must be translated to | [optional] 

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
**404** | Country not found |  -  |
**503** | Error retrieving country |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_country_by_id**
> Dict[str, object] setup_retrieve_country_by_id(id, lang=lang)

Get country by ID. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    id = 56 # int | ID of country
    lang = 'lang_example' # str | Code of the language the name of the country must be translated to (optional)

    try:
        # Get country by ID. 🔐
        api_response = api_instance.setup_retrieve_country_by_id(id, lang=lang)
        print("The response of SetupApi->setup_retrieve_country_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_country_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of country | 
 **lang** | **str**| Code of the language the name of the country must be translated to | [optional] 

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
**404** | Country not found |  -  |
**503** | Error retrieving country |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_country_by_iso**
> Dict[str, object] setup_retrieve_country_by_iso(iso, lang=lang)

Get country by Iso. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    iso = 'iso_example' # str | ISO of country (3 characters)
    lang = 'lang_example' # str | Code of the language the name of the country must be translated to (optional)

    try:
        # Get country by Iso. 🔐
        api_response = api_instance.setup_retrieve_country_by_iso(iso, lang=lang)
        print("The response of SetupApi->setup_retrieve_country_by_iso:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_country_by_iso: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iso** | **str**| ISO of country (3 characters) | 
 **lang** | **str**| Code of the language the name of the country must be translated to | [optional] 

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
**404** | Country not found |  -  |
**503** | Error retrieving country |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_establishments**
> List[str] setup_retrieve_establishments()

Get the list of establishments. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)

    try:
        # Get the list of establishments. 🔐
        api_response = api_instance.setup_retrieve_establishments()
        print("The response of SetupApi->setup_retrieve_establishments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_establishments: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**503** | Error when retrieving list of establishments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_etablishment_by_id**
> Dict[str, object] setup_retrieve_etablishment_by_id(id)

Get establishment by ID. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    id = 56 # int | ID of establishment

    try:
        # Get establishment by ID. 🔐
        api_response = api_instance.setup_retrieve_etablishment_by_id(id)
        print("The response of SetupApi->setup_retrieve_etablishment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_etablishment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of establishment | 

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
**404** | Establishment not found |  -  |
**503** | Error when retrieving establishment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_extrafields**
> List[str] setup_retrieve_extrafields(attrname, elementtype)

 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    attrname = 'attrname_example' # str | extrafield attrname
    elementtype = 'elementtype_example' # str | extrafield elementtype

    try:
        #  🔐
        api_response = api_instance.setup_retrieve_extrafields(attrname, elementtype)
        print("The response of SetupApi->setup_retrieve_extrafields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_extrafields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attrname** | **str**| extrafield attrname | 
 **elementtype** | **str**| extrafield elementtype | 

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

# **setup_retrieve_list_of_action_triggers**
> List[str] setup_retrieve_list_of_action_triggers(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, elementtype=elementtype, lang=lang, sqlfilters=sqlfilters)

Get the list of Action Triggers. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (optional)
    elementtype = 'elementtype_example' # str | Type of element ('adherent', 'commande', 'thirdparty', 'facture', 'propal', 'product', ...) (optional)
    lang = 'lang_example' # str | Code of the language the label of the type must be translated to (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.label:like:'SO-%')\" (optional)

    try:
        # Get the list of Action Triggers. 🔐
        api_response = api_instance.setup_retrieve_list_of_action_triggers(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, elementtype=elementtype, lang=lang, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_action_triggers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_action_triggers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **elementtype** | **str**| Type of element (&#39;adherent&#39;, &#39;commande&#39;, &#39;thirdparty&#39;, &#39;facture&#39;, &#39;propal&#39;, &#39;product&#39;, ...) | [optional] 
 **lang** | **str**| Code of the language the label of the type must be translated to | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.label:like:&#39;SO-%&#39;)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of action triggers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_civilities**
> List[str] setup_retrieve_list_of_civilities(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, module=module, active=active, lang=lang, sqlfilters=sqlfilters)

Get the list of civilities. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    module = 'module_example' # str | To filter on module events (optional)
    active = 56 # int | Civility is active or not (optional)
    lang = 'lang_example' # str | Code of the language the label of the civility must be translated to (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of civilities. 🔐
        api_response = api_instance.setup_retrieve_list_of_civilities(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, module=module, active=active, lang=lang, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_civilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_civilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **module** | **str**| To filter on module events | [optional] 
 **active** | **int**| Civility is active or not | [optional] 
 **lang** | **str**| Code of the language the label of the civility must be translated to | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of civilities |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_contact_types**
> List[str] setup_retrieve_list_of_contact_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, module=module, active=active, lang=lang, sqlfilters=sqlfilters)

Get the list of contacts types. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    type = 'type_example' # str | To filter on type of contact (optional)
    module = 'module_example' # str | To filter on module contacts (optional)
    active = 56 # int | Contact's type is active or not (optional)
    lang = 'lang_example' # str | Code of the language the label of the civility must be translated to (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of contacts types. 🔐
        api_response = api_instance.setup_retrieve_list_of_contact_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, module=module, active=active, lang=lang, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_contact_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_contact_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **type** | **str**| To filter on type of contact | [optional] 
 **module** | **str**| To filter on module contacts | [optional] 
 **active** | **int**| Contact&#39;s type is active or not | [optional] 
 **lang** | **str**| Code of the language the label of the civility must be translated to | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of contacts types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_countries**
> List[str] setup_retrieve_list_of_countries(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, filter=filter, lang=lang, sqlfilters=sqlfilters)

Get the list of countries. 🔐

 The names of the countries will be translated to the given language if the $lang parameter is provided. The value of $lang must be a language code supported by Dolibarr, for example 'en_US' or 'fr_FR'. The returned list is sorted by country ID.

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    filter = 'filter_example' # str | To filter the countries by name (optional)
    lang = 'lang_example' # str | Code of the language the label of the countries must be translated to (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of countries. 🔐
        api_response = api_instance.setup_retrieve_list_of_countries(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, filter=filter, lang=lang, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **filter** | **str**| To filter the countries by name | [optional] 
 **lang** | **str**| Code of the language the label of the countries must be translated to | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error retrieving list of countries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_currencies**
> List[str] setup_retrieve_list_of_currencies(multicurrency=multicurrency, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of currencies. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    multicurrency = 56 # int | Multicurrency rates (0: no multicurrency, 1: last rate, 2: all rates) (optional)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    active = 56 # int | Payment term is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of currencies. 🔐
        api_response = api_instance.setup_retrieve_list_of_currencies(multicurrency=multicurrency, sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicurrency** | **int**| Multicurrency rates (0: no multicurrency, 1: last rate, 2: all rates) | [optional] 
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of currencies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_event_types**
> List[str] setup_retrieve_list_of_event_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, module=module, active=active, sqlfilters=sqlfilters)

Get the list of events types. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    type = 'type_example' # str | To filter on type of event (optional)
    module = 'module_example' # str | To filter on module events (optional)
    active = 56 # int | Event's type is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of events types. 🔐
        api_response = api_instance.setup_retrieve_list_of_event_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, type=type, module=module, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_event_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_event_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **type** | **str**| To filter on type of event | [optional] 
 **module** | **str**| To filter on module events | [optional] 
 **active** | **int**| Event&#39;s type is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of events types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_expense_reports_types**
> List[str] setup_retrieve_list_of_expense_reports_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, module=module, active=active, sqlfilters=sqlfilters)

Get the list of Expense Report types. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    module = 'module_example' # str | To filter on module (optional)
    active = 56 # int | Event's type is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of Expense Report types. 🔐
        api_response = api_instance.setup_retrieve_list_of_expense_reports_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, module=module, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_expense_reports_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_expense_reports_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **module** | **str**| To filter on module | [optional] 
 **active** | **int**| Event&#39;s type is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of expense report types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_extrafields**
> List[str] setup_retrieve_list_of_extrafields(sortfield=sortfield, sortorder=sortorder, elementtype=elementtype, sqlfilters=sqlfilters)

Get the list of extra fields. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    elementtype = 'elementtype_example' # str | Type of element ('adherent', 'commande', 'thirdparty', 'facture', 'propal', 'product', ...) (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.label:like:'SO-%')\" (optional)

    try:
        # Get the list of extra fields. 🔐
        api_response = api_instance.setup_retrieve_list_of_extrafields(sortfield=sortfield, sortorder=sortorder, elementtype=elementtype, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_extrafields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_extrafields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **elementtype** | **str**| Type of element (&#39;adherent&#39;, &#39;commande&#39;, &#39;thirdparty&#39;, &#39;facture&#39;, &#39;propal&#39;, &#39;product&#39;, ...) | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.label:like:&#39;SO-%&#39;)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of extra fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_incoterms**
> List[str] setup_retrieve_list_of_incoterms(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)

Get the list of incoterms. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    active = 56 # int | Payment term is active or not (optional)
    lang = 'lang_example' # str | Code of the language the label of the type must be translated to (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of incoterms. 🔐
        api_response = api_instance.setup_retrieve_list_of_incoterms(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_incoterms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_incoterms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **lang** | **str**| Code of the language the label of the type must be translated to | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**503** | Error when retrieving list of incoterms types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_legal_form**
> List[str] setup_retrieve_list_of_legal_form(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, country=country, active=active, sqlfilters=sqlfilters)

Get the list of legal form of business. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    country = 56 # int | To filter on country (optional)
    active = 56 # int | Lega form is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of legal form of business. 🔐
        api_response = api_instance.setup_retrieve_list_of_legal_form(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, country=country, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_legal_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_legal_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **country** | **int**| To filter on country | [optional] 
 **active** | **int**| Lega form is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of legal form |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_measuring_units**
> List[str] setup_retrieve_list_of_measuring_units(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of measuring units. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    active = 56 # int | Measuring unit is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of measuring units. 🔐
        api_response = api_instance.setup_retrieve_list_of_measuring_units(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_measuring_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_measuring_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Measuring unit is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of measuring units |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_regions**
> List[str] setup_retrieve_list_of_regions(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, country=country, filter=filter, sqlfilters=sqlfilters)

Get the list of regions. 🔐

 The returned list is sorted by region ID.

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    country = 56 # int | To filter on country (optional)
    filter = 'filter_example' # str | To filter the regions by name (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of regions. 🔐
        api_response = api_instance.setup_retrieve_list_of_regions(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, country=country, filter=filter, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **country** | **int**| To filter on country | [optional] 
 **filter** | **str**| To filter the regions by name | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error retrieving list of regions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_staff**
> List[str] setup_retrieve_list_of_staff(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of staff. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    active = 56 # int | Staff is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of staff. 🔐
        api_response = api_instance.setup_retrieve_list_of_staff(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_staff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_staff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Staff is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of staff |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_states**
> List[str] setup_retrieve_list_of_states(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, country=country, filter=filter, sqlfilters=sqlfilters)

Get the list of states/provinces. 🔐

 The names of the states will be translated to the given language if the $lang parameter is provided. The value of $lang must be a language code supported by Dolibarr, for example 'en_US' or 'fr_FR'. The returned list is sorted by state ID.

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    country = 56 # int | To filter on country (optional)
    filter = 'filter_example' # str | To filter the states by name (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of states/provinces. 🔐
        api_response = api_instance.setup_retrieve_list_of_states(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, country=country, filter=filter, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **country** | **int**| To filter on country | [optional] 
 **filter** | **str**| To filter the states by name | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error retrieving list of states |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_of_towns**
> List[str] setup_retrieve_list_of_towns(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, zipcode=zipcode, town=town, active=active, sqlfilters=sqlfilters)

Get the list of towns. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    zipcode = 'zipcode_example' # str | To filter on zipcode (optional)
    town = 'town_example' # str | To filter on city name (optional)
    active = 56 # int | Town is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of towns. 🔐
        api_response = api_instance.setup_retrieve_list_of_towns(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, zipcode=zipcode, town=town, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_of_towns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_of_towns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **zipcode** | **str**| To filter on zipcode | [optional] 
 **town** | **str**| To filter on city name | [optional] 
 **active** | **int**| Town is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of towns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_list_ofsocial_networks**
> List[str] setup_retrieve_list_ofsocial_networks(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of social networks. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    active = 56 # int | Social network is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of social networks. 🔐
        api_response = api_instance.setup_retrieve_list_ofsocial_networks(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_list_ofsocial_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_list_ofsocial_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Social network is active or not | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of social networks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_modules**
> List[str] setup_retrieve_modules()

Get list of enabled modules 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)

    try:
        # Get list of enabled modules 🔐
        api_response = api_instance.setup_retrieve_modules()
        print("The response of SetupApi->setup_retrieve_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_modules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_ordering_methods**
> List[str] setup_retrieve_ordering_methods(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of ordering methods. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (optional)
    active = 56 # int | Payment type is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter with. Syntax example \"(t.code:=:'OrderByWWW')\" (optional)

    try:
        # Get the list of ordering methods. 🔐
        api_response = api_instance.setup_retrieve_ordering_methods(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_ordering_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_ordering_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Payment type is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter with. Syntax example \&quot;(t.code:&#x3D;:&#39;OrderByWWW&#39;)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**403** | Access denied |  -  |
**503** | Error retrieving list of ordering methods |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_ordering_origins**
> List[str] setup_retrieve_ordering_origins(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of ordering origins. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (optional)
    active = 56 # int | Payment type is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter with. Syntax example \"(t.code:=:'OrderByWWW')\" (optional)

    try:
        # Get the list of ordering origins. 🔐
        api_response = api_instance.setup_retrieve_ordering_origins(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_ordering_origins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_ordering_origins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Payment type is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter with. Syntax example \&quot;(t.code:&#x3D;:&#39;OrderByWWW&#39;)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**403** | Access denied |  -  |
**503** | Error retrieving list of ordering origins |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_payment_terms**
> List[str] setup_retrieve_payment_terms(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of payments terms. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (optional)
    active = 56 # int | Payment term is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter. Syntax example \"(t.code:=:'CHQ')\" (optional)

    try:
        # Get the list of payments terms. 🔐
        api_response = api_instance.setup_retrieve_payment_terms(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_payment_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_payment_terms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter. Syntax example \&quot;(t.code:&#x3D;:&#39;CHQ&#39;)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**403** | Access denied |  -  |
**503** | Error when retrieving list of payments terms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_payment_types**
> List[str] setup_retrieve_payment_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)

Get the list of payments types. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (optional)
    active = 56 # int | Payment type is active or not (optional)
    sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter with. Syntax example \"(t.code:=:'CHQ')\" (optional)

    try:
        # Get the list of payments types. 🔐
        api_response = api_instance.setup_retrieve_payment_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_payment_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_payment_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Payment type is active or not | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter with. Syntax example \&quot;(t.code:&#x3D;:&#39;CHQ&#39;)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**403** | Access denied |  -  |
**503** | Error retrieving list of payment types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_region_by_code**
> Dict[str, object] setup_retrieve_region_by_code(code)

Get region by Code. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    code = 'code_example' # str | Code of region

    try:
        # Get region by Code. 🔐
        api_response = api_instance.setup_retrieve_region_by_code(code)
        print("The response of SetupApi->setup_retrieve_region_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_region_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of region | 

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
**404** | Region not found |  -  |
**503** | Error when retrieving region |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_region_by_id**
> Dict[str, object] setup_retrieve_region_by_id(id)

Get region by ID. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    id = 56 # int | ID of region

    try:
        # Get region by ID. 🔐
        api_response = api_instance.setup_retrieve_region_by_id(id)
        print("The response of SetupApi->setup_retrieve_region_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_region_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of region | 

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
**404** | Region not found |  -  |
**503** | Error retrieving region |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_shipping_modes**
> List[str] setup_retrieve_shipping_modes(limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)

Get the list of shipping methods. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (optional)
    active = 56 # int | Shipping methodsm is active or not (optional)
    lang = 'lang_example' # str | Code of the language the label of the method must be translated to (optional)
    sqlfilters = 'sqlfilters_example' # str | SQL criteria to filter. Syntax example \"(t.code:=:'CHQ')\" (optional)

    try:
        # Get the list of shipping methods. 🔐
        api_response = api_instance.setup_retrieve_shipping_modes(limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_shipping_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_shipping_modes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number | [optional] 
 **active** | **int**| Shipping methodsm is active or not | [optional] 
 **lang** | **str**| Code of the language the label of the method must be translated to | [optional] 
 **sqlfilters** | **str**| SQL criteria to filter. Syntax example \&quot;(t.code:&#x3D;:&#39;CHQ&#39;)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of shipping modes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_state_by_code**
> Dict[str, object] setup_retrieve_state_by_code(code)

Get state by Code. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    code = 'code_example' # str | Code of state

    try:
        # Get state by Code. 🔐
        api_response = api_instance.setup_retrieve_state_by_code(code)
        print("The response of SetupApi->setup_retrieve_state_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_state_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of state | 

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
**404** | State not found |  -  |
**503** | Error retrieving state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_state_by_id**
> Dict[str, object] setup_retrieve_state_by_id(id)

Get state by ID. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    id = 56 # int | ID of state

    try:
        # Get state by ID. 🔐
        api_response = api_instance.setup_retrieve_state_by_id(id)
        print("The response of SetupApi->setup_retrieve_state_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_state_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of state | 

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
**404** | State not found |  -  |
**503** | Error retrieving state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_tickets_categories**
> List[str] setup_retrieve_tickets_categories(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)

Get the list of tickets categories. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    active = 56 # int | Payment term is active or not (optional)
    lang = 'lang_example' # str | Code of the language the label of the category must be translated to (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of tickets categories. 🔐
        api_response = api_instance.setup_retrieve_tickets_categories(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_tickets_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_tickets_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **lang** | **str**| Code of the language the label of the category must be translated to | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of tickets categories |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_tickets_severities**
> List[str] setup_retrieve_tickets_severities(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)

Get the list of tickets severity. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    active = 56 # int | Payment term is active or not (optional)
    lang = 'lang_example' # str | Code of the language the label of the severity must be translated to (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of tickets severity. 🔐
        api_response = api_instance.setup_retrieve_tickets_severities(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_tickets_severities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_tickets_severities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **lang** | **str**| Code of the language the label of the severity must be translated to | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of tickets severities |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_retrieve_tickets_types**
> List[str] setup_retrieve_tickets_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)

Get the list of tickets types. 🔐

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
    api_instance = dolibarr_api.SetupApi(api_client)
    sortfield = 'sortfield_example' # str | Sort field (optional)
    sortorder = 'sortorder_example' # str | Sort order (optional)
    limit = 56 # int | Number of items per page (optional)
    page = 56 # int | Page number (starting from zero) (optional)
    active = 56 # int | Payment term is active or not (optional)
    lang = 'lang_example' # str | Code of the language the label of the type must be translated to (optional)
    sqlfilters = 'sqlfilters_example' # str | Other criteria to filter answers separated by a comma. Syntax example \"(t.code:like:'A%') and (t.active:>=:0)\" (optional)

    try:
        # Get the list of tickets types. 🔐
        api_response = api_instance.setup_retrieve_tickets_types(sortfield=sortfield, sortorder=sortorder, limit=limit, page=page, active=active, lang=lang, sqlfilters=sqlfilters)
        print("The response of SetupApi->setup_retrieve_tickets_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_retrieve_tickets_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortfield** | **str**| Sort field | [optional] 
 **sortorder** | **str**| Sort order | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **page** | **int**| Page number (starting from zero) | [optional] 
 **active** | **int**| Payment term is active or not | [optional] 
 **lang** | **str**| Code of the language the label of the type must be translated to | [optional] 
 **sqlfilters** | **str**| Other criteria to filter answers separated by a comma. Syntax example \&quot;(t.code:like:&#39;A%&#39;) and (t.active:&gt;&#x3D;:0)\&quot; | [optional] 

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
**400** | Bad value for sqlfilters |  -  |
**503** | Error when retrieving list of tickets types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_update_extrafields**
> int setup_update_extrafields(attrname, elementtype, setup_update_extrafields_model=setup_update_extrafields_model)

Update Extrafield object 🔐

### Example

* Api Key Authentication (api_key):

```python
import dolibarr_api
from dolibarr_api.models.setup_update_extrafields_model import SetupUpdateExtrafieldsModel
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
    api_instance = dolibarr_api.SetupApi(api_client)
    attrname = 'attrname_example' # str | extrafield attrname
    elementtype = 'elementtype_example' # str | extrafield elementtype
    setup_update_extrafields_model = dolibarr_api.SetupUpdateExtrafieldsModel() # SetupUpdateExtrafieldsModel | request_data    (optional)

    try:
        # Update Extrafield object 🔐
        api_response = api_instance.setup_update_extrafields(attrname, elementtype, setup_update_extrafields_model=setup_update_extrafields_model)
        print("The response of SetupApi->setup_update_extrafields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupApi->setup_update_extrafields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attrname** | **str**| extrafield attrname | 
 **elementtype** | **str**| extrafield elementtype | 
 **setup_update_extrafields_model** | [**SetupUpdateExtrafieldsModel**](SetupUpdateExtrafieldsModel.md)| request_data    | [optional] 

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

