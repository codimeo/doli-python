# ExpensereportsAddPaymentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.expensereports_add_payment_model import ExpensereportsAddPaymentModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExpensereportsAddPaymentModel from a JSON string
expensereports_add_payment_model_instance = ExpensereportsAddPaymentModel.from_json(json)
# print the JSON string representation of the object
print(ExpensereportsAddPaymentModel.to_json())

# convert the object into a dict
expensereports_add_payment_model_dict = expensereports_add_payment_model_instance.to_dict()
# create an instance of ExpensereportsAddPaymentModel from a dict
expensereports_add_payment_model_from_dict = ExpensereportsAddPaymentModel.from_dict(expensereports_add_payment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


