from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app=Flask(__name__)

cb=ChatBot(
    "Hung",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_url='sqlite:///database.sqlite3' 
)
trainer = ChatterBotCorpusTrainer(cb)
trainer.train("chatterbot.corpus.english.movie")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText= request.args.get('msg')
    return str(cb.get_response(userText))

if __name__ == "__main__":
    app.run()

