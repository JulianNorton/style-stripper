def read_txt():

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

    # index = 0
    for css_selector in list_styles:
        # print(list_styles[index])
        # print(index)
        # index = index + 1
        if css_selector[-1] == ',':
            # print('BEFORE', css_selector)
            # print(css_selector[-1], '== Comma!')
            css_selector = css_selector[:-1]
            # print('AFTER', css_selector, '\n')
        # else:
        #     print(css_selector)
        #     print(css_selector[-1], '|| No comma \n')

    ###########################
    # Find range of selector and values
    
    # Temporary values
    selector = 'body'
    test_list = before_stylesheet[0]

    # Find location of selector
    location_index = test_list.index(selector)
    selector_location_beginning = location_index
    print(selector_location_beginning, ' || selector location begins')
    # selector_location_end = location_index + len(selector)
    # print(selector_location_end)

    # Find range of styles for that selector
    styles_index_beginning = test_list[selector_location_beginning:].index('{')
    styles_index_end = test_list[selector_location_beginning:].index('}') + 1 # +1 because we want to include the '}'

    print(styles_index_end, ' || how long the selection + styles are')
    selector_range = test_list[selector_location_beginning: selector_location_beginning + styles_index_end]
    selector_range_index = selector_location_beginning + styles_index_end
    print(selector_range, 'selection range')

    print(test_list, '\n\n')


    print(test_list[:selector_location_beginning])
    print(test_list[selector_range_index:])
    print('\n')
    test_list = test_list[:selector_location_beginning] + test_list[selector_range_index:]
    print(test_list)

    print('\n\n\n\n')

    








read_txt()

