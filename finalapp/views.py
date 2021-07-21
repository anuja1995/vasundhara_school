from django.shortcuts import render
'''
Using Python 3
pip install --pre xhtml2pdf 
Successfully built xhtml2pdf future
Installing collected packages: future, reportlab, python-bidi, pyPdf2, html5lib, arabic-reshaper, xhtml2pdf

Using Python 2
pip install xhtml2pdf

pip install xhtml2pdf
'''
# Create your views here.

from django.http import HttpResponse
from django.views.generic import View
import datetime
# from .utils import render_to_pdf #created in step 4
from django.template.loader import get_template
# from django.contrib.staticfiles import finders
from .models import Student_Details
# from django.contrib.auth.models import User
from .forms import RegisterForm,RegisterForm_class9

from io import BytesIO
# from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template import Context

from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')

def Grade(sub_marks):
    if sub_marks > 80:
        return 'A'
    elif sub_marks > 60:
        return 'B'
    elif sub_marks > 33:
        return 'C'
    else:
        return 'D'

def StudentDetailsView(request, *args, **kwargs):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # print(form)

        if form.is_valid():
            # form.save()
            Academic_Session = form.data['Academic_Session']
            Stud_class = form.data['Stud_class']
            Section = form.data['Section']
            Roll_no = form.data['Roll_no']
            Student_name = form.data['Student_name']
            Father_name = form.data['Father_name']
            Mother_name = form.data['Mother_name']
            Date_of_Birth = form.data['Date_of_Birth']

            Subject_English = 'English'
            English_p_test_term1 = form.data['English_p_test_term1']
            English_Note_Book_term1 = form.data['English_Note_Book_term1']
            English_Sub_Enrichment_term1 = form.data['English_Sub_Enrichment_term1']
            English_Half_Yearly_Exam_term1 = form.data['English_Half_Yearly_Exam_term1']
            English_Marks_obtained_term1 = int(English_p_test_term1) + int(English_Note_Book_term1) + int(English_Sub_Enrichment_term1) + int(English_Half_Yearly_Exam_term1)
            # English_Grade_term1 = form.data['English_Grade_term1']
            English_Grade_term1 = Grade(English_Marks_obtained_term1)

            English_p_test_term2 = form.data['English_p_test_term2']
            English_Note_Book_term2 = form.data['English_Note_Book_term2']
            English_Sub_Enrichment_term2 = form.data['English_Sub_Enrichment_term2']
            English_Half_Yearly_Exam_term2 = form.data['English_Half_Yearly_Exam_term2']
            English_Marks_obtained_term2 = int(English_p_test_term2) + int(English_Note_Book_term2) + int(English_Sub_Enrichment_term2) + int(English_Half_Yearly_Exam_term2)
            # English_Grade_term2 = form.data['English_Grade_term2']
            English_Grade_term2 = Grade(English_Marks_obtained_term2)

            Subject_Hindi = 'Hindi'
            Hindi_p_test_term1 = form.data['Hindi_p_test_term1']
            Hindi_Note_Book_term1 = form.data['Hindi_Note_Book_term1']
            Hindi_Sub_Enrichment_term1 = form.data['Hindi_Sub_Enrichment_term1']
            Hindi_Half_Yearly_Exam_term1 = form.data['Hindi_Half_Yearly_Exam_term1']
            Hindi_Marks_obtained_term1 = int(Hindi_p_test_term1) + int(Hindi_Note_Book_term1) + int(Hindi_Sub_Enrichment_term1) + int(Hindi_Half_Yearly_Exam_term1)
            # Hindi_Grade_term1 = form.data['Hindi_Grade_term1']
            Hindi_Grade_term1 = Grade(Hindi_Marks_obtained_term1)

            Hindi_p_test_term2 = form.data['Hindi_p_test_term2']
            Hindi_Note_Book_term2 = form.data['Hindi_Note_Book_term2']
            Hindi_Sub_Enrichment_term2 = form.data['Hindi_Sub_Enrichment_term2']
            Hindi_Half_Yearly_Exam_term2 = form.data['Hindi_Half_Yearly_Exam_term2']
            Hindi_Marks_obtained_term2 = int(Hindi_p_test_term2) + int(Hindi_Note_Book_term2) + int(Hindi_Sub_Enrichment_term2) + int(Hindi_Half_Yearly_Exam_term2)
            # Hindi_Grade_term2 = form.data['Hindi_Grade_term2']
            Hindi_Grade_term2 = Grade(Hindi_Marks_obtained_term2)

            Subject_Marathi = 'Marathi'
            Marathi_p_test_term1 = form.data['Marathi_p_test_term1']
            Marathi_Note_Book_term1 = form.data['Marathi_Note_Book_term1']
            Marathi_Sub_Enrichment_term1 = form.data['Marathi_Sub_Enrichment_term1']
            Marathi_Half_Yearly_Exam_term1 = form.data['Marathi_Half_Yearly_Exam_term1']
            Marathi_Marks_obtained_term1 = int(Marathi_p_test_term1) + int(Marathi_Note_Book_term1) + int(Marathi_Sub_Enrichment_term1) + int(Marathi_Half_Yearly_Exam_term1)
            # Marathi_Grade_term1 = form.data['Marathi_Grade_term1']
            Marathi_Grade_term1 = Grade(Marathi_Marks_obtained_term1)

            Marathi_p_test_term2 = form.data['Marathi_p_test_term2']
            Marathi_Note_Book_term2 = form.data['Marathi_Note_Book_term2']
            Marathi_Sub_Enrichment_term2 = form.data['Marathi_Sub_Enrichment_term2']
            Marathi_Half_Yearly_Exam_term2 = form.data['Marathi_Half_Yearly_Exam_term2']
            Marathi_Marks_obtained_term2 = int(Marathi_p_test_term2) + int(Marathi_Note_Book_term2) + int(Marathi_Sub_Enrichment_term2) + int(Marathi_Half_Yearly_Exam_term2)
            # Marathi_Grade_term2 = form.data['Marathi_Grade_term2']
            Marathi_Grade_term2 = Grade(Marathi_Marks_obtained_term2)

            Subject_Math = 'Math'
            Math_p_test_term1 = form.data['Math_p_test_term1']
            Math_Note_Book_term1 = form.data['Math_Note_Book_term1']
            Math_Sub_Enrichment_term1 = form.data['Math_Sub_Enrichment_term1']
            Math_Half_Yearly_Exam_term1 = form.data['Math_Half_Yearly_Exam_term1']
            Math_Marks_obtained_term1 = int(Math_p_test_term1) + int(Math_Note_Book_term1) + int(Math_Sub_Enrichment_term1) + int(Math_Half_Yearly_Exam_term1)
            # Math_Grade_term1 = form.data['Math_Grade_term1']
            Math_Grade_term1 = Grade(Math_Marks_obtained_term1)

            Math_p_test_term2 = form.data['Math_p_test_term2']
            Math_Note_Book_term2 = form.data['Math_Note_Book_term2']
            Math_Sub_Enrichment_term2 = form.data['Math_Sub_Enrichment_term2']
            Math_Half_Yearly_Exam_term2 = form.data['Math_Half_Yearly_Exam_term2']
            Math_Marks_obtained_term2 = int(Math_p_test_term2) + int(Math_Note_Book_term2) + int(Math_Sub_Enrichment_term2) + int(Math_Half_Yearly_Exam_term2)
            # Math_Grade_term2 = form.data['Math_Grade_term2']
            Math_Grade_term2 = Grade(Math_Marks_obtained_term2)

            Subject_Sci = 'Science/EVS'
            Sci_p_test_term1 = form.data['Sci_p_test_term1']
            Sci_Note_Book_term1 = form.data['Sci_Note_Book_term1']
            Sci_Sub_Enrichment_term1 = form.data['Sci_Sub_Enrichment_term1']
            Sci_Half_Yearly_Exam_term1 = form.data['Sci_Half_Yearly_Exam_term1']
            Sci_Marks_obtained_term1 = int(Sci_p_test_term1) + int(Sci_Note_Book_term1) + int(Sci_Sub_Enrichment_term1) + int(Sci_Half_Yearly_Exam_term1)
            # Sci_Grade_term1 = form.data['Sci_Grade_term1']
            Sci_Grade_term1 = Grade(Sci_Marks_obtained_term1)

            Sci_p_test_term2 = form.data['Sci_p_test_term2']
            Sci_Note_Book_term2 = form.data['Sci_Note_Book_term2']
            Sci_Sub_Enrichment_term2 = form.data['Sci_Sub_Enrichment_term2']
            Sci_Half_Yearly_Exam_term2 = form.data['Sci_Half_Yearly_Exam_term2']
            Sci_Marks_obtained_term2 = int(Sci_p_test_term2) + int(Sci_Note_Book_term2) + int(Sci_Sub_Enrichment_term2) + int(Sci_Half_Yearly_Exam_term2)
            # Sci_Grade_term2 = form.data['Sci_Grade_term2']
            Sci_Grade_term2 = Grade(Sci_Marks_obtained_term2)

            Subject_So_Sci = 'So-Science'
            So_Sci_p_test_term1 = form.data['So_Sci_p_test_term1']
            So_Sci_Note_Book_term1 = form.data['So_Sci_Note_Book_term1']
            So_Sci_Sub_Enrichment_term1 = form.data['So_Sci_Sub_Enrichment_term1']
            So_Sci_Half_Yearly_Exam_term1 = form.data['So_Sci_Half_Yearly_Exam_term1']
            So_Sci_Marks_obtained_term1 = int(So_Sci_p_test_term1) + int(So_Sci_Note_Book_term1) + int(So_Sci_Sub_Enrichment_term1) + int(So_Sci_Half_Yearly_Exam_term1)
            # So_Sci_Grade_term1 = form.data['So_Sci_Grade_term1']
            So_Sci_Grade_term1 = Grade(So_Sci_Marks_obtained_term1)

            So_Sci_p_test_term2 = form.data['So_Sci_p_test_term2']
            So_Sci_Note_Book_term2 = form.data['So_Sci_Note_Book_term2']
            So_Sci_Sub_Enrichment_term2 = form.data['So_Sci_Sub_Enrichment_term2']
            So_Sci_Half_Yearly_Exam_term2 = form.data['So_Sci_Half_Yearly_Exam_term2']
            So_Sci_Marks_obtained_term2 = int(So_Sci_p_test_term2) + int(So_Sci_Note_Book_term2) + int(So_Sci_Sub_Enrichment_term2) + int(So_Sci_Half_Yearly_Exam_term2)
            # So_Sci_Grade_term2 = form.data['So_Sci_Grade_term2']
            So_Sci_Grade_term2 = Grade(So_Sci_Marks_obtained_term2)

            Work_Education_term1 = form.data['Work_Education_term1']
            Work_Education_term2 = form.data['Work_Education_term2']
            Art_Education_term1 = form.data['Art_Education_term1']
            Art_Education_term2 = form.data['Art_Education_term2']
            H_P_Education_term1 = form.data['H_P_Education_term1']
            H_P_Education_term2 = form.data['H_P_Education_term2']
            Discipline_term1 = form.data['Discipline_term1']
            Discipline_term2 = form.data['Discipline_term2']
            Promoted_to_class = form.data['Promoted_to_class']



            stud_list = {'Academic_Session':Academic_Session,'Stud_class':Stud_class,'Section':Section,'Roll_no':Roll_no,'Student_name':Student_name,
                         'Father_name':Father_name,'Mother_name':Mother_name,'Date_of_Birth':Date_of_Birth,
                         'Subject_English':Subject_English,
                         'English_p_test_term1':English_p_test_term1,'English_Note_Book_term1':English_Note_Book_term1,
                         'English_Sub_Enrichment_term1':English_Sub_Enrichment_term1,'English_Half_Yearly_Exam_term1':English_Half_Yearly_Exam_term1,
                         'English_Marks_obtained_term1':English_Marks_obtained_term1,'English_Grade_term1':English_Grade_term1,
                         'English_p_test_term2':English_p_test_term2,'English_Note_Book_term2': English_Note_Book_term2,
                         'English_Sub_Enrichment_term2': English_Sub_Enrichment_term2,'English_Half_Yearly_Exam_term2': English_Half_Yearly_Exam_term2,
                         'English_Marks_obtained_term2': English_Marks_obtained_term2,'English_Grade_term2': English_Grade_term2,

                         'Subject_Hindi':Subject_Hindi,'Hindi_p_test_term1':Hindi_p_test_term1,'Hindi_Note_Book_term1':Hindi_Note_Book_term1,
                         'Hindi_Sub_Enrichment_term1':Hindi_Sub_Enrichment_term1,'Hindi_Half_Yearly_Exam_term1':Hindi_Half_Yearly_Exam_term1,
                         'Hindi_Marks_obtained_term1':Hindi_Marks_obtained_term1,'Hindi_Grade_term1':Hindi_Grade_term1,
                         'Hindi_p_test_term2': Hindi_p_test_term2, 'Hindi_Note_Book_term2': Hindi_Note_Book_term2,
                         'Hindi_Sub_Enrichment_term2': Hindi_Sub_Enrichment_term2,'Hindi_Half_Yearly_Exam_term2': Hindi_Half_Yearly_Exam_term2,
                         'Hindi_Marks_obtained_term2': Hindi_Marks_obtained_term2,'Hindi_Grade_term2': Hindi_Grade_term2,

                         'Subject_Marathi': Subject_Marathi,'Marathi_p_test_term1': Marathi_p_test_term1,'Marathi_Note_Book_term1': Marathi_Note_Book_term1,
                         'Marathi_Sub_Enrichment_term1': Marathi_Sub_Enrichment_term1,'Marathi_Half_Yearly_Exam_term1': Marathi_Half_Yearly_Exam_term1,
                         'Marathi_Marks_obtained_term1': Marathi_Marks_obtained_term1,'Marathi_Grade_term1': Marathi_Grade_term1,
                         'Marathi_p_test_term2': Marathi_p_test_term2,'Marathi_Note_Book_term2': Marathi_Note_Book_term2,
                         'Marathi_Sub_Enrichment_term2': Marathi_Sub_Enrichment_term2,'Marathi_Half_Yearly_Exam_term2': Marathi_Half_Yearly_Exam_term2,
                         'Marathi_Marks_obtained_term2': Marathi_Marks_obtained_term2,'Marathi_Grade_term2': Marathi_Grade_term2,

                         'Subject_Math': Subject_Math,
                         'Math_p_test_term1': Math_p_test_term1,
                         'Math_Note_Book_term1': Math_Note_Book_term1,
                         'Math_Sub_Enrichment_term1': Math_Sub_Enrichment_term1,
                         'Math_Half_Yearly_Exam_term1': Math_Half_Yearly_Exam_term1,
                         'Math_Marks_obtained_term1': Math_Marks_obtained_term1,
                         'Math_Grade_term1': Math_Grade_term1,
                         'Math_p_test_term2': Math_p_test_term2,
                         'Math_Note_Book_term2': Math_Note_Book_term2,
                         'Math_Sub_Enrichment_term2': Math_Sub_Enrichment_term2,
                         'Math_Half_Yearly_Exam_term2': Math_Half_Yearly_Exam_term2,
                         'Math_Marks_obtained_term2': Math_Marks_obtained_term2,
                         'Math_Grade_term2': Math_Grade_term2,

                         'Subject_Sci': Subject_Sci,
                         'Sci_p_test_term1': Sci_p_test_term1,
                         'Sci_Note_Book_term1': Sci_Note_Book_term1,
                         'Sci_Sub_Enrichment_term1': Sci_Sub_Enrichment_term1,
                         'Sci_Half_Yearly_Exam_term1': Sci_Half_Yearly_Exam_term1,
                         'Sci_Marks_obtained_term1': Sci_Marks_obtained_term1,
                         'Sci_Grade_term1': Sci_Grade_term1,
                         'Sci_p_test_term2': Sci_p_test_term2,
                         'Sci_Note_Book_term2': Sci_Note_Book_term2,
                         'Sci_Sub_Enrichment_term2': Sci_Sub_Enrichment_term2,
                         'Sci_Half_Yearly_Exam_term2': Sci_Half_Yearly_Exam_term2,
                         'Sci_Marks_obtained_term2': Sci_Marks_obtained_term2,
                         'Sci_Grade_term2': Sci_Grade_term2,

                         'Subject_So_Sci': Subject_So_Sci,
                         'So_Sci_p_test_term1': So_Sci_p_test_term1,
                         'So_Sci_Note_Book_term1': So_Sci_Note_Book_term1,
                         'So_Sci_Sub_Enrichment_term1': So_Sci_Sub_Enrichment_term1,
                         'So_Sci_Half_Yearly_Exam_term1': So_Sci_Half_Yearly_Exam_term1,
                         'So_Sci_Marks_obtained_term1': So_Sci_Marks_obtained_term1,
                         'So_Sci_Grade_term1': So_Sci_Grade_term1,
                         'So_Sci_p_test_term2': So_Sci_p_test_term2,
                         'So_Sci_Note_Book_term2': So_Sci_Note_Book_term2,
                         'So_Sci_Sub_Enrichment_term2': So_Sci_Sub_Enrichment_term2,
                         'So_Sci_Half_Yearly_Exam_term2': So_Sci_Half_Yearly_Exam_term2,
                         'So_Sci_Marks_obtained_term2': So_Sci_Marks_obtained_term2,
                         'So_Sci_Grade_term2': So_Sci_Grade_term2,

                         'Work_Education_term1':Work_Education_term1,'Work_Education_term2':Work_Education_term2,
                         'Art_Education_term1':Art_Education_term1,'Art_Education_term2':Art_Education_term2,
                         'H_P_Education_term1':H_P_Education_term1,'H_P_Education_term2':H_P_Education_term2,
                         'Discipline_term1':Discipline_term1,'Discipline_term2':Discipline_term2,
                         'Promoted_to_class':Promoted_to_class,



                         }
            # stud_list = {'Academic_Session':Academic_Session,'Stud_class':Stud_class,'Section':Section,'Roll_no':Roll_no,
            #              'Student_name':Student_name,'Father_name':Father_name,'Mother_name':Mother_name,'Date_of_Birth':Date_of_Birth,
            #              'Subject_English':Subject_English}
            # print(stud_list)

            # stud_list = Student_Details.objects.filter(id=id)
            data = {
                'stud_list':stud_list,
            }
            pdf = render_to_pdf('studentform.html', data)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "%s_%s.pdf" % (Roll_no,Student_name)
                content = "inline; filename=%s" % (filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=%s" % (filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")
