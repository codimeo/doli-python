# ListLoginModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | User login | 
**password** | **str** | User password | 
**entity** | **str** | Entity (when multicompany module is used). &#39;&#39; means 1&#x3D;first company. | [optional] 
**reset** | **int** | Reset token (0&#x3D;get current token, 1&#x3D;ask a new token and canceled old token. This means access using current existing API token of user will fails: new token will be required for new access) | [optional] 

## Example

```python
from dolibarr_api.models.list_login_model import ListLoginModel

# TODO update the JSON string below
json = "{}"
# create an instance of ListLoginModel from a JSON string
list_login_model_instance = ListLoginModel.from_json(json)
# print the JSON string representation of the object
print(ListLoginModel.to_json())

# convert the object into a dict
list_login_model_dict = list_login_model_instance.to_dict()
# create an instance of ListLoginModel from a dict
list_login_model_from_dict = ListLoginModel.from_dict(list_login_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


