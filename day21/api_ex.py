# APT - Application Programming Interface
# # IBM Stock Market API  
# import requests

# def get_stock_data():
#     url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY" \
#     "&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         last_refreshed = data["Meta Data"]["3. Last Refreshed"]
#         price = data["Time Series (5min)"][last_refreshed]["1. open"]
#         return price
#     else:
#         return None
    
# price = get_stock_data()
# Symbol = "IBM"

# if price is not None:
#     print(f"{Symbol}: {price}")
# else:
#     print("Failed to retrieve data")

# import json
# import urllib.request

# url = "http://api.open-notify.org/astros.json"
# response = urllib.request.urlopen(url)
# result = json.loads(response.read())
# print(result)

# HTTP Methods

# # GET Method

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# print("Status Code: ",response.status_code)
# print("Response Data:")
# print(response.json())

# # POST Method

# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title":"Python API",
#     "body":"Learning POST Requests",
#     "userId":1
# }

# response = requests.post(url,json=data)

# print("Status Code: ",response.status_code)
# print("Created Data:")
# print(response.json())

# # PUT Method

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# updated_data = {
#     "id":1,
#     "title":"Updated Python API",
#     "body":"Learning PUT Requests",
#     "userId":1
# }

# response = requests.put(url,json=updated_data)

# print("Status Code: ",response.status_code)
# print("Created Data:")
# print(response.json())

# # PATCH Method

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# patched_data = {
#     "title":"Updated Python API"
# }

# response = requests.put(url,json=patched_data)

# print("Status Code: ",response.status_code)
# print("Created Data:")
# print(response.json())

# # DELETE Method

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.delete(url)

# print("Status Code: ",response.status_code)

# if response.status_code == 200:
#     print("Data Deleted Successfully")
# else:
#     print("Delete failed")

# # HEAD Method

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.head(url)

# print("Status Code: ",response.status_code)
# print("Data:")
# print(response.headers)

# # OPTIONS Method

# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.options(url)

# print("Status Code:", response.status_code)
# print("Allowed Methods:")
# print(response.headers.get('Allow'))