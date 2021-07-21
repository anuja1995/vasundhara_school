from django import forms
from django.forms import ModelForm,Textarea
from .models import Student_Details


class DateInput(forms.DateInput):
    input_type = 'date'


class RegisterForm(ModelForm):
    # Student_name = forms.CharField(label='Student_Name', max_length=100)
    # Father_name = forms.CharField(label='Father_Name', max_length=100)
    # Mother_name = forms.CharField(label='Mother_Name', max_length=100)

    class Meta:
        model = Student_Details
    #     fields = '__all__'
        fields = ['Academic_Session','Stud_class','Section','Roll_no','Student_name','Father_name','Mother_name','Date_of_Birth',
                  'English_p_test_term1','English_Note_Book_term1','English_Sub_Enrichment_term1',
                  'English_Half_Yearly_Exam_term1','English_p_test_term2','English_Note_Book_term2',
                  'English_Sub_Enrichment_term2','English_Half_Yearly_Exam_term2',
                  'Hindi_p_test_term1','Hindi_Note_Book_term1','Hindi_Sub_Enrichment_term1','Hindi_Half_Yearly_Exam_term1',
                  'Hindi_p_test_term2','Hindi_Note_Book_term2', 'Hindi_Sub_Enrichment_term2', 'Hindi_Half_Yearly_Exam_term2',
                  'Marathi_p_test_term1','Marathi_Note_Book_term1','Marathi_Sub_Enrichment_term1','Marathi_Half_Yearly_Exam_term1',
                  'Marathi_p_test_term2', 'Marathi_Note_Book_term2','Marathi_Sub_Enrichment_term2','Marathi_Half_Yearly_Exam_term2',
                  'Math_p_test_term1','Math_Note_Book_term1', 'Math_Sub_Enrichment_term1','Math_Half_Yearly_Exam_term1',
                  'Math_p_test_term2','Math_Note_Book_term2','Math_Sub_Enrichment_term2', 'Math_Half_Yearly_Exam_term2',
                  'Sci_p_test_term1', 'Sci_Note_Book_term1', 'Sci_Sub_Enrichment_term1','Sci_Half_Yearly_Exam_term1',
                  'Sci_p_test_term2','Sci_Note_Book_term2', 'Sci_Sub_Enrichment_term2', 'Sci_Half_Yearly_Exam_term2',
                  'So_Sci_p_test_term1', 'So_Sci_Note_Book_term1', 'So_Sci_Sub_Enrichment_term1','So_Sci_Half_Yearly_Exam_term1',
                  'So_Sci_p_test_term2','So_Sci_Note_Book_term2', 'So_Sci_Sub_Enrichment_term2', 'So_Sci_Half_Yearly_Exam_term2',
                  'Work_Education_term1','Work_Education_term2','Art_Education_term1','Art_Education_term2','H_P_Education_term1',
                  'H_P_Education_term2','Discipline_term1','Discipline_term2','Promoted_to_class'

                  ]
        widgets = {
            'Date_of_Birth': DateInput(),
        }


class RegisterForm_class9(ModelForm):
    # Student_name = forms.CharField(label='Student_Name', max_length=100)
    # Father_name = forms.CharField(label='Father_Name', max_length=100)
    # Mother_name = forms.CharField(label='Mother_Name', max_length=100)

    class Meta:
        model = Student_Details
        fields = ['Academic_Session','Stud_class','Section','Roll_no','Student_name','Father_name','Mother_name','Date_of_Birth',
                  'English_p_test_term2','English_Note_Book_term2',
                  'English_Sub_Enrichment_term2','English_Half_Yearly_Exam_term2',
                  'Hindi_p_test_term2','Hindi_Note_Book_term2', 'Hindi_Sub_Enrichment_term2', 'Hindi_Half_Yearly_Exam_term2',
                  'Math_p_test_term2','Math_Note_Book_term2','Math_Sub_Enrichment_term2', 'Math_Half_Yearly_Exam_term2',
                  'Sci_p_test_term2','Sci_Note_Book_term2', 'Sci_Sub_Enrichment_term2', 'Sci_Half_Yearly_Exam_term2',
                  'So_Sci_p_test_term2','So_Sci_Note_Book_term2', 'So_Sci_Sub_Enrichment_term2', 'So_Sci_Half_Yearly_Exam_term2',
                  'IT_p_test_term2','IT_Note_Book_term2','IT_Sub_Enrichment_term2','IT_Half_Yearly_Exam_term2',
                  'Work_Education_term2','Art_Education_term2',
                  'H_P_Education_term2','Discipline_term2','Promoted_to_class'

                  ]
        widgets = {
                    'Date_of_Birth': DateInput(),
                }

# class RegisterForm(forms.Form):
#         Roll_no = forms.CharField(label='Roll_no')
#         Student_name = forms.CharField(label='Student_Name', max_length=100)
