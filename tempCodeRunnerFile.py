import lmproof
def proofread(text):
    proofread = lmproof.load("en")
    correction = proofread.proofread(text)
    print("Original: {}".format(text))
    print("Correction: {}".format(correction))
    
proofread("Hey I am dev sharma. I aam 16 years old")