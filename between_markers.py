def between_markers(text, begin, end):
    op = ''
    cl = ''
    for i in text:
        print(i)




text='<head><title>My new site</title'
between_markers(text, begin, end)


# 'What is >apple<', '>', '<') == "apple", "One sym"
# "<head><title>My new site</title></head>","<title>", "</title>") == "My new site", "HTML"
# 'No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
# 'No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
# 'No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
# 'No <hi>', '>', '<') == '', 'Wrong direction'