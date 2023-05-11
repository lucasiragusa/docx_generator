import json
import jsonschema
from jsonschema import validate

def load_json_schema(schema_path):
    """
    Load JSON schema from a file.
    """
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    return schema

def validate_json_data(json_data, schema):
    """
    Validate JSON data against a given JSON schema.
    """
    try:
        validate(instance=json_data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"JSON data validation error: {e}")
        return False

def save_json_data(json_data, file_path):
    """
    Save JSON data to a file.
    """
    with open(file_path, 'w') as f:
        json.dump(json_data, f, indent=2)
