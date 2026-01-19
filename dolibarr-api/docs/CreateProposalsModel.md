# CreateProposalsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_proposals_model import CreateProposalsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProposalsModel from a JSON string
create_proposals_model_instance = CreateProposalsModel.from_json(json)
# print the JSON string representation of the object
print(CreateProposalsModel.to_json())

# convert the object into a dict
create_proposals_model_dict = create_proposals_model_instance.to_dict()
# create an instance of CreateProposalsModel from a dict
create_proposals_model_from_dict = CreateProposalsModel.from_dict(create_proposals_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


