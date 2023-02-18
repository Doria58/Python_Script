import os
import math
import linecache

class Student:
    def __init__(self, stdNumber, name, python_grade, java_grade):
        self.stdNumber = stdNumber
        self.name = name
        self.python_grade = python_grade
        self.java_grade = java_grade

class Student_mag_System:

    def __init__(self):
        self.Student_List = []

    def AddStudentsInfo(self, student):
        self.Student_List.append(student)
        print("已成功添加学生信息")

    def ShowStudentInfo(self):
        if not self.Student_List:
            print("没有学生信息")
        else:
            for student in self.Student_List:
                print(f"学号:{student.stdNumber}, 姓名:{student.name} , Python成绩:{student.python_grade}, Java成绩:{student.java_grade}")
    
    def Sort_Student_grade(self):
        if not self.Student_List:
            print("没有学生信息")
            return False

        # 定义一个根据学生成绩排序的函数
        def sort_by_grade(grade):
            return sorted(self.Student_List, key=lambda x: getattr(x, grade))

        # 菜单选择排序方式
        print("请选择排序方式:")
        print("1. 按Python成绩排序")
        print("2. 按Java成绩排序")
        print("3. 按总成绩排序")
        Sort_input = input("请选择：")

        if Sort_input == "1":
            print("将按Python成绩进行排序...")
            sorted_list = sort_by_grade('python_grade')
        elif Sort_input == "2":
            print("将按Java成绩进行排序...")
            sorted_list = sort_by_grade('java_grade')
        elif Sort_input == "3":
            print("将按总成绩进行排序...")
            sorted_list = sorted(self.Student_List, key=lambda x: x.python_grade + x.java_grade)

        # 打印排序结果
        for student in sorted_list:
            print(f"学号:{student.stdNumber}, 姓名:{student.name}, Python成绩:{student.python_grade}, Java成绩:{student.java_grade}")

    def Delect_Student_Info(self):
        if not self.Student_List:
             print("没有学生信息")
             return False

        # 输入要删除的学生学号
        std_num = input("请输入要删除的学生学号：")
        for i, student in enumerate(self.Student_List):
            if student.stdNumber == std_num:
                # 找到学生信息并删除
                del self.Student_List[i]
                print("已成功删除学生信息")
                return True

         # 没有找到学生信息

        print("没有找到该学生信息")
        return False
        
    def Find_Students_Info(self):
        
        if not self.Student_List:
            print("没有学生信息")
            return False
        
        Find_input = input("1.输入学号以查找, 2.输入名字查找:")
        
        if Find_input == "1":
        
            find_target = input("请输入您想查找的学号:")
            for student in self.Student_List:
                if student.stdNumber == find_target:
                    return f"学号:{student.stdNumber}, 姓名:{student.name}, Python成绩:{student.python_grade}, Java成绩:{student.java_grade}"
            # 没有找到学生信息
            print("没有找到该学生信息")

        elif Find_input == "2":
    
            find_target = input("请输入您想查找的姓名:")
            for student in self.Student_List:
                if student.name == find_target:
                    return f"学号:{student.stdNumber}, 姓名:{student.name}, Python成绩:{student.python_grade}, Java成绩:{student.java_grade}"
            # 没有找到学生信息
            print("没有找到该学生信息")
    
    def Save_Students_Info(self,path,filename):
        
        if not self.Student_List:
            print('没有学生信息')
            return False
        
        if path == "":
            if filename == "":
                for student in self.Student_List:
                    with open('./student_info.txt', 'a+') as fp:
                        print(f"ID: {student.stdNumber}, Name: {student.name}, Python_Grade: {student.python_grade}, Java_Grade: {student.java_grade}",file=fp)
            else:
                for student in self.Student_List:
                    with open(f'./{filename}', 'a+') as fp:
                        print(f"ID: {student.stdNumber}, Name: {student.name}, Python_Grade: {student.python_grade}, Java_Grade: {student.java_grade}",file=fp)
        elif filename == "":
            for student in self.Student_List:
                with open(f'{path}/student_info.txt', 'a+') as fp:
                    print(f"ID: {student.stdNumber}, Name: {student.name}, Python_Grade: {student.python_grade}, Java_Grade: {student.java_grade}",file=fp)
        else:
            for student in self.Student_List:
                with open(f'{path}/{filename}', 'a+') as fp:
                    print(f"ID: {student.stdNumber}, Name: {student.name}, Python_Grade: {student.python_grade}, Java_Grade: {student.java_grade}",file=fp)
        
    def Import_InfoFile(self,ImportFile):
        
        # 检查文件是否存在
        if not os.path.exists(ImportFile):
            print("文件不存在...")
            return False
        
        # 统计行数
        with open(ImportFile , 'r') as fp:
            count = sum(1 for _ in fp)   

        for item in range(1,count + 1):
            info = linecache.getline(ImportFile , item).split()
            file_StdNumber = info[1]
            file_name = info[3]
            file_python_grade = info[5]
            file_java_grade = info[7]
            student_info = Student(file_StdNumber, file_name, file_python_grade, file_java_grade)
            self.AddStudentsInfo(student_info)
        print(f'导入了 {count} 条信息,导入完成')
            
        
### main function ###

std_mag = Student_mag_System()

while True:
    print('===========================学生管理系统===========================')
    print('                        1. 新增学生信息')
    print('                        2. 显示学生信息')
    print('                        3. 成绩排序')
    print('                        4. 删除学生信息')
    print('                        5. 查找学生信息')
    print('                        6. 导出学生信息')
    print('                        7. 导入学生信息')
    print('                        0. 退出系统')
    print('===========================学生管理系统===========================')
    USerInput = str(input())

    if USerInput == "0":
        print("感谢使用....")
        break
    elif USerInput == "1":
        StdNumber = input("请输入学生学号:")
        name = input("请输入学生姓名:")
        python_grade = input("请输入学生的Python成绩:")
        java_grade = input("请输入学生的Java成绩:")
        student_info = Student(StdNumber, name, python_grade, java_grade)
        std_mag.AddStudentsInfo(student_info)
    elif USerInput == "2":
        std_mag.ShowStudentInfo()
    elif USerInput == "3":
        std_mag.Sort_Student_grade()
    elif USerInput == "4":
        std_mag.Delect_Student_Info()
    elif USerInput == "5":
        print(std_mag.Find_Students_Info())
    elif USerInput == "6":
        Save_path = input('输入保存路径(回车将使用默认当前路径):')
        Save_FileName = input('输入保存文件名(回车将使用默认名称):')
        std_mag.Save_Students_Info(Save_path,Save_FileName)
    elif USerInput == "7":
        input_file_path = input('请输入文件路径:')
        std_mag.Import_InfoFile(input_file_path)
        