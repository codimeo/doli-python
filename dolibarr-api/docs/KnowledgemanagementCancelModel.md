# KnowledgemanagementCancelModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.knowledgemanagement_cancel_model import KnowledgemanagementCancelModel

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgemanagementCancelModel from a JSON string
knowledgemanagement_cancel_model_instance = KnowledgemanagementCancelModel.from_json(json)
# print the JSON string representation of the object
print(KnowledgemanagementCancelModel.to_json())

# convert the object into a dict
knowledgemanagement_cancel_model_dict = knowledgemanagement_cancel_model_instance.to_dict()
# create an instance of KnowledgemanagementCancelModel from a dict
knowledgemanagement_cancel_model_from_dict = KnowledgemanagementCancelModel.from_dict(knowledgemanagement_cancel_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


