# CreateContractsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_contracts_model import CreateContractsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractsModel from a JSON string
create_contracts_model_instance = CreateContractsModel.from_json(json)
# print the JSON string representation of the object
print(CreateContractsModel.to_json())

# convert the object into a dict
create_contracts_model_dict = create_contracts_model_instance.to_dict()
# create an instance of CreateContractsModel from a dict
create_contracts_model_from_dict = CreateContractsModel.from_dict(create_contracts_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


