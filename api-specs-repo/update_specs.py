import os
import yaml
import json
from pathlib import Path
import requests
from utils.fetch_specs import fetch_and_save_specs
from utils.extract_endpoints import extract_endpoints_from_file
from utils.utils import ensure_directories_exist, load_etags, save_etags, save_endpoints

# Load API URLs from YAML file
with open("api_urls.yaml", "r") as file:
    api_specs = yaml.safe_load(file)

# Directory to save the fetched specs
specs_dir = "api-specs-repo/specs"
json_dir = "api-specs-repo/json"
etag_file = "api-specs-repo/etags.json"

# Ensure the directories exist
ensure_directories_exist(specs_dir, json_dir)

# Load existing ETags from file
etags = load_etags(etag_file)

# Create a dictionary to store the endpoints
endpoints = {}

# Fetch and save API specifications, then extract endpoints
for name, base_url in api_specs.items():
    try:
        # Fetch YAML and JSON files
        yaml_url = f"{base_url}.yaml?branch=main"
        json_url = f"{base_url}.json?branch=main"
        
        # Fetch and save YAML specification
        yaml_file_path = fetch_and_save_specs(yaml_url, name + "_yaml", specs_dir, etag_file, etags)
        
        # Fetch and save JSON specification
        json_file_path = fetch_and_save_specs(json_url, name + "_json", json_dir, etag_file, etags)

        # Extract endpoints from the JSON file
        extract_endpoints_from_file(json_file_path, name, endpoints)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {name}: {e}")

# Save the ETags to a file
save_etags(etag_file, etags)

# Save the endpoints to a file after processing all files
save_endpoints("endpoints.json", endpoints)
