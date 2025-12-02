# CreateSupplierproposalsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_supplierproposals_model import CreateSupplierproposalsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupplierproposalsModel from a JSON string
create_supplierproposals_model_instance = CreateSupplierproposalsModel.from_json(json)
# print the JSON string representation of the object
print(CreateSupplierproposalsModel.to_json())

# convert the object into a dict
create_supplierproposals_model_dict = create_supplierproposals_model_instance.to_dict()
# create an instance of CreateSupplierproposalsModel from a dict
create_supplierproposals_model_from_dict = CreateSupplierproposalsModel.from_dict(create_supplierproposals_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


