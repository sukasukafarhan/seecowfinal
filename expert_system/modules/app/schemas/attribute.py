from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

attribute_schema = {
    "type": "object",
    "properties": {
        "namaAttribute": {
            "type": "string",
        },
        "attributeIdentity": {
            "type": "number"
        }
    },
    "required": ["namaAttribute","attributeIdentity"],
    "additionalProperties": False
}


def validate_label(data):
    try:
        validate(data, label_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}