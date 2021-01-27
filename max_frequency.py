# Max Frequency

text = "Hello how are you I am fine and very very very"

D={}
max_freq = 0
max_text = ""
for i in text.split():
    if i not in D:
        D[i]=1
    else:
        D[i]+=1
    if D[i]>max_freq:
        max_freq = D[i]
        max_text = i

print(max_text)
