from django.db import models


class Students(models.Model):
    study_program = models.CharField(max_length=40, blank=True, null=True)  # Πρόγραμμα Σπουδών (Study Program)
    registration_number = models.IntegerField(blank=True, null=True)  # Αρ. Μητρώου (Registration Number)
    id_number_1 = models.FloatField(blank=True, null=True)  # Αρ. Ταυτότητας (ID Number)
    name = models.CharField(max_length=100, null=True)  # Όνομα (Name)
    surname = models.CharField(max_length=100)  # Επώνυμο (Surname)
    nationality = models.CharField(max_length=10)  # Εθνικότητα
    student_semester = models.IntegerField(blank=True, null=True)  # Εξάμηνο (Semester)
    latest_year = models.IntegerField(blank=True, null=True)  # Τελευταίο έτος (Latest Year)
    id_gunet = models.CharField(max_length=30)
    latest_period = models.CharField(max_length=15)  # Τελευταίο εξάμηνο (Latest Semester)
    year_of_enrolment = models.IntegerField(blank=True, null=True)  # Έτος Εισαγωγής (Year of Enrolment)
    registration_period = models.CharField(max_length=20)  # Περίοδος Εγγραφής (Registration Period)
    way_of_enrolment = models.CharField(max_length=100)  # Τρόπος Εισαγωγής (Way of Enrolment)
    student_category = models.CharField(max_length=50)  # Κατηγορία Φοιτητή (Student Category)
    free_of_tuition = models.CharField(max_length=10)  # Απαλλαγή Διδάκτρων (Free of Tuition)
    active = models.CharField(max_length=10)  # Ενεργός (Active)
    web_active = models.CharField(max_length=10)  # Ενεργός στο web (Web Active)
    exemption_from_prerequisites = models.CharField(max_length=10)  # Εξαίρεση από Προαπαιτούμενα (Excluded)
    part_time = models.CharField(max_length=10)  # Μερικής Φοίτησης (Part-time)
    current_status = models.CharField(max_length=25)  # Κατάσταση (Current Status)
    gender = models.CharField(max_length=20)  # Φύλο (Gender)
    amka = models.CharField(max_length=60)  # ΑΜΚΑ
    tin = models.CharField(max_length=60)  # ΑΦΜ (TIN)
    username = models.CharField(max_length=100)  # Όνομα χρήστη (Username)
    email = models.EmailField(max_length=100)  # Email
    mobile_number = models.CharField(max_length=20)  # Κινητό (Mobile Number)
    phone_number = models.CharField(max_length=20)  # Σταθερό (Phone Number)
    address = models.CharField(max_length=255)  # Διεύθυνση (Address)
    city = models.CharField(max_length=105)  # Πόλη (City)
    name_in_english = models.CharField(max_length=100)  # Όνομα (En) (Name in English)
    last_name_in_english = models.CharField(max_length=100)  # Επώνυμο (En) (Last Name in English)
    fathers_name = models.CharField(max_length=100)  # Πατρώνυμο (Father's Name)
    mothers_Name = models.CharField(max_length=100)  # Μητρώνυμο (Mother's Name)
    date_of_birth = models.CharField(max_length=20)  # Ημ/νία Γέννησης (Date of Birth)
    place_of_birth = models.CharField(max_length=100)  # Τόπος γέννησης (Place of Birth)
    id_number_2 = models.CharField(max_length=255)  # Αρ. Ταυτότητας (ID Number)
    type_of_id = models.CharField(max_length=50)  # Τύπος ταυτότητας (Type of ID)
    rollback_year = models.CharField(max_length=10)  # Αναδρ. Έτος Εισαγωγής (Rollback Year)
    date_of_registration = models.CharField(max_length=20)  # Ημ/νία Πρώτης Εγγραφής (Date of 1st Registration)
    department_registration = models.CharField(max_length=200)  # Τμήμα Εισαγωγής (Department Registration)
    code_of_department = models.IntegerField(blank=True, null=True)  # Κωδικός τμήματος εισαγωγής (Code of Department)

    def __str__(self):
        return self.name + ' ' + self.surname


class StudentGrades(models.Model):
    student = models.ForeignKey(Students, default=None, on_delete=models.CASCADE)
    subject = models.CharField(max_length=40)  # Μάθημα (Subject)
    subject_code = models.CharField(max_length=20, )  # Κωδ. μαθ. (Subject Code)
    subject_of_academic_year = models.CharField(max_length=40, )  # Μάθημα Ακ. Έτους (Subject of Academic Year)
    student_class = models.CharField(max_length=40, )  # Τμήμα Τάξης (Class)
    department = models.CharField(max_length=100, )  # Τμήμα (Department)
    registration_number = models.IntegerField(null=True, blank=True)  # AM (Registration Number - Primary Key)
    grade = models.CharField(max_length=40)  # Βαθμός (Grade)
    exam_period = models.CharField(max_length=100)  # Εξ. Περ. (Exam Period)
    semester = models.CharField(max_length=40)  # Εξάμηνο βαθμολογίας
    thesis = models.CharField(max_length=10)  # Διπλωματική (Thesis)
    internship = models.CharField(max_length=10)  # Πρακτική (Internship)
    ects = models.FloatField(null=True, default=True)  # ECTS
    ps = models.CharField(max_length=40)  # ΠΣ
    date1 = models.CharField(max_length=40)  # Ημ. Πρ. (Date 1)
    modified_by = models.CharField(max_length=40)  # Τροποποίηση από (Modified by)
    date2 = models.CharField(max_length=40)  # Ημ. Επ. (Date 2)

    def __str__(self):
        return self.subject + ' ' + self.student.name + ' ' + self.student.surname
