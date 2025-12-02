# UpdateInvoicesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Datas | [optional] 

## Example

```python
from dolibarr_api.models.update_invoices_model import UpdateInvoicesModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInvoicesModel from a JSON string
update_invoices_model_instance = UpdateInvoicesModel.from_json(json)
# print the JSON string representation of the object
print(UpdateInvoicesModel.to_json())

# convert the object into a dict
update_invoices_model_dict = update_invoices_model_instance.to_dict()
# create an instance of UpdateInvoicesModel from a dict
update_invoices_model_from_dict = UpdateInvoicesModel.from_dict(update_invoices_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


