# ProposalsCloseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Must be 2 (accepted) or 3 (refused) | 
**note_private** | **str** | Add this mention at end of private note | [optional] 
**notrigger** | **int** | Disabled triggers | [optional] 
**note_public** | **str** | Add this mention at end of public note | [optional] 

## Example

```python
from dolibarr_api.models.proposals_close_model import ProposalsCloseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProposalsCloseModel from a JSON string
proposals_close_model_instance = ProposalsCloseModel.from_json(json)
# print the JSON string representation of the object
print(ProposalsCloseModel.to_json())

# convert the object into a dict
proposals_close_model_dict = proposals_close_model_instance.to_dict()
# create an instance of ProposalsCloseModel from a dict
proposals_close_model_from_dict = ProposalsCloseModel.from_dict(proposals_close_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


