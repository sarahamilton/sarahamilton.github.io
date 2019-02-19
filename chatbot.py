from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from wit import Wit

access_token = "OLTVFO6BQS76EAPSORRRSUNHVIXNVC4E"

compiled_text = []
questions_array = ["red or orange?","peas or carrots","pancetta or pancetta?"]

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    text = entities[entity][0]['value']
    if not val:
        return None
    return val

def handle_message(response):
    """
    Customizes our response to the message and sends it
    """
    entities = response['entities']
    text = response['_text']
    compiled_text.append(text)
    print(compiled_text)

client = Wit(access_token=access_token)
client.interactive(handle_message=handle_message)

# convert compiled_text into PDF
