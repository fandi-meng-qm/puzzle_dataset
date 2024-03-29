# The accuracy of gpt3.5 answering 100 questions based on manual judgment： 90%
# The accuracy of gpt4 answering 100 questions based on manual judgment： 91%
# 1，1，1，1，1，1，1，1，1，1
# 1，1，1，1，1，1，1，1

import json
import openai

openai.api_key = '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'

with open('jeopardy_data.json') as user_file:
    file1 = user_file.read()
data1 = json.loads(file1)
questions = []
for i in range(100):
    questions.append(data1[i]['Question'])

with open('jeopardy_data.json') as user_file:
    file1 = user_file.read()
data1 = json.loads(file1)
answers0 = []
for i in range(100):
    answers0.append(data1[i]['Answer'])


with open('jeopardy_gpt_answers.json') as user_file:
    file2 = user_file.read()
data2 = json.loads(file2)
answers1 = []
for i in range(100):
    answers1.append(data2[i]["GPT_Answer"])


# def get_completion(prompt, model="gpt-4"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0,  # Control randomness
#     )
#     return response.choices[0].message["content"]
#
#
# prompt = f"""
# Here are 100 questions and 100 correct answers, \
# as well as one person's answers to 100 questions. \
# Please tell me which of these people's answers are wrong and why based on the questions\
# and comparing them with the correct answers. Finally, \
# please count the number of correct answers from him.
#
# The 100 questions delimited with ' \
# The 100 correct answers delimited with ''\
# The 100 answers of this person delimited with '''\
#
# questions: '{questions}'
# correct answers: ''{answers0}''
# answers of this person: '''{answers1}'''
#
# """
#
# response = get_completion(prompt)
#
# print(response)

'''
The person's wrong answers and the reasons are as follows:

1. No. 14: The person answered 'Burt Lancaster' but the correct answer is 'Jim Brown'. The question was about a sportsman who also acted, not an actor who also played sports.
2. No. 22: The person answered 'Harry Selfridge' but the correct answer is '(Paul) Bonwit'. The question was about the partner of Edward Teller in selling high fashions to women.
3. No. 29: The person answered 'Sheet' but the correct answer is 'ply'. The question was about a single layer of paper.
4. No. 38: The person answered 'Teddybears' but the correct answer is 'Care Bears'. The question was about a band name.
5. No. 45: The person answered 'Pit' but the correct answer is 'the stone'. The question was about the hard interior of a peach.
6. No. 62: The person answered 'Green Day' but the correct answer is 'Billy Idol'. The question was about a punk rock hitmaker.
7. No. 64: The person answered 'Double-decker buses' but the correct answer is 'Trams (smart)'. The question was about a vehicle that returned to London in 1999.
8. No. 70: The person answered "Gulliver's Travels" but the correct answer is 'Jonathan Swift'. The question was about the author of a book, not the book itself.
9. No. 71: The person answered 'Dinghy' but the correct answer is 'Sloop (pools)'. The question was about a type of boat.
10. No. 96: The person answered 'United Kingdom' but the correct answer is 'Great Britain/England'. The question was about a kingdom, not a country.

The person got 90 out of 100 answers correct.

'''

