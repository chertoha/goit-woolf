from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc
from models import Student, Grade, Subject, Teacher, Group
from config import engine

Session = sessionmaker(bind=engine)
session = Session()

# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    return session.query(Student.name, func.avg(Grade.grade).label('avg_grade')).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

# 2. Знайти студента із найвищим середнім балом з певного предмета.
def select_2(subject_id):
    return session.query(Student.name, func.avg(Grade.grade).label('avg_grade')).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc('avg_grade')).first()

# 3. Знайти середній бал у групах з певного предмета.
def select_3(subject_id):
    return session.query(Group.name, func.avg(Grade.grade).label('avg_grade')).select_from(Group).join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()



# 4. Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    return session.query(func.avg(Grade.grade)).scalar()

# 5. Знайти які курси читає певний викладач.
def select_5(teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

# 6. Знайти список студентів у певній групі.
def select_6(group_id):
    return session.query(Student.name).filter(Student.group_id == group_id).all()

# 7. Знайти оцінки студентів у окремій групі з певного предмета.
def select_7(group_id, subject_id):
    return session.query(Student.name, Grade.grade).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(teacher_id):
    return session.query(func.avg(Grade.grade)).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()

# 9. Знайти список курсів, які відвідує певний студент.
def select_9(student_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).distinct().all()

# 10. Список курсів, які певному студенту читає певний викладач.
def select_10(student_id, teacher_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).distinct().all()

if __name__ == "__main__":
    print("1)  Топ 5 студентів з найвищим середнім балом:", select_1())
    print("2)  Студент з найвищим балом з предмета (ID=2):", select_2(2))
    print("3)  Середній бал у групах з предмета (ID=3):", select_3(3))
    print("4)  Середній бал на потоці:", select_4())
    print("5)  Курси, які читає викладач (ID=1):", select_5(1))
    print("6)  Студенти у групі (ID=1):", select_6(1))
    print("7)  Оцінки студентів у групі (ID=1) з предмета (ID=2):", select_7(1, 2))
    print("8)  Середній бал, який ставить викладач (ID=1):", select_8(1))
    print("9)  Курси, які відвідує студент (ID=1):", select_9(1))
    print("10) Курси, які студенту (ID=1) читає викладач (ID=1):", select_10(1, 1))

# Закриваємо сесію після виконання запитів
session.close()
