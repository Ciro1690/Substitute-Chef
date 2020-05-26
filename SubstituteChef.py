from uszipcode import SearchEngine, SimpleZipcode, Zipcode
import PyPDF2
from PIL import ImageTk
from PIL import Image
import tkinter

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=19143&distance=25&API_KEY=2BD82EC1-20B4-4EB0-8A1F-49D2771204C4
def welcome():

    canvas = make_canvas(1000, 600, 'Ciros Final Project')
    canvas.configure(bg='#49A')
    canvas.create_text(100, 200, anchor='w', font='Courier 48', text='Welcome to Substitute Chef!')
    image = ImageTk.PhotoImage(Image.open("chef.jpg"))
    canvas.create_image(400,300,anchor="w",image=image)

    canvas.mainloop()

def main():
    welcome()
    get_name()
    search_criteria()
    background()
    zipcode()

def get_name():
    name = input("What is your name? ")
    print("We are here to help you get employed, Chef "+ name + "!")

def search_criteria():
    print("What is your availability, from the following?: ")
    availability = input("A One shift \nB Part-time \nC Full-time \nD Any option ")
    availability_info(availability)
    print("Please choose what position you are looking for, from the following: ")
    position = input("1 Dishwasher \n2 Prep cook \n3 Line Cook \n4 Sous Chef ")
    position_info(position)

def position_info(position):
    correct = True
    while correct == True:
        if int(position) in range (0,5):
            if int(position) == 1:
                print("You will be considered for jobs as a Dishwasher. Let's review your background and experience. ")
                correct = False
            elif int(position) == 2:
                print("You will be considered for jobs as a Prep Cook. Let's review your background and experience. ")
                correct = False
            elif int(position) == 3:
                print("You will be considered for jobs as a Line Cook. Let's review your background and experience. ")
                correct = False
            elif int(position) == 4:
                print("You will be considered for jobs as a Sous Chef. Let's review your background and experience. ")
                correct = False
        else:
            print("Please choose one of the options and enter the corresponding number. ")
            position = input("1 Dishwasher 2 Prep cook 3 Line Cook 4 Sous Chef ")

def availability_info(availability):
    correct = True
    while correct == True:
        if availability == "A" or availability == "B" or availability == "C" or availability == "D":
            if availability == "A":
                print("We will search for jobs on a day-to-day basis. ")
                correct = False
            elif availability == "B":
                print("We will search for part-time restaurant jobs. ")
                correct = False
            elif availability == "C":
                print("We will search for full-time restaurant jobs. ")
                correct = False
            elif availability == "D":
                print("We will search for all types of restaurant jobs for you. ")
                correct = False
        else:
            print("Please choose one of the options and enter the corresponding letter. ")
            availability = input("A One shift B Part-time C Full-time D Any option ")

def background():
    print("Please upload a copy of your resume, highlighting your relevant work experience. ")
    print("If you have at least one year of relevant experience, we will set up a working interview to better tailor your job search. ")
    print("We are an equal opportunity employment and will search for meaningful work for every person. ")
    answer = input("Would you like to upload a copy of your resume? (Y/N) ")
    if answer == "Y":
        pdfFileObj = open('C.Griffiths.resume.pdf', 'rb')
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()
def zipcode():
    search = SearchEngine()
    code = input("Please enter your five digit zipcode: ")
    zipcode = search.by_zipcode(code)
    print("We will be searching for jobs in " + zipcode.county +", " + zipcode.state)
    return zipcode

def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()

    return canvas


if __name__ == '__main__':
    main()