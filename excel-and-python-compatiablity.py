from openpyxl import Workbook, load_workbook 
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

data = {
    "Alex": {
        "Bingus": 100,
        "Bongus": 99,
        "metagaming": 0,
        "sponsorship": 50
    },
    "Tanya": {
        "Nya": 80,
        "Horny": 10000,
        'gaming': 30,
        'gayming': 99,
        'headpats': 100
    },
    "Hot Floppa": {
        'Spicyness': 80,
        'loyalty': 99,
        'free realestate': 100
    },
    'Sogga': {
        'henlo': 80,
        'best boy': 50,
        'in love with floppa': 100,
        "loves you": 90
    },
}










wb = Workbook
dest_filename = "Created-Spreadsheet.xlsx"

# ws = wb.active

# for row in range(1,11):
#     for col in range (1,5):
#         char = get_column_letter(col)
#         ws[char + str(row)] = char + str(row)

# ws.unmerge_cells("A1:D1")

# ws.move_range('C1:d5', rows=8, cols=5)
# ws.insert_row(row)
# ws.instert_cols(colounm) 




wb.save('')
