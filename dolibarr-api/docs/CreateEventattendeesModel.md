# CreateEventattendeesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_eventattendees_model import CreateEventattendeesModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventattendeesModel from a JSON string
create_eventattendees_model_instance = CreateEventattendeesModel.from_json(json)
# print the JSON string representation of the object
print(CreateEventattendeesModel.to_json())

# convert the object into a dict
create_eventattendees_model_dict = create_eventattendees_model_instance.to_dict()
# create an instance of CreateEventattendeesModel from a dict
create_eventattendees_model_from_dict = CreateEventattendeesModel.from_dict(create_eventattendees_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


