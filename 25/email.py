#An Email Simulation
class Email:
    #class variables
    has_been_read, is_spam = False, False

    def __init__(self, from_address,email_contents):
        self.from_address = from_address
        self.email_contents = email_contents

    def mark_as_read(self):
        self.has_been_read = True
    
    def mark_as_spam(self):
        self.is_spam = True

inbox = []

def add_email(contents, email_address):
    new_email = Email(email_address, contents)
    inbox.append(new_email)

    #testing
    #print(new_email.from_address)
    #print(new_email.has_been_read)
    #print(new_email.is_spam)
    #print(new_email.email_contents)


add_email('blah blah', 'yi@gmail.com')
add_email('blah blah', 'yasefi@gmail.com')
add_email('blah blah', 'yiadawd@gmail.com')
add_email('blah blah', 'asdeyi@gmail.com')
add_email('blah blah', 'hdthdfyi@gmail.com')
add_email('blah blah', 'hoilo8yi@gmail.com')
add_email('blah blah', 'cbcbftjyi@gmail.com')


print(inbox)

def get_count():
    return(len(inbox))

def get_email(i):
    inbox[i].mark_as_read()

    return inbox[i]

#print(get_count(), get_email(0))

def get_unread_emails():
    temp = []
    for i in inbox:
        if not i.has_been_read:
            temp.append(i)
    return temp


#print(get_unread_emails())

def get_spam_emails():
    temp = []
    for i in inbox:
        if i.is_spam:
            temp.append(i)
    return temp


def delete(i):
    del inbox[i]


user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/delete/get spam/ get unread/quit?")
    if user_choice == "read":
        index = int(input('select the index of the email you want to read: '))
        email = get_email(index)
        email.mark_as_read()
        print(email.email_contents)

        pass #Place your logic here
    elif user_choice == "mark spam":
        index = int(input('select the index of the email you want to mark as spam: '))
        email = get_email(index)
        email.mark_as_spam()

        pass #Place your logic here
    elif user_choice == "send":
        email_address = input('enter an email address: ')
        contents = input('enter the contents of your email: ')
        add_email(contents, email_address)

        pass #Place your logic here#
    elif user_choice == 'delete':
        index = int(input('select the index of the email you want to delete: '))
        delete(index)
    
    elif user_choice == 'get spam':
        spam = get_spam_emails()
        for i in spam:
            print(i.from_address)
            print(i.emaul_contents)

    elif user_choice == 'get unread':
        unread = get_unread_emails()
        for i in unread:
            print(i.from_address)
            print(i.email_contents)

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")


