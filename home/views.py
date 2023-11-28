from django.shortcuts import render, redirect
import pandas as pd
from .models import Students, StudentGrades
import json
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(redirect_field_name='next', login_url='/login')
def dashboard(request):
    return render(request, 'home/dashboard.html')


@login_required(redirect_field_name='next', login_url='/login')
def dashboard_redirect(request):
    return redirect('dashboard')


def login(request):
    page_data = {}
    next = request.GET.get('next')
    if request.POST:
        loginusername = request.POST['username']
        loginpassword = request.POST['password']
        if User.objects.filter(username=loginusername).exists():
            user = authenticate(username=loginusername, password=loginpassword)
            if user is not None:
                auth.login(request, user)
                if next is not None:
                    return redirect(next)
                else:
                    return redirect('/')
            else:
                page_data['error'] = 'Invalid credentials! Please try again'
        else:
            page_data['error'] = "Account Not Found.."

    return render(request, 'auth/login.html', {'page_data': page_data})


def register(request):
    page_data = {}
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        # phone = request.POST['phone']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                page_data['error'] = 'Username Taken'
                # return redirect('register')

            elif User.objects.filter(email=email).exists():
                page_data['error'] = 'Email Taken'
                # return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1)
                user.save()
                context = {'callback_url': "/login", "message": 'Successfully Registered!', 'col': 'success'}
                return render(request, 'auth/register.html', context)
        else:
            page_data['error'] = 'Password not maching'
            # return redirect('register')
    return render(request, 'auth/register.html', {'page_data': page_data})


def logout(request):
    django_logout(request)
    return redirect('/login')


