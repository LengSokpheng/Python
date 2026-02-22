myarray = []

class student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.age = 0
        self.gender = ""

    def Input(self):
        self.id = str(input("Enter Id: "))
        self.name = str(input("Enter Name: "))
        self.age = int(input("Enter Age: "))
        self.gender = str(input("Enter Gender: "))
        myarray.append(self)

    def Output(self):
        if len(myarray) == 0:
            print("No data.")
            return

        for mydata in myarray:
            print(f"""
ID     : {mydata.id}
Name   : {mydata.name}
Age    : {mydata.age}
Gender : {mydata.gender}
""")

    def Search(self):
        Search_id = str(input("Enter Id: "))
        for mydata in myarray:
            if mydata.id == Search_id:
                print("ID:", mydata.id)
                print("Name:", mydata.name)
                print("Age:", mydata.age)
                print("Gender:", mydata.gender)
                return
        print("Student not found.")

    def Update(self):
        Update_id = str(input("Enter ID to Update: "))
        for mydata in myarray:
            if mydata.id == Update_id:
                # update fields
                mydata.name = str(input("Enter New Name: "))
                mydata.age = int(input("Enter New Age: "))
                mydata.gender = str(input("Enter New Gender: "))
                print("Update successful.")
                return
        print("Student not found.")

    def Delete(self):
        Delete_id = str(input("Enter ID to Delete: "))
        for i, mydata in enumerate(myarray):
            if mydata.id == Delete_id:
                myarray.pop(i)
                print("Delete successful.")
                return
        print("Student not found.")


while True:
    stu = student()

    print("""
1. Input
2. Output
3. Search
4. Update
5. Delete
6. Exit
""")

    option = int(input("Enter Option(1-6): "))

    if option == 1:
        print("=" * 50)
        print(" " * 20, "INPUT")
        print("=" * 50)
        stu.Input()

    elif option == 2:
        print("=" * 50)
        print(" " * 20, "OUTPUT")
        print("=" * 50)
        stu.Output()

    elif option == 3:
        print("=" * 50)
        print(" " * 20, "SEARCH")
        print("=" * 50)
        stu.Search()

    elif option == 4:
        print("=" * 50)
        print(" " * 20, "UPDATE")
        print("=" * 50)
        stu.Update()

    elif option == 5:
        print("=" * 50)
        print(" " * 20, "DELETE")
        print("=" * 50)
        stu.Delete()

    elif option == 6:
        break
