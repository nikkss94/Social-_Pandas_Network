class Panda:
    ID = 0
    def __init__(self, name, email, gender):
        self.id = self.ID
        self.__class__.ID += 1
        self._name = name
        self._email = email
        self._gender = gender

    def isMale(self):
        if self._gender == "male":
            return True
        else:
            return False
    def get_id(self):
        return self.id

    def isFemale(self):
        if self._gender == "female":
            return True
        else:
            return False

    def __str__(self):
        return self._name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isValidAddress(self):
        if '@' not in self._email:
            return False
        else:
            address = self._email.split('@')
            if '.' not in address[1]:
                return False
            else:
                return True

def main():
    vladko = Panda('Vladko', 'vladko@pandamail.com', 'male')

if __name__ == '__main__':
    main()
