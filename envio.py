import os
import smtplib 
from email.message import EmailMessage
from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
        <style>
            body {
                background: linear-gradient(to bottom, #87CEEB, #0071BC);
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }

            .button {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin-top: 20px;
                cursor: pointer;
                border-radius: 8px;
            }

            .container {
                text-align: center;
            }
        </style>
        <title>Envio de E-mail</title>
    </head>
    <body>
        <div class="container">
            <h1 style="color: white;">Envio de e-mail usando SAAS e PASS</h1>
            <form action="/execute" method="post">
            <input type="submit" value="Enviar E-mail" />
        </form>
        </div>
    </body>
    </html> 
    '''

@app.route('/execute', methods=['POST'])
def execute_command():
    # Configura e-mail, senha 
    EMAIL_ADDRESS = 'leonardo.moraes22012002@gmail.com'
    EMAIL_PASSWORD = 'npkj zicd hrvy bcce'

    # Criar um e-mail
    msg =  EmailMessage()
    msg['Subject'] = 'Teste de Mensagem - Aula Aldriano'
    msg['From'] = 'leonardo.moraes22012002@gmail.com'
    msg['To'] = 'l.leitedemoraes@hotmail.com'
    msg.set_content('Olá, este foi um teste de envio de mensagem para o e-mail.')

    # Enviar uma imagem 
    with open('joia.png', 'rb') as content_file:
        content = content_file.read()
        msg.add_attachment(content, maintype='application', subtype='png', filename='joia.png')

    # Enviar a mensagem 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    
