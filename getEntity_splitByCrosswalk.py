import requests

# Function to fetch entity from Reltio API
def fetch_entity(entity_id, api_key):
    url = f"https://<your_reltio_instance>/entities/{entity_id}"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch entity. Status code: {response.status_code}")
        return None

# Function to split attributes by crosswalks
def split_attributes_by_crosswalks(entity):
    attributes_by_crosswalks = {}
    attributes = entity.get("attributes", {})
    for attribute, value in attributes.items():
        crosswalks = value.get("crosswalks", [])
        for crosswalk in crosswalks:
            crosswalk_type = crosswalk["crosswalkType"]
            if crosswalk_type not in attributes_by_crosswalks:
                attributes_by_crosswalks[crosswalk_type] = {}
            attributes_by_crosswalks[crosswalk_type][attribute] = value["value"]
    return attributes_by_crosswalks

# Main function
def main():
    # Replace with your Reltio API key and entity ID
    api_key = "<your_api_key>"
    entity_id = "<your_entity_id>"

    # Fetch entity from Reltio API
    entity = fetch_entity(entity_id, api_key)
    if entity:
        # Split attributes by crosswalks
        attributes_by_crosswalks = split_attributes_by_crosswalks(entity)
        # Print attributes grouped by crosswalks
        for crosswalk_type, attributes in attributes_by_crosswalks.items():
            print(f"Crosswalk Type: {crosswalk_type}")
            for attribute, value in attributes.items():
                print(f"{attribute}: {value}")
            print()

if __name__ == "__main__":
    main()
