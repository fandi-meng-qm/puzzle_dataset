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

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # Control randomness
    )
    return response.choices[0].message["content"]

prompt = f"""
Please answer all the 100 riddles correctly with one word or phrase
The 100 questions delimited with triple backticks. \
Format your response in order as a list.

Review text: '''{questions}'''
"""
response = get_completion(prompt)
print(response)

# response = [
#     "Silence",
#     "Lunch and Dinner",
#     "Paris",
#     "Nothing",
#     "Glass",
#     "With a pumpkin patch",
#     "Its lid",
#     "A cold",
#     "A stamp",
#     "A mushroom",
#     "When it's ajar",
#     "An envelope",
#     "They are all below deck",
#     "Bookkeeper",
#     "C",
#     "Post Office",
#     "Edam",
#     "Light",
#     "Day and Night",
#     "The man himself",
#     "A coffin",
#     "Darkness",
#     "Electric trains don't produce smoke",
#     "In a dictionary",
#     "NOON",
#     "W",
#     "The letter R",
#     "Incorrectly",
#     "Your name",
#     "Halfway, then you are walking out of the forest",
#     "Kangchenjunga",
#     "A hole",
#     "Smiles",
#     "Hiss and Hers",
#     "The egg won't crack the concrete floor",
#     "Chicago",
#     "To the dock",
#     "Because it has Greece at the bottom",
#     "A tongue",
#     "The library",
#     "Your legs",
#     "A garbage truck",
#     "All of them",
#     "A palm",
#     "A teapot",
#     "A deck of cards",
#     "The letter G",
#     "They are both in the middle of water",
#     "A relationship",
#     "A priest",
#     "Wet",
#     "A yardstick",
#     "A foot",
#     "A feather",
#     "A bottle",
#     "A clock",
#     "A refrigerator",
#     "The letter M",
#     "Corn on the cob",
#     "SWIMS",
#     "SEE O DOUBLE YOU",
#     "The letter E",
#     "Queue",
#     "Stone",
#     "A bank",
#     "Alphabet",
#     "A plant",
#     "An echo",
#     "Your photograph",
#     "An anchor",
#     "They were all on different roads",
#     "A secret",
#     "Fire",
#     "Plates",
#     "Your breath",
#     "Footsteps",
#     "A river",
#     "9",
#     "Ton",
#     "Your left hand",
#     "A promise",
#     "They are a grandfather, father, and son",
#     "Your mother",
#     "They were born in different time zones",
#     "He is bald",
#     "He is walking",
#     "Seven",
#     "A hot dog",
#     "A carrot",
#     "Frostbite",
#     "Because they are always stuffed",
#     "David",
#     "A kitten",
#     "The 26th",
#     "Counterfeit money",
#     "Eat",
#     "B is A's daughter",
#     "The word 'and'",
#     "Because it got the salsa",
#     "Goldfish"
# ]
#
# #
# gpt_answer=[]
# for i in range(100):
#     gpt_answer.append({"GPT_Answer":response[i]})
#
# print(gpt_answer)
#
# data = json.dumps(gpt_answer, indent=1)
# with open("riddle_gpt_answers.json", 'w', newline='\n') as f:
#     f.write(data)
