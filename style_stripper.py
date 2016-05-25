def style_stripper():

    print('\n\n')

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

    ###########################
    # Cleaning audit list for bad commas
    for css_selector in list_styles:
        if css_selector[-1] == ',':
            css_selector = css_selector[:-1]

    after_stylesheet = list()
    def selector_processor(x):
        i = 0
        did_find = list()
        while i < len(before_stylesheet):
            selector = str(x)
            # Chunks are each 'item' in before_stylesheet
            # If there are no whitespaces, there will only be 1 chunk.
            stylesheet_chunk = before_stylesheet[i]

            # Try and find location of the selector
            try:
                selector_location_beginning = stylesheet_chunk.index(selector)
                # print(selector_location_beginning, ' || selector location begins')

                # Find range of styles for that selector
                styles_index_beginning = stylesheet_chunk[selector_location_beginning:].index('{')
                # +1 for index because we want to include the '}'
                styles_index_end = stylesheet_chunk[selector_location_beginning:].index('}') + 1 

                # print(styles_index_end, ' || how long the selection + styles are')
                # Ran
                selector_range = stylesheet_chunk[selector_location_beginning: selector_location_beginning + styles_index_end]
                selector_range_index = selector_location_beginning + styles_index_end
                # print(selector_range, '|| selection range')


                # print('length before:        ', len(stylesheet_chunk))
                stylesheet_chunk = stylesheet_chunk[:selector_location_beginning] + stylesheet_chunk[selector_range_index:]
                # print('length after deletion:' ,len(stylesheet_chunk))

                # If it's found, save which chunk it was found in
                did_find.append(i)

            except:
                # print(selector, 'not found in stylesheet_chunk', '#',i)
                pass

            after_stylesheet.append(stylesheet_chunk)
            i += 1

        if did_find != list():
            # print('Chunks edited:', did_find)
            pass
        else:
            # print('No chunks edited')
            pass


    ###########################
    # Searches all of the stylesheet chunks for the selectors
    for selector in range(0,len(list_styles)):
        # print(selector)
        selector_processor(selector)

    ###########################
    # Is the newer stylesheet smaller than the new one?
    # print('before_stylesheet', len(before_stylesheet.join()))
    before_stylesheet = ''.join(before_stylesheet)
    print('Char length Before', len(before_stylesheet))
    print('Char length After', len(after_stylesheet))

    print('Compressed %: ', len(after_stylesheet)/len(before_stylesheet))

    print('\n')

style_stripper()