#             return HttpResponse(pdf, content_type='application/pdf')
    else:
        form = RegisterForm()
    return render(request, 'finalapp/student_details_form.html',{'form':form})



def class9_StudentDetailsView(request, *args, **kwargs):
    if request.method == 'POST':
        form = RegisterForm_class9(request.POST)
        # print(form)
        if form.is_valid():
            # print(form)
            # form.save()
            Academic_Session = form.data['Academic_Session']
            Stud_class = form.data['Stud_class']
            Section = form.data['Section']
            Roll_no = form.data['Roll_no']
            Student_name = form.data['Student_name']
            Father_name = form.data['Father_name']
            Mother_name = form.data['Mother_name']
            Date_of_Birth = form.data['Date_of_Birth']

            Subject_English = 'English'
            English_p_test_term2 = form.data['English_p_test_term2']
            English_Note_Book_term2 = form.data['English_Note_Book_term2']
            English_Sub_Enrichment_term2 = form.data['English_Sub_Enrichment_term2']
            English_Half_Yearly_Exam_term2 = form.data['English_Half_Yearly_Exam_term2']
            English_Marks_obtained_term2 = int(English_p_test_term2) + int(English_Note_Book_term2) + int(English_Sub_Enrichment_term2) + int(English_Half_Yearly_Exam_term2)
            # English_Grade_term2 = form.data['English_Grade_term2']
            English_Grade_term2 = Grade(English_Marks_obtained_term2)

            Subject_Hindi = 'Hindi'
            Hindi_p_test_term2 = form.data['Hindi_p_test_term2']
            Hindi_Note_Book_term2 = form.data['Hindi_Note_Book_term2']
            Hindi_Sub_Enrichment_term2 = form.data['Hindi_Sub_Enrichment_term2']
            Hindi_Half_Yearly_Exam_term2 = form.data['Hindi_Half_Yearly_Exam_term2']
            Hindi_Marks_obtained_term2 = int(Hindi_p_test_term2) + int(Hindi_Note_Book_term2) + int(Hindi_Sub_Enrichment_term2) + int(Hindi_Half_Yearly_Exam_term2)
            # Hindi_Grade_term2 = form.data['Hindi_Grade_term2']
            Hindi_Grade_term2 = Grade(Hindi_Marks_obtained_term2)


            Subject_Math = 'Math'
            Math_p_test_term2 = form.data['Math_p_test_term2']
            Math_Note_Book_term2 = form.data['Math_Note_Book_term2']
            Math_Sub_Enrichment_term2 = form.data['Math_Sub_Enrichment_term2']
            Math_Half_Yearly_Exam_term2 = form.data['Math_Half_Yearly_Exam_term2']
            Math_Marks_obtained_term2 = int(Math_p_test_term2) + int(Math_Note_Book_term2) + int(Math_Sub_Enrichment_term2) + int(Math_Half_Yearly_Exam_term2)
            # Math_Grade_term2 = form.data['Math_Grade_term2']
            Math_Grade_term2 = Grade(Math_Marks_obtained_term2)

            Subject_Sci = 'Science/EVS'
            Sci_p_test_term2 = form.data['Sci_p_test_term2']
            Sci_Note_Book_term2 = form.data['Sci_Note_Book_term2']
            Sci_Sub_Enrichment_term2 = form.data['Sci_Sub_Enrichment_term2']
            Sci_Half_Yearly_Exam_term2 = form.data['Sci_Half_Yearly_Exam_term2']
            Sci_Marks_obtained_term2 = int(Sci_p_test_term2) + int(Sci_Note_Book_term2) + int(Sci_Sub_Enrichment_term2) + int(Sci_Half_Yearly_Exam_term2)
            # Sci_Grade_term2 = form.data['Sci_Grade_term2']
            Sci_Grade_term2 = Grade(Sci_Marks_obtained_term2)

            Subject_So_Sci = 'So-Science'
            So_Sci_p_test_term2 = form.data['So_Sci_p_test_term2']
            So_Sci_Note_Book_term2 = form.data['So_Sci_Note_Book_term2']
            So_Sci_Sub_Enrichment_term2 = form.data['So_Sci_Sub_Enrichment_term2']
            So_Sci_Half_Yearly_Exam_term2 = form.data['So_Sci_Half_Yearly_Exam_term2']
            So_Sci_Marks_obtained_term2 = int(So_Sci_p_test_term2) + int(So_Sci_Note_Book_term2) + int(So_Sci_Sub_Enrichment_term2) + int(So_Sci_Half_Yearly_Exam_term2)
            # So_Sci_Grade_term2 = form.data['So_Sci_Grade_term2']
            So_Sci_Grade_term2 = Grade(So_Sci_Marks_obtained_term2)

            Subject_IT = 'IT'
            IT_p_test_term2 = form.data['IT_p_test_term2']
            IT_Note_Book_term2 = form.data['IT_Note_Book_term2']
            IT_Sub_Enrichment_term2 = form.data['IT_Sub_Enrichment_term2']
            IT_Half_Yearly_Exam_term2 = form.data['IT_Half_Yearly_Exam_term2']
            IT_Marks_obtained_term2 = int(IT_p_test_term2) + int(IT_Note_Book_term2) + int(IT_Sub_Enrichment_term2) + int(IT_Half_Yearly_Exam_term2)
            # So_Sci_Grade_term2 = form.data['So_Sci_Grade_term2']
            IT_Grade_term2 = Grade(IT_Marks_obtained_term2)

            Work_Education_term2 = form.data['Work_Education_term2']
            Art_Education_term2 = form.data['Art_Education_term2']
            H_P_Education_term2 = form.data['H_P_Education_term2']
            Discipline_term2 = form.data['Discipline_term2']
            Promoted_to_class = form.data['Promoted_to_class']



            stud_list = {'Academic_Session':Academic_Session,'Stud_class':Stud_class,'Section':Section,'Roll_no':Roll_no,'Student_name':Student_name,
                         'Father_name':Father_name,'Mother_name':Mother_name,'Date_of_Birth':Date_of_Birth,
                         'Subject_English':Subject_English,
                         'English_p_test_term2':English_p_test_term2,'English_Note_Book_term2': English_Note_Book_term2,
                         'English_Sub_Enrichment_term2': English_Sub_Enrichment_term2,'English_Half_Yearly_Exam_term2': English_Half_Yearly_Exam_term2,
                         'English_Marks_obtained_term2': English_Marks_obtained_term2,'English_Grade_term2': English_Grade_term2,

                         'Subject_Hindi':Subject_Hindi,
                         'Hindi_p_test_term2': Hindi_p_test_term2, 'Hindi_Note_Book_term2': Hindi_Note_Book_term2,
                         'Hindi_Sub_Enrichment_term2': Hindi_Sub_Enrichment_term2,'Hindi_Half_Yearly_Exam_term2': Hindi_Half_Yearly_Exam_term2,
                         'Hindi_Marks_obtained_term2': Hindi_Marks_obtained_term2,'Hindi_Grade_term2': Hindi_Grade_term2,


                         'Subject_Math': Subject_Math,
                         'Math_p_test_term2': Math_p_test_term2,
                         'Math_Note_Book_term2': Math_Note_Book_term2,
                         'Math_Sub_Enrichment_term2': Math_Sub_Enrichment_term2,
                         'Math_Half_Yearly_Exam_term2': Math_Half_Yearly_Exam_term2,
                         'Math_Marks_obtained_term2': Math_Marks_obtained_term2,
                         'Math_Grade_term2': Math_Grade_term2,

                         'Subject_Sci': Subject_Sci,
                         'Sci_p_test_term2': Sci_p_test_term2,
                         'Sci_Note_Book_term2': Sci_Note_Book_term2,
                         'Sci_Sub_Enrichment_term2': Sci_Sub_Enrichment_term2,
                         'Sci_Half_Yearly_Exam_term2': Sci_Half_Yearly_Exam_term2,
                         'Sci_Marks_obtained_term2': Sci_Marks_obtained_term2,
                         'Sci_Grade_term2': Sci_Grade_term2,

                         'Subject_So_Sci': Subject_So_Sci,
                         'So_Sci_p_test_term2': So_Sci_p_test_term2,
                         'So_Sci_Note_Book_term2': So_Sci_Note_Book_term2,
                         'So_Sci_Sub_Enrichment_term2': So_Sci_Sub_Enrichment_term2,
                         'So_Sci_Half_Yearly_Exam_term2': So_Sci_Half_Yearly_Exam_term2,
                         'So_Sci_Marks_obtained_term2': So_Sci_Marks_obtained_term2,
                         'So_Sci_Grade_term2': So_Sci_Grade_term2,

                         'Subject_IT': Subject_IT,
                         'IT_p_test_term2': IT_p_test_term2,
                         'IT_Note_Book_term2': IT_Note_Book_term2,
                         'IT_Sub_Enrichment_term2': IT_Sub_Enrichment_term2,
                         'IT_Half_Yearly_Exam_term2': IT_Half_Yearly_Exam_term2,
                         'IT_Marks_obtained_term2': IT_Marks_obtained_term2,
                         'IT_Grade_term2': IT_Grade_term2,

                         'Work_Education_term2':Work_Education_term2,
                         'Art_Education_term2':Art_Education_term2,
                         'H_P_Education_term2':H_P_Education_term2,
                         'Discipline_term2':Discipline_term2,
                         'Promoted_to_class':Promoted_to_class,

                         }
            # stud_list = {'Academic_Session':Academic_Session,'Stud_class':Stud_class,'Section':Section,'Roll_no':Roll_no,
            #              'Student_name':Student_name,'Father_name':Father_name,'Mother_name':Mother_name,'Date_of_Birth':Date_of_Birth,
            #              'Subject_English':Subject_English}
            # print(stud_list)

            # stud_list = Student_Details.objects.filter(id=id)
            data = {
                'stud_list':stud_list,
            }
            # print('Stud_class',Stud_class)
            pdf = render_to_pdf('result_9th_class.html', data)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "%s_%s.pdf" % (Roll_no,Student_name)
                content = "inline; filename=%s" % (filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=%s" % (filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")
