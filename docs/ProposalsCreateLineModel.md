# ProposalsCreateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Commercial proposal line data | [optional] 

## Example

```python
from dolibarr_api.models.proposals_create_line_model import ProposalsCreateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProposalsCreateLineModel from a JSON string
proposals_create_line_model_instance = ProposalsCreateLineModel.from_json(json)
# print the JSON string representation of the object
print(ProposalsCreateLineModel.to_json())

# convert the object into a dict
proposals_create_line_model_dict = proposals_create_line_model_instance.to_dict()
# create an instance of ProposalsCreateLineModel from a dict
proposals_create_line_model_from_dict = ProposalsCreateLineModel.from_dict(proposals_create_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


