import json
from xml.etree import ElementTree

def message_text(file_type,message_type):

    if file_type == 'json':

        json_text(message_type)

    elif file_type == 'xml':

        xml_text(message_type)


def json_text(message_type):

    messages = open("messages.json")

    for line in messages.readlines():

        parsed = json.loads(line)

        if parsed['type'] == message_type:
            print parsed['message']

    messages.close()


def xml_text(message_type):

    messages = ElementTree.parse('messages.xml').getroot()

    for message in messages:

        if message.attrib['type'] == message_type:
            print message.text
