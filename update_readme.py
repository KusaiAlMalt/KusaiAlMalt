from datetime import date

grad_date : date = date(2028, 6, 1)
today : date = date.today()
days_left = (grad_date-today).days

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace(
    "{{ graduationCountdown }}",
    str(days_left)
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
