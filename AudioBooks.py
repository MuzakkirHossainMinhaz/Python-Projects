import pyttsx3
import PyPDF2

# python_oop.pdf is the pdf file name, you can set your pdf location here
book = open('python_oop.pdf', 'rb')
speaker = pyttsx3.init()

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

# If want to start a page number and read to the end of book
for page in range(7, pages):
    page = pdfReader.getPage(7)  # to find 7 no page, you can put your page number
    text = page.extractText()  # extract text from the page
    speaker.say(text)
    speaker.runAndWait()