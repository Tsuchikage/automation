import os
import json
import pandas as pd
import re


def parse_log_files(log_files):
    # Создаем пустой DataFrame для заполнения таблицы
    columns = ["Module_Name", "File_Path", "Test_Name", "Test_Type", "Test_Marks", "External_Id", "Work_Item_Ids",
               "Error_Message",
               "Test_Code", "Cause"]
    data = []
    result_df = pd.DataFrame(data, columns=columns)

    # Регулярное выражение для извлечения идентификаторов из строки вида
    # "@report.external_id('7e879e1e-9732-49af-bfea-e6f74f5a6627')"
    external_id_pattern = re.compile(r"@report.external_id\('([^']+)'\)")
    work_item_ids_pattern = re.compile(r"@report.work_item_ids\('([^']+)'\)")

    # Распарсим лог-файл
    for log_file_path in log_files:
        with open(log_file_path, "r") as log_file:
            log_file_content = log_file.read()

        for line in log_file_content.split("\n"):
            try:
                if line.strip(): # Пропускаем пустые строки
                    log_entry = json.loads(line)
                    if log_entry.get("outcome") == "failed":
                        test_name = log_entry["nodeid"]
                        file_path = test_name.split("::")[0]
                        # Извлекаем имя теста (без пути и имени файла)
                        test_name = test_name.split("::")[-1]

                        # Разбиваем file_path на части
                        parts = file_path.split("/")
                        # Извлекаем имя модуля
                        module_name = parts[1]

                        error_message = log_entry["longrepr"]["reprcrash"].get("message", "")
                        # line_number = log_entry["longrepr"]["reprcrash"].get("lineno", "")
                        reprentries = log_entry["longrepr"]["reprtraceback"].get("reprentries", "")

                        # Извлечение значений новых столбцов из log_entry
                        external_id_match = external_id_pattern.search(line)
                        external_id = external_id_match.group(1) if external_id_match else ""
                        work_item_ids_match = work_item_ids_pattern.search(line)
                        work_item_ids = work_item_ids_match.group(1) if work_item_ids_match else ""

                        # Извлекаем строки и номера строк из reprentries и longrepr
                        lines = []
                        for entry in reprentries:
                            if "data" in entry and "lines" in entry["data"]:
                                lines.extend(entry["data"]["lines"])

                        keywords = log_entry.get("keywords", {})
                        marks = []
                        test_type = ""
                        for keyword in keywords:
                            if keyword in ["health_check", "smoke_api", "smoke_ui", "abac", "critical_way_api",
                                           "critical_way_ui", "sanity"]:
                                marks.append(keyword)
                            if "api" in keyword:
                                test_type = "api"
                            elif "ui" in keyword:
                                test_type = "ui"

                        result_df = pd.concat([result_df, pd.DataFrame({
                            "Module_Name": [module_name],
                            "File_Path": [file_path],
                            "Test_Name": [test_name],
                            "Test_Type": [test_type],
                            "Test_Marks": [", ".join(marks)],
                            "External_Id": [external_id],
                            "Work_Item_Ids": [work_item_ids],
                            # "Error_Line": [line_number],
                            "Error_Message": [error_message],
                            "Test_Code": ["\n".join(lines)],
                            "Cause": [""]
                        })], ignore_index=True)
            except (json.JSONDecodeError, TypeError, KeyError):
                pass  # Пропускаем строки, которые не являются JSON или имеют неверный формат

    return result_df


# Получение списка всех файлов .log в папке "logs"
log_files = [os.path.join("logs", file) for file in os.listdir("logs") if file.endswith(".log")]

# Парсим все лог-файлы
result_df = parse_log_files(log_files)

# Сохраняем DataFrame в файл CSV, режим 'a' для добавления данных к существующему файлу
result_df.to_csv("results.csv", mode='a', index=False, header=not os.path.exists("results.csv"), encoding='utf-8-sig')

print("Результаты всех лог-файлов сохранены в файл results.csv")
