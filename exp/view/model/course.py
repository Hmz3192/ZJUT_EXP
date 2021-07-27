class Course:

    def __init__(self, course_name, img_url, exp_url, watching_num):
        self.course_name = course_name
        self.img_url = img_url
        self.exp_url = exp_url
        self.watching_num = watching_num

    def __str__(self) -> str:
        return super().__str__()
