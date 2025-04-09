import os

def update_project_status(project_name):
    if "main" in project_name:
        status = {
            "project": project_name,
            "message": "Project is updated",
            "action": "updated"
        }
        print(status)
    else:
        print("Error: Project name should be 'main'.")

if __name__ == "__main__":
    update_project_status("main")
