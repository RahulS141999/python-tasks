import urllib3
#print(dir(urllib3))

url = 'https://www.w3schools.com' # url to download data 

http = urllib3.PoolManager()
response = http.request('GET', url) #send GET request to URL

if response.status == 200:
    data = response.data
    with open('downloaded_data.txt', 'wb') as f:
        f.write(data)
    
    print("data downloaded successfully and save in downloaded_data.txt")

else:
    print(f"Error: failed to download data from url")