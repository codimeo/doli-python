# EventattendeesUpdateByIdModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.eventattendees_update_by_id_model import EventattendeesUpdateByIdModel

# TODO update the JSON string below
json = "{}"
# create an instance of EventattendeesUpdateByIdModel from a JSON string
eventattendees_update_by_id_model_instance = EventattendeesUpdateByIdModel.from_json(json)
# print the JSON string representation of the object
print(EventattendeesUpdateByIdModel.to_json())

# convert the object into a dict
eventattendees_update_by_id_model_dict = eventattendees_update_by_id_model_instance.to_dict()
# create an instance of EventattendeesUpdateByIdModel from a dict
eventattendees_update_by_id_model_from_dict = EventattendeesUpdateByIdModel.from_dict(eventattendees_update_by_id_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