def update_or_create_student(df):
    try:
        df = df[0]
    except:
        return redirect('/dashboard/upload/students')

    for i in range(len(df)):
        AM = df.iloc[i]['ΑΜ']
        if Students.objects.filter(registration_number=AM).exists():
            print('updated..')
            Students.objects.filter(registration_number=AM).update(
                study_program=df.iloc[i]['ΠΣ'],
                registration_number=df.iloc[i]['ΑΜ'],
                id_number_1=df.iloc[i]['Ακ. Ταυτότητα'],
                name=df.iloc[i]['Όνομα'],
                surname=df.iloc[i]['Επώνυμο'],
                nationality=df.iloc[i]['Υπηκοότητα'],
                student_semester=df.iloc[i]['Εξάμηνο Φοιτητή'],
                latest_year=df.iloc[i]['Τελευταίο Ακ. Έτος Φοίτησης'],
                id_gunet=df.iloc[i]['ID GUNET'],
                latest_period=df.iloc[i]['Τελευταία Περίοδος Φοίτησης'],
                year_of_enrolment=df.iloc[i]['Ακ. Έτος Εισαγ.'],
                registration_period=df.iloc[i]['Περίοδος Εισαγ.'],
                way_of_enrolment=df.iloc[i]['Τρόπος Εισαγ.'],
                student_category=df.iloc[i]['Κατηγορία Φοιτητή'],
                free_of_tuition=df.iloc[i]['Απαλλαγή από δίδακτρα'],
                active=df.iloc[i]['Ενεργόs'],
                web_active=df.iloc[i]['Ενεργόs σε web'],
                exemption_from_prerequisites=df.iloc[i]['Εξαίρεση από Προαπαιτούμενα'],
                part_time=df.iloc[i]['Μερικής Φοίτησης'],
                current_status=df.iloc[i]['Κατάσταση'],
                gender=df.iloc[i]['Φύλο'],
                amka=df.iloc[i]['ΑΜΚΑ'],
                tin=df.iloc[i]['ΑΦΜ'],
                username=df.iloc[i]['Username'],
                email=df.iloc[i]['Email'],
                mobile_number=df.iloc[i]['Κινητό'],
                phone_number=df.iloc[i]['Τηλέφωνο'],
                address=df.iloc[i]['Διεύθυνση'],
                city=df.iloc[i]['Πόλη'],
                name_in_english=df.iloc[i]['Όνομα'],
                last_name_in_english=df.iloc[i]['Επώνυμο'],
                fathers_name=df.iloc[i]["Πατρώνυμο"],
                mothers_Name=df.iloc[i]["Μητρώνυμο"],
                date_of_birth=df.iloc[i]['Ημ/νία Γέννησης'],
                place_of_birth=df.iloc[i]["Τόπος γέννησης"],
                id_number_2=df.iloc[i]['Αρ. ταυτότητας'],
                type_of_id=df.iloc[i]['Τύπος ταυτότητας'],
                rollback_year=df.iloc[i]['Αναδρ. Έτος Εισαγωγής'],
                date_of_registration=df.iloc[i]['Ημ/νία Πρώτης Εγγραφής'],
                department_registration=df.iloc[i]['Τμήμα Εισαγωγής'],
                code_of_department=df.iloc[i]['Κωδικός τμήματος εισαγωγής'],
            )
        else:
            print('created..')
            Students(
                study_program=df.iloc[i]['ΠΣ'],
                registration_number=df.iloc[i]['ΑΜ'],
                id_number_1=df.iloc[i]['Ακ. Ταυτότητα'],
                name=df.iloc[i]['Όνομα'],
                surname=df.iloc[i]['Επώνυμο'],
                nationality=df.iloc[i]['Υπηκοότητα'],
                student_semester=df.iloc[i]['Εξάμηνο Φοιτητή'],
                latest_year=df.iloc[i]['Τελευταίο Ακ. Έτος Φοίτησης'],
                id_gunet=df.iloc[i]['ID GUNET'],
                latest_period=df.iloc[i]['Τελευταία Περίοδος Φοίτησης'],
                year_of_enrolment=df.iloc[i]['Ακ. Έτος Εισαγ.'],
                registration_period=df.iloc[i]['Περίοδος Εισαγ.'],
                way_of_enrolment=df.iloc[i]['Τρόπος Εισαγ.'],
                student_category=df.iloc[i]['Κατηγορία Φοιτητή'],
                free_of_tuition=df.iloc[i]['Απαλλαγή από δίδακτρα'],
                active=df.iloc[i]['Ενεργόs'],
                web_active=df.iloc[i]['Ενεργόs σε web'],
                exemption_from_prerequisites=df.iloc[i]['Εξαίρεση από Προαπαιτούμενα'],
                part_time=df.iloc[i]['Μερικής Φοίτησης'],
                current_status=df.iloc[i]['Κατάσταση'],
                gender=df.iloc[i]['Φύλο'],
                amka=df.iloc[i]['ΑΜΚΑ'],
                tin=df.iloc[i]['ΑΦΜ'],
                username=df.iloc[i]['Username'],
                email=df.iloc[i]['Email'],
                mobile_number=df.iloc[i]['Κινητό'],
                phone_number=df.iloc[i]['Τηλέφωνο'],
                address=df.iloc[i]['Διεύθυνση'],
                city=df.iloc[i]['Πόλη'],
                name_in_english=df.iloc[i]['Όνομα'],
                last_name_in_english=df.iloc[i]['Επώνυμο'],
                fathers_name=df.iloc[i]["Πατρώνυμο"],
                mothers_Name=df.iloc[i]["Μητρώνυμο"],
                date_of_birth=df.iloc[i]['Ημ/νία Γέννησης'],
                place_of_birth=df.iloc[i]["Τόπος γέννησης"],
                id_number_2=df.iloc[i]['Αρ. ταυτότητας'],
                type_of_id=df.iloc[i]['Τύπος ταυτότητας'],
                rollback_year=df.iloc[i]['Αναδρ. Έτος Εισαγωγής'],
                date_of_registration=df.iloc[i]['Ημ/νία Πρώτης Εγγραφής'],
                department_registration=df.iloc[i]['Τμήμα Εισαγωγής'],
                code_of_department=df.iloc[i]['Κωδικός τμήματος εισαγωγής'],
            ).save()


