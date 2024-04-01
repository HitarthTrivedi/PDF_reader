import pyttsx3
#only works in python 3.9
import PyPDF4


book=open('ball_poem.pdf', 'rb')
pdfreader=PyPDF4.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)
speaker=pyttsx3.init()
page=pdfreader.getPage(0

                       )
text=page.extractText()
print(text)
speaker.say(text
            )
speaker.runAndWait()
