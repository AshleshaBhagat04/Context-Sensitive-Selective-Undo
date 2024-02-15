import main_hist_list as mhl
import main_1 as m1


def user_action():
        MAIN = mhl.MainHistList()

        MAIN.add_item("Typing", "apples ", 0)
        MAIN.add_item("Bold", "apples", 0)
        MAIN.add_item("Typing", "a day ", 7)
        MAIN.add_item("Italicize", "a day", 7)
        MAIN.add_item("Delete", "s", 6)
        MAIN.add_item("Typing", "An ", 0)
        MAIN.add_item("Typing", "keeps the doctor away.", 15)
        # MAIN.add_item("Delete", "Q", 0)
        MAIN.add_item("Strikethrough", "doctor", 25)
        MAIN.add_item("Unstrikethrough", "doctor", 25)
        MAIN.add_item("Unitalicize", "a ", 9)
        MAIN.add_item("Underline", "doctor away", 25)
        return MAIN


def algorithm_process(MAIN):
        selected_content = ("a day", 6)
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

