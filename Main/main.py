__author__ = 'Narvi'
from Events.events import registrationEvents

registrationPage = registrationEvents()
class registrationClass(object):
    def clickRegistration(self):
        return registrationPage.initial()
        return registrationPage.signIn()
        return registrationPage.registration()

#clickRegistration(self,initial)
register = registrationClass()
register.clickRegistration()




