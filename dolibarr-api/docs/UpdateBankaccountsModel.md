# UpdateBankaccountsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | data | [optional] 

## Example

```python
from dolibarr_api.models.update_bankaccounts_model import UpdateBankaccountsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBankaccountsModel from a JSON string
update_bankaccounts_model_instance = UpdateBankaccountsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateBankaccountsModel.to_json())

# convert the object into a dict
update_bankaccounts_model_dict = update_bankaccounts_model_instance.to_dict()
# create an instance of UpdateBankaccountsModel from a dict
update_bankaccounts_model_from_dict = UpdateBankaccountsModel.from_dict(update_bankaccounts_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


