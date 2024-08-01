import os
import json

def ensure_directories_exist(*dirs):
    """Ensure that directories exist."""
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)

def load_etags(etag_file):
    """Load existing ETags from file."""
    if os.path.exists(etag_file):
        with open(etag_file, "r") as f:
            return json.load(f)
    return {}

def save_etags(etag_file, etags):
    """Save the ETags to a file."""
    with open(etag_file, "w") as f:
        json.dump(etags, f, indent=4)

def save_endpoints(file_path, endpoints):
    """Save the endpoints to a file."""
    with open(file_path, "w") as f:
        json.dump(endpoints, f, indent=4)
