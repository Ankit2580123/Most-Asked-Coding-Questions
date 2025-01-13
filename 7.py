# File Handling
# Read a file and count the occurrences of each word.
from collections import Counter
def write_to_text(file_path):
    try:
        with open(file_path,'r') as f:
            data=f.read()
            
            freq={}
            for i in data:
                if i in freq:
                    freq[i]+=1
                else:
                    if i=='\n':
                        continue
                    freq[i]=1
            
            # print(freq)
            return freq
    except Exception as e:
        print(e)


path='sample.text'
word_count=write_to_text(path)
print(word_count)
