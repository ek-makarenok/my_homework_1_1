from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", lastname="lastname1", homephone="homephone1", email="email11", email2="email2"),
    Contact(firstname="firstname2", lastname="lastname2", homephone="homephone2", email="email21", email2="email22")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", homephone="")] + [
    Contact(firstname=random_string("firstn", 10), lastname=random_string("lastn", 20),
          homephone=random_string("homeph", 11), email=random_string("email", 20), email2=random_string("email2", 20))
    for i in range(5)
]

