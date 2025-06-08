from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        incoming_msg = request.values.get("Body", "").lower()
        from_number = request.values.get("From", "")

        # Basic response simulation
        if "שלום" in incoming_msg:
            response_msg = "שלום וברוך הבא! אני בוט הלוואות. מה סכום ההלוואה שתרצה?"
        else:
            response_msg = "תודה שפנית! תוכל לרשום 'שלום' כדי להתחיל."

        return f"<Response><Message>{response_msg}</Message></Response>"
    return "Bot is running."

if __name__ == "__main__":
    app.run(debug=True)
