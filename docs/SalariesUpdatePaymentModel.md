# SalariesUpdatePaymentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | data | [optional] 

## Example

```python
from dolibarr_api.models.salaries_update_payment_model import SalariesUpdatePaymentModel

# TODO update the JSON string below
json = "{}"
# create an instance of SalariesUpdatePaymentModel from a JSON string
salaries_update_payment_model_instance = SalariesUpdatePaymentModel.from_json(json)
# print the JSON string representation of the object
print(SalariesUpdatePaymentModel.to_json())

# convert the object into a dict
salaries_update_payment_model_dict = salaries_update_payment_model_instance.to_dict()
# create an instance of SalariesUpdatePaymentModel from a dict
salaries_update_payment_model_from_dict = SalariesUpdatePaymentModel.from_dict(salaries_update_payment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


