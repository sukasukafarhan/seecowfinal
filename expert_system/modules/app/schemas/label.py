from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

label_schema = {
    "type": "object",
    "properties": {
        "namaLabel": {
            "type": "string",
        },
        "attribute": {
            "type": "array",
            "items": {
                "type":"string"
            },
            "minItems": 1,
            "uniqueItems": true
        },
        "labelIdentity": {
            "type": "number"
        }
    },
    "required": ["namaLabel", "attribute","labelIdentity"],
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