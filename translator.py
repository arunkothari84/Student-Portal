import translators as Translator


class Trans:
    def __init__(self, query):
        self.translation = None
        self.query = query

    def get_translation(self, lang='en'):
        self.translation = Translator.google(self.query, if_use_cn_host=True, to_language=lang)
        return self.translation

    def get_dict(self):
        return {'Translation': self.get_translation()}


if __name__ == '__main__':
    print(Trans('My name is arun kothari').get_translation('hi'))
