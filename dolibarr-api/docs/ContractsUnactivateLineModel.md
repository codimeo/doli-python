# ContractsUnactivateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datestart** | **str** | Date start | 
**comment** | **str** | Comment | [optional] 

## Example

```python
from dolibarr_api.models.contracts_unactivate_line_model import ContractsUnactivateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of ContractsUnactivateLineModel from a JSON string
contracts_unactivate_line_model_instance = ContractsUnactivateLineModel.from_json(json)
# print the JSON string representation of the object
print(ContractsUnactivateLineModel.to_json())

# convert the object into a dict
contracts_unactivate_line_model_dict = contracts_unactivate_line_model_instance.to_dict()
# create an instance of ContractsUnactivateLineModel from a dict
contracts_unactivate_line_model_from_dict = ContractsUnactivateLineModel.from_dict(contracts_unactivate_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