#             return HttpResponse(pdf, content_type='application/pdf')
    else:
        form = RegisterForm_class9()
    return render(request, 'finalapp/student_details_form_9th.html',{'form':form})

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    # pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result, link_callback=links)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None





# def StudentDetailsView_demo(request):
#     pdf = render_to_pdf('pdfdemo.html')
#     return HttpResponse(pdf, content_type='application/pdf')

# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             form = RegisterForm(request.POST)
#             # print('form',form)
#             id = form.data['Roll_no']
#             # print(id)
#             if form.is_valid():
#                 # print('valid form')
#                 form.save()
#                 stud_list = Student_Details.objects.filter(id=id)
#                 data = {
#                     'today': datetime.date.today(),
#                     'amount': 39.99,
#                     'customer_name': 'Cooper Mann',
#                     'order_id': 1233434,
#                     'stud_list': stud_list,
#                 }
#         context = {
#             "invoice_id": 123,
#             "customer_name": "John Cooper",
#             "amount": 1399.99,
#             "today": "Today",
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('finalapp/student_details_form.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" %("12341231")
#             content = "inline; filename='%s'" %(filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" %(filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")



'''class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(),
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('finalapp/student_details_form.html', data)
        return HttpResponse(pdf, content_type='application/pdf')'''
