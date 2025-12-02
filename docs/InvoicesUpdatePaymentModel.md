# InvoicesUpdatePaymentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_payment** | **str** | Payment number | [optional] 

## Example

```python
from dolibarr_api.models.invoices_update_payment_model import InvoicesUpdatePaymentModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesUpdatePaymentModel from a JSON string
invoices_update_payment_model_instance = InvoicesUpdatePaymentModel.from_json(json)
# print the JSON string representation of the object
print(InvoicesUpdatePaymentModel.to_json())

# convert the object into a dict
invoices_update_payment_model_dict = invoices_update_payment_model_instance.to_dict()
# create an instance of InvoicesUpdatePaymentModel from a dict
invoices_update_payment_model_from_dict = InvoicesUpdatePaymentModel.from_dict(invoices_update_payment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


