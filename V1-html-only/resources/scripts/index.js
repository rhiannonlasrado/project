//import covidData variable from ./data/data.js  
//write variable to html table


function callDataAPI() {
    var xhr = new XMLHttpRequest();
    xhr.open(
      "GET",
      "https://api.coronavirus.data.gov.uk/v1/data?filters=areaType%3Dnation%3BareaName%3Dengland&structure=%7B%22date%22%3A%22date%22%2C%22name%22%3A%22areaName%22%2C%22code%22%3A%22areaCode%22%2C%22cases%22%3A%7B%22daily%22%3A%22newCasesByPublishDate%22%2C%22cumulative%22%3A%22cumCasesByPublishDate%22%7D%2C%22deaths%22%3A%7B%22daily%22%3A%22newDeathsByDeathDate%22%2C%22cumulative%22%3A%22cumDeathsByDeathDate%22%7D%2C%22vaccines%22%3A%7B%22weekly2nddose%22%3A%22weeklyPeopleVaccinatedSecondDoseByVaccinationDate%22%2C%22weekly1stdose%22%3A%22weeklyPeopleVaccinatedFirstDoseByVaccinationDate%22%2C%22cum1stdose%22%3A%22cumPeopleVaccinatedFirstDoseByVaccinationDate%22%2C%22cum2nddose%22%3A%22cumPeopleVaccinatedSecondDoseByVaccinationDate%22%7D%7D",
      false
    );
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(null);
    
    var jsonObject = JSON.parse(xhr.responseText);
    return jsonObject;
  }

console.log(callDataAPI())