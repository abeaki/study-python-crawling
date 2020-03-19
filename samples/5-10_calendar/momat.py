from __future__ import print_function

import re
from datetime import datetime, timezone, timedelta
import httplib2
import os

import requests
import lxml.html
from apiclient import discovery
import oauth2client
from oauth2client import client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

import argparse
flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

JST = timezone(timedelta(hours=9), 'JST')


def main():
    exhibitions = scrape()
    save_to_calendar(exhibitions)


def scrape():
    response = requests.get('http://www.momat.go.jp/')
    root = lxml.html.fromstring(response.content)

    exhibitions = []

    for ribbon in root.cssselect('.momat-top-ribbon'):
        url = ribbon.cssselect('a')[0].get('href')
        text = ribbon.cssselect('span')[0].text.strip()

        m = re.search(r'(\S+)\s*-\s*(\S+)\s*(.*)', text)
        str_date_from = m.group(1)
        str_date_to = m.group(2)
        name = m.group(3)

        date_from = datetime.strptime(str_date_from, '%Y.%m.%d')
        try:
            date_to = datetime.strptime(str_date_to, '%Y.%m.%d')
        except ValueError:
            date_to = datetime.strptime(str_date_to, '%m.%d').replace(year=date_from.year)
        assert date_from < date_to

        exhibitions.append({
            'name': name,
            'url': url,
            'date_from': date_from.replace(tzinfo=JST),
            'date_to': date_to.replace(tzinfo=JST),
        })

    return exhibitions


def save_to_calendar(exhibitions):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    calendar_id = 'primary'

    for exhibition in exhibitions:
        print('{date_from} - {date_to} {name} {url}'.format(**exhibition))

        if exhibition['date_to'] < datetime.now(JST):
            print('Past event')
            continue

        str_date_from = exhibition['date_from'].date().isoformat()

        eventsResult = service.events().list(
            calendarId=calendar_id,
            timeMin=exhibition['date_from'].isoformat(),
            timeMax=(exhibition['date_from'] + timedelta(days=1)).isoformat(),
            singleEvents=True).execute()

        events = eventsResult.get('items', [])
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))

            if (start == str_date_from and end == str_date_from and
                    event['summary'] == exhibition['name']):
                print('Event already exists')
                break
        else:
            event = {
                'start': {'date': str_date_from},
                'end': {'date': str_date_from},
                'summary': exhibition['name'],
            }
            created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
            print('Event created: ', created_event)


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)

    return credentials


if __name__ == '__main__':
    main()
