import jinja2
import pdfkit
from datetime import datetime

name = 'Olaoluwa'
product = 'Coffee'
price = 15
date = datetime.today().strftime("%d %b, %y")

context = {'name':name, 'product':product, 'price':price, 'date':date}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template('pdf4.html')
output_text = template.render(context)

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_string(output_text, 'receipt4.pdf', configuration=config)