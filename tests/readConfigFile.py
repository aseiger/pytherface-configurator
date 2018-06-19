import context
import logging

import pytherface.yamlFileReader

#initialize the logger
logger = logging.getLogger('pytherface')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

data = pytherface.yamlFileReader.loadYamlFile("interface.yaml")
# logger.debug(data)
pytherface.yamlFileReader.parseYamlConfig(data)
