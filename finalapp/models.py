from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

ACADEMIC_SESSION = (
    ('-','Select'),
    ('2019-2020','2019-2020'),
    ('2000-2021','2000-2021'),
    ('2021-2022','2021-2022')
)
# SUBJECTS_CHOICES = (
#     ('1','Select'),
#     ('2','English'),
#     ('3','Hindi'),
#     ('4','Marathi'),
#     ('5','Mathematics'),
#     ('6','Science / EVS'),
#     ('7','So. Science'),
# )
CLASSES_CHOICES = (
    ('5','Select'),
    ('5th','5th'),
    ('6th','6th'),
    ('7th','7th'),
    ('8th','8th'),
    ('9th','9th')
)
SECTION_CHOICES = (
    ('1','Select'),
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D')
)

GRADE_CHOICES = (
    ('-','Select'),
    ('A','A'),
    ('B','B'),
    ('C','C')
)

class Classes_Master(models.Model):
    Class_Name = models.CharField('Class', max_length=30)
    def __str__(self):
        return self.Class_Name

    class Meta:
        db_table = 'classes_master'

class Section_Master(models.Model):
    # Classes_Section = models.ForeignKey(Classes_Master, on_delete=models.CASCADE, null=True)
    Section_Name = models.CharField('Section', max_length=30)

    def __str__(self):
        return self.Section_Name

    class Meta:
        db_table = 'section_master'

