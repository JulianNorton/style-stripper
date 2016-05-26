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

        
    for selector_index in range(0,len(list_styles)):
        selector = list_styles[selector_index]
        # Try and find location of the selector
        if selector in after_stylesheet:
            selector_location_beginning = after_stylesheet.index(selector)
            closing_bracket_index = after_stylesheet.index('}', selector_location_beginning) + 1
            # Look for a double closing bracket
            if after_stylesheet[closing_bracket_index-1:closing_bracket_index] == '}':
                try:
                    if after_stylesheet[closing_bracket_index-1:closing_bracket_index + 1] == '}}':
                        closing_bracket_index += 1
                except:
                    print('EXCEPTION')
            range_to_delete = after_stylesheet[selector_location_beginning:closing_bracket_index]
            after_stylesheet = after_stylesheet[:selector_location_beginning] + after_stylesheet[closing_bracket_index:]
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
    # statinfo_before = os.stat('before_stylesheet.css').st_size
    statinfo_after = os.stat('clean.css').st_size
    print('original css (KB) ==', statinfo_original/1000)
    # print(statinfo_before/1000, '~ kilobytes || before css')
    print('Clean css (KB)   == ', statinfo_after/1000)


style_stripper()
