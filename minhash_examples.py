'''
Some examples for MinHash
'''

from hashlib import sha1
from minhash.minhash import MinHash

dataFile = "./texts/articles_100.train"
truthFile = "./texts/articles_100.truth"
data1=[]
data2=[]
'''
Get first and second line from the document, and convert into a list.
First line and second line must be the texts to compare. No newlines.
'''
def extract_text(text):
    global data1,data2
    dataset1=[]
    dataset2=[]

    with open(text, "r") as f:
        data1.extend(f[0].split())
        data2.extend(f[1].split())
    data1=dataset1
    data2=dataset2
def eg1():
    global dataFile
    extract_text(dataFile)
    m1 = MinHash()
    m2 = MinHash()
    for d in data1:
        m1.update(d.encode('utf8'))
    for d in data2:
        m2.update(d.encode('utf8'))
    print(extract_text(dataFile), m1.jaccard(m2))

    s1 = set(data1)
    s2 = set(data2)
    actual_jaccard = float(len(s1.intersection(s2))) /\
            float(len(s1.union(s2)))
    print("Actual Jaccard for data1 and data2 is", actual_jaccard)

if __name__ == "__main__":
    eg1()
