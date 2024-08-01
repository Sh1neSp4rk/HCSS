import requests
import os

def fetch_and_save_specs(url, name, dir_path, etag_file, etags):
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
        return None
    
    response.raise_for_status()
    
    # Save the new ETag
    new_etag = response.headers.get('ETag')
    if new_etag:
        etags[name] = new_etag
    
    # Save the API specification to a file
    file_path = os.path.join(dir_path, f"{name}.yaml" if url.endswith(".yaml") else f"{name}.json")
    with open(file_path, "wb") as file:
        file.write(response.content)
    
    return file_path