class Student_Details(models.Model):
    Academic_Session = models.CharField('Academic Session',choices=ACADEMIC_SESSION,max_length=50,null=True)
    Stud_class = models.CharField('Student Class',choices=CLASSES_CHOICES,max_length=50,null=True)
   # Stud_class = models.ForeignKey(Classes_Master,on_delete=models.SET_NULL, null=True,related_name='stud_info')
    Section = models.CharField('Student Section',choices=SECTION_CHOICES,max_length=50,null=True)
    # Section = models.ForeignKey(Section_Master,on_delete=models.SET_NULL, null=True,related_name='stud_info_sec')
    Roll_no = models.IntegerField('Roll No',blank=False,unique=True)
    Student_name = models.CharField('Student`s Name',max_length=100)
    Father_name = models.CharField('Father`s Name',max_length=100)
    Mother_name = models.CharField('Mother`s Name', max_length=100)
    Date_of_Birth = models.DateField()
    # term 1
    # English
    # Subject_name = models.CharField('Subject_name',choices=SUBJECTS_CHOICES,max_length=10)
    Subject_English = models.CharField('English', default='English', max_length=10)
    English_p_test_term1 = models.IntegerField('English_p_test_term1',validators=[MinValueValidator(0),MaxValueValidator(20)], default="")
    English_Note_Book_term1 = models.IntegerField('English_Note_Book_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    English_Sub_Enrichment_term1 = models.IntegerField('English_Sub_Enrichment_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    English_Half_Yearly_Exam_term1 = models.IntegerField('English_Half_Yearly_Exam_term1',validators=[MinValueValidator(0),MaxValueValidator(60)])
    English_Marks_obtained_term1 = models.IntegerField('English_Marks_obtained_term1')
    English_Grade_term1 = models.CharField('English_Grade_term1', max_length=10)
    # term 2
    English_p_test_term2 = models.IntegerField('English_p_test_term2',validators=[MinValueValidator(0),MaxValueValidator(20)])
    English_Note_Book_term2 = models.IntegerField('English_Note_Book_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    English_Sub_Enrichment_term2 = models.IntegerField('English_Sub_Enrichment_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    English_Half_Yearly_Exam_term2 = models.IntegerField('English_Half_Yearly_Exam_term2',validators=[MinValueValidator(0),MaxValueValidator(60)])
    English_Marks_obtained_term2 = models.IntegerField('English_Marks_obtained_term2')
    English_Grade_term2 = models.CharField('English_Grade_term2', max_length=10)

    # Hindi
    Subject_Hindi = models.CharField('Hindi', default='Hindi', max_length=10)
    Hindi_p_test_term1 = models.IntegerField('Hindi_p_test_term1',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    Hindi_Note_Book_term1 = models.IntegerField('Hindi_Note_Book_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Hindi_Sub_Enrichment_term1 = models.IntegerField('Hindi_Sub_Enrichment_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Hindi_Half_Yearly_Exam_term1 = models.IntegerField('Hindi_Half_Yearly_Exam_term1',validators=[MinValueValidator(0),MaxValueValidator(60)])
    Hindi_Marks_obtained_term1 = models.IntegerField('Hindi_Marks_obtained_term1')
    Hindi_Grade_term1 = models.CharField('Hindi_Grade_term1', max_length=10)
    # term 2
    Hindi_p_test_term2 = models.IntegerField('Hindi_p_test_term2',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    Hindi_Note_Book_term2 = models.IntegerField('Hindi_Note_Book_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Hindi_Sub_Enrichment_term2 = models.IntegerField('Hindi_Sub_Enrichment_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Hindi_Half_Yearly_Exam_term2 = models.IntegerField('Hindi_Half_Yearly_Exam_term2',validators=[MinValueValidator(0),MaxValueValidator(60)])
    Hindi_Marks_obtained_term2 = models.IntegerField('Hindi_Marks_obtained_term2')
    Hindi_Grade_term2 = models.CharField('Hindi_Grade_term2', max_length=10)

    # Marathi
    Subject_Marathi = models.CharField('Marathi', default='Marathi', max_length=10)
    Marathi_p_test_term1 = models.IntegerField('Marathi_p_test_term1',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    Marathi_Note_Book_term1 = models.IntegerField('Marathi_Note_Book_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Marathi_Sub_Enrichment_term1 = models.IntegerField('Marathi_Sub_Enrichment_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Marathi_Half_Yearly_Exam_term1 = models.IntegerField('Marathi_Half_Yearly_Exam_term1',validators=[MinValueValidator(0),MaxValueValidator(60)])
    Marathi_Marks_obtained_term1 = models.IntegerField('Marathi_Marks_obtained_term1')
    Marathi_Grade_term1 = models.CharField('Marathi_Grade_term1', max_length=10)
    # term 2
    Marathi_p_test_term2 = models.IntegerField('Marathi_p_test_term2',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    Marathi_Note_Book_term2 = models.IntegerField('Marathi_Note_Book_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Marathi_Sub_Enrichment_term2 = models.IntegerField('Marathi_Sub_Enrichment_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Marathi_Half_Yearly_Exam_term2 = models.IntegerField('Marathi_Half_Yearly_Exam_term2',validators=[MinValueValidator(0),MaxValueValidator(60)])
    Marathi_Marks_obtained_term2 = models.IntegerField('Marathi_Marks_obtained_term2')
    Marathi_Grade_term2 = models.CharField('Marathi_Grade_term2', max_length=10)

    # Mathematics
    Subject_Math = models.CharField('Math', default='Math', max_length=10)
    Math_p_test_term1 = models.IntegerField('Math_p_test_term1',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    Math_Note_Book_term1 = models.IntegerField('Math_Note_Book_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Math_Sub_Enrichment_term1 = models.IntegerField('Math_Sub_Enrichment_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Math_Half_Yearly_Exam_term1 = models.IntegerField('Math_Half_Yearly_Exam_term1',validators=[MinValueValidator(0),MaxValueValidator(60)])
    Math_Marks_obtained_term1 = models.IntegerField('Math_Marks_obtained_term1')
    Math_Grade_term1 = models.CharField('Math_Grade_term1', max_length=10)
    # term 2
    Math_p_test_term2 = models.IntegerField('Math_p_test_term2',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    Math_Note_Book_term2 = models.IntegerField('Math_Note_Book_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Math_Sub_Enrichment_term2 = models.IntegerField('Math_Sub_Enrichment_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Math_Half_Yearly_Exam_term2 = models.IntegerField('Math_Half_Yearly_Exam_term2',validators=[MinValueValidator(0),MaxValueValidator(60)])
    Math_Marks_obtained_term2 = models.IntegerField('Math_Marks_obtained_term2')
    Math_Grade_term2 = models.CharField('Math_Grade_term2', max_length=10)

    # Science/EVS
    Subject_Sci = models.CharField('Science', default='Science', max_length=10)
    Sci_p_test_term1 = models.IntegerField('Sci_p_test_term1',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    Sci_Note_Book_term1 = models.IntegerField('Sci_Note_Book_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Sci_Sub_Enrichment_term1 = models.IntegerField('Sci_Sub_Enrichment_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Sci_Half_Yearly_Exam_term1 = models.IntegerField('Sci_Half_Yearly_Exam_term1',validators=[MinValueValidator(0),MaxValueValidator(60)])
    Sci_Marks_obtained_term1 = models.IntegerField('Sci_Marks_obtained_term1')
    Sci_Grade_term1 = models.CharField('Sci_Grade_term1', max_length=10)
    # term 2
    Sci_p_test_term2 = models.IntegerField('Sci_p_test_term2',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    Sci_Note_Book_term2 = models.IntegerField('Sci_Note_Book_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Sci_Sub_Enrichment_term2 = models.IntegerField('Sci_Sub_Enrichment_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    Sci_Half_Yearly_Exam_term2 = models.IntegerField('Sci_Half_Yearly_Exam_term2',validators=[MinValueValidator(0),MaxValueValidator(60)])
    Sci_Marks_obtained_term2 = models.IntegerField('Sci_Marks_obtained_term2')
    Sci_Grade_term2 = models.CharField('Sci_Grade_term2', max_length=10)

    # So.Science
    Subject_So_Sci = models.CharField('So_Science', default='So_Science', max_length=10)
    So_Sci_p_test_term1 = models.IntegerField('So_Sci_p_test_term1',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    So_Sci_Note_Book_term1 = models.IntegerField('So_Sci_Note_Book_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    So_Sci_Sub_Enrichment_term1 = models.IntegerField('So_Sci_Sub_Enrichment_term1',validators=[MinValueValidator(0),MaxValueValidator(10)])
    So_Sci_Half_Yearly_Exam_term1 = models.IntegerField('So_Sci_Half_Yearly_Exam_term1',validators=[MinValueValidator(0),MaxValueValidator(60)])
    So_Sci_Marks_obtained_term1 = models.IntegerField('So_Sci_Marks_obtained_term1')
    So_Sci_Grade_term1 = models.CharField('So_Sci_Grade_term1', max_length=10)
    # term 2
    So_Sci_p_test_term2 = models.IntegerField('So_Sci_p_test_term2',validators=[MinValueValidator(0), MaxValueValidator(20)], default="")
    So_Sci_Note_Book_term2 = models.IntegerField('So_Sci_Note_Book_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    So_Sci_Sub_Enrichment_term2 = models.IntegerField('So_Sci_Sub_Enrichment_term2',validators=[MinValueValidator(0),MaxValueValidator(10)])
    So_Sci_Half_Yearly_Exam_term2 = models.IntegerField('So_Sci_Half_Yearly_Exam_term2',validators=[MinValueValidator(0),MaxValueValidator(60)])
    So_Sci_Marks_obtained_term2 = models.IntegerField('So_Sci_Marks_obtained_term2')
    So_Sci_Grade_term2 = models.CharField('So_Sci_Grade_term2', max_length=10)

    Work_Education_term1 = models.CharField('Work_Education_term1',choices=GRADE_CHOICES,max_length=50,null=True)
    Work_Education_term2 = models.CharField('Work_Education_term2', choices=GRADE_CHOICES, max_length=50, null=True)
    Art_Education_term1  = models.CharField('Art_Education_term1', choices=GRADE_CHOICES, max_length=50, null=True)
    Art_Education_term2 = models.CharField('Art_Education_term2', choices=GRADE_CHOICES, max_length=50, null=True)
    H_P_Education_term1 = models.CharField('H_P_Education_term1', choices=GRADE_CHOICES, max_length=50, null=True)
    H_P_Education_term2 = models.CharField('H_P_Education_term2', choices=GRADE_CHOICES, max_length=50, null=True)
    Discipline_term1 = models.CharField('Discipline_term1', choices=GRADE_CHOICES, max_length=50, null=True)
    Discipline_term2 = models.CharField('Discipline_term2', choices=GRADE_CHOICES, max_length=50, null=True)

    Promoted_to_class = models.CharField('Promoted_to_class',choices=CLASSES_CHOICES,max_length=50,null=True)



    # term 2
    # English
    # English_p_test_term2 = models.IntegerField('English_p_test_term2', default="")
    # English_Note_Book_term2 = models.IntegerField('English_Note_Book_term2')
    # English_Sub_Enrichment_term2 = models.IntegerField('English_Sub_Enrichment_term2')
    # English_Half_Yearly_Exam_term2 = models.IntegerField('English_Half_Yearly_Exam_term2')
    # English_Marks_obtained_term2 = models.IntegerField('English_Marks_obtained_term2')
    # English_Grade_term2 = models.CharField('English_Grade_term2', max_length=10)
    # # Hindi
    # Hindi_p_test_term2 = models.IntegerField('Hindi_p_test_term2', default="")
    # Hindi_Note_Book_term2 = models.IntegerField('Hindi_Note_Book_term2')
    # Hindi_Sub_Enrichment_term2 = models.IntegerField('Hindi_Sub_Enrichment_term2')
    # Hindi_Half_Yearly_Exam_term2 = models.IntegerField('Hindi_Half_Yearly_Exam_term2')
    # Hindi_Marks_obtained_term2 = models.IntegerField('Hindi_Marks_obtained_term2')
    # Hindi_Grade_term2 = models.CharField('Hindi_Grade_term2', max_length=10)

    def __str__(self):
        return self.Student_name

    class Meta:
        db_table = 'student_details'

'''
class Term1(models.Model):
    Stud_Name = models.ForeignKey(Student_info, on_delete=models.SET_NULL, null=False)
    Subject = models.CharField(Subject_Master, choices=SUBJECTS_CHOICES, null=False)
    p_test = models.IntegerField('p_test', default="")
    Note_Book = models.IntegerField('Note_Book')
    Sub_Enrichment = models.IntegerField('Sub_Enrichment')
    Half_Yearly_Exam = models.IntegerField('Half_Yearly_Exam')
    Marks_obtained = models.IntegerField('Marks_obtained')
    Grade = models.CharField('Grade',max_length=10)

    def __str__(self):
        return self.Student_name + self.Subject

    class Meta:
        db_table = 'Term1'

class Term2(models.Model):
    Stud_Name = models.ForeignKey(Student_info, on_delete=models.SET_NULL, null=True)
    Subject = models.ForeignKey(Subject_Master, on_delete=models.SET_NULL, null=True)
    p_test = models.IntegerField('p_test', default="")
    Note_Book = models.IntegerField('Note_Book')
    Sub_Enrichment = models.IntegerField('Sub_Enrichment')
    Half_Yearly_Exam = models.IntegerField('Half_Yearly_Exam')
    Marks_obtained = models.IntegerField('Marks_obtained')
    Grade = models.CharField('Grade', max_length=10)

    def __str__(self):
        return self.Student_name + self.Subject

    class Meta:
        db_table = 'Term2'
   '''
'''        
class Subject_Master(models.Model):
    Subject_Name = models.CharField('Subject', max_length=50)
    def __str__(self):
        return self.Subject_Name

    class Meta:
        db_table = 'subject_master'

class Classes_Master(models.Model):
    Class_Name = models.CharField('Class', max_length=30)
    def __str__(self):
        return self.Class_Name

    class Meta:
        db_table = 'classes_master'

class Section_Master(models.Model):
    # Classes_Section = models.ForeignKey(Classes_Master, on_delete=models.CASCADE, null=True)
    Section_Name = models.CharField('Section ', max_length=30)

    def __str__(self):
        return self.Section_Name

    class Meta:
        db_table = 'section_master'

'''