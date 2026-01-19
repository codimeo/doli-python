# dolibarr_api.AccountancyApi

All URIs are relative to *http://dolibarr.codimeo.com/api/index.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountancy_export_data**](AccountancyApi.md#accountancy_export_data) | **GET** /accountancy/exportdata | Accountancy export data 🔐


# **accountancy_export_data**
> str accountancy_export_data(period, date_min=date_min, date_max=date_max, format=format, lettering=lettering, alreadyexport=alreadyexport, notnotifiedasexport=notnotifiedasexport)

Accountancy export data 🔐

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
    api_instance = dolibarr_api.AccountancyApi(api_client)
    period = 'period_example' # str | Period : 'lastmonth', 'currentmonth', 'last3months', 'last6months', 'currentyear', 'lastyear', 'fiscalyear', 'lastfiscalyear', 'actualandlastfiscalyear' or 'custom' (see above)
    date_min = 'date_min_example' # str | [=''] Start date of period if 'custom' is set in period parameter Date format is 'YYYY-MM-DD' (optional)
    date_max = 'date_max_example' # str | [=''] End date of period if 'custom' is set in period parameter Date format is 'YYYY-MM-DD' (optional)
    format = 'format_example' # str | [=''] by default uses '1' for 'Configurable (CSV)' for format number or '1000' for FEC or '1010' for FEC2 (see AccountancyExport class) (optional)
    lettering = 56 # int | [=0] by default don't export or 1 to export lettering data (columns 'letterring_code' and 'date_lettering' returns empty or not) (optional)
    alreadyexport = 56 # int | [=0] by default export data only if it's not yet exported or 1 already exported (always export data even if 'date_export\" is set) (optional)
    notnotifiedasexport = 56 # int | [=0] by default notified as exported or 1 not notified as exported (when the export is done, notified or not the column 'date_export') (optional)

    try:
        # Accountancy export data 🔐
        api_response = api_instance.accountancy_export_data(period, date_min=date_min, date_max=date_max, format=format, lettering=lettering, alreadyexport=alreadyexport, notnotifiedasexport=notnotifiedasexport)
        print("The response of AccountancyApi->accountancy_export_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountancyApi->accountancy_export_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Period : &#39;lastmonth&#39;, &#39;currentmonth&#39;, &#39;last3months&#39;, &#39;last6months&#39;, &#39;currentyear&#39;, &#39;lastyear&#39;, &#39;fiscalyear&#39;, &#39;lastfiscalyear&#39;, &#39;actualandlastfiscalyear&#39; or &#39;custom&#39; (see above) | 
 **date_min** | **str**| [&#x3D;&#39;&#39;] Start date of period if &#39;custom&#39; is set in period parameter Date format is &#39;YYYY-MM-DD&#39; | [optional] 
 **date_max** | **str**| [&#x3D;&#39;&#39;] End date of period if &#39;custom&#39; is set in period parameter Date format is &#39;YYYY-MM-DD&#39; | [optional] 
 **format** | **str**| [&#x3D;&#39;&#39;] by default uses &#39;1&#39; for &#39;Configurable (CSV)&#39; for format number or &#39;1000&#39; for FEC or &#39;1010&#39; for FEC2 (see AccountancyExport class) | [optional] 
 **lettering** | **int**| [&#x3D;0] by default don&#39;t export or 1 to export lettering data (columns &#39;letterring_code&#39; and &#39;date_lettering&#39; returns empty or not) | [optional] 
 **alreadyexport** | **int**| [&#x3D;0] by default export data only if it&#39;s not yet exported or 1 already exported (always export data even if &#39;date_export\&quot; is set) | [optional] 
 **notnotifiedasexport** | **int**| [&#x3D;0] by default notified as exported or 1 not notified as exported (when the export is done, notified or not the column &#39;date_export&#39;) | [optional] 

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
**401** | Insufficient rights |  -  |
**404** | Accountancy export format not found |  -  |
**500** | Error on accountancy export |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

