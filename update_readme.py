from datetime import date

grad_date : date = date(2028, 6, 1)
today : date = date.today()
new_day_count = (grad_date - today).days

with open("README.md", "r", encoding="utf-8") as f:
    content_lines = f.readlines()

grad_line_list = content_lines[-1].split()

if new_day_count > 0:
    grad_line_list[-2] = str(new_day_count)
    grad_line_list[-1] = f"day{'s' if new_day_count !=1 else ''}"
else:
    grad_line_list[-2] = "🎉🎉I have Graduated !!!!🎉🎉"
    grad_line_list.pop()

old_grad_line = content_lines[-1]
new_grad_line = " ".join(grad_line_list)

content = "".join(content_lines)

new_content = content.replace(old_grad_line, new_grad_line)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)