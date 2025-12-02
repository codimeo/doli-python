# ProposalsUpdateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Commercial proposal line data | [optional] 

## Example

```python
from dolibarr_api.models.proposals_update_line_model import ProposalsUpdateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProposalsUpdateLineModel from a JSON string
proposals_update_line_model_instance = ProposalsUpdateLineModel.from_json(json)
# print the JSON string representation of the object
print(ProposalsUpdateLineModel.to_json())

# convert the object into a dict
proposals_update_line_model_dict = proposals_update_line_model_instance.to_dict()
# create an instance of ProposalsUpdateLineModel from a dict
proposals_update_line_model_from_dict = ProposalsUpdateLineModel.from_dict(proposals_update_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


