class Balloon(object):
    def __init__(self, color, size, shape):
        self.color = color
        self.size = size
        self.shape = shape
        self.inflated = False
        self.working = True

    def paint(self, color):
        self.color = color

    def inflate(self):
        if self.working:
            if self.inflated:
                self.explode()
            else:
                self.inflated = True
        else:
            print "You exploded this balloon. It can no longer be inflated."

    def explode(self):
        self.inflated = False
        self.working = False
        print "BANG!"

    def deflate(self):
        if self.inflated:
            self.inflated = False
        else:
            print "This Balloon is already deflated. It can't be deflated any farther."


class BigGreenRoundBalloon(Balloon):
    def __init__(self):
        super(Balloon, self).__init__('green', 'Big', 'round')


balloon = BigGreenRoundBalloon()
balloon.paint('red')
