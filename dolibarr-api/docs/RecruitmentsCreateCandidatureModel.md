# RecruitmentsCreateCandidatureModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.recruitments_create_candidature_model import RecruitmentsCreateCandidatureModel

# TODO update the JSON string below
json = "{}"
# create an instance of RecruitmentsCreateCandidatureModel from a JSON string
recruitments_create_candidature_model_instance = RecruitmentsCreateCandidatureModel.from_json(json)
# print the JSON string representation of the object
print(RecruitmentsCreateCandidatureModel.to_json())

# convert the object into a dict
recruitments_create_candidature_model_dict = recruitments_create_candidature_model_instance.to_dict()
# create an instance of RecruitmentsCreateCandidatureModel from a dict
recruitments_create_candidature_model_from_dict = RecruitmentsCreateCandidatureModel.from_dict(recruitments_create_candidature_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