def updated_or_create_grades(df):
    try:
        df = df[0]
    except:
        return redirect('/dashboard/upload/grades')

    student_id = None
    for i in range(len(df)):
        reg_no = df.iloc[i]["AM"]
        if Students.objects.filter(registration_number=reg_no).exists():
            student_id = Students.objects.get(registration_number=reg_no)

        if StudentGrades.objects.filter(student=student_id, subject_code=df.iloc[i]["Κωδ. μαθ."]).exists():
            print('Student updated at position i = ', i, ', AM = ', df.iloc[i]["AM"], ', Subject Code = ', df.iloc[i]["Κωδ. μαθ."], ', Student ID = ', student_id)
            StudentGrades.objects.filter(student=student_id, subject_code=df.iloc[i]["Κωδ. μαθ."]).update(
                student=student_id,
                subject_code=df.iloc[i]['Κωδ. μαθ.'],
                subject_of_academic_year=df.iloc[i]['Μάθημα Ακ. Έτους'],
                student_class=df.iloc[i]['Τμήμα Τάξης'],
                department=df.iloc[i]['Τμήμα'],
                registration_number=df.iloc[i]['AM'],
                grade=df.iloc[i]['Βαθμός'],
                exam_period=df.iloc[i]['Εξ. Περ.'],
                semester=df.iloc[i]['Εξάμηνο βαθμολογίας'],
                thesis=df.iloc[i]['Διπλωματική'],
                internship=df.iloc[i]['Πρακτική'],
                ects=df.iloc[i]['ECTS'],
                ps=df.iloc[i]['ΠΣ'],
                subject=df.iloc[i]['Μάθ. ΠΣ'],
                date1=df.iloc[i]['Ημ. Πρ.'],
                modified_by=df.iloc[i]['Τροποποίηση από'],
                date2=df.iloc[i]['Ημ. Επ.']
            )
        else:
            print('Student created at position i = ', i, ', AM = ', df.iloc[i]["AM"], ', Subject Code = ', df.iloc[i]["Κωδ. μαθ."], ', Student ID = ', student_id)
            StudentGrades(
                student=student_id,
                subject_code=df.iloc[i]['Κωδ. μαθ.'],
                subject_of_academic_year=df.iloc[i]['Μάθημα Ακ. Έτους'],
                student_class=df.iloc[i]['Τμήμα Τάξης'],
                department=df.iloc[i]['Τμήμα'],
                registration_number=df.iloc[i]['AM'],
                grade=df.iloc[i]['Βαθμός'],
                exam_period=df.iloc[i]['Εξ. Περ.'],
                semester=df.iloc[i]['Εξάμηνο βαθμολογίας'],
                thesis=df.iloc[i]['Διπλωματική'],
                internship=df.iloc[i]['Πρακτική'],
                ects=df.iloc[i]['ECTS'],
                ps=df.iloc[i]['ΠΣ'],
                subject=df.iloc[i]['Μάθ. ΠΣ'],
                date1=df.iloc[i]['Ημ. Πρ.'],
                modified_by=df.iloc[i]['Τροποποίηση από'],
                date2=df.iloc[i]['Ημ. Επ.']
            ).save()


@login_required(redirect_field_name='next', login_url='/login')
def download(request):
    if request.method == 'POST':
        column_name_list = request.POST.getlist("column_name_list")

    return render(request, 'home/download.html')


def translate_columns(selected_cols):
    columns = [{"study_program": "ΠΣ",
                "registration_number": "ΑΜ",
                "id_number": "Ακ. Ταυτότητα",
                "name": "Όνομα",
                "surname": "Επώνυμο",
                "nationality": "Υπηκοότητα",
                "student_semester": "Εξάμηνο Φοιτητή",
                "latest_year": "Τελευταίο Ακ. Έτος Φοίτησης",
                "id_gunet": "ΠID GUNETΣ",
                "latest_period": "Τελευταία Περίοδος Φοίτησης",
                "year_of_enrolment": "Ακ. Έτος Εισαγ.",
                "registration_period": "Περίοδος Εισαγ.",
                "way_of_enrolment": "Τρόπος Εισαγ.",
                "student_category": "Κατηγορία Φοιτητή",
                "free_of_tuition": "Απαλλαγή από δίδακτρα",
                "active": "Ενεργόs",
                "web_active": "Ενεργόs σε web",
                "exemption_from_prerequisites": "Εξαίρεση από Προαπαιτούμενα",
                "part_time": "Μερικής Φοίτησης",
                "current_status": "Κατάσταση",
                "gender": "Φύλο",
                "amka": "ΑΜΚΑ",
                "tin": "ΑΦΜ",
                "username": "Username",
                "email": "Email",
                "mobile_number": "Κινητό",
                "phone_number": "Τηλέφωνο",
                "address": "Διεύθυνση",
                "city": "Πόλη",
                "name_in_english": "Όνομα (En)",
                "last_name_in_english": "Επώνυμο",
                "fathers_name": "Πατρώνυμο",
                "others_Name": "Μητρώνυμο",
                "date_of_birth": "Ημ/νία Γέννησης",
                "place_of_birth": "Τόπος γέννησης",
                "id_number2": "Αρ. Ταυτότητας",
                "type_of_id": "Τύπος ταυτότητας",
                "rollback_year": "Αναδρ. Έτος Εισαγωγής",
                "date_of_registration": "Ημ/νία Πρώτης Εγγραφής",
                "department_registration": "Τμήμα Εισαγωγής",
                "code_of_department": "Κωδικός τμήματος εισαγωγής",
                "subject": "Μάθημα",
                "subject_code": "Κωδ. μαθ.",
                "subject_of_academic_year": "Μάθημα Ακ. Έτους",
                "student_class": "Τμήμα Τάξης",
                "department": "Τμήμα",
                "grade": "Βαθμός",
                "exam_period": "Εξ. Περ.",
                "semester": "Εξάμηνο βαθμολογίας",
                "semester_t": "Εξάμηνο",
                "thesis": "Διπλωματική",
                "internship": "Πρακτική",
                "ects": "ECTS",
                "ps": "ΠΣ",
                "date1": "Ημ. Πρ.",
                "modified_by": "Τροποποίηση από",
                "date2": "Ημ. Επ."}]

    translated_cols = []
    for i in columns[0]:
        if i in selected_cols:
            translated_cols.append(columns[0][i])
    return translated_cols


