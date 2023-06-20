import json
from export_excel import generate_report
  
# Opening JSON file
f = open('answers.json')
g = open('questions.json')

# returns JSON object as 
# a dictionary
data = json.load(f)
questions = json.load(g)

def get_questions():
    items = questions['items']
    all_questions = {}
    for item in items:
        questionItem = item.get('questionItem')
        if questionItem != None:
            question = questionItem.get('question').get('questionId')
            all_questions[question] = item['title']
    return all_questions


def get_data():
    question_list = get_questions()
    answer_list = data['responses']
    formated_answers = []

    for response in answer_list:
        answer_formated = {}
        answer_formated['email'] = response['respondentEmail']
        time = response["createTime"][0:10]
        location = ''
        # print(response["createTime"][0:10], response['answers'][next(iter(response['answers']['textAnswers']))])
        for questionId, answers in response['answers'].items():
            if 'textAnswers' in answers:
                value = answers['textAnswers']['answers'][0]['value']
                question = question_list.get(questionId)
                if questionId == '6146a411':
                    location = value
                answer_formated[question] = value
        formated_answers.append(answer_formated)
        answer_formated['id'] = f'{time}-{location}'
    
    return formated_answers
       


def get_ids(info):
    return [x.get('id') for x in info]

def find_element_by_id(arr, id):
    for element in arr:
        if element.get('id') == id:
            return element
    return None

info = get_data()
selected_report = find_element_by_id(info, '2023-05-31-Tbilisi')


# generate_report(selected_report)