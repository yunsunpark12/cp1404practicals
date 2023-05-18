from Prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)

    print("The dynamically typed languages are: ")
    ProgrammingLanguage.is_dynamic(ruby)
    ProgrammingLanguage.is_dynamic(python)
    ProgrammingLanguage.is_dynamic(visual_basic)


if __name__ == '__main__':
    main()