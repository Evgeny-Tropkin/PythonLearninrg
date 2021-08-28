from lxml import etree

xml_string = input()

root = etree.fromstring(xml_string)
number_of_child_elements = len(root)
number_of_attributes = len(root.keys())

print(number_of_child_elements, number_of_attributes)
