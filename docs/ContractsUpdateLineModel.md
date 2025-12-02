# ContractsUpdateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Contractline data | [optional] 

## Example

```python
from dolibarr_api.models.contracts_update_line_model import ContractsUpdateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of ContractsUpdateLineModel from a JSON string
contracts_update_line_model_instance = ContractsUpdateLineModel.from_json(json)
# print the JSON string representation of the object
print(ContractsUpdateLineModel.to_json())

# convert the object into a dict
contracts_update_line_model_dict = contracts_update_line_model_instance.to_dict()
# create an instance of ContractsUpdateLineModel from a dict
contracts_update_line_model_from_dict = ContractsUpdateLineModel.from_dict(contracts_update_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


