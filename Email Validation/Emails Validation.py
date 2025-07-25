# -*- coding: utf-8 -*-
"""Valid Emails from Excel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VNSD3VEb-i_rIqbl4OHoXPgdow4f9Nn0
"""

def validate_email(email):
    if '@' in email and '.' in email:
        try:
            username, domain = email.split('@')
            if username and domain:
                if '.' in domain:
                    x, y = domain.split('.', 1)
                    if x and y:
                        return True
        except:
            return False
    return False

def emails_from_excel():
    import openpyxl


    excel_file = '/content/E-mails.xlsx'


    valid_emails = []
    domains = []

    try:

        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active


        for row in sheet.iter_rows(min_row=2, values_only=True):
            email = row[3]
            if isinstance(email, str) and email.strip() and validate_email(email):
                valid_emails.append(email)
                domain = email.split('@')[1]
                if domain not in domains:
                    domains.append(domain)


        with open('email_domains_output', 'w') as f:
            f.write("Valid Emails:")
            for email in valid_emails:
                f.write(f"{email}")
            f.write("Domains of valid emails:")
            for domain in domains:
                f.write(f"{domain}")


        print("Valid Emails:")
        for email in valid_emails:
            print(email)
        print("Domains of valid emails:")
        for domain in domains:
            print(domain)

    except FileNotFoundError:
        print(f" Not found. Please upload file.")
    except Exception as e:
        print(f"Error")


emails_from_excel()