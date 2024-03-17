import json
import pandas as pd
import re

def parse_log_file(log_file_content):
    # Создаем пустой DataFrame для заполнения таблицы
    columns = ["Test", "File", "Line", "Error Message", "@report.external_id", "@report.work_item_ids"]
    data = []
    result_df = pd.DataFrame(data, columns=columns)

    # Регулярное выражение для извлечения идентификаторов из строки вида "@report.external_id('7e879e1e-9732-49af-bfea-e6f74f5a6627')"
    external_id_pattern = re.compile(r"@report.external_id\('([^']+)'\)")
    work_item_ids_pattern = re.compile(r"@report.work_item_ids\('([^']+)'\)")

    # Распарсим лог-файл
    for line in log_file_content.split("\n"):
        try:
            if line.strip():  # Пропускаем пустые строки
                log_entry = json.loads(line)
                if log_entry.get("outcome") == "failed":
                    test_name = log_entry["nodeid"]
                    file_path = test_name.split("::")[0]
                    # Извлекаем имя теста (без пути и имени файла)
                    test_name = test_name.split("::")[-1]

                    line_number = log_entry.get("location", [])[1]
                    error_message = log_entry["longrepr"]["reprcrash"].get("message", "")
                    reprentries = log_entry["longrepr"]["reprtraceback"].get("reprentries", "")

                    # Извлечение значений новых столбцов из log_entry
                    external_id_match = external_id_pattern.search(line)
                    external_id = external_id_match.group(1) if external_id_match else ""
                    work_item_ids_match = work_item_ids_pattern.search(line)
                    work_item_ids = work_item_ids_match.group(1) if work_item_ids_match else ""

                    result_df = pd.concat([result_df, pd.DataFrame({
                        "Test": [test_name],
                        "File": [file_path],
                        "Line": [line_number],
                        "Error Message": [error_message],
                        "@report.external_id": [external_id],
                        "@report.work_item_ids": [work_item_ids],
                    })], ignore_index=True)
        except (json.JSONDecodeError, TypeError, KeyError):
            pass  # Пропускаем строки, которые не являются JSON или имеют неверный формат

    return result_df

log_file_path = "results_test.log"

with open(log_file_path, "r") as log_file:
    log_file_content = log_file.read()

# Парсим лог-файл
result_df = parse_log_file(log_file_content)

# Сохраняем DataFrame в файл CSV
result_df.to_csv("results_test.csv", index=False, encoding='utf-8-sig')

print("DataFrame сохранен в файл results_test.csv")
