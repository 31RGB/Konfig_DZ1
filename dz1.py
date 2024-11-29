import os
import subprocess

# Функция для выполнения команды в командной строке
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Создание виртуальной файловой системы
virtual_fs_path = "/tmp/virtual_fs"
os.makedirs(virtual_fs_path, exist_ok=True)

# Создание логического файла
log_file_path = os.path.join(virtual_fs_path, "log.json")
with open(log_file_path, "w") as log_file:
    log_file.write("{}")

# Создание стартового скрипта
start_script_path = os.path.join(virtual_fs_path, "start.sh")
with open(start_script_path, "w") as start_script:
    start_script.write("#!/bin/bash\n")
    start_script.write("echo 'Start script executed'\n")
os.chmod(start_script_path, 0o755)

# Основной цикл для обработки команд
current_path = virtual_fs_path
while True:
    command = input(f"{current_path}> ")
    if command == "exit":
        break
    elif command.startswith("cd "):
        new_path = os.path.join(current_path, command[3:].strip())
        if os.path.isdir(new_path):
            current_path = new_path
        else:
            print("Directory not found")
    elif command == "ls":
        print("\n".join(os.listdir(current_path)))
    elif command == "tree":
        print(run_command(f"tree {current_path}"))
    elif command == "du":
        print(run_command(f"du -sh {current_path}/*"))
    elif command.startswith("echo "):
        print(command[5:])
    else:
        print("Unknown command")
