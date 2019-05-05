def user_selection(message, options):
    # taken from https://github.com/Asana/python-asana/blob/master/examples/example-create-task.py
    option_list = list(options)
    print(message)
    for i, option in enumerate(option_list):
        print(i, ": " + option["name"])
    index = int(input("Enter choice (default 0): ") or 0)
    return option_list[index]
