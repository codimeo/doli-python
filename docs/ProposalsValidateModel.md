# ProposalsValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.proposals_validate_model import ProposalsValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProposalsValidateModel from a JSON string
proposals_validate_model_instance = ProposalsValidateModel.from_json(json)
# print the JSON string representation of the object
print(ProposalsValidateModel.to_json())

# convert the object into a dict
proposals_validate_model_dict = proposals_validate_model_instance.to_dict()
# create an instance of ProposalsValidateModel from a dict
proposals_validate_model_from_dict = ProposalsValidateModel.from_dict(proposals_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


