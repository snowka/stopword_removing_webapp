# main.py

import os
from flask import Flask
from flask import request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

@app.route("/")
def index():
    """Renders the webpage in html and allows user input."""

    print(request.args)
    user_input = request.args.get("user_input", "")
    if user_input:
        remove_stopwords = stopword_remover(user_input)
    else:
        remove_stopwords = ""
    return (
        "<h1>Remove Stopwords</h1>"
        "<h2>This tool uses the Python Natural Language Toolkit (NLTK)<br>"
        "to remove stopwords from a phrase you enter below</h2>"
        """<form action="" method="get">
            Phrase: <input type="text" name="user_input">
            <input type="submit" value="Convert">
        </form>"""
        + "Phrase without stopwords: "
        + remove_stopwords
    )


def stopword_remover(user_input):
    """Removes stopwords listed in the NLTK package from an entered string."""

    # The following codeblock should redirect the NLTK download for the corpora and tokenizer to the
    # local folder.
    # from: https://stackoverflow.com/questions/62209018/any-way-to-import-pythons-nltk-downloadpunkt-into-google-cloud-functions/65220192#65220192
    # Be careful to the match the file structure rendered by the code block.

    root = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(root, 'nltk_data')
    os.chdir(download_dir)
    nltk.data.path.append(download_dir)

    try:
        words_in_quote = word_tokenize(user_input)
        stop_words = set(stopwords.words("english"))
        filtered_list = []
        filtered_list = [
            word for word in words_in_quote if word.casefold() not in stop_words
        ]
        return str(filtered_list)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=808, debug=True)
