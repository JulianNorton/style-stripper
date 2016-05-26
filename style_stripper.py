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
    before_stylesheet_file.close()  
    before_stylesheet = ''.join(before_stylesheet)

    saved_path = os.getcwd()
    name_of_file = 'before_stylesheet'
    completeName = os.path.join(saved_path, name_of_file+".css")
    file1 = open(completeName, "w")
    toFile = before_stylesheet
    file1.write(toFile)
    file1.close()
    # Need to make copy to not run into errors
    after_stylesheet = before_stylesheet

    ###########################
    # Cleaning audit list for bad commas
    for css_selector in list_styles:
        if css_selector[-1] == ',':
            css_selector = css_selector[:-1]

        
    # print(len(list_styles))
    # for selector_index in range(0,len(list_styles)):
    # print(len(before_stylesheet), len(after_stylesheet), 'len before/after')
    for selector_index in range(0,len(list_styles)):
    # for selector_index in range(0,4):
        # print(list_styles[selector_index])
        selector = list_styles[selector_index]
        # Try and find location of the selector
        if selector in after_stylesheet:
            print('\n', selector)
            # print(selector, 'selector found!')
            selector_location_beginning = after_stylesheet.index(selector)
            print(after_stylesheet.index(selector), 'selector beginning index')
            # print(before_stylesheet.index(selector))
            # # Single bracket?
            # print('single bracket found')
            # print(after_stylesheet)
            # closing_bracket_index = selector_location_beginning
            closing_bracket_index = after_stylesheet.index('}', selector_location_beginning) + 1
            if after_stylesheet[closing_bracket_index-1:closing_bracket_index] == '}':
                print('one bracket found')
                try:
                    if after_stylesheet[closing_bracket_index-1:closing_bracket_index + 1] == '}}':
                        print(after_stylesheet[closing_bracket_index-1:closing_bracket_index + 1])
                        print('double bracket', selector)
                        print(closing_bracket_index)
                        closing_bracket_index += 1
                        print(closing_bracket_index)
                except:
                    print('EXCEPTION')
            print(closing_bracket_index, 'closing bracket index')
            range_to_delete = after_stylesheet[selector_location_beginning:closing_bracket_index]
            print('del -->|',range_to_delete,'|<-- del')
            after_stylesheet = after_stylesheet[:selector_location_beginning] + after_stylesheet[closing_bracket_index:]
            # print('\n', after_stylesheet, '\n')
        else:
            print('selector not found', selector)


    after_stylesheet = after_stylesheet.replace('\n', '')
    after_stylesheet = after_stylesheet.replace('  ', '')

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
    print(statinfo_original/1000, '~ kilobytes || original css')
    print(statinfo_before/1000, '~ kilobytes || before css')
    print(statinfo_after/1000, '~ kilobytes || clean css')


style_stripper()
