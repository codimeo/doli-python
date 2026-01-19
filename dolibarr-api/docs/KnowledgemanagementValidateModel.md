# KnowledgemanagementValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.knowledgemanagement_validate_model import KnowledgemanagementValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgemanagementValidateModel from a JSON string
knowledgemanagement_validate_model_instance = KnowledgemanagementValidateModel.from_json(json)
# print the JSON string representation of the object
print(KnowledgemanagementValidateModel.to_json())

# convert the object into a dict
knowledgemanagement_validate_model_dict = knowledgemanagement_validate_model_instance.to_dict()
# create an instance of KnowledgemanagementValidateModel from a dict
knowledgemanagement_validate_model_from_dict = KnowledgemanagementValidateModel.from_dict(knowledgemanagement_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


