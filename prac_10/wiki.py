import wikipedia

searching_input = input("Enter page title: ")
while searching_input != '':
    try:
        page_title = wikipedia.page(searching_input, auto_suggest=False)
        print(wikipedia.summary(page_title))
        print(wikipedia.page(page_title).url)

    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f'Page id "{searching_input}" does not match any pages. Try another id!')

    searching_input = input("Enter page title: ")
print('Thank you.')


