# InterventionsValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.interventions_validate_model import InterventionsValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of InterventionsValidateModel from a JSON string
interventions_validate_model_instance = InterventionsValidateModel.from_json(json)
# print the JSON string representation of the object
print(InterventionsValidateModel.to_json())

# convert the object into a dict
interventions_validate_model_dict = interventions_validate_model_instance.to_dict()
# create an instance of InterventionsValidateModel from a dict
interventions_validate_model_from_dict = InterventionsValidateModel.from_dict(interventions_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


