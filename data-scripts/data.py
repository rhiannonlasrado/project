#API LINK https://coronavirus.data.gov.uk/details/developers-guide
#Helpful for terminology: https://www.gov.uk/government/publications/coronavirus-covid-19-testing-data-methodology/covid-19-testing-data-methodology-note

import pandas as pd, requests, json
from urllib.parse import urlencode

area_types = ['overview','nation','region','nhsRegion','utla','ltla']

def create_query_string_params(area_type="nation", area_name="england"):
    """This function returns the query string parameters for the coronavirus.data.gov.uk base api"""
        
    AREA_TYPE = "nation"
    AREA_NAME = "england"

    filters = [
        f"areaType={ AREA_TYPE }",
        f"areaName={ AREA_NAME }"
    ]

    structure = {
        "date": "date", #YYYY-MM-DD
        "name": "areaName",
        "code": "areaCode",
        "cases": {
            "daily": "newCasesByPublishDate",
            "cumulative": "cumCasesByPublishDate"
        },
        "deaths": {
            "daily": "newDeathsByDeathDate",
            "cumulative": "cumDeathsByDeathDate"
        },
        "vaccines" : {
            "weekly2nddose": "weeklyPeopleVaccinatedSecondDoseByVaccinationDate",
            "weekly1stdose": "weeklyPeopleVaccinatedFirstDoseByVaccinationDate",
            "cum1stdose": "cumPeopleVaccinatedFirstDoseByVaccinationDate",
            "cum2nddose": "cumPeopleVaccinatedSecondDoseByVaccinationDate"
        }
    }

    api_params = {
        "filters": str.join(";", filters),
        "structure": json.dumps(structure, separators=(",", ":"))
    }

    encoded_params = urlencode(api_params)

    query_string_parameters = (f"/v1/data?{ encoded_params }")
    
    return query_string_parameters

def get_data(url):
    """This function returns the data from the given url and returns a dictionary"""
    response = requests.get(url)
    
    if response.status_code == 200: #code 200 = success
        return json.loads(response.content.decode('utf-8'))
    else: 
        return None
    
def format_data():
    API_base = 'https://api.coronavirus.data.gov.uk'
    query_str_params = create_query_string_params() #default is Nation, England 
    full_url = API_base + query_str_params
    print(full_url) #for debugging
    
    data = get_data(full_url) #get data from api - returns a dictionary
    df = pd.DataFrame.from_dict(data['data'])  #create dataframe
    
    #pull out dictionary into two columns
    cases = df['cases'].apply(pd.Series)
    deaths = df['deaths'].apply(pd.Series)
    
    #rename columns
    cases.columns= ['cases_daily','cases_cumulative']
    deaths.columns = ['deaths_daily', 'deaths_cumulative']  
    #####come back and unpack vaccines if you get time - need to fix data grab from API####
    
    
    df = df.drop(['cases', 'deaths', 'vaccines'], axis=1) #delete dictionary column
    covid_data = pd.concat([df,cases,deaths], axis=1).iloc[::-1] #put dataframes together and reverse index
    
    return covid_data
    
print(format_data())