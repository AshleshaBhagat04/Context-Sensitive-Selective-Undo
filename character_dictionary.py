CHAR = 0
START_INDEX = 1
LOC = 1


class CharDict:
    ## Class for our character dictionary

    def __init__(self):
        """
        Creates a Card Dictionary Object
        """
        self.__contents = {}
        self.__index = 0

    def get_all_id_list(self):
        """
        Returns the main dictionary contents of CardDict
        """
        return  list(self.__contents.keys())

    def get_char(self, key):
        """
        Returns the character for a give character id key
        :param key: The character id
        :return: a single character if key found else returns None
        """
        if key not in self.__contents.keys():
            print("Key not found")
            return None
        else:
            return self.__contents[key][CHAR]

    # def get_start_index(self, key):
    #     """
    #     Returns the starting index of the character
    #     :param key:
    #     :return:
    #     """
    #     return self.__contents[key][START_INDEX]

    def get_char_loc(self, key):
        """
        Returns the character location in a particular format for debugging purposes
        A string where the location of character at time of intitatization is returned
        :param key: The character id
        :return: a string of characters that have the format "$H$ello", "H$e$llo", "He$l$lo", etc... if key found else
        returns None
        """
        if key not in self.__contents.keys():
            print("Key not found")
            return None
        else:
            return self.__contents[key][LOC]

    def get_all_char_loc(self):
        """
        Returns the debug locations for all characters
        :return: a list of the locations of all the characters if key found else returns None
        """
        loc_list = []
        for value in self.__contents:
            loc_list.append(self.__contents[value][1])
        return loc_list

    def add_chars(self, characters):
        """
        Creates new dictionary indexes/keys everytime new characters are typed
        :param characters: the string of characters or a single characters which is added to the dictionary
        """
        for i in range(len(characters)):
            loc = characters[:i] + "$" + characters[i] + "$" + characters[i + 1:]
            if len(self.__contents) == 0:
                self.__contents[self.__index] = (characters[i],loc)
                # self.__contents[self.__index] = (characters[i],start_index, loc)
            else:
                value_list = self.get_all_char_loc()
                if loc not in value_list:
                    self.__contents[self.__index] = (characters[i], loc)
                    # self.__contents[self.__index] = (characters[i], start_index, loc)
            self.__index += 1
            # start_index += 1

    def __str__(self) -> str:
        """
        Returns the string version to print properly
        """
        return str(self.__contents)

    def __repr__(self) -> str:
        """
        Returns the string version to print properly
        """
        return str(self)


if __name__ == "__main__":
    test_dict = CharDict()
    test_dict.add_chars("method.")
    test_dict.add_chars("Qq_z!")
    print(test_dict)
    print(test_dict.get_char(10))
    print(test_dict.get_all_id_list())
