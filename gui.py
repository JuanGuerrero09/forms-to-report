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

def get_dropdown_options():
    data = get_formated_answers()
    ids = get_ids(data)
    return create_dropdown_option(ids)


def main(page: ft.Page):
    page.title = "Report Generator"
    page.window_height = 400
    page.window_width = 800
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    if (not exists('questions.json')):
        get_raw_questions()

    title = ft.Text('Get Reports', size=30)
    page.add(title)

    ## TODO ADD A BUTTON TO GET QUESTIONS AND ONE TO GET ANSWERS

    def create_report_button(e):
        extra_text.value = f"Creating report..."
        data = get_formated_answers()
        visit = find_element_by_id(data, dd.value)
        generate_report(visit)
        extra_text.value = f"Report created:  {dd.value}"
        page.update()

    def get_data_button(e):
        get_raw_answers()
        dd.disabled = False
        b.disabled = False
        dropdown_options = get_dropdown_options()
        dd.options = dropdown_options
        page.update()

    t = ft.ElevatedButton(text="Get Data from Form", on_click=get_data_button)
    b = ft.FilledButton(text="Create Report", on_click=create_report_button)
    dd = ft.Dropdown(
        width=400,
        options= get_dropdown_options() if exists('answers.json') else None
    )
    extra_text = ft.Text()
    menu = ft.Row(controls=[t, dd, b])
    menu.alignment = ft.MainAxisAlignment.CENTER

    if(not exists('answers.json')):
        dd.disabled = True
        b.disabled = True
    page.add(menu)
    page.add(extra_text)
    


ft.app(target=main)