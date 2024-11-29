
class Utils:
    @staticmethod
    def save_data_to_csv(student_list, filename):
        student_list.save_to_csv(filename)

    @staticmethod
    def load_data_from_csv(student_list, filename):
        student_list.load_from_csv(filename)
