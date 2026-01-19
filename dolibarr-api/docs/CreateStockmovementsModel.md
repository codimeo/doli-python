# CreateStockmovementsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Id product id | 
**warehouse_id** | **int** | Id warehouse | 
**qty** | **float** | Qty to add (Use negative value for a stock decrease) | 
**type** | **int** | Optionally specify the type of movement. 0&#x3D;input (stock increase by a stock transfer), 1&#x3D;output (stock decrease by a stock transfer), 2&#x3D;output (stock decrease), 3&#x3D;input (stock increase). | [optional] 
**lot** | **str** | Lot | [optional] 
**movementcode** | **str** | Movement code | [optional] 
**movementlabel** | **str** | Movement label | [optional] 
**price** | **str** | To update AWP (Average Weighted Price) when you make a stock increase (qty must be higher then 0). | [optional] 
**datem** | **date** | Date of movement | [optional] 
**dlc** | **date** | Eat-by date. | [optional] 
**dluo** | **date** | Sell-by date. | [optional] 
**origin_type** | **str** | Origin type (Element of source object, like &#39;project&#39;, &#39;inventory&#39;, ...) | [optional] 
**origin_id** | **int** | Origin id (Id of source object) | [optional] 

## Example

```python
from dolibarr_api.models.create_stockmovements_model import CreateStockmovementsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStockmovementsModel from a JSON string
create_stockmovements_model_instance = CreateStockmovementsModel.from_json(json)
# print the JSON string representation of the object
print(CreateStockmovementsModel.to_json())

# convert the object into a dict
create_stockmovements_model_dict = create_stockmovements_model_instance.to_dict()
# create an instance of CreateStockmovementsModel from a dict
create_stockmovements_model_from_dict = CreateStockmovementsModel.from_dict(create_stockmovements_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


