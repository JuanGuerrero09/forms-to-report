import json

def get_questions():
    g = open('questions.json')
    questions = json.load(g)
    items = questions['items']
    all_questions = {}
    questions_by_section = {}
    current_section = ''
    for item in items:
        questionSection = item.get("pageBreakItem")
        if questionSection != None:
            current_section = item.get("title")
            questions_by_section[current_section] = []
        questionItem = item.get('questionItem')
        if questionItem != None:
            question = questionItem.get('question').get('questionId')
            questions_by_section[current_section].append(question)
            all_questions[question] = item['title']
    questions_by_section['ID'] = '0'
    all_questions['0']='id'
    return questions_by_section, all_questions


def get_data():
    f = open('answers.json')
    data = json.load(f)
    question_list = get_questions()[1]
    answer_list = data['responses']
    formated_answers = []

    for response in answer_list:
        answer_formated = {}
        answer_formated['email'] = response['respondentEmail']
        time = response["createTime"][0:16]
        infraestructure = ''
        for questionId, answers in response['answers'].items():
            if 'textAnswers' in answers:
                value = answers['textAnswers']['answers'][0]['value']
                question = question_list.get(questionId)
                if questionId == '1c398b32':
                    infraestructure = value
                answer_formated[question] = value
            if 'fileUploadAnswers' in answers:
                value = answers['fileUploadAnswers']['answers']
                question = question_list.get(questionId)
                img_id_list = []
                for img in value:
                    imgId = img['fileId']
                    img_id_list.append(imgId)
                answer_formated[question] = img_id_list
        formated_answers.append(answer_formated)
        answer_formated['id'] = f'{time}-{infraestructure}'
    return formated_answers


def get_ids(info):
    return [x.get('ID') for x in info]

def find_element_by_id(arr, id):
    for element in arr:
        if element.get('ID') == id:
            return element
    return None

def get_formated_answers():
    question_by_section, question_texts = get_questions()
    data = get_data()
    all_answers = []
    # Iterar sobre cada sección en el diccionario original
    for element in data:
        # Diccionario final con las secciones, preguntas y respuestas combinadas
        combined_sections = {}
        for section, questions in question_by_section.items():
            # Combinar los elementos correspondientes en un solo diccionario
            combined = {}
            for question_id in questions:
                question_text = question_texts.get(question_id)
                if question_text:
                    answer = element.get(question_text)
                    if answer:
                        combined[question_text] = answer 
            combined_sections[section] = combined
            # Agregar el diccionario combinado a la sección correspondiente
        combined_sections['ID'] = combined_sections['ID'].get('id')
        all_answers.append(combined_sections)
    return all_answers

