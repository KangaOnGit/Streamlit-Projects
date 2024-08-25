import streamlit as st


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([w.strip().lower() for w in lines]))
    return words


vocabs = load_vocab(file_path='./vocab.txt')


def leven_distance(target, source):
    distances = [[None] * ((len(target) + 1)) for i in range(len(source) + 1)]
    
    for t in range(len(target)):
        distances [0][t] = t
    for s in range(len(source)):
        distances[s][0] = s
    for i in range(1, len(source)+ 1):
        for j in range (1, len(target) + 1 ):
            if source[i - 1] == target [ j-1]:
                cost  = 0
            else:
                cost = 1
                distances [s][t] = min(distances[i-1][j] + 1, distances[i][j+1] + 1, distances [i-1][j-1] + cost)
                
    return distances[len(source)][len(target)]

def main():
    st.title("Word correction using Levenshtein Distance")
    word = st.text_input('Word: ')
    
    if st.button('Compute'):
        edit_distance = dict()
        for vocab in vocabs:
            edit_distance [vocab] = leven_distance(vocab, word)
            #return the number of edit distance to reach the target vocab from the input word   
             
        sorted_distances = dict(sorted(edit_distance.items(), key = lambda item: item[1]))
    #sort based on the value of edit distance, from smallest to largest // kinda like an algo
        correct_word  = list(sorted_distances.keys()) [0]
    #return the "correct word" which is the word with the least amt of edit/leven_distance required
    
        col1, col2 = st.columns(2)
        col1.write('Vocabulary: ')
        col1.write(vocabs)
    
        col2.write('Distances: ')
        col2.write(sorted_distances)
if __name__ == '__main__':
    main()
