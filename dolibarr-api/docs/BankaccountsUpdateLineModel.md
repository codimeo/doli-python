# BankaccountsUpdateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label | 

## Example

```python
from dolibarr_api.models.bankaccounts_update_line_model import BankaccountsUpdateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountsUpdateLineModel from a JSON string
bankaccounts_update_line_model_instance = BankaccountsUpdateLineModel.from_json(json)
# print the JSON string representation of the object
print(BankaccountsUpdateLineModel.to_json())

# convert the object into a dict
bankaccounts_update_line_model_dict = bankaccounts_update_line_model_instance.to_dict()
# create an instance of BankaccountsUpdateLineModel from a dict
bankaccounts_update_line_model_from_dict = BankaccountsUpdateLineModel.from_dict(bankaccounts_update_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


