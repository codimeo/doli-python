# UpdateContractsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_contracts_model import UpdateContractsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContractsModel from a JSON string
update_contracts_model_instance = UpdateContractsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateContractsModel.to_json())

# convert the object into a dict
update_contracts_model_dict = update_contracts_model_instance.to_dict()
# create an instance of UpdateContractsModel from a dict
update_contracts_model_from_dict = UpdateContractsModel.from_dict(update_contracts_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


