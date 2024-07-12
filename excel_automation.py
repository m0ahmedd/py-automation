from openpyxl import Workbook
from win32com.client import Dispatch
import os

# Creating a new folder to store the Excel files if it doesn't exist.
folder_name = "Excel Files"
os.makedirs(folder_name, exist_ok=True)

# Creating a new workbook and setting the filename and path.
filename = os.path.join(folder_name,"CodeAlpha.xlsx")
path = r'E:\projects\CodeAlpha_internship\python dev\Py Automation'
workbook = Workbook()

#A workbook is always created with at least one worksheet. You can get it by using the Workbook.active property:
worksheet = workbook.active

# #Setting the title of the worksheet
# worksheet.title = "Sample Data"

worksheet["A1"] = "tti Code"
worksheet["B1"] = "Code Alpha"

# Saving the workbook
# workbook.save(filename= filename)

# To Change it's contents
cell = worksheet['A1']
cell.value = "zoz"

# Saving the workbook
workbook.save(filename= filename)

# Opening the Excel file
xl = Dispatch("Excel.Application")
xl.Visible = True
# wb = xl.Workbooks.Open(r'E:\projects\CodeAlpha_internship\python dev\Py Automation\\' + filename)
wb = xl.Workbooks.Open(os.path.join(path, filename))