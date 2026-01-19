# ExpensereportsUpdatePaymentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | data | [optional] 

## Example

```python
from dolibarr_api.models.expensereports_update_payment_model import ExpensereportsUpdatePaymentModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExpensereportsUpdatePaymentModel from a JSON string
expensereports_update_payment_model_instance = ExpensereportsUpdatePaymentModel.from_json(json)
# print the JSON string representation of the object
print(ExpensereportsUpdatePaymentModel.to_json())

# convert the object into a dict
expensereports_update_payment_model_dict = expensereports_update_payment_model_instance.to_dict()
# create an instance of ExpensereportsUpdatePaymentModel from a dict
expensereports_update_payment_model_from_dict = ExpensereportsUpdatePaymentModel.from_dict(expensereports_update_payment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


