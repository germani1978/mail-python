import smtplib

destinatario = 'maidanyscruzgonzalez@gmail.com'
remitente = 'gatotimizu@gmail.com'
password = 'password de app en gmail(no es la del correo)' # hay que activar la verificacion de 2 pasos y despues a generar una contraseña en los ajustes de gmail
mensaje = 'Subject:Princesa\n\nBuenos dias mi amor'

connection = smtplib.SMTP('smtp.gmail.com',587)
connection.starttls()
connection.login(remitente, password)
connection.sendmail(from_addr=remitente, to_addrs=destinatario,msg=mensaje)
connection.close()


