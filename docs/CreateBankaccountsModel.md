# CreateBankaccountsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_bankaccounts_model import CreateBankaccountsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBankaccountsModel from a JSON string
create_bankaccounts_model_instance = CreateBankaccountsModel.from_json(json)
# print the JSON string representation of the object
print(CreateBankaccountsModel.to_json())

# convert the object into a dict
create_bankaccounts_model_dict = create_bankaccounts_model_instance.to_dict()
# create an instance of CreateBankaccountsModel from a dict
create_bankaccounts_model_from_dict = CreateBankaccountsModel.from_dict(create_bankaccounts_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


