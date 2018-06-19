#reads in the protocol requirements and stores the information in a class

import yaml
import logging

logger = logging.getLogger(__name__)

def loadYamlFile(filename):
    #open up the filename
    logger.debug("Opening file {}".format(filename))
    try:
        fObject = open(filename, 'r')
    except FileNotFoundError:
        logger.error("Config File {} not Found!".format(filename))
        return []
    else:
        data = yaml.load(fObject.read())
        fObject.close()

    return data

def parseYamlConfig(data):
    # we already have all of the information we need stored in the data from
    # the YAML file. However, it's worthwhile to also generate a list of all
    # incoming and outgoing variables. This allows checking for duplicates.
    incomingVariables = []
    outgoingVariables = []

    # go through each message
    for msg, metadata in data.items():
        for k, v in metadata['variables'].items():
            if metadata['type'] == 'incoming':
                incomingVariables.append({k: v})
            elif metadata['type'] == 'outgoing':
                outgoingVariables.append(k, v)

    logger.debug(incomingVariables)
