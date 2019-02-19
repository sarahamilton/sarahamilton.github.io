'use strict';

let Wit = null;
let interactive = null;
try {
  // if running from repo
  Wit = require('../').Wit;
  interactive = require('../').interactive;
} catch (e) {
  Wit = require('node-wit').Wit;
  interactive = require('node-wit').interactive;
}

const accessToken = "OLTVFO6BQS76EAPSORRRSUNHVIXNVC4E"

function first_entity_value(entities, entity): {
    if entity not in entities:
        return None
    text = entities[entity][0]['value']
    if not val:
        return None
    return val 
}

function handle_message(response): {
    entities = response['entities']
    text = response['_text']
    compiled_text.append(text)
    print(compiled_text)
}

const client = new Wit({accessToken});
interactive(client);