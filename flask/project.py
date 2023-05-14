from flask import Flask, render_template,request
import re

def parse_logic_sentence(sentence):
    sentence = sentence.lower()
    # All A's are B's
    match = re.match(r"^all (.*) are (.*)$", sentence)
    if match:
        a = match.group(1)
        b = match.group(2)
        return f"∀X ({a}(X) ⇒ {b}(X))"
    # No A's are B's
    match = re.match(r"^no (.*) are (.*)$", sentence)
    if match:
        a = match.group(1)
        b = match.group(2)
        return f"∀X ({a}(X) ⇒ ~{b}(X))"
    # Some A's are B's
    match = re.match(r"^some (.*) are (.*)$", sentence)
    if match:
        a = match.group(1)
        b = match.group(2)
        return f"∃X ({a}(X) & {b}(X))"
    # Some A's are not B's
    match = re.match(r"^some (.*) are not (.*)$", sentence)
    if match:
        a = match.group(1)
        b = match.group(2)
        return f"∃X ({a}(X) & ~{b}(X))"
    # All and only A's are B's
    match = re.match(r"^all and only (.*) are (.*)$", sentence)
    if match:
        a = match.group(1)
        b = match.group(2)
        return f"∀X ({a}(X) ⇔ {b}(X))"
    # Only A's are B's
    match = re.match(r"^only (.*) are (.*)$", sentence)
    if match:
        a = match.group(1)
        b = match.group(2)
        return f"∀X ({b}(X) ⇒ {a}(X))"
    # Not all A's are B's
    match = re.match(r"^not all (.*) are (.*)$", sentence)
    if match:
        a = match.group(1)
        b = match.group(2)
        return f"∃X ({a}(X) & ~{b}(X))"
    # All A's are not B's
    match = re.match(r"^all (.*) are not (.*)$", sentence)
    if match:
        a = match.group(1)
        b = match.group(2)
        return f"∀X ({a}(X) ⇒ ~{b}(X))"
    return None
# Example usage


app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        paragraphs=request.form.get('paragraphs')
        logic_expr = parse_logic_sentence(paragraphs)
        output=f"{paragraphs} -> {logic_expr}"
        if request.form.get('convert') == 'convert':
            return render_template("home.html",sentence=output)
    return render_template("home.html")
    

if __name__ == '__main__':
    app.run(debug=True,port=4000)