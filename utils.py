import pdfplumber

'''
takes path to pdf file 
and return every text from all pages as one string 

'''

def extract_words(path:str)->str:
    with pdfplumber.open(path) as pdf:
        complete_text=""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                complete_text+=text+' '
        return complete_text