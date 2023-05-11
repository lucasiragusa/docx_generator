import json

def ssim_to_json(ssim_dataframe):
    json_data = ssim_dataframe.to_dict(orient='records')
    return json_data

def save_json_data(json_data, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(json_data, outfile, indent=2)
        