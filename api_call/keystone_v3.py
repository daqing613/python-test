import requests
import pprint
from keystoneauth1.identity import v3
from keystoneauth1 import session


def auth_token():
    v3_auth = v3.Password(auth_url="http://192.168.64.29/identity/v3",
                          username="demo",
                          password="supersecret",
                          project_name="demo",
                          project_domain_name="default",
                          user_domain_name="default")
    print("Start to acquire the token.")
    v3_ses = session.Session(auth=v3_auth)
    auth_token = v3_ses.get_token()
    return auth_token


def create_server(auth_token):
    print("The auth_token is : %s" % auth_token)
    url = "http://192.168.64.29/compute/v2.1/servers"
    payload = "{\n  \"server\": {\n    \"name\": \"wp-vm1\",\n    \"imageRef\": \"c095bd35-798f-4d82-942a-d2fa2d1f1e43\",\n    \"flavorRef\": \"1\",\n    \"max_count\": 1,\n    \"min_count\": 1,\n    \"networks\": [\n      {\n        \"uuid\": \"16d268b3-e629-439d-9cb3-46f9d713724b\"\n      }\n    ],\n    \"security_groups\": [\n      {\n        \"name\": \"default\"\n      }\n    ]\n  }\n}"
    headers = {'X-Auth-Token': auth_token}

    response = requests.request("POST", url, data=payload, headers=headers)

    pprint.pprint(response.text)


if __name__ == '__main__':
    token = auth_token()
    create_server(token)
