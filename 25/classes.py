class wolf:
    classification = 'canine'
    habitat = 'forest'
    sleeping = False

    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def wake_up(self):
        self.sleeping = False

    def sleep(self):
        self.sleeping = True

    def sleep_state(self):
        if self.sleeping == False:
            return self.name + ' is awake'
        else:
            return self.name + ' is sleeping'


silver = wolf('silvertooth', 5)
print(silver.sleep_state())

silver.sleep()

print(silver.name)
print(silver.habitat)
