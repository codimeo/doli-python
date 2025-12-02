# CreateAgendaeventsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_agendaevents_model import CreateAgendaeventsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgendaeventsModel from a JSON string
create_agendaevents_model_instance = CreateAgendaeventsModel.from_json(json)
# print the JSON string representation of the object
print(CreateAgendaeventsModel.to_json())

# convert the object into a dict
create_agendaevents_model_dict = create_agendaevents_model_instance.to_dict()
# create an instance of CreateAgendaeventsModel from a dict
create_agendaevents_model_from_dict = CreateAgendaeventsModel.from_dict(create_agendaevents_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


