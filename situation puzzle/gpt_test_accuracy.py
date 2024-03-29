# The accuracy of gpt3.5 answering 100 questions based on manual judgment： 90%
# The accuracy of gpt3.5 answering 100 questions based on manual judgment： 92%
# 1，1，1，1，1，1，1，1，1，1
# 1，1，1，1，1，1，1，1

import json
import openai

openai.api_key = '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'

with open('sp_data.json') as user_file:
    file1 = user_file.read()
data1 = json.loads(file1)
questions = []
for i in range(100):
    questions.append(data1[i]['Question'])

with open('sp_data.json') as user_file:
    file1 = user_file.read()
data1 = json.loads(file1)
answers0 = []
for i in range(100):
    answers0.append(data1[i]['Answer'])


with open('riddle_gpt_answers.json') as user_file:
    file2 = user_file.read()
data2 = json.loads(file2)
answers1 = []
for i in range(100):
    answers1.append(data2[i]["GPT_Answer"])


def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # Control randomness
    )
    return response.choices[0].message["content"]


prompt = f"""
Here are 100 riddle questions and 100 correct answers, \
as well as one person's answers to 100 questions. \
Please tell me which of these people's answers are wrong and why based on the questions\
and comparing them with the correct answers. \
Finally, please count the number of correct answers from they.

The 100 questions delimited with ' \
The 100 correct answers delimited with ''\
The 100 answers of this person delimited with '''\

questions: '{questions}'
correct answers: ''{answers0}''
answers of this person: '''{answers1}'''

"""

response = get_completion(prompt)

print(response)



'''

The person's wrong answers and the reasons are:

3. 'Paris' - The correct answer is 'The letter F is the only capital letter in France'. The question is a play on words, asking for the capital letter in the word 'France', not the capital city of France.

13. 'They are all below deck' - The correct answer is 'They were all married'. The question is a play on words, implying that you can't see the people because they are all below deck, but the actual reason is that they are all married, so you don't see a 'single' person.

30. 'Kangchenjunga' - The correct answer is 'It was still Mt. Everest'. Before Mt. Everest was discovered, it was still the tallest mountain, it just hadn't been discovered yet.

35. "The egg won't crack the concrete floor" - The correct answer is 'Concrete floors are very hard to crack'. The question is a play on words, implying that the egg won't crack because the concrete floor is very hard.

48. 'A refrigerator' - The correct answer is 'A river'. The question is a play on words, implying that a refrigerator is always running but never gets hot, but the actual answer is a river, which is always running but never gets hot.

64. 'They were all on different roads' - The correct answer is 'They all made right-hand turns'. The question is a play on words, implying that the cars didn't crash because they were on different roads, but the actual reason is that they all made right-hand turns, which would prevent them from crashing into each other.

67. 'Plates' - The correct answer is 'Cutlery'. The question is a play on words, implying that you buy plates to eat but never consume them, but the actual answer is cutlery, which you buy to eat but never consume.

76. 'He is walking' - The correct answer is 'He was walking'. The question is a play on words, implying that the bus driver is walking, not driving, so he doesn't get stopped by the cops.

79. 'A hot dog' - The correct answer is 'A hot dog!'. The question is a play on words, implying that a chihuahua in the summer is a hot dog.

83. 'The 26th' - The correct answer is 'The 27th'. The question is asking for the day after tomorrow if the day before yesterday was the 23rd, which would be the 27th.

The person got 90 out of 100 answers correct.

'''