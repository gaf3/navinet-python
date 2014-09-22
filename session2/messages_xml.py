# Smaller symbol
from xml.etree import ElementTree

# Better naming
messages = ElementTree.parse('messages.xml').getroot()

messages.tag
messages[0].attrib['type']

for message in messages:
    print "%s: %s" % (message.attrib['type'],message.text)

