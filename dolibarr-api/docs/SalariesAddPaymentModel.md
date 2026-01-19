# SalariesAddPaymentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.salaries_add_payment_model import SalariesAddPaymentModel

# TODO update the JSON string below
json = "{}"
# create an instance of SalariesAddPaymentModel from a JSON string
salaries_add_payment_model_instance = SalariesAddPaymentModel.from_json(json)
# print the JSON string representation of the object
print(SalariesAddPaymentModel.to_json())

# convert the object into a dict
salaries_add_payment_model_dict = salaries_add_payment_model_instance.to_dict()
# create an instance of SalariesAddPaymentModel from a dict
salaries_add_payment_model_from_dict = SalariesAddPaymentModel.from_dict(salaries_add_payment_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


