# lead-crm-library/hubspot/utils.py

# TODO utils generic? 
def normalize_lead_data(lead_data, mapping):
    normalized_data = {}
    for key, value in lead_data.items():
        if key in mapping:
            normalized_data[mapping[key]] = value
    return normalized_data