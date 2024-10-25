abstract_file = open('article.txt', 'r', encoding='utf-8')

def read_last(lines, file):
    if not lines >= 0 :
        print('Число строк должно быть больше нуля')
        exit()
    abstract_file = open(file, 'r', encoding='utf-8')
    rows = abstract_file.readlines()
    print(rows)
print(read_last(2,'article.txt'))