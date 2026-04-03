from openpyxl import Workbook
import os


def save_rtm_to_excel(rtm_data, file_name):
    wb = Workbook()
    ws = wb.active
    ws.title = "RTM"

    headers = ["Requirement ID", "Requirement", "Test Cases", "Coverage"]
    ws.append(headers)

    for row in rtm_data:
        ws.append([
            row["Requirement ID"],
            row["Requirement"],
            row["Test Cases"],
            row["Coverage"]
        ])

    os.makedirs("output", exist_ok=True)
    path = f"output/{file_name}_RTM.xlsx"
    wb.save(path)

    return path