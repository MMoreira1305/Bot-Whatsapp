from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from BancoPalavras import apresentacao
from Respostas import Respostas

app = Flask(__name__)
respostas = Respostas()

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    responded_first_question = False
    responded = False
    
    for word in apresentacao:
        if word.lower() in incoming_msg:
            responded_first_question = True
            responded = True
            msg.body(respostas.respostaInicial())
            break
   
    if str(1) == incoming_msg:
        responded = True
        msg.body(respostas.respostaDoNumero1())
    
    elif str(2) == incoming_msg:
        responded = True
        msg.body(respostas.respostaDoNumero2())

    elif str(3) == incoming_msg:
        responded = True
        msg.body(respostas.respostaDoNumero3())

    elif str(4) == incoming_msg:
        responded = True
        msg.body(respostas.respostaDoNumero4())
    
    elif str(5) == incoming_msg:
        responded = True
        msg.body(respostas.respostaDoNumero5())

    elif str(6) == incoming_msg:
        responded = True
        msg.body(respostas.respostaInicial())

    elif str(7) == incoming_msg:
        responded = True
        msg.body("Chat finalizado")
    
    if not responded:
        msg.body(respostas.respostaNulaComeco())
    
    return str(resp)

if __name__ == '__main__':
    app.run()