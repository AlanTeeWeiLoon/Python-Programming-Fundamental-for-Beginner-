import imapclient

print('\n1------------------------------\n')
# IMAPClient() - domain name, ssl -  encryption
# .login() - with email address and password

conn = imapclient.IMAPClient('imap.gmail.com', ssl = True)

conn.login('alantee0302@gmail.com','Alantee907850731@')

print('\n2------------------------------\n')
# .select_folder() - select a folder in email box and the method
# .search() - search an email

conn.select_folder('INBOX', readonly = True) # folder name 'INBOX' with read only method

UIDs = conn.search(['SINCE 20-Aug-2020']) # search the email since 20-Aug-2020 - will return UID of the email

print('\n3------------------------------\n')
# .fetch() - to translate UID into actual email

rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS']) # UID, body of the email

print('\n4------------------------------\n')
import pyzmail

# .Pyzmail.factory()
# .get_addresses()

message = pyzmail.Pyzmail.factory(rawMessage[47474][b'BODY[]'])

print(message.get_addresses('from'))

print(message.get_addresses('to'))

print(message.get_addresses('bcc'))

print('\n4------------------------------\n')
# .text_part
# .html_part

print(message.text_part)

print(message.html_part == None)

print('\n5------------------------------\n')
# .text_part.get_payload().decode()
# .text_part.charset

print(message.text_part.get_payload().decode('UTF-8'))
print(message.text_part.charset == None)

print('\n6------------------------------\n')
# .list_folders()

print(conn.list_folders())

print('\n7------------------------------\n')
# delete an email
# .deletemessage()

conn.select_folders('INBOX', readonly = False)
UIDs = conn.search(['ON 24-Aug-2020'])
conn.delete_message(UIDs)

print('\n8------------------------------\n')






















