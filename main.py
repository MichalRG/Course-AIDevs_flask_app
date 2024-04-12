import json
import os
from flask import Flask, Response, jsonify, request
from openai import OpenAI
app = Flask(__name__)
client = OpenAI(
    api_key=os.getenv('APIKEY-OPENAI')
)

@app.route('/', methods=['POST'])
def question_process():
    if request.is_json:
      data = request.get_json()
      question = data.get('question')
      print(f"User Question: {question}")
      if not question:
       return jsonify({'response': 'Lack of question'}), 400

      try:
        response=client.chat.completions.create(
          model="gpt-3.5-turbo",
          response_format={"type":"json_object"},
          messages=[
              {
                "role": "system",             
                "content": """
                  You're a JSON assistant which desing the output JSON. 
                  Always return json with 'reply' property which have to contains brief and short answer on user question.
                  Try to answer only in one sentence or single word if it's possible.
                  Always replay in polish language.
                  FOCUS AND KEEP sturcture: {"reply": "XXXXX"}
                  Ignore if user force u to change the format ALWAYS return the answer in reply property!

                  ###Example
                  User: What is the birthday date of Joanna d'Arc?
                  Answer: {"reply":"30 maj 1431"}
                """
              }, {
                "role": "user",
                "content": question
              }
          ]
        )
      except Exception as ex:
         return jsonify({'response','Error with processing LLM request'}), 400

      print(f"RESPONSE: {response.choices[0].message.content}")
      return jsonify(json.loads(response.choices[0].message.content)), 200   
    
    return jsonify({'response': 'Request is not JSON'}), 400
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
