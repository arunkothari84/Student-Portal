from flask import Flask, render_template, redirect, url_for, request,  jsonify
from dictionary import Dictionary
from wikipedia import Wiki, PageException
from translator import Trans
app = Flask(__name__)


# Route to index
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translator', methods=['GET'])
def translator():
    # Taking sentence from the URL
    sentence = request.args.get('sentence')
    if sentence:
        translat = Trans(sentence)
        return render_template('translator-popup.html', result=translat.get_dict())
    return render_template('translator-popup.html', result='')


@app.route('/wiki', methods=['GET'])
def wiki():
    word = request.args.get('word')
    try:
        if word:
            wiki = Wiki(word)
            return render_template('wiki-popup.html', wiki=wiki.get_wiki(), visi='visible')
        else:
            return render_template('wiki-popup.html', wiki='', visi='hidden')
    except PageException:
        return render_template('index.html')


@app.route('/dict', methods=['GET'])
def dictionary():
    word = request.args.get('word')
    dictin_empty = {'Noun': '', 'Verb': '', 'Adj': ''}
    if word:
        dictin = Dictionary(word)
        visi_adj = "hidden"
        visi_verb = "hidden"
        visi_noun = "hidden"
        dictin_empty['word'] = word.capitalize()
        try:
            dicti = dictin.get_dict()
            if dicti["Noun"]:
                dictin_empty['Noun'] = '\n'.join(dicti['Noun'])
                visi_noun = 'visible'
            if dicti["Verb"]:
                dictin_empty['Verb'] = '\n'.join(dicti['Verb'])
                visi_verb = 'visible'
            if dicti["Adj"]:
                dictin_empty['Adj'] = '\n'.join(dicti['Adj'])
                visi_adj = 'visible'
            return dict_return(dictin_empty, visi_noun, visi_verb, visi_adj)
        except:
            return dict_return(dictin_empty)
    return dict_return(dictin_empty)


@app.route('/todo', methods=['GET','POST'])
def todo():
    return render_template("ToDo-popup.html")


def dict_return(dictin, visi_noun='hidden', visi_verb='hidden', visi_adj='hidden'):
    return render_template('dictionary-popup.html', dict=dictin, visi_noun=visi_noun, visi_verb=visi_verb,
                           visi_adj=visi_adj)

if __name__ == '__main__':
    app.run(debug=True)
