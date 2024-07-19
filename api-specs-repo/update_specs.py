import requests
import os

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
specs_dir = "specs"

# Ensure the directory exists
os.makedirs(specs_dir, exist_ok=True)

for name, url in api_specs.items():
    try:
        # Fetch the API specification
        response = requests.get(url)
        response.raise_for_status()
        
        # Save the API specification to a file
        file_path = os.path.join(specs_dir, f"{name}.yaml")
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        print(f"Updated {name} specification.")
    except Exception as e:
        print(f"Failed to update {name}: {e}")

print("All specifications updated.")
