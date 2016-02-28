from datetime import date
from PIL import Image

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError

class Article(Content):

    def __init__(self, year, month, day, headline, content, contributors):
        
        super(Article, self).__init__(year, month, day, contributors)

        self.headline = headline

        self.content = content

    def show(self):
        print self.headline
        print "-" * 80
        print "Creation Date: {0}".format(self.creation_date.strftime("%A, %B, %d"))
        print "-" * 80
        r = self.contributors[0]
        if len(self.contributors) > 1:
            for contributor in self.contributors[1:len(self.contributors)]:
                r += contributor + ', '
        print "Contributors: {0}".format(r)
        print "-" * 80
        print self.content

class Picture(Content):
    
    def __init__(self, year, month, day, title, caption, path, contributors):

        super(Picture, self).__init__(year, month, day, contributors)

        self.title = title

        self.caption = caption

        self.path = path

    def show(self):
        print self.title
        print "-" * 80
        print "Creation Date: {0}".format(self.creation_date.strftime("%A, %B %d, %Y"))
        print "-" * 80
        print "Path: {0}".format(self.path)
        print "-" * 80
        r = self.contributors[0]
        if len(self.contributors) > 1:
            for contributor in self.contributors[1:len(self.contributors)]:
                r += ' ,' + contributor  
        print "Contributors: {0}".format(r)
        print "-" * 80
        print "Caption: {0}".format(self.caption)
        im = Image.open(self.path)
        im.show()



