from datetime import date

grad_date : date = date(2028, 6, 1)
today : date = date.today()
new_day_count = (grad_date - today).days

with open("README.md", "r", encoding="utf-8") as f:
    content_lines = f.readlines()

old_day_string = " ".join(content_lines[-1].split()[4:])
new_day_string = f"{new_day_count} day{'s' if new_day_count != 1 else ''}" if new_day_count > 0 else "🎉🎉I have Graduated !!!!🎉🎉"

content = "".join(content_lines)

new_content = content.replace(old_day_string, new_day_string)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)