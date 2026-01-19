# InvoicesAddPaymentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datepaye** | **str** | Payment date | 
**paymentid** | **int** | Payment mode Id | 
**closepaidinvoices** | **str** | Close paid invoices | 
**accountid** | **int** | Account Id | 
**num_payment** | **str** | Payment number (optional) | [optional] 
**comment** | **str** | Note private (optional) | [optional] 
**chqemetteur** | **str** | Payment issuer (mandatory if paymentcode &#x3D; &#39;CHQ&#39;) | [optional] 
**chqbank** | **str** | Issuer bank name (optional) | [optional] 

## Example

```python
from dolibarr_api.models.invoices_add_payment_model import InvoicesAddPaymentModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesAddPaymentModel from a JSON string
invoices_add_payment_model_instance = InvoicesAddPaymentModel.from_json(json)
# print the JSON string representation of the object
print(InvoicesAddPaymentModel.to_json())

# convert the object into a dict
invoices_add_payment_model_dict = invoices_add_payment_model_instance.to_dict()
# create an instance of InvoicesAddPaymentModel from a dict
invoices_add_payment_model_from_dict = InvoicesAddPaymentModel.from_dict(invoices_add_payment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


