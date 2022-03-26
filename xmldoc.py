import csv
import xml.etree.ElementTree as Xet
import requests
import pandas as pd

cols = ["FHRSID", "LocalAuthorityBusinessID", "BusinessName", "AddressLine4", "PostCode", "RatingValue", "RatingDate", "LocalAuthorityEmailAddress"]
rows = []
dataxml = Xet.parse('ratings.xml')
root = dataxml.getroot()
for i in root:
    ID = i.find("FHRSID")
    BID = i.find("LocalAuthorityBusinessID")
    BNAME = i.find("BusinessName")
    Address = i.find("AddressLine4")
    PostCode = i.find("PostCode")
    rating = i.find("RatingValue")
    RatingDate = i.find("RatingDate")
    email = i.find("LocalAuthorityEmailAddress")
    rows.append({"FHRSID": ID,
                "LocalAuthorityBusinessID": BID,
                "BusinessName": BNAME,
                "AddressLine4": Address,
                "PostCode": PostCode,
                "RatingValue": rating,
                "RatingDate": RatingDate,
                "email": email})

df = pd.DataFrame(rows, columns = cols)
df.to_csv('output.csv')