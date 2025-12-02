# CreateInvoicesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_invoices_model import CreateInvoicesModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvoicesModel from a JSON string
create_invoices_model_instance = CreateInvoicesModel.from_json(json)
# print the JSON string representation of the object
print(CreateInvoicesModel.to_json())

# convert the object into a dict
create_invoices_model_dict = create_invoices_model_instance.to_dict()
# create an instance of CreateInvoicesModel from a dict
create_invoices_model_from_dict = CreateInvoicesModel.from_dict(create_invoices_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


