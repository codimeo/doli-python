# Obj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_encoder_function** | **str** |  | 
**number_encoder_function** | **str** |  | 
**fix** | **List[str]** | key value pairs for fixing value types using functions. For example &#39;id&#39;&#x3D;&gt;&#39;intval&#39; will make sure all values of the id properties will be converted to integers intval function &#39;password&#39;&#x3D;&gt; null will remove all the password entries | 
**separator_char** | **str** | character that is used to identify sub objects For example when Object::$separatorChar &#x3D; &#39;.&#39;; array(&#39;my.object&#39;&#x3D;&gt;true) will result in array( &#39;my&#39;&#x3D;&gt;array(&#39;object&#39;&#x3D;&gt;true) ); | 
**remove_empty** | **bool** | set it to true when empty arrays, blank strings, null values to be automatically removed from response | 
**remove_null** | **bool** | set it to true to remove all null values from the result | 

## Example

```python
from dolibarr_api.models.obj import Obj

# TODO update the JSON string below
json = "{}"
# create an instance of Obj from a JSON string
obj_instance = Obj.from_json(json)
# print the JSON string representation of the object
print(Obj.to_json())

# convert the object into a dict
obj_dict = obj_instance.to_dict()
# create an instance of Obj from a dict
obj_from_dict = Obj.from_dict(obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


