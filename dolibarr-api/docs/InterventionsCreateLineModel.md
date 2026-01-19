# InterventionsCreateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.interventions_create_line_model import InterventionsCreateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of InterventionsCreateLineModel from a JSON string
interventions_create_line_model_instance = InterventionsCreateLineModel.from_json(json)
# print the JSON string representation of the object
print(InterventionsCreateLineModel.to_json())

# convert the object into a dict
interventions_create_line_model_dict = interventions_create_line_model_instance.to_dict()
# create an instance of InterventionsCreateLineModel from a dict
interventions_create_line_model_from_dict = InterventionsCreateLineModel.from_dict(interventions_create_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


