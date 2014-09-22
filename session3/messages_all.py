import json
from xml.etree import ElementTree

def message_text(file_type,message_type):

    if file_type == 'json':

        messages = open("messages.json")

        for line in messages.readlines():

            parsed = json.loads(line)

            if parsed['type'] == message_type:
                print parsed['message']

        messages.close()

    elif file_type == 'xml':

        messages = ElementTree.parse('messages.xml').getroot()

        for message in messages:

            if message.attrib['type'] == message_type:
                print message.text

