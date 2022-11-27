import xml.etree.ElementTree as ET 

# Pass the path of the xml document 
tree = ET.parse(r'./CONFIG.xml') 

# get the parent tag 
root = tree.getroot() 

# print(dir(root))

# print the root (parent) tag along with its memory location 
MUX_path = root.find("relay").find("bin_path").text

print(MUX_path)

# print the text contained within first subtag of the 5th tag from the parent 
# print(root[2][0].text) 
