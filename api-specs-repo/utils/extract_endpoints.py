import yaml
import json
from urllib.parse import urlparse

def extract_endpoints_from_file(file_path, name, endpoints):
    """Extract and structure endpoints from the OpenAPI YAML file."""
    try:
        # Parse the OpenAPI YAML file
        with open(file_path, "r") as file:
            openapi_yaml = yaml.safe_load(file)
        
        # Determine the base URL
        base_url = ''
        if 'openapi' in openapi_yaml:
            if 'servers' in openapi_yaml and openapi_yaml['servers']:
                base_url = urlparse(openapi_yaml['servers'][0]['url']).netloc
                base_url = f"https://{base_url}/"
        elif 'swagger' in openapi_yaml:
            base_url = urlparse(f"{openapi_yaml['schemes'][0]}://{openapi_yaml['host']}").netloc
            base_url = f"https://{base_url}/"

        # Initialize structure for endpoints
        if name not in endpoints:
            endpoints[name] = {"base": base_url}

        # Extract and group by version and methods
        for path, methods in openapi_yaml.get("paths", {}).items():
            path_parts = path.strip('/').split('/')
            if len(path_parts) > 2:
                version = path_parts[1]  # Extract version from the path
                if version not in endpoints[name]:
                    endpoints[name][version] = {"base": version + "/", "GET": [], "PUT": [], "POST": [], "DELETE": [], "PATCH": []}
                
                # Construct the endpoint path
                path = '/'.join(path_parts[2:])  # Remove base path
                for method, _ in methods.items():
                    if method.upper() not in endpoints[name][version]:
                        endpoints[name][version][method.upper()] = []
                    endpoints[name][version][method.upper()].append(path)
        
    except Exception as e:
        print(f"Error processing {name}: {e}")
