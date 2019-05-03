
text = "X-DSPAM-Confidence:    0.8475";
spos=text.find('0')
epos=text.find('5')

text=float(text[spos:epos+1])
print(text)
