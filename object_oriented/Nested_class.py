class Human:
    def __init__(self,name):
        print('Human object creation')
        self.name=name
        self.head=self.Head()
    def info(self):
        print('My info')
        self.head.talk()
        self.head.brain.think()

    class Head:
        def __init__(self):
            print('Head object creation')
            self.brain=self.Brain()
        def talk(self):
            print('Talking....')
        class Brain:
            def __init__(self):
                print('Brain object creation..')
            def think(self):
                print('Thinking......')
obj=Human('Bapu')
obj.info()