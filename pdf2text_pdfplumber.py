import pdfplumber

pagesList = []

with pdfplumber.open(r'pdfFileName.pdf') as pdf:
    
    for i in range(0,52):
        page = pdf.pages[i]
        text = page.extract_text()
        pagesList.append(text)
    
    
    
with open('readme.txt', 'w') as f:
    for line in pagesList:
        f.write(line)
        f.write('\n_______________________\n')
        
        
f.close()
    
