from __future__ import print_function
import json
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

form_id = ''

def get_form_id(form_type):
    form_ids = {
        "pumping stations": '1b04zZwAB0l6MDE9_7d6lHO8bwxjc8kMBv6rWGXyGV9s',
        "reservoirs": '1gkOlqoamzIujA72xV8HkF-nd3gFkx6pxtUk3yXnYn3o'
    }
    return form_ids[form_type]


def get_raw_answers(form_type):
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
    form_id = get_form_id(form_type)
    result = service.forms().responses().list(formId=form_id).execute()
    # Serializing json
    json_object = json.dumps(result, indent=4)
    
    # Writing to sample.json
    with open(f"{form_type}_answers.json", "w") as outfile:
        outfile.write(json_object)

def get_raw_questions(form_type):

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
    form_id = get_form_id(form_type)
    result = service.forms().get(formId=form_id).execute()
    # Serializing json
    json_object = json.dumps(result, indent=4)
    
    # Writing to sample.json
    with open(f"{form_type}_questions.json", "w") as outfile:
        outfile.write(json_object)