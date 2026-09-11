import json
class Task:
    def __init__(self,title,description,status="Pending"):
        self.title=title
        self.description=description
        self.status=status

    def mark_complete(self):
        self.status="Completed"

    def __str__(self):
        return f"[{self.status}] {self.title}: {self.description}"

    def to_dict(self):
        return {"title": self.title, "description": self.description, "status": self.status}
    
class TaskManager:
    def __init__(self,filename="tasks.json"):
        self.filename=filename
        self.tasks=[]

    def add_task(self,title,description):
        new_task=Task(title,description)
        self.tasks.append(new_task)
        self.save_tasks()

    def display_tasks(self):
        if len(self.tasks)==0:
            print("No Task Found!")
        else:
            for index,task in enumerate(self.tasks):
                print(f"{index}.{task}")

    def save_tasks(self):
        dict_list=[]
        for task in self.tasks:
            dict_list.append(task.to_dict())

        with open(self.filename,"w") as file:
            json.dump(self.dict_list,file,indent=4)