@login_required(redirect_field_name='next', login_url='/login')
def upload_student_excel(request):
    return render(request, 'home/upload_student.html')


@login_required(redirect_field_name='next', login_url='/login')
def upload_grade_excel(request):
    return render(request, 'home/upload_grades.html')


temp_data = []


@login_required(redirect_field_name='next', login_url='/login')
def student_preview_dataset(request):
    global data
    context = {}
    if request.FILES.get('student_dataset', False):
        try:
            data = request.FILES['student_dataset'].read()
            df = pd.read_excel(data)
            print('The length is : ', len(df))
            columns = list(df.columns)
            json_records = df.to_json(orient='records')
            data = json.loads(json_records)
            temp_data.append(df)
            html_table_body = ""
            for col in data:
                html_table_body = html_table_body + "<tr>"
                for key in col.keys():
                    html_table_body = html_table_body + f"<td>{col[key]}</td>"
                html_table_body = html_table_body + "</tr>"

            context = {'d': data, "columns": columns, "html_table_body": html_table_body}

        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            context = {'callback_url': "/dashboard/upload/students", "message": 'Something went wrong!',
                       'col': 'danger'}
        return render(request, 'home/preview_dataset.html', context)

    if request.method == "POST":
        # Saving Student datasets in database
        try:
            res = update_or_create_student(temp_data)
            context = {"message": 'File uploaded Successfully!', 'col': 'success',
                       "callback_url": "/dashboard/download"}
            temp_data.clear()

        except Exception as e:

            print(f"An exception occurred: {str(e)}")

            context = {'callback_url': "/dashboard/upload/students", "message": 'Please check your dataset columns!',
                       'col': 'danger'}
    return render(request, 'home/preview_dataset.html', context)


@login_required(redirect_field_name='next', login_url='/login')
def grade_preview_dataset(request):
    global data
    context = {}
    if request.FILES.get('student_dataset', False):
        try:
            files = request.FILES.getlist('student_dataset')
            for index, data in enumerate(files):
                if not index:
                    df = pd.read_excel(data)
                    continue
                df = pd.concat([df,pd.read_excel(data)])
            columns = list(df.columns)
            json_records = df.to_json(orient='records')
            data = json.loads(json_records)
            temp_data.append(df)
            html_table_body = ""
            for col in data:
                html_table_body = html_table_body + "<tr>"
                for key in col.keys():
                    html_table_body = html_table_body + f"<td>{col[key]}</td>"
                html_table_body = html_table_body + "</tr>"
            context = {'d': data, "columns": columns, "html_table_body": html_table_body}

        except Exception as e:

            print(f"An exception occurred: {str(e)}")

            context = {'callback_url': "/dashboard/upload/grades", "message": 'Something went wrong!', 'col': 'danger'}
        return render(request, 'home/preview_dataset.html', context)

    if request.method == "POST":
        # Saving Student datasets in database
        try:
            res = updated_or_create_grades(temp_data)
            temp_data.clear()
            context = {"message": 'File uploaded Successfully!', 'col': 'success',
                       "callback_url": "/dashboard/download"}

        except Exception as e:

            print(f"An exception occurred: {str(e)}")
            context = {'callback_url': "/dashboard/upload/grades", "message": 'Please check your dataset columns!',
                       'col': 'danger'}

    return render(request, 'home/preview_dataset.html', context)


