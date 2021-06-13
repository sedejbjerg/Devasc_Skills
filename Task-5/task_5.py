import json
import requests

requests.packages.urllib3.disable_warnings()

header_a = { "Accept": "application/yang-data+json",
             "Content-type": "application/yang-data+json"
           }
header_b = { "Accept": "application/yang-data+json" }

basicauth = ("cisco", "cisco123!")

def options():
    api_url = "https://192.168.20.38:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" 

    resp = requests.options(api_url, auth=basicauth, headers=header_b, verify=False)

    print("\n\n-1- OPTIONS\n")
    print(resp.status_code)

    for key in resp.headers:
        print(key, ":", resp.headers[key])

def post():
    api_url = "https://192.168.20.38:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor"

    data = {"severity": "alerts"}

    resp = requests.post(api_url, data=json.dumps(data), auth=basicauth, headers=header_a, verify=False)

    print("\n\n-2- POST\n")
    print(resp.status_code)

    for key in resp.headers:
        print(key, ":", resp.headers[key])

def put():
    api_url = "https://192.168.20.38:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

    data = {"severity": "warnings"}

    resp = requests.put(api_url, data=json.dumps(data), auth=basicauth, headers=header_a, verify=False)

    print("\n\n-3- PUT\n")
    print(resp.status_code)

    for key in resp.headers:
        print(key, ":", resp.headers[key])

def patch():
    api_url = "https://192.168.20.38:443/restconf/data/Cisco-IOS-XE-native:native"

    data = {"native": {"logging": {"monitor": {"severity": "informational"}}}}

    resp = requests.patch(api_url, data=json.dumps(data), auth=basicauth, headers=header_a, verify=False)

    print("\n\n-4- PATCH\n")
    print(resp.status_code)
 
    for key in resp.headers:
        print(key, ":", resp.headers[key])

def get():
    api_url = "https://192.168.20.38:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" 

    resp = requests.get(api_url, auth=basicauth, headers=header_b, verify=False)

    print("\n\n-5- OPTIONS\n")
    print(resp.status_code)
 
    for key in resp.headers:
        print(key, ":", resp.headers[key])

if __name__ == "__main__":
    options()
    post()
    put()
    patch()
    get()
