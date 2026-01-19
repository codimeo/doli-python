# UpdateAgendaeventsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_agendaevents_model import UpdateAgendaeventsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgendaeventsModel from a JSON string
update_agendaevents_model_instance = UpdateAgendaeventsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateAgendaeventsModel.to_json())

# convert the object into a dict
update_agendaevents_model_dict = update_agendaevents_model_instance.to_dict()
# create an instance of UpdateAgendaeventsModel from a dict
update_agendaevents_model_from_dict = UpdateAgendaeventsModel.from_dict(update_agendaevents_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


