class employee:

    def __init__(self, name, id, branch, position):
        self.__name = name
        self.__id = id
        self.__branch = branch
        self.__position = position

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_branch(self, branch):
        self.__branch = branch

    def set_position(self, position):
        self.__position = position

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_branch(self):
        return self.__branch

    def get_position(self):
        return self.__position