import requests


def geturl():
    dagenham = "https://ratings.food.gov.uk/OpenDataFiles/FHRS501en-GB.xml"
    southwark = "https://ratings.food.gov.uk/OpenDataFiles/FHRS528en-GB.xml"
    response = requests.get(southwark)
    statuscode = response.status_code
    if statuscode == 200:
        print("Successfully pulled data with status code:", statuscode)
        with open('ratingssouthwark.xml', 'wb') as f:
            f.write(response.content)
    else:
        print("Error in pulling data ", statuscode)
        exit()