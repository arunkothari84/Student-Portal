import wikipediaapi


class PageException(Exception):
    """This page DOES NOT EXIST"""
    pass


class Wiki:
    wiki = wikipediaapi.Wikipedia('en')

    def __init__(self, title, wiki=wiki):
        self.page = wiki.page(title)
        if not self.page.exists():
            raise PageException
        self.url = self.page.fullurl

    def get_url(self):
        return self.url

    def get_summary(self):
        summary = '.\n'.join([x for x in self.page.summary[0:5000].split('. ')[0:3]]) + '.'
        return summary

    def get_wiki(self):
        return {'Summary': self.get_summary(), 'URL': self.get_url()}


if __name__ == '__main__':
    print(Wiki('MEin arun kothari hu').get_wiki())
