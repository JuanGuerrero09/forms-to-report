from __future__ import print_function
import json
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

def get_raw_answers():
    SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    store = file.Storage('token.json')
    creds = None
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

    # Prints the title of the sample form:
    form_id = '1b04zZwAB0l6MDE9_7d6lHO8bwxjc8kMBv6rWGXyGV9s'
    result = service.forms().responses().list(formId=form_id).execute()
    print(result)
    # Serializing json
    json_object = json.dumps(result, indent=4)
    
    # Writing to sample.json
    with open("answers.json", "w") as outfile:
        outfile.write(json_object)

def get_raw_questions():

    SCOPES = "https://www.googleapis.com/auth/forms.body.readonly"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    store = file.Storage('token.json')
    creds = None
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

    # Prints the title of the sample form:
    form_id = '1b04zZwAB0l6MDE9_7d6lHO8bwxjc8kMBv6rWGXyGV9s'
    result = service.forms().get(formId=form_id).execute()
    print(result)
    # Serializing json
    json_object = json.dumps(result, indent=4)
    
    # Writing to sample.json
    with open("questions.json", "w") as outfile:
        outfile.write(json_object)