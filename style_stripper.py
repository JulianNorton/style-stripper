def read_txt():
    list_styles = list()
    unused_styles_file = open('style-audit.txt')
    for line in unused_styles_file:
        list_styles.append(line.strip())
    unused_styles_file.close()
    print('test')
    print(list_styles)



read_txt()


# print(unused_styles)