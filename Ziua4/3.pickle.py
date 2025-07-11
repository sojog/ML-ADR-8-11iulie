import pickle
from student import Student

    
obiect_student = Student("Ion", "Ionescu")
print(obiect_student)

result = pickle.dumps(obiect_student)
print(result)


with open("pickled_student.pkl", "wb") as file_writer:
    pickle.dump(obiect_student, file_writer)
