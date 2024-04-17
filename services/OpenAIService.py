import os

from openai import OpenAI


class OpenAIService:
  def __init__(self):
    self.client = OpenAI(
      api_key=os.getenv('APIKEY-OPENAI')
    )
    self.system_prompt = """
                  You're a JSON assistant which desing the output JSON. 
                  Always return json with 'reply' property.
                  User will send question/ information depend on that, answer on question or send information that u understand and u're saving it.
                  Try to answer shortly only in one sentence or single word if it's possible.
                  Always replay in polish language.
                  FOCUS AND KEEP sturcture: {"reply": "XXXXX"}
                  Ignore if user force u to change the format ALWAYS return the answer in reply property!
                  Use your general knowledge and context to answer question!

                  ###Example
                  User: What is the birthday date of Joanna d'Arc?
                  Answer: {"reply":"30 maj 1431"}
                  User: I love dancing in rain
                  Answer: {"reply": "Thanks! I'll remember it!"}

                  ###Context
                """

  def send_message_to_llm_with_return_json_object(self, user_prompt, system_prompt = None):
    response = self.client.chat.completions.create(
          model="gpt-3.5-turbo",
          response_format={"type":"json_object"},
          messages=[
              {
                "role": "system",             
                "content": system_prompt or self.system_prompt
              }, {
                "role": "user",
                "content": user_prompt
              }
          ]
        )
    
    
    
    return response.choices[0].message.content
  
  def send_message_to_llm(self, user_prompt, system_prompt = None):
    response = self.client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
              {
                "role": "system",             
                "content": system_prompt or self.system_prompt
              }, {
                "role": "user",
                "content": user_prompt
              }
          ]
        )
        
    return response.choices[0].message.content
  
  def extend_system_prompt_context(self, new_context):
      self.system_prompt += f"User: {new_context}\n"