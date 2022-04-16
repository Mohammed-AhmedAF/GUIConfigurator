import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

tree = ET.parse("uartConfig.xml")
root = tree.getroot()


#Get coin attribute
def createConfig(buadrateValue):
    baudrateElement = ET.Element("Baudrate")
    baudrateElement.text = buadrateValue 

    root.append(baudrateElement)
    tree.write("uartConfig.xml")
