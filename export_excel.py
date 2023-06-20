import xlsxwriter
import os


def generate_report(data):

    excel_name = 'Report' 

    workbook = xlsxwriter.Workbook(f'{excel_name}.xlsx')
    worksheet = workbook.add_worksheet('Data')

    worksheet.set_paper(9)
    worksheet.center_horizontally()
    worksheet.set_header('&CHello')


    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
    ital = workbook.add_format({'italic': True})
    # Add a number format for cells with money.
    # number_format = workbook.add_format({'num_format': '#,##'})
    # Adjust the column width.
    # Create a format to use in the merged range.
    title_format = workbook.add_format(
        {
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "fg_color": "#CCFFFF",
        }
    )

    cells_format = workbook.add_format(
        {
            
            "align": "center",
            "valign": "vcenter",
        }
    )

    group_format = workbook.add_format(
        {
            "border": 1,
            "align": "center",
            "valign": "vcenter",
        }
    )

    row = 1
    col = 1

    worksheet.set_column('B:B', 65, cell_format=cells_format)
    worksheet.set_column('C:C', 25, cell_format=cells_format)
    # worksheet.set_column('D:D', 25, cell_format=cells_format)
    # worksheet.merge_range('B1:D1', 'Channel Report',title_format)
    # worksheet.set_row(0, 40)


    row += 1


    for key in data:
        initial_row = row
        worksheet.write(row, col, key, bold)
        worksheet.write(row, col + 1, data[key], ital)
        row += 1  
        final_row = row



    row+=1


    # worksheet.insert_image('E2', './logo.png')

    worksheet.print_area(0,0, row, col + 1)

    workbook.close()

    os.system(f"start EXCEL.EXE {excel_name}.xlsx")