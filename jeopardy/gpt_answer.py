import os
import openai
import json

openai.api_key = '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'

with open('jeopardy_data.json') as user_file:
    file_contents = user_file.read()

jeopardy_data = json.loads(file_contents)
questions=[]

for i in range(100):
    questions.append(f"{i+1} {jeopardy_data[i]['Question']}.")
print(questions)

# def get_completion(prompt, model="gpt-4"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0, # Control randomness
#     )
#     return response.choices[0].message["content"]
#
# prompt = f"""
# Please answer the 100 questions correctly with one word or phrase
# The 100 questions delimited with triple backticks. \
# Format your response as a list with 100 answers.
#
# Review text: '''{questions}'''
# """
# response = get_completion(prompt)
# print(response)

# response = ["Copernicus", "Jim Thorpe", "Arizona", "McDonald's", "John Adams", "Ant", "Appian Way", "Michael Jordan", "Washington", "Crate & Barrel", "Jackie Gleason", "Cud", "Sri Lanka", "Jim Brown", "UV Index", "Bulova", "Jesse James", "Imp", "First International", "Lou Gehrig", "Morocco", "Paul Poiret", "Hattie McDaniel", "Era", "Indian National Congress", "Wilt Chamberlain", "K2", "Ethan Allen", "Ply", "Scotland", "Miley Cyrus", "Skin", "48", "Dribble", "Heart", "Yerevan", "Jonas Brothers", "Water", "98", "SONAR", "Dart", "Easter Island", "Avril Lavigne", "Stone", "360", "Jacks", "Part", "Egypt", "Colbie Caillat", "Leaves", "750", "Moonwalk", "Chart", "Ellis Island", "OneRepublic", "Buds", "2070", "Springboard", "Mozart", "Princess Diana", "The West Wing", "Tokyo", "Avril Lavigne", "Heart of Darkness", "Double-decker bus", "Elizabeth I", "James Brolin", "Bangkok", "Ivan the Terrible", "Jonathan Swift", "Sailboat", "Cleopatra", "The Monkees", "Prague", "John Cleese", "Ayn Rand", "Coca-Cola", "Queen Victoria", "The Love Boat", "Nairobi", "Isaiah", "On the Origin of Species", "Shakespeare", "Isabella", "Will Ferrell", "Rome", "Lee Iacocca", "Wonk", "Enamel", "Mrs. O'Leary's", "United Kingdom", "World Trade Center", "Pulp Fiction", "Pupil", "Half-life", "Pikes Peak", "India", "San Francisco", "Speed", "Whip"]
response = ["Copernicus", "Jim Thorpe", "Arizona", "McDonald's", "John Adams", "Ant", "Appian Way", "Michael Jordan", "Washington", "Crate & Barrel", "Jackie Gleason", "Cud", "Sri Lanka", "Burt Lancaster", "UV index", "Bulova", "Jesse James", "Imp", "Internationals", "Lou Gehrig", "Morocco", "Harry Selfridge", "Hattie McDaniel", "Era", "Indian National Congress", "Wilt Chamberlain", "K2", "Ethan Allen", "Sheet", "England", "Miley Cyrus", "Skin", "48", "Dribble", "Heart", "Yerevan", "Teddybears", "Water", "98", "Sonar", "Dart", "Easter Island", "Avril Lavigne", "Pit", "360", "Jacks", "Part", "Egypt", "Colbie Caillat", "Leaves", "750", "Moonwalk", "Chart", "Ellis Island", "OneRepublic", "Blossoms", "2070", "Trampoline", "Mozart", "Diana", "The West Wing", "Tokyo", "Green Day", "Heart of Darkness", "Double-decker buses", "Elizabeth I", "James Brolin", "Bangkok", "Ivan the Terrible", "Gulliver's Travels", "Dinghy", "Cleopatra", "The Monkees", "Prague", "Eric Idle", "Ayn Rand", "Evian", "Queen Victoria", "The Love Boat", "Nairobi", "Isaiah", "On the Origin of Species", "Dew", "Isabella I", "Will Ferrell", "Rome", "Lee Iacocca", "Wonk", "Enamel", "Mrs. O'Leary's Cow", "United Kingdom", "World Trade Center", "Pulp Fiction", "Pupil", "Half-life", "Pike's Peak", "India", "San Francisco", "Speed", "Lash"]

gpt_answer=[]
for i in range(100):
    gpt_answer.append({"GPT_Answer":response[i]})

print(gpt_answer)

data = json.dumps(gpt_answer, indent=1)
with open("jeopardy_gpt_answers.json", 'w', newline='\n') as f:
    f.write(data)
