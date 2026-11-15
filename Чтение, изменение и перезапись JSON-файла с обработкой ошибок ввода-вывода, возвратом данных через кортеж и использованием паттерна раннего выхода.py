import json

settings = {"theme": "dark", "font_size": 14, "language": "ru", "notifications": True, "last_login": "2026-11-14 15:00"}

def save_settings(data, filename): 
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_settings(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file), None
    except FileNotFoundError:
        error_msg = "Ошибка: Файл не найден! (FileNotFoundError)"
        return None, error_msg
    except json.JSONDecodeError:
        error_msg = "Ошибка: В файле мусор, а не JSON! (JSONDecodeError)"
        return None, error_msg

def main():
    save_settings(settings, "user_settings.json")
    new_settings, error_msg = load_settings("user_settings.json")
    if error_msg is not None:
        print(error_msg)
        return
    new_settings["theme"] = "light"
    new_settings["font_size"] = 16
    print(new_settings)
    save_settings(new_settings, "user_settings.json")

if __name__ == "__main__":
    main()

