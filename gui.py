import flet as ft
from form_manipulation import find_element_by_id, generate_report, get_data, get_ids

data = get_data()
ids = get_ids(data)

def create_dropdown_option(ids):
    dropdown_options = []
    for id in ids:
        new_option = ft.dropdown.Option(id)
        dropdown_options.append(new_option)
    return dropdown_options

dropdown_options = create_dropdown_option(ids)

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    title = ft.Text('Get Reports')
    page.add(title)

    def button_clicked(e):
        extra_text.value = f"Dropdown value is:  {dd.value}"
        page.add(extra_text)
        page.update()

    def get_data_button(e):
        dd.disabled = False
        b.disabled = False
        page.update()

    t = ft.ElevatedButton(text="Get Data from Form", on_click=get_data_button)
    b = ft.ElevatedButton(text="Create Report", on_click=button_clicked)
    dd = ft.Dropdown(
        width=400,
        options=dropdown_options,
    )
    extra_text = ft.Text()
    menu = ft.Row(controls=[t, dd, b])
    menu.alignment = ft.MainAxisAlignment.CENTER

    dd.disabled = True
    b.disabled = True
    page.add(menu)
    




ft.app(target=main)