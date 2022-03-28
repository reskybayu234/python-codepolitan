def create_html(tag, text):
    html = f"<{tag}>{text}</{tag}>"
    return html

html = create_html("p","Hello Python")
print(html)
html = create_html("a","ini link")
print(html)

print(" ")
print("="*50)
print(" ")

def create_html2(tag,text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key} = '{value}'"

    html = html + f"> {text}</{tag}"
    return html

html = create_html2("p","Hello Python")
print(html)
html = create_html2("a","ini link", href="www.google.com", style="link")
print(html)