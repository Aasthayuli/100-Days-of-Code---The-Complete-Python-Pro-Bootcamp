from datetime import datetime
import requests

# user_params = {
#     "token":"sdkjnladn2rk2",
#     "username":"aasthayuli",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }
# pixela_endpoint = "https://pixe.la/v1/users"

# commented because already ran this line . So, it has created this user - "aasthayuli".
# So, running it again would cause error.
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#-----------------------------------------------------------------------------------------------------------------------

# # POST (creating a graph)

# USERNAME = "aasthayuli"
# TOKEN = "sdkjnladn2rk2"
#
#
# pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token":TOKEN,
#     "username":USERNAME,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id":"graph1",
#     "name":"Cycling Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"shibafu"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#-----------------------------------------------------------------------------------------------------------------------
# POST (adding data)
# USERNAME = "aasthayuli"
# TOKEN = "sdkjnladn2rk2"
# GRAPH_ID = "graph1"
# today = datetime.now()
#
# pixela_endpoint = "https://pixe.la/v1/users"
# add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# add_pixel_config = {
#     "date":today.strftime("%Y%m%d"),
#     "quantity":input("How many Kilometers did you cycle today?: "),
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=add_pixel_endpoint, json=add_pixel_config , headers=headers)
# print(response.text)

# ----------------------------------------------------------------------------------------------------------------------
# PUT (updating the data)

# USERNAME = "aasthayuli"
# TOKEN = "sdkjnladn2rk2"
# GRAPH_ID = "graph1"
#
#
# pixela_endpoint = "https://pixe.la/v1/users"
#
# day = datetime(year=2025, month=7, day=6)
# day_to_be_updated = day.strftime("%Y%m%d")
# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_to_be_updated}"
# update_pixel_config = {
#     "quantity":"15",
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config , headers=headers)
# print(response.text)

# ----------------------------------------------------------------------------------------------------------------------

# DELETE (deleteing the data)

USERNAME = "aasthayuli"
TOKEN = "sdkjnladn2rk2"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"
day = datetime(year=2025, month=7, day=5)
day_to_be_deleted = day.strftime("%Y%m%d")
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_to_be_deleted}"

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.delete(url=delete_pixel_endpoint,  headers=headers)
print(response.text)