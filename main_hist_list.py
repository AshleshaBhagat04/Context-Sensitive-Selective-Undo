import main_hist_list_item as mhli
import character_dictionary as cd


class MainHistList:

    def __init__(self):
        """
        Creates a Main History List Object
        """
        self.__chardictionary = cd.CharDict()
        self.__contents = []

    def __get_contents(self):
        return self.__contents

    def __get_chardict(self):
        """
        Returns the character dictionary
        :return: a dictionary
        """
        return self.__chardictionary

    def len_hist_list(self):
        """
        Returns the length of the history list
        :return: an integer value
        """
        return len(self.__contents)

    def add_item(self, property, characters, start_time, addtlinfo=None):
        """
        Adds a main history list item
        :param property: the property of the item
        :param characters: the characters to which the action was done
        :param start_time: the cursor position at the time of exceution of statement
        :param addtlinfo: any other information about the action being done
        """
        list_item = mhli.MainHistListItem(property, characters, start_time, self.len_hist_list(), addtlinfo)
        self.__contents.append(list_item)
        property = list_item.get_prop()
        chars = list_item.get_chars()
        time_start = list_item.get_start_time()
        task_number = list_item.get_tasknum()
        if property == "Typing":
            self.__chardictionary.add_chars(chars)
        if property == "Delete":
            char_key_list = self.__find_char_key(chars, time_start, task_number - 1)
            list_item.set_char_list(char_key_list)
        else:
            char_key_list = self.__find_char_key(chars, time_start, task_number)
            list_item.set_char_list(char_key_list)

    def get_hist_item(self, item_num):
        """
        Returns the main hist list item position at the specified number
        :param item_num: the number for which the item in the list is needed
        :return: a main hist list item object
        """
        return self.__contents[item_num]

    def doc_snapshot(self, tasknum):
        """
        Returns the snapshot of the document after executing number of main hist list items
        :param tasknum: an integer value representing the task number at which we want to look at the Document's snapshot
        :return: a list with the first item being a string of characters and second being a list with corresponding
        character keys / ids
        """

        char_dict = self.__get_chardict()
        sentence_key = []
        sentence = ""
        for i in range(tasknum + 1):
            item = self.__contents[i]
            if item.get_prop() == "Typing":
                index_to_add = item.get_start_time()
                characters = item.get_chars()
                for i in range(len(characters)):
                    loc = characters[:i] + "$" + characters[i] + "$" + characters[i + 1:]
                    for key in char_dict.get_all_id_list():
                        if loc in char_dict.get_char_loc(key):
                            sentence_key = sentence_key[:index_to_add] + [key] + sentence_key[index_to_add:]
                            sentence = sentence[:index_to_add] + characters[i] + sentence[index_to_add:]
                            index_to_add += 1

            elif item.get_prop() == "Delete":
                index = item.get_start_time()
                sentence = sentence.replace(item.get_chars(), '', index)
                for i in range(len(item.get_chars())):
                    sentence_key.pop(index)

        return [sentence, sentence_key]

    def final_snapshot(self):
        """
        Returns the doc snapshot after the execution of the full history list
        :return:
        """
        length = self.len_hist_list()
        return self.doc_snapshot(length - 1)

    def __convert_mhl_char_id(self, tasknum):
        item = self.get_hist_item(tasknum)
        property = item.get_prop()
        characters = item.get_char()
        start_index = item.get_index_start()
        if property == "Delete":
            char_key_list = self.__find_char_key(characters, start_index, tasknum)
        else:
            char_key_list = self.__find_char_key(characters, start_index, tasknum + 1)
        converted_item = mhli.MainHistListItem(property, char_key_list, start_index, item.get_addInfo())
        return converted_item

    def __find_char_key(self, characters, position, task_num):
        """
        Returns a lst containing character id of select characters at a particular cursor position and task number
        :param characters: the characters fo which we need to find the ids
        :param position: the position of the characters
        :param task_num: the task number at which we need to find the ids
        :return:
        """
        sentence_struc = self.doc_snapshot(task_num)
        list = []
        chars = characters
        cursor_pos = position
        sentence = sentence_struc[0]
        sentence_index = sentence_struc[1]
        start_pos = sentence[cursor_pos:].find(chars)
        for i in range(start_pos, start_pos + len(chars)):
            list.append(sentence_index[i + cursor_pos])
        return list

    def id_to_char(self, id):
        """
        Returns the corresponding character for a given ID
        :param id: the character id
        :return: a single char
        """
        return self.__chardictionary.get_char(id)

    def __str__(self) -> str:
        return str(self.__contents)

    def __repr__(self) -> str:
        return str(self)
