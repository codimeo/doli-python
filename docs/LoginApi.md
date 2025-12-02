# dolibarr_api.LoginApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_login**](LoginApi.md#list_login) | **POST** /login | Login 🔓
[**login_login_unsecured**](LoginApi.md#login_login_unsecured) | **GET** /login | Login 🔓


# **list_login**
> List[str] list_login(list_login_model)

Login 🔓

Request the API token for a couple username / password. WARNING: You should NEVER use this API, like you should never use the similar API that uses the POST method. This will expose your password. To use the APIs, you should instead set an API token to the user you want to allow to use API (This API token called DOLAPIKEY can be found/set on the user page) and use this token as credential for any API call. From the API explorer, you can enter directly the "DOLAPIKEY" into the field at the top right of the page to get access to any allowed APIs.

### Example


```python
import dolibarr_api
from dolibarr_api.models.list_login_model import ListLoginModel
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)


# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.LoginApi(api_client)
    list_login_model = dolibarr_api.ListLoginModel() # ListLoginModel | **login** (required)   **password** (required)   entity   reset   

    try:
        # Login 🔓
        api_response = api_instance.list_login(list_login_model)
        print("The response of LoginApi->list_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->list_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_login_model** | [**ListLoginModel**](ListLoginModel.md)| **login** (required)   **password** (required)   entity   reset    | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Access denied |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_login_unsecured**
> List[str] login_login_unsecured(login, password, entity=entity, reset=reset)

Login 🔓

Request the API token for a couple username / password. WARNING: You should NEVER use this API, like you should never use the similar API that uses the POST method. This will expose your password. To use the APIs, you should instead set an API token to the user you want to allow to use API (This API token called DOLAPIKEY can be found/set on the user page) and use this token as credential for any API call. From the API explorer, you can enter directly the "DOLAPIKEY" into the field at the top right of the page to get access to any allowed APIs.

### Example


```python
import dolibarr_api
from dolibarr_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://dolibarr.codimeo.com/api/index.php
# See configuration.py for a list of all supported configuration parameters.
configuration = dolibarr_api.Configuration(
    host = "http://dolibarr.codimeo.com/api/index.php"
)


# Enter a context with an instance of the API client
with dolibarr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dolibarr_api.LoginApi(api_client)
    login = 'login_example' # str | User login
    password = 'password_example' # str | User password
    entity = 'entity_example' # str | Entity (when multicompany module is used). '' means 1=first company. (optional)
    reset = 56 # int | Reset token (0=get current token, 1=ask a new token and canceled old token. This means access using current existing API token of user will fails: new token will be required for new access) (optional)

    try:
        # Login 🔓
        api_response = api_instance.login_login_unsecured(login, password, entity=entity, reset=reset)
        print("The response of LoginApi->login_login_unsecured:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->login_login_unsecured: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| User login | 
 **password** | **str**| User password | 
 **entity** | **str**| Entity (when multicompany module is used). &#39;&#39; means 1&#x3D;first company. | [optional] 
 **reset** | **int**| Reset token (0&#x3D;get current token, 1&#x3D;ask a new token and canceled old token. This means access using current existing API token of user will fails: new token will be required for new access) | [optional] 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Access denied |  -  |
**500** | System error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

