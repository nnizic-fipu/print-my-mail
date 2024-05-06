"""  Printanje amilova  """

import email
import imaplib
from email.message import EmailMessage
from email.header import Header, decode_header, make_header

read_file = open("mail_data.txt", "r")
data_rows = read_file.readlines()
read_file.close()
data_row = []
for row in data_rows:
    data_row.append(row)

email_address = (data_row[0]).strip()
email_password = (data_row[1]).strip()
email_server = (data_row[2]).strip()

EMAIL = str(email_address)
PASSWORD = str(email_password)
SERVER = str(email_server)


mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
mail.select("inbox")
status, data = mail.search(None, "(UNSEEN)")
mail_ids = []

for block in data:
    mail_ids += block.split()

for i in mail_ids:
    status, data = mail.fetch(i, "(RFC822)")
    for response_part in data:
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])
            message.set_charset("utf-8")
            mail_from = make_header(decode_header(message["from"]))
            mail_subject = make_header(decode_header(message["subject"]))
            mail_date = message["date"]

            if message.is_multipart():
                mail_content = ""

                for part in message.get_payload():
                    if part.get_content_type() == "text/plain":
                        mail_content += part.get_payload()
            else:
                mail_content = message.get_payload()
            with open("mail_archive.txt", "a") as write_file:
                write_file.write(f"{mail_date} : \n")
                write_file.write(f"From: {mail_from} \n")
                write_file.write(f"Subject: {mail_subject} \n")
                write_file.write(f"Content: {mail_content} \n \n")
                write_file.close()
                print("Podatci upisani ...")
