import flet as ft
from form_manipulation import get_formated_answers, get_ids, find_element_by_id
from export_excel import generate_report
from os.path import exists
from api import get_raw_answers, get_raw_questions


def create_dropdown_option(ids):
    dropdown_options = []
    for id in ids:
        new_option = ft.dropdown.Option(id)
        dropdown_options.append(new_option)
    return dropdown_options



def main(page: ft.Page):
    page.title = "Report Generator"
    page.window_height = 400
    page.window_width = 800
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def get_dropdown_options():
        data = get_formated_answers(dd1.value)
        ids = get_ids(data)
        return create_dropdown_option(ids)

    title = ft.Text('Get Reports', size=30)
    page.add(title)

    ## TODO ADD A BUTTON TO GET QUESTIONS AND ONE TO GET ANSWERS

    def create_report_button(e):
        extra_text.value = f"Creating report..."
        data = get_formated_answers(dd1.value)
        visit = find_element_by_id(data, dd2.value)
        generate_report(visit)
        extra_text.value = f"Report created:  {dd2.value}"
        page.update()
        print('Report generated')

    def get_questions_button(e):
        if (not exists(f'{dd1.value}_questions.json')):
            get_raw_questions(dd1.value)


    def get_data_button(e):
        get_raw_answers(dd1.value)
        dd2.disabled = False
        b.disabled = False
        dropdown_options = get_dropdown_options()
        dd2.options = dropdown_options
        page.update()

    q = ft.ElevatedButton(text="Get Questions from Form", on_click=get_questions_button)
    t = ft.ElevatedButton(text="Get Answers from Form", on_click=get_data_button)
    b = ft.FilledButton(text="Create Report", on_click=create_report_button)
    dd1 = ft.Dropdown(
        width=200,
        options= create_dropdown_option(["reservoirs", "pumping stations"])
    )
    dd2 = ft.Dropdown(
        width=400,
        options= get_dropdown_options() if exists(f'{dd1.value}_answers.json') else None
    )
    extra_text = ft.Text()
    form_text = ft.Text(value="Form Type: ")
    row = ft.Row(controls=[form_text, dd1, q])
    menu = ft.Row(controls=[t, dd2, b])
    row.alignment = ft.MainAxisAlignment.CENTER
    menu.alignment = ft.MainAxisAlignment.CENTER

    if(not exists('answers.json')):
        dd2.disabled = True
        b.disabled = True
    page.add(row,  menu)
    page.add(extra_text)
    


ft.app(target=main)