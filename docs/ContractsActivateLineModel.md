# ContractsActivateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datestart** | **str** | Date start | 
**dateend** | **str** | Date end | [optional] 
**comment** | **str** | Comment | [optional] 

## Example

```python
from dolibarr_api.models.contracts_activate_line_model import ContractsActivateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of ContractsActivateLineModel from a JSON string
contracts_activate_line_model_instance = ContractsActivateLineModel.from_json(json)
# print the JSON string representation of the object
print(ContractsActivateLineModel.to_json())

# convert the object into a dict
contracts_activate_line_model_dict = contracts_activate_line_model_instance.to_dict()
# create an instance of ContractsActivateLineModel from a dict
contracts_activate_line_model_from_dict = ContractsActivateLineModel.from_dict(contracts_activate_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