@login_required(redirect_field_name='next', login_url='/login')
def preview(request):
    global data
    columns = None
    html_table_body = None
    if request.method == 'POST':
        column_name_list = request.POST.getlist("column_name_list")
        print(f"Selected columns: {column_name_list}")
        column_name_list = [x for x in column_name_list[0].split(',')]
        # translated_cols = translate_columns(column_name_list)
        student_cols = []
        grades_cols = []
        rows = request.POST.get('rows')
        if rows == 'all':
            students = Students.objects.all()
        else:
            students = Students.objects.all()[:int(rows)]

        for field in Students._meta.fields:
            student_cols.append(field.name)

        for field in StudentGrades._meta.fields:
            grades_cols.append(field.name)

        selected_student_cols = [x for x in student_cols if x in column_name_list]
        selected_grades_cols = [x for x in grades_cols if x in column_name_list]
        selected_student_cols.append('registration_number')
        datas = list(students.values(*selected_student_cols))
        has_subject = False
        has_grade = False
        print(f"Data retrieved: {datas}")
        for data in datas:
            student_id = Students.objects.get(registration_number=data['registration_number'])
            stud = StudentGrades.objects.filter(student=student_id)
            grade = list(stud.values(*selected_grades_cols))
            grades_list = []
            data.update({'grades':grades_list})
            if len(grade) >= 1:
                for gr in grade:
                    if 'subject' in gr.keys() and 'grade' in gr.keys():
                        has_subject = True
                        has_grade = True
                        grades_list.append({'subject':gr["subject"], 'grade':gr["grade"]})
                    elif 'subject' in gr.keys():
                        has_subject = True
                        grades_list.append({'subject':gr["subject"]})
                    elif 'grade' in gr.keys():
                        has_grade = True
                        grades_list.append({'grade':gr["grade"]})
                data.update({'grades':grades_list}) 
        
        print("Rendering HTML table...")
        html_table_body = ""
        for col in datas:
            if has_subject or has_grade:
                for sub in col["grades"]:
                    html_table_body = html_table_body + "<tr>"
                    for key in col.keys():
                        if key not in ['grades']:
                            html_table_body = html_table_body + f"<td>{col[key]}</td>"
                    if has_subject:      
                        html_table_body = html_table_body + f"<td>{sub['subject']}</td>"
                    if has_grade:
                        html_table_body = html_table_body + f"<td>{sub['grade']}</td>"
                    html_table_body = html_table_body + "</tr>"
            else:
                html_table_body = html_table_body + "<tr>"
                for key in col.keys():
                    if key not in ['grades']:
                        html_table_body = html_table_body + f"<td>{col[key]}</td>"
                html_table_body = html_table_body + "</tr>"

        print("HTML table rendered.")

        if len(datas) < 1:
            return HttpResponse('No Data Found')

        columns = translate_columns(list(data.keys()))
        if has_subject:
            columns.append("Μάθημα")
        if has_grade:
            columns.append("Βαθμός")

        data_values = []
        for i in datas:
            print("\nI is:", i)
            grades_temp = i['grades'].copy()
            if has_subject or has_grade:
                for grades_obj in grades_temp:
                    values=[]
                    for value in list(i.values()):
                        if not isinstance(value,list):
                            values.append(value)
                    if has_subject:
                        values.append(grades_obj['subject'])
                    if has_grade:
                        values.append(grades_obj['grade'])
                    data_values.append(values)
            else:
                del i['grades']
                data_values.append(list(i.values()))

        # Save the Excel file
        df = pd.DataFrame(data_values, columns=columns)
        if 'ΑΜ' in df.columns:
            df = df.sort_values(by=['ΑΜ'])
        print(df)
        writer = pd.ExcelWriter('files/merged/student_and_grades.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()

    return render(request, 'home/preview.html', {"data": columns, "html_table_body": html_table_body})



