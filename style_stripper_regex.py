import os
import re

def style_stripper():

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
    before_stylesheet = "_<begeee>_".join(before_stylesheet)


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
    new_list_styles = []
    for css_selector in list_styles:
        if css_selector[-1] == ',':
            css_selector = css_selector[:-1]
        new_list_styles.append(css_selector)

    list_styles = new_list_styles
    print(list_styles)
    #pattern = re.compile(after_stylesheet)

    #print(before_stylesheet, '\n')
    print("---------------------------------")
    # print(list_item)
    print("---------------------------------")
    for list_item in list_styles:
        
        before_stylesheet = re.sub(r'_<begeee>_' + re.escape(list_item)+r'(\s)*\{[^\}]+\}',' ',before_stylesheet)
    # print(before_stylesheet, '\n')
    after_stylesheet = before_stylesheet
    
    after_stylesheet = re.sub(r'_<begeee>_', ' ',after_stylesheet)
    after_stylesheet = re.sub(r'\s+', ' ',after_stylesheet)


    
    # Remove unnecessary white spaces
    # after_stylesheet = after_stylesheet.replace('\n', '')
    
    # pattern = re.compile(after_stylesheet)
    # for index, css_selector in enumerate(list_styles):
    #     print(index,css_selector)
    #     if pattern.search(list_styles[index]) == True:
    #         print(list_styles[index], '!MATCH!')
    #     else:
    #         print(pattern.search(list_styles[index]), list_styles[index], 'not found')



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
    print('Original css  ==', statinfo_original/1000, 'kb')
    print(statinfo_before/1000, '~ kilobytes || before css')
    print('Clean css     ==', statinfo_after/1000, 'kb')
    print('              ==', statinfo_after/statinfo_original, '%', '\n')

style_stripper()
