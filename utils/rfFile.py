
def write(path,  body, encoding='utf8'):
    with open(path, 'w', encoding=encoding) as f:
        f.write(body)

def append(path, body, encoding='utf8'):
    with open(path, 'a', encoding=encoding) as f:
        f.write(body)

def read_to_str(path, encoding='utf8'):
    with open(path, 'r', encoding=encoding) as f:
        return ''.join(f.readlines()).replace('\n','')              

def file_map(path, fn, encoding='utf8'):
    with open(path, 'r', encoding='utf8') as f:
        for sentence in f.readlines():
            fn(sentence)
            