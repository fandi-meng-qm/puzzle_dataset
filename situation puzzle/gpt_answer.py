import os
import openai
import json

openai.api_key =

with open('riddle.json') as user_file:
    file_contents = user_file.read()

riddle_data = json.loads(file_contents)
questions=[]

for i in range(100):
    questions.append(f"{i+1} {riddle_data[i]['Question']}.")
# print(questions)
#
def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # Control randomness
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-4", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

prompt = f"""
Please answer all the 100 riddles correctly with one word or phrase
The 100 questions delimited with triple backticks. \
Format your response in order as a list.

Review text: '''{questions}'''
"""
response = get_completion(prompt)
print(response)


# gpt_answer=[]
# for i in range(100):
#     gpt_answer.append({"GPT_Answer":response[i]})
#
# print(gpt_answer)
#
# data = json.dumps(gpt_answer, indent=1)
# with open("riddle_gpt_answers.json", 'w', newline='\n') as f:
#     f.write(data)
