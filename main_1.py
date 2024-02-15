import main_hist_list as mhl
import main_hist_list_item as mhli
import character_dictionary as cd


def convert_selected_chars_to_id(selected_content, sentence_struc):
    """
    Returns the character ids for the selected characters
    :param selected_content: the characters selected by the user
    :param sentence_struc: the snapshot of the document at the time of selection of content
    :return: a list of integeres representing the ids of the corresponding characters
    """
    id_list = []
    characters = selected_content[0]
    cursor_pos = selected_content[1]
    sentence = sentence_struc[0]
    sentence_index = sentence_struc[1]
    index = sentence[cursor_pos:].find(characters)
    for i in range(index, index + len(characters)):
        id_list.append(sentence_index[i + cursor_pos])
    return id_list


def create_format_list(selected_content_id_list, MHL):
    """
    Creates a format list which keeps track of everything done to all characters selected
    :param selected_content_id_list: the list of corresponding ids of the selected content
    :param MHL: Main History List
    :return: a nested list of tuples with characters and their property lists
    Format: [(7, [('Typing', 'a day ', 7), ('Italicize', 'a day', 7), ('Unitalicize', 'a ', 9)]),
    (8, [('Typing', 'a day ', 7), ('Italicize', 'a day', 7), ('Unitalicize', 'a ', 9)]),
    (9, [('Typing', 'a day ', 7), ('Italicize', 'a day', 7)])]
    """
    format_list = []
    for character in selected_content_id_list:
        prop_list = []
        for i in range(MHL.len_hist_list()):
            property = MHL.get_hist_item(i)
            if character in property.get_char_id_list():
                prop_list.append(property)
        character_tuple = (character, prop_list)
        format_list.append(character_tuple)
    return format_list


def create_modified_hist_list(format_list, counter_dict):
    """
    Creates a modified history list of the format list checking all characters and properties for counters
    :param format_list: Format List of characters and their properties
    :param counter_dict: Dictionary with all the possible counters to actions, eg. Bold:Unbold, Font Color:Font Color
    :return: A nested list of tuples with property list, character and whether is it countered or not
    Sample: [(('Typing', 'Qq', 0), 54, 'n'), (('Bold', 'Qq', 0), 54, 'n'), (('Typing', 'Qq', 0), 55, 'n'),
    (('Bold', 'Qq', 0), 55, 'c'), (('Italicize', 'q', 1), 55, 'n'), (('Unbold', 'q', 1), 55, 'c'),
    (('Bold', 'q_z', 1), 55, 'n')]
    """
    modHL = []
    for character_list in format_list:
        character = character_list[0]
        prop_list = character_list[1]
        for i in range(len(prop_list)):
            property = []
            for prop in prop_list[i + 1:]:
                property.append(prop.get_prop())
            if counter_dict[prop_list[i].get_prop()] in property:
                modHL.append((prop_list[i], character, "c"))
            else:
                modHL.append((prop_list[i], character, "n"))
    return modHL


def taskNumber(list):
    """
    Sorts the list based on the tasknumber in history list
    :param list: list that needs to be sorted
    :return: a sorted list
    """
    return list[0].get_tasknum()


def compile_modified_hist_list(modified_hist_list):
    """
    Combines the characters in the modified history list based on the concept of counters.
    :param modified_hist_list:
    :return: a grouped list of tuples
    Sample:  [(('Typing', 'Qq', 0), [54, 55]), (('Bold', 'Qq', 0), [54]), (('Bold', 'Qq', 0), [55]),
    (('Italicize', 'q', 1), [55]), (('Typing', '_z! ', 2), [56, 57, 58])]
    """
    dict = {}
    for prop_tuple in modified_hist_list:
        property = prop_tuple[0]
        character = prop_tuple[1]
        state = prop_tuple[2]
        if (property, state) in dict:
            dict[(property, state)].append(character)
        else:
            dict[(property, state)] = [character]
    final_list = []
    for key in dict:
        final_list.append((key[0], dict[key]))
    final_list.sort(key=taskNumber)
    return final_list


def print_compiled_list(compiled_list, MHL):
    """
    Prints the final list that the user sees
    :param compiled_list: compiled list from compile_modified_hist_list() method
    :param MHL: Main History List
    """
    final_list = []
    for i in compiled_list:
        property = i[0]
        characters = i[1]
        char_str = ""
        for key in characters:
            char_str += MHL.id_to_char(key)
        if property.get_addInfo() == None:
            final_list.append((property.get_prop(), char_str))
        else:
            final_list.append((property.get_prop(), char_str, property.get_addInfo()))
    for task in final_list:
        print(task)

