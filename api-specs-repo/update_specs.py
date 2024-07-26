import requests
import os
import json
from pathlib import Path
import yaml

# Define API specification URLs
api_specs = {
    "HeavyBid Estimate Insights": "https://api.redocly.com/registry/bundle/hcss-64o/heavybid/v2/openapi.yaml?branch=main",
    "HeavyBid Pre-Construction": "https://api.redocly.com/registry/bundle/hcss-64o/precon/v1/openapi.yaml?branch=main",
    "HeavyJob": "https://api.redocly.com/registry/bundle/hcss-64o/heavyjob/v1/openapi.yaml?branch=main",
    "HCSS Safety": "https://api.redocly.com/registry/bundle/hcss-64o/safety/v1/openapi.yaml?branch=main",
    "HCSS Skills": "https://api.redocly.com/registry/bundle/hcss-64o/skills%2Fapi/v1/openapi.yaml?branch=main",
    "Equipment360": "https://api.redocly.com/registry/bundle/hcss-64o/e360/v1/openapi.yaml?branch=main",
    "HCSS Telematics": "https://api.redocly.com/registry/bundle/hcss-64o/telematics/v1/openapi.yaml?branch=main",
    "Identity": "https://api.redocly.com/registry/bundle/hcss-64o/identity/v1/openapi.yaml?branch=main",
    "Setups": "https://api.redocly.com/registry/bundle/hcss-64o/setups/v1/openapi.yaml?branch=main",
    "Users": "https://api.redocly.com/registry/bundle/hcss-64o/users/v1/openapi.yaml?branch=main",
    "Webhooks": "https://api.redocly.com/registry/bundle/hcss-64o/webhooks/v1/openapi.yaml?branch=main",
    "Attachments": "https://api.redocly.com/registry/bundle/hcss-64o/attachments/1/openapi.yaml?branch=main",
    "Contacts": "https://api.redocly.com/registry/bundle/hcss-64o/contacts/1.0/openapi.yaml?branch=main",
    # Add other API URLs here
}

# Directory to save the fetched specs
specs_dir = "api-specs-repo/specs"
json_dir = "api-specs-repo/json"
# File to store ETags
etag_file = "api-specs-repo/etags.json"

# Ensure the directories exist
os.makedirs(specs_dir, exist_ok=True)
os.makedirs(json_dir, exist_ok=True)

# Load existing ETags from file
if os.path.exists(etag_file):
    with open(etag_file, "r") as f:
        etags = json.load(f)
else:
    etags = {}

# Create a dictionary to store the endpoints
endpoints = {}

for name, url in api_specs.items():
    try:
        # Get the last known ETag
        last_etag = etags.get(name)
        
        # Fetch the API specification with headers to get ETag
        headers = {}
        if last_etag:
            headers['If-None-Match'] = last_etag
        response = requests.get(url, headers=headers)
        
        # Check if the content has changed
        if response.status_code == 304:
            print(f"No changes for {name}.")
            continue
        
        response.raise_for_status()
        
        # Save the new ETag
        new_etag = response.headers.get('ETag')
        if new_etag:
            etags[name] = new_etag
        
        # Save the API specification to a file
        file_path = os.path.join(specs_dir, f"{name}.yaml")
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        # Parse the OpenAPI YAML file
        with open(file_path, "r") as file:
            openapi_yaml = yaml.safe_load(file)

        # Save the JSON version of the API specification to a file
        json_file_path = os.path.join(json_dir, f"{name}.json")
        with open(json_file_path, "w") as file:
            json.dump(openapi_yaml, file, indent=4)

        # Extract the endpoints
        for path, methods in openapi_yaml["paths"].items():
            for method, _ in methods.items():
                endpoint = f"{method.upper()} {path}"
                if name not in endpoints:
                    endpoints[name] = {}
                if method.upper() not in endpoints[name]:
                    endpoints[name][method.upper()] = []
                
                                # Construct the full URL
                if 'openapi' in openapi_yaml:
                    # OpenAPI 3.0
                    if 'servers' in openapi_yaml:
                        server_url = openapi_yaml['servers'][0]['url']
                    else:
                        server_url = ''
                else:
                    # OpenAPI 2.0
                    server_url = openapi_yaml['host'] + openapi_yaml['basePath']

                full_url = server_url + path.replace('{', '{{').replace('}', '}}')
                endpoints[name][method.upper()].append(full_url)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {name}: {e}")

# Save the ETags to a file
with open(etag_file, "w") as f:
    json.dump(etags, f, indent=4)

# Save the endpoints to a file
with open("endpoints.json", "w") as f:
    json.dump(endpoints, f, indent=4)