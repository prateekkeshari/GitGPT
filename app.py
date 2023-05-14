from flask import Flask, render_template, request, jsonify
import os
import getpass
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ACTIVELOOP_TOKEN = os.getenv('ACTIVELOOP_TOKEN')

embeddings = OpenAIEmbeddings(disallowed_special=())
db = DeepLake(dataset_path="hub://davitbun/twitter-algorithm", read_only=True, embedding_function=embeddings)
retriever = db.as_retriever()
retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['fetch_k'] = 100
retriever.search_kwargs['maximal_marginal_relevance'] = True
retriever.search_kwargs['k'] = 10

def filter(x):
    # filter based on source code
    if 'com.google' in x['text'].data()['value']:
        return False
    
    # filter based on path e.g. extension
    metadata =  x['metadata'].data()['value']
    return 'scala' in metadata['source'] or 'py' in metadata['source']

# retriever.search_kwargs['filter'] = filter

model = ChatOpenAI(model_name='gpt-4')
qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)
chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_question():
    question = request.form.get("question")
    result = qa({"question": question, "chat_history": chat_history})
    chat_history.append((question, result['answer']))
    return jsonify({"question": question, "answer": result['answer']})

if __name__ == "__main__":
    app.run(debug=True)
