from utils import rfFile
import numpy as np

def generate_word_vector(words, dim=5, ):
    '''生成词向量
    input:
        words: 单词合集
        dim: 词向量的维度
    output: 
        dict -> {word: vector[dim]}
    '''
    pass

demo_path = './data/honglou/第1章.txt'
# text = nfFile.read_to_str(demo_path)
# generate_word_vector(text)

# np.unifrom((1,2))
a = np.random.random((1,2))
# print(a.shape)