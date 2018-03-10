class Person(object):
    def __init__(self, name):
        self.name = name
        self.friends = []

    def greet(self):
        print 'Hello, %s! Nice to meet you!' % (self.name)

    def introduce(self, new_friend):
        self.friends.append(new_friend.name)
        print '%s made friends with %s' % (self.name, new_friend.name)
