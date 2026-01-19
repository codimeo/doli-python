# SupplierinvoicesAddPaymentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datepaye** | **str** | Payment date | 
**payment_mode_id** | **int** | Payment mode ID (look it up via REST GET to /setup/dictionary/payment_types) | 
**closepaidinvoices** | **str** | Close paid invoices | 
**accountid** | **int** | Bank account ID (look it up via REST GET to /bankaccounts) | 
**num_payment** | **str** | Payment number (optional) | [optional] 
**comment** | **str** | Note (optional) | [optional] 
**chqemetteur** | **str** | Payment issuer (mandatory if payment_mode_id corresponds to &#39;CHQ&#39;-payment type) | [optional] 
**chqbank** | **str** | Issuer bank name (optional) | [optional] 
**amount** | **float** | Amount of payment if we don&#39;t want to use the remain to pay | [optional] 

## Example

```python
from dolibarr_api.models.supplierinvoices_add_payment_model import SupplierinvoicesAddPaymentModel

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierinvoicesAddPaymentModel from a JSON string
supplierinvoices_add_payment_model_instance = SupplierinvoicesAddPaymentModel.from_json(json)
# print the JSON string representation of the object
print(SupplierinvoicesAddPaymentModel.to_json())

# convert the object into a dict
supplierinvoices_add_payment_model_dict = supplierinvoices_add_payment_model_instance.to_dict()
# create an instance of SupplierinvoicesAddPaymentModel from a dict
supplierinvoices_add_payment_model_from_dict = SupplierinvoicesAddPaymentModel.from_dict(supplierinvoices_add_payment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


