import time

class ToDoList:
    def __init__(self, heading='', color='yellow'):
        self.content = None
        self.check = False
        self.heading = heading
        self.color = color
        self.time = time.ctime(time.time())

    def put_check(self, done):
        if not isinstance(done, bool):
            raise Exception
        else:
            self.check = done

    def put_text(self, content):
        self.content = content

    def get_text(self):
        return self.content

    def get_list(self):
        return {'Heading': self.heading, 'Content': self.content, 'Color': self.color, 'Time': self.time,
                'Check': self.check}


if __name__ == '__main__':
    list1 = ToDoList("TO DO LIST")
    list1.put_text("Made new list")
    print(list1.get_list())


