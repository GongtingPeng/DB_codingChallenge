import requests
from bs4 import BeautifulSoup

def process(item):
    """
    Main function to parse everything and format output
    """
    org, add, mail, phone, email = item
    
    office_name, _ = org.split('-')
    office_name = office_name.replace(':', '').strip()
    
    office_link = handle_link(office_name) # done
    
    office_address, state_city_zip = add.split('\n')
    office_city, office_state, office_zip = handle_add(state_city_zip)
    
    po_box, mail_addres, mail_city, mail_state, mail_zip, mail_phone = handle_mail(mail) # done
    
    office_phone  = handle_phone(phone)
    
    res = {
        'office_name': office_name,
        'office_link': office_link,
        'office_adress': office_address,
        'office_city': office_city,
        'office_state': office_state,
        'office_zip': office_zip,
        'office_phone': office_phone,
        'mail_address': mail_addres,
        'mail_pobox': po_box,
        'mail_city': mail_city,
        'mail_state': mail_state,
        'mail_zip': mail_zip,
        'mail_phone': mail_phone
    }
    return res

def handle_link(office_name):
    """
    Handle http link
    """
    url = 'http://www.dot.ca.gov/'
    if office_name == 'Headquarters':
        return url
    else:
        return url + 'dist' + office_name.split(' ')[1] + '/'

def handle_mail(mail):
    """
    Handle all address info
    """
    po_box, mail_address = None, None
    ad1 = mail.split('\n')[0].strip()
    ad2 = mail.split('\n')[-1].strip()
    if ad1.startswith('P.O.'):
        po_box = ad1
    else:
        mail_address = ad1.split(',')[0]
    idx = ad2.find('CA')
    mail_state = 'CA'
    mail_city, mail_zip = ad2[:idx-1].replace(',', ''), ad2[idx+3:].replace('.', '')
    mail_phone = None
    
    return po_box, mail_address, mail_city, mail_state, mail_zip, mail_phone

def handle_phone(phone):
    """
    Handle phone number
    """
    if len(phone.split('\n')) >= 2:
        phone = phone.split('\n')[1].strip()
    else:
        phone = phone.strip()
    
    for char in ['(', ' ']:
        phone = phone.replace(char, '')
    phone = phone.replace(')', '-')
    return phone

def handle_add(state_city_zip):
    """
    Handle street address
    """
    idx = state_city_zip.find('CA')
    city, zip_code = state_city_zip[:idx-1].replace(',', '').strip(), state_city_zip[idx+3:].replace('.', '').strip()
    return city, 'CA', zip_code


if __name__ == "__main__":
    r = requests.get('https://dot.ca.gov/contact-us')
    soup = BeautifulSoup(r.text, 'html.parser')

    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.find_all("tr")

    headers = {}
    thead = soup.find("thead")
    thead = thead.find_all("th")
    for i in range(len(thead)):
        headers[i] = thead[i].text.strip().lower()
        data = []
        for row in rows:
            cells = row.find_all("td")
            items = []
            for index in cells:
                items.append(index.text.strip())
            if len(items) != 5:
                continue
            data.append(process(items))

print(data) 
