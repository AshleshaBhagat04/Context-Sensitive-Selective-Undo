import main_hist_list as mhl
import main_1 as m1


def user_action():
    MAIN = mhl.MainHistList()
    MAIN.add_item("Typing", "Qq_z! X This is an example of a old new type of Ctrl+Z method.", 0)  #
    MAIN.add_item("Bold", "Qq_z!", 0)
    MAIN.add_item("Strikethrough", "old", 30)
    MAIN.add_item("Font Size", "Ctrl+Z", 46, 14)
    MAIN.add_item("Italicize", "Ctrl+Z method.", 46)
    MAIN.add_item("Unbold", "z!", 3)
    MAIN.add_item("Underline", "example", 17)
    MAIN.add_item("Font Color", "new type", 34, "Red")
    MAIN.add_item("Bold", "new type", 34)
    MAIN.add_item("Unitalicize", "method.", 53)
    MAIN.add_item("Bold", "z", 3)
    return MAIN


def algorithm_process(MAIN):
    selected_content = ("Qq_z!", 0)
    sentence_info = MAIN.final_snapshot()
    # print("--------------------------------")
    # print(sentence_info)
    sentence = sentence_info[0]

    dict = {"Bold": "Unbold", "Typing": "Delete", "Unbold": "Bold", "Italicize": "Unitalicize",
            "Unitalicize": "Italicize", "Underline": "Ununderline", "Ununderline": "Underline",
            "Strikethrough": "Unstrikethrough", "Unstrikethrough": "Strikethrough", "Delete": "Typing",
            "Font Size": "Font Size", "Font Color": "Font Color"}

    high_list = m1.convert_selected_chars_to_id(selected_content, sentence_info)
    # print("-----------------------", high_list)
    format_list = m1.create_format_list(high_list, MAIN)
    # print("FORMAT LIST \n", format_list, "\n")

    modHL = m1.create_modified_hist_list(format_list, dict)
    # print("MODHL \n", modHL, "\n")

    compile_list = m1.compile_modified_hist_list(modHL)

    # print("COMPILED LIST \n", compile_list, "\n")

    m1.print_compiled_list(compile_list, MAIN)


if __name__ == "__main__":
    MAIN = user_action()
    algorithm_process(MAIN)
