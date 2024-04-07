import phonenumbers
from phonenumbers import geocoder
# pip install phonenumbers
import opencage
import folium

# add a phone number to find provider and country of that number , !!! phone number with + char starts
number = "+323463653636363563565"
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


from phonenumbers import carrier
service_provider= phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
# country name will be showed

########################################################################################################################
# pip install opencage

#### to get an API key need to register and get free api key from here :https://opencagedata.com/api#bestpractices #####
key = '6970fd30b1b644978b6b6cc51f6777c1'

not_need = 'rxyjkbrltnnjfgearpil'
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query  = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
# privider from phone number and longitude and latitude  will be shown

########################################################################################################################
# pip install folium
# import folium

myMap = folium.Map(location= [lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
