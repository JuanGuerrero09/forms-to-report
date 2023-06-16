import json
  
# Opening JSON file
f = open('sample.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
question_list = {
    "4b45ab37": "Tiempo de visita",
    "1903a5b1": "In what year did the United States land a mission on the moon?",
    "0f9b95c0": "Fecha de visita",
    "7edf2a1b": "Ubicacion",
    "34852e97": "Reporte",
    "5cbe24de": "Estado de visita",
}
def get_data(data):
    answer_list = data['responses']
    formated_answers = []

    for response in answer_list:
        answer_formated = {}
        answer_formated['email'] = response['respondentEmail']
        for questionId, answers in response['answers'].items():
            value = answers['textAnswers']['answers'][0]['value']
            question = question_list.get(questionId)
            answer_formated[question] = value
        formated_answers.append(answer_formated)
    
    print(formated_answers)
       

    # print(answer_list)

get_data(data)