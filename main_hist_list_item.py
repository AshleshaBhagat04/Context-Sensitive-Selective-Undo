
class MainHistListItem:

    def __init__(self, property, characters, start_time, tasknum, addtlinfo=None):
        """
        Creates a Main History List Item Object
        :param property: string representing the action done in the item
        :param characters: string of characters to which the action is donw
        :param start_time: integer representing the cursor position at the time of the execution of task
        :param tasknum: integer representing the position of the task in whole history list
        :param addtlinfo: any extra information about the task - can be any data type like string (for Font Style /
        Color) or integer (for Font Size)
        __char_id_list = a list of numbers representing the corresponding ids of the characters
        Example: mhli.MainHistListItem("Font Color", "new type", 34, 5, "Red")
                __prop: Font Color (string), __chars: "new type" (string), __start_time: 34 (int),
                __tasknum: 5 (integer), __addInfo: "Red" (string), __char_id_list = [34,35,36,37,40,45,23,24]
        """
        self.__prop = property
        self.__chars = characters
        self.__start_time = start_time
        self.__tasknum = tasknum
        self.__addInfo = addtlinfo
        self.__char_id_list = []

    def get_prop(self):
        """
        Returns the main action / property of the given main history list item
        :return: a string of characters with properties / actions done such as "Typing", "Bold", etc.
        """
        return self.__prop

    def get_chars(self):
        """
        Returns the characters of the given main history list item
        :return: a string of characters or a character to which the action was done
        """
        return self.__chars

    def get_start_time(self):
        """
        Returns the position of the cursor for the main history list item when the task was executed
        :return: an integer value
        """
        return self.__start_time
    
    def get_tasknum(self):
        """
        Returns the position / number at which the item fall in the whole main history list
        :return: an integer value
        """
        return self.__tasknum

    def get_char_id_list(self):
        """
        Returns a list containing the corresponding keys of the characters to which the action was applied.
        :return: a list of integer values
        """
        return self.__char_id_list

    def get_addInfo(self):
        """
        Returns whether there is any other information about the action that is to be taken note of
        :return: a string of characters with information like "Red" or "Green" when property is Font Color or 22 or 14
        when property is Font Size or else return None
        """
        return self.__addInfo

    def set_tasknum(self,num):
        self.__tasknum = num

    def set_char_list(self, value):
        self.__char_id_list = value

    def __str__(self) -> str:
        """
        Returns the string version to print properly
        """
        return str((self.__prop,self.__chars,self.__start_time))
    
    def __repr__(self) -> str:
        """
        Returns the string version to print properly
        """
        return str(self)