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
# File to store ETags
etag_file = "api-specs-repo/etags.json"

# Ensure the directory exists
os.makedirs(specs_dir, exist_ok=True)

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
                    # OpenAPI format
                    server_url = openapi_yaml['servers'][0]['url']
                    full_url = server_url + path
                elif 'swagger' in openapi_yaml:
                    # Swagger format
                    host = openapi_yaml['host']
                    base_path = openapi_yaml.get('basePath', '')
                    scheme = openapi_yaml['schemes'][0]
                    full_url = f"{scheme}://{host}{base_path}{path}"
                else:
                    raise ValueError(f"Unknown format for {name}")

                endpoints[name][method.upper()].append(full_url)

        print(f"Updated {name} specification.")

    except Exception as e:
        print(f"Failed to update {name}: {e}")

# Save updated ETags to file
with open(etag_file, "w") as f:
    json.dump(etags, f)

# Create the Markdown file
markdown_file = Path("Endpoints.md")
if not markdown_file.exists() or len(endpoints) > 0:
    with open("Endpoints.md", "w") as f:
        for name, methods in endpoints.items():
            f.write(f"### {name}\n")
            for method, urls in methods.items():
                f.write(f"#### {method}\n")
                for url in urls:
                    f.write(f"* {url}\n")
            f.write("\n")
    print("Endpoints.md file updated.")
else:
    print("No changes to Endpoints.md file.")