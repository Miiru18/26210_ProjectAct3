import requests
#API key goes here
API_KEY = '719bb81181c5781c882d70f3d5372f6a'

#API key checker
def get_ip_info():
    url = f"http://api.ipstack.com/check?access_key={API_KEY}"
    #try catch for catching any exceptions and errors
    try:
        response = requests.get(url)
        data = response.json()
        
        #variables go here
        ipv4 = data.get('ip')
        ipv6 = data.get('ipv6')
        location = f"{data.get('city')}, {data.get('region_name')}, {data.get('country_name')}"
        isp = data.get('isp')
        country_code = data.get('country_code')

        #outputs all the information
        print(f"IPv4 Address: {ipv4}")
        print(f"IPv6 Address: {ipv6}")
        print(f"Location: {location}")
        print(f"ISP: {isp}")
        print(f"Country Code: {country_code}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    get_ip_info()
