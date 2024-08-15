// Define the Student class
class Student {
  String name;
  int age;
  int gradeLevel;

  Student(this.name, this.age, this.gradeLevel);

  void printStudentInfo() {
    print('Student Name: $name');
    print('Age: $age');
    print('Grade Level: $gradeLevel');
  }
}

// Define the Teacher class
class Teacher {
  String name;
  int age;
  String subject;

  Teacher(this.name, this.age, this.subject);

  void printTeacherInfo() {
    print('Teacher Name: $name');
    print('Age: $age');
    print('Subject: $subject');
  }
}


class School {
  Student student;
  Teacher teacher;

  School(this.student, this.teacher);

  void printInfo() {
    print('--- Student Information ---');
    student.printStudentInfo();
    print('--- Teacher Information ---');
    teacher.printTeacherInfo();
  }
}

void main() {
  
  var student = Student('Alice', 15, 10);
  var teacher = Teacher('Mr. Smith', 40, 'Mathematics');

  
  var school = School(student, teacher);

  
  school.printInfo();
}
