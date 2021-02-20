import pandas, requests, json

#LINK https://coronavirus.data.gov.uk/details/developers-guide#options-responses
data_url = 'https://api.covidtracking.com/v1/us/current.json'

def get_data(api_url):
    """This function returns the data from the given url"""
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else: 
        return None


endpoint = (
    '',
    'filers=',
    'structure='
    
)
data = get_data(data_url)
print(data)