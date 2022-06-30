#  Error cant connet to the server

import smtplib

print('\n1------------------------------------------\n')
# starttls
# .ehlo()
# .login()

conn = smtplib.SMTP('smtp.gmail.com', 587) # domain name and port number
print(type(conn)) # <class 'smtplib.SMTP'>

conn.starttls() # begin encryption - have to start encryption before login

conn.ehlo() # to start the connection with smtp server
print(conn.ehlo())

conn.login('alantee0302@gmail.com','Alantee907850731@')

print('\n2------------------------------------------\n')
# .sendmail() - send the email
# .quit() - to disconnect

conn.sendmail('alantee0302@gmail.com','caemas@gmail.com', 'Subject: So long....\n\nDear Alan,\nSo long, and thanks for all the fish.\n\n-Alan') # from_addr, to_addrs, msg
conn.quit()
















































