import yaml

# Replace 'openapi.yaml' with the path to your OpenAPI Specification file
file_path = 'openapi.yaml'

try:
    # Load the OpenAPI Specification from a YAML file
    with open(file_path, 'a+') as file:
        openapi_spec = yaml.safe_load(file)

    # Check if the loaded data is not None
    if openapi_spec is not None and isinstance(openapi_spec, dict):
        # Extract and print the OpenAPI version
        openapi_version = openapi_spec.get('openapi')
        if openapi_version is not None:
            print(f"OpenAPI Version: {openapi_version}")
        else:
            print("Error: 'openapi' field not found in the document.")
    else:
        print("Error: Unable to load the YAML file or it does not contain a valid dictionary structure.")

except Exception as e:
    print(f"Error: {e}")
