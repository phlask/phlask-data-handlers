import json
import sys
import os

from jsonschema import Draft202012Validator, ValidationError

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the project root directory to the Python path
sys.path.append(project_root)

from admin.admin_classes import prodAdmin

schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "access": {"type": "string"},
        "address": {"type": "string"},
        "city": {"type": "string"},
        "description": {"type": "string"},
        "filtration": {"type": "string"},
        "gp_id": {"type": "string"},
        "handicap": {"type": "string"},
        "hours": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "close": {
                        "type": "object",
                        "properties": {
                            "day": {"type": "integer", "minimum": 0, "maximum": 6},
                            "time": {"type": "string", "pattern": "\\d{4}"}
                        },
                        "required": ["day", "time"]
                    },
                    "open": {
                        "type": "object",
                        "properties": {
                            "day": {"type": "integer", "minimum": 0, "maximum": 6},
                            "time": {"type": "string", "pattern": "\\d{4}"}
                        },
                        "required": ["day", "time"]
                    }
                },
                "required": ["close", "open"]
            },
            "minItems": 7,
            "maxItems": 7
        },
        "lat": {"type": "number"},
        "lon": {"type": "number"},
        "norms_rules": {"type": "string"},
        "organization": {"type": "string"},
        "permanently_closed": {"type": "boolean"},
        "phone": {"type": "string"},
        "quality": {"type": "string"},
        "service": {"type": "string"},
        "statement": {"type": "string"},
        "status": {"type": "string"},
        "tap_type": {"type": "string"},
        "tapnum": {"type": "integer"},
        "vessel": {"type": "string"},
        "zip_code": {"type": "number"}
    },
    # I have take hours out of the required list because it is not required in all cases
    "required": [
        "access", "address", "city", "description", "filtration", "gp_id", "handicap", "lat", "lon",
        "norms_rules", "organization", "permanently_closed", "phone", "quality", "service", "statement",
        "status", "tap_type", "tapnum", "vessel", "zip_code"
    ]
}
#  Use the Draft202012Validator class to validate the schema
Draft202012Validator.check_schema(schema)

#  Create a validator instance
draft_202012_validator = Draft202012Validator(schema)

#  Create a valid data instance
water_prod = prodAdmin().water_db_live
invalid_data = prodAdmin().getTap(water_prod, 263)

# Valid data will actually throw an error because the zip_code field is missing from the data instance
valid_data = prodAdmin().getTap(water_prod, 1)

log_file_path = "./misc_scripts/schema_errors.log"

print("Log file path:", log_file_path)

import datetime

try:
    draft_202012_validator.validate(invalid_data)
    print("Data is valid.")
    # passes all of the tests
except ValidationError as e:
    print("Data is invalid.")
    try:
        # Log the schema errors to a file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"Validation Error:\n{str(e)}\n"
        schema_message = f"Schema:\n{json.dumps(schema, indent=4)}\n"
        log_entry = f"{timestamp}\n{error_message}\n{schema_message}\n"
        
        with open(log_file_path, "a") as log_file:
            log_file.write(log_entry)
        
        print("Schema errors logged successfully.")
    except Exception as ex:
        print("Error writing to log file:", ex)

