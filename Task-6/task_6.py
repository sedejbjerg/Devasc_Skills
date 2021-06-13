# ZTY0YTRiOWItNzk4MS00YmE2LWE5MDMtN2U1ZGJjMTU2OWFkMTgxM2JlZDYtYTc4_P0A1_5d96674f-de50-43d7-ae6b-8071b71cb457


import requests
import json
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder

access_token = 'ZTY0YTRiOWItNzk4MS00YmE2LWE5MDMtN2U1ZGJjMTU2OWFkMTgxM2JlZDYtYTc4_P0A1_5d96674f-de50-43d7-ae6b-8071b71cb457'

def authentication():
    url = 'https://webexapis.com/v1/people/me'

    headers = { 'Authorization': 'Bearer {}'.format(access_token) }
    
    res = requests.get(url, headers=headers)

    print("Testing authentication, status: ", res.status_code)
    

def create_room(room_name):
    url = 'https://webexapis.com/v1/rooms'
    
    headers = { 'Authorization': 'Bearer {}'.format(access_token),
                'Content-Type': 'application/json'
              }
    params = { 'title': room_name}

    res = requests.post(url, headers=headers, json=params)

    room_id = res.json()["id"]
    
    print("Room creation, status: ", res.status_code)
    print("Room created: ", res.json()["title"])

    return room_id


def create_member(email, room_id):
    url = 'https://webexapis.com/v1/memberships'

    headers = { 'Authorization': 'Bearer {}'.format(access_token),
                'Content-Type': 'application/json'
              }

    params = { 'roomId': room_id, 'personEmail': email }

    res = requests.post(url, headers=headers, json=params)

    print("Added member, status: ", res.status_code)


def create_message(message, room_id):
    
    url = 'https://webexapis.com/v1/messages'
    headers = { 'Authorization': 'Bearer {}'.format(access_token),
                'Content-Type': 'application/json'
              }
    params = {'roomId': room_id, 'markdown': message}

    res = requests.post(url, headers=headers, json=params)
    
    print("Create message, status: ", res.status_code)

def upload_files(path, room_id):
    url = 'https://webexapis.com/v1/messages'

    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):    
            m = MultipartEncoder({'roomId': room_id,
                                  'text': 'File: {}'.format(entry),
                                  'files': (entry, open(path+'/'+entry, 'rb'),
                                  'image/png')})

            res = requests.post( url, data=m,
                                 headers={ 'Authorization': 'Bearer {}'.format(access_token),
                                           'Content-Type': m.content_type } )

            print("Uploading file: "+entry+", status: ", res.status_code)

    print("Last file uploaded!")


if __name__ == "__main__":
    authentication()
    room_id = create_room("Netacad_devasc_skills_SD")
    create_member("yvan.rooseleer@biasc.be", room_id)
    create_message("My github remote repository: https://github.com/sedejbjerg/Devasc_Skills", room_id)
    create_message("Here are some of my screenshots of netacad-devasc skills-based exam.", room_id)
    create_message("All screenshots can be found on the github repository in the different ./Task folders.", room_id)
    upload_files("./screenshots", room_id)
