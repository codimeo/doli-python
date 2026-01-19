# ContractsCreateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Contractline data | [optional] 

## Example

```python
from dolibarr_api.models.contracts_create_line_model import ContractsCreateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of ContractsCreateLineModel from a JSON string
contracts_create_line_model_instance = ContractsCreateLineModel.from_json(json)
# print the JSON string representation of the object
print(ContractsCreateLineModel.to_json())

# convert the object into a dict
contracts_create_line_model_dict = contracts_create_line_model_instance.to_dict()
# create an instance of ContractsCreateLineModel from a dict
contracts_create_line_model_from_dict = ContractsCreateLineModel.from_dict(contracts_create_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


