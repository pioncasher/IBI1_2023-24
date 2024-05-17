class students(object):
    def __init__(self,students_name:str,major:str , score_for_code_portfolio:int ,score_for_group_project:int ,exam_score:int):
        if not 0 <= score_for_code_portfolio <= 100:  
            raise ValueError          
        
        if not 0 <= score_for_group_project <= 100:  
            raise ValueError
          
        if not 0 <= exam_score <= 100:  
            raise ValueError
        if not major=="BMS" and not major=="BMI":
            raise ValueError
        
        self.students_name=students_name
        self.major=major
        self.score_for_code_portfolio=score_for_code_portfolio
        self.score_for_group_project=score_for_group_project
        self.exam_score=exam_score

    def print_attributes(self):
        return f"Student name:{self.students_name}, Major:{self.major}, Score for code portfolio: {self.score_for_code_portfolio}, Score for group project: {self.score_for_group_project}, Exam score: {self.exam_score}"
    



# An example of using this class

student = students("Frank", "BMS", 90, 95, 95)


student.print_attributes()