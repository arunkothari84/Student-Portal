from PyDictionary import PyDictionary


class Dictionary:
    def __init__(self, query, get_synonyms=False):
        self.dictionary = PyDictionary()
        self.meaning = self.dictionary.meaning(query)
        self.synonyms = self.get_synonyms(query)
        if get_synonyms:
            self.synonyms = self.get_synonyms(query=query)

    def get_synonyms(self, query):
        return self.dictionary.getSynonyms(query)

    def get_meaning(self):
        return self.meaning

    def get_dict(self):
        dictin_empty = {'Noun': None, 'Verb': None, 'Adj': None}
        dicti = self.meaning
        if 'Noun' in dicti.keys():
            dictin_empty['Noun'] = dicti['Noun']
        if 'Verb' in dicti.keys():
            dictin_empty['Verb'] = dicti['Verb']
        if 'Adjective' in dicti.keys():
            dictin_empty['Adj'] = dicti['Adjective']
        return dictin_empty


if __name__ == '__main__':
    dictionary = Dictionary("red")
    print(dictionary.get_dict())
    dictionary = Dictionary("death", True)
    print(dictionary.get_dict())
