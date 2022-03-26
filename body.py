from xml.dom import minidom
import pandas as pd
import os
def body():
        cols = ["FHRSID", "BusinessName", "LocalAuthorityBusinessID", "BusinessType",
                        "BusinessTypeID", "RatingValue", "RatingDate", "LocalAuthorityName", "PostCode"]
        rows = []

        doc = minidom.parse("ratingssouthwark.xml")

        # doc.getElementsByTagName returns the NodeList
        #name = doc.getElementsByTagName("BusinessName")[0]
        #print(name.firstChild.data)

        estdetails = doc.getElementsByTagName("EstablishmentDetail")
        for EstablishmentDetail in estdetails:

                fhrsid = EstablishmentDetail.getElementsByTagName("FHRSID")[0]
                bid = EstablishmentDetail.getElementsByTagName("LocalAuthorityBusinessID")[0]
                name = EstablishmentDetail.getElementsByTagName("BusinessName")[0]
                btype = EstablishmentDetail.getElementsByTagName("BusinessType")[0]
                btypeid = EstablishmentDetail.getElementsByTagName("BusinessTypeID")[0]
                rating = EstablishmentDetail.getElementsByTagName("RatingValue")[0]
                ratingdate = EstablishmentDetail.getElementsByTagName("RatingDate")[0]
                #print (type(ratingdate))
                Authorityname = EstablishmentDetail.getElementsByTagName("LocalAuthorityName")[0]
                postcode = EstablishmentDetail.getElementsByTagName("PostCode")

                        #print("FHRSID:% s, BusinessName:% s "%
                    #(fhrsid.firstChild.data, name.firstChild.data))
                rows.append({"FHRSID":fhrsid.firstChild.data,
                        "LocalAuthorityBusinessID": bid.firstChild.data,
                        "BusinessName": name.firstChild.data,
                        "BusinessType": btype.firstChild.data,
                        "BusinessTypeID": btypeid.firstChild.data,
                        #"AddressLine4": Address,
                        "PostCode": postcode,
                        "RatingValue": rating.firstChild.data,
                        "RatingDate": ratingdate,
                        #"PostCode": postcode,
                        "LocalAuthorityName": Authorityname.firstChild.data})
                        #"email": email})
        df = pd.DataFrame(rows, columns = cols)
        df.to_csv('.csv')
        print("sussessfully saved data to",os.getcwd())