import pickle
from student import Student


with open("pickled_student.pkl", "rb") as file_reader:
    read_result:Student = pickle.load(file_reader)
    print(read_result, type(read_result))
    print(read_result.nume)
    




with open("trained_model.pkl", "rb") as file_reader:
    read_result:tf.keras.model = pickle.load(file_reader)
    print(read_result, type(read_result))
    print(read_result.nume)