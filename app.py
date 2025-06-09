
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'הלוואה' in incoming_msg:
        msg.body("תודה שפנית אלינו! נבדוק את התנאים הטובים ביותר להלוואה ונתקדם.")
    else:
        msg.body("שלום! כתוב 'הלוואה' כדי להתחיל תהליך קבלת הצעה.")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
