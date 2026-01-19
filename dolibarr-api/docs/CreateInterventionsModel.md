# CreateInterventionsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_interventions_model import CreateInterventionsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInterventionsModel from a JSON string
create_interventions_model_instance = CreateInterventionsModel.from_json(json)
# print the JSON string representation of the object
print(CreateInterventionsModel.to_json())

# convert the object into a dict
create_interventions_model_dict = create_interventions_model_instance.to_dict()
# create an instance of CreateInterventionsModel from a dict
create_interventions_model_from_dict = CreateInterventionsModel.from_dict(create_interventions_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


