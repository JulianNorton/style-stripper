import os

def style_stripper():

    print('\n\n\n\n')

    ###########################
    # importing unused styles
    list_styles = list()
    unused_styles_file = open('style-audit.txt')
    for line in unused_styles_file:
        list_styles.append(line.strip())
    unused_styles_file.close()

    ###########################
    # importing full stylesheet
    before_stylesheet_file = open('style.css')
    before_stylesheet = before_stylesheet_file.readlines()
    original_stylesheet = before_stylesheet
    before_stylesheet_file.close()  
    before_stylesheet = ''.join(before_stylesheet)

    saved_path = os.getcwd()
    name_of_file = 'before_stylesheet'
    completeName = os.path.join(saved_path, name_of_file+".css")
    file1 = open(completeName, "w")
    toFile = before_stylesheet
    file1.write(toFile)
    file1.close()

    after_stylesheet = str()

    ###########################
    # Cleaning audit list for bad commas
    for css_selector in list_styles:
        if css_selector[-1] == ',':
            css_selector = css_selector[:-1]


        
    # print(len(list_styles))
    # for selector_index in range(0,len(list_styles)):
    # print(len(before_stylesheet), len(after_stylesheet), 'len before/after')
    for selector_index in range(0,3):
        # print(list_styles[selector_index])
        selector = list_styles[selector_index]
        # Try and find location of the selector
        if selector in before_stylesheet:
            # print(selector, 'selector found!')
            selector_location_beginning = before_stylesheet.index(selector)
            # print(before_stylesheet.index(selector))
            # # Single bracket?
            # print('single bracket found')
            closing_bracket_index = before_stylesheet[selector_location_beginning:].index('}')
            print(before_stylesheet[closing_bracket_index: closing_bracket_index + 1], 'c')
            print(before_stylesheet[closing_bracket_index: closing_bracket_index + 2], 'd')
            if before_stylesheet[closing_bracket_index: closing_bracket_index + 2] == '}}':
                print('Double bracket')
                print(selector)
            elif before_stylesheet[closing_bracket_index: closing_bracket_index + 1] == '}':
                print('single bracket')
                print(selector)
            # if before_stylesheet[closing_bracket_index: closing_bracket_index + 1] == '}}':
            #     print('double bracket!')
            #     closing_bracket_index = before_stylesheet[selector_location_beginning:].index('}') + 1
            #     print(closing_bracket_index)
            # else:
            #     print('No double bracket')
            #     print('fail')


    ##########################
    # Writing new file
    saved_path = os.getcwd()
    name_of_file = 'clean'
    completeName = os.path.join(saved_path, name_of_file+".css")
    file1 = open(completeName, "w")
    toFile = after_stylesheet
    file1.write(toFile)
    file1.close()


    ##########################
    # Size comparison
    statinfo_original = os.stat('original_stylesheet.css').st_size
    statinfo_before = os.stat('before_stylesheet.css').st_size
    statinfo_after = os.stat('clean.css').st_size
    print('\n')
    # print(statinfo_original/1000, '~ kilobytes || original css')
    # print(statinfo_before/1000, '~ kilobytes || before css')
    # print(statinfo_after/1000, '~ kilobytes || clean css')


style_stripper()
