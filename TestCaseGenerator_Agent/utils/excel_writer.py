from openpyxl import Workbook
import os
from datetime import datetime


def save_to_excel(test_cases, base_name="test_cases"):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"{base_name}_{timestamp}.xlsx"
    file_path = os.path.join(output_dir, file_name)

    wb = Workbook()
    ws = wb.active
    ws.title = "Test Cases"

    headers = ["Test Case ID", "Precondition", "Scenario", "Steps", "Expected Result", "Actual Result", "Priority", "Test Case Type" ,"Severity" ]
    ws.append(headers)

    for tc in test_cases:
        ws.append(tc)

    wb.save(file_path)

    return file_path