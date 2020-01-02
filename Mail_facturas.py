import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
mail=input('Ingrese su mail:')
passw=input('Ingrese su contraseña:')
path=input('Ingrese la ruta donde se encuentran sus archivos( ejemplo:"C:\\Users\\bcespedes.ap\\Desktop\\Automatizacion" : ')
facturas=input('Tus facturas son Provisorias o finales:')
nombre_buque=input('Nombre buque:')
CC=input('CC:')
# fill in the variables
smtp_server = "smtp.gmail.com"
smtp_port = 587                                 # for smtp.gmail.com
from_address = mail            # e.g. username@gmail.com
from_password = passw   # required by script to login using your username
to_address = "belen.cespedes.ap@copec.cl"        # e.g. username2@gmail.com
subject = ('Facturas' ' ' + facturas +' '+ 'BT'+ ' ' +nombre_buque+' ' +'CC'+ ' ' + CC)               
mail_body = ('Felipe adjunto ' 'Facturas'+ facturas +' '+ 'BT'+ ' ' +nombre_buque+' ' +'CC'+' ' +CC+ ' ', favor validar')
#+ facturas +  "BT" +nombre_buque+ CC "YY_YY"


msg = MIMEMultipart()
msg['Subject'] =  subject
msg['To'] = to_address
msg.attach(MIMEText(mail_body))
 
files_1 = path
files = [os.path.join(files_1, f) for f in os.listdir(files_1)]

for file in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
    msg.attach(part)
 
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(from_address, from_password)
server.sendmail(from_address, to_address, msg.as_string())
server.quit()