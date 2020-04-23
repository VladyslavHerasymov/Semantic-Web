import requests
import lxml.html
from bs4 import BeautifulSoup as BS
import xml.etree.ElementTree as ET
from xml.dom import minidom

r = requests.get('https://www.ebay.com/b/Football-Clothing-Shoes-Accessories/159113/bn_1941036')
html = BS(r.content, 'html.parser')
z=-1

tree = lxml.html.fromstring(r.text)
shipping = tree.xpath('//span[@class="s-item__shipping s-item__logisticsCost"]/@span')

for vd in html.select('.s-item__wrapper.clearfix'):
	z+=1
	def main():
		n = vd.select('.s-item__title > h3')
		p = vd.select('.s-item__price')
		b = vd.select('.s-item__dynamic s-item__dynamicAttributes1')
		hr = n[0]['href']

		elem = ET.Element('all_data')
		product = ET.SubElement(new, 'product')
		product.set('id', shipping[k])
		name = ET.SubElement(product, 'name')
		name.text = n[0]['h3']
		price = ET.SubElement(product, 'price')
		price.text = p[0].text
		brand = ET.SubElement(product, 'brand')
		brand.text = b[0].text
		characters = ET.SubElement(product, 'characters')

		r2 = requests.get('https://www.ebay.com' + hr)
		html2 = BS(r2.content, 'html.parser')
	
		for el2 in html2.select('#mainContent'):
			delivery = el2.select('.sh-del-frst  > b')
			returns = el2.select('.rpColWid > a')
			
		delivery_date = ET.SubElement(characters, 'delivery')
		delivery_date.text = delivery
		returns = ET.SubElement(characters, 'returns')
		returns.text = returns
	    
		save_xml('test.xml', new)
	 
	def save_xml(filename, xml_code):
		xml_string = ET.tostring(xml_code).decode()

		xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
		with open(filename, 'a') as xml_file:
			xml_file.write(xml_prettyxml)

	if __name__ == '__main__':
		main()