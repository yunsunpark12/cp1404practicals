import csv
from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __repr__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip the header line
        for row in reader:
            name, start_date, priority, estimate, completion = row
            project = Project(name, start_date, int(priority), float(estimate), int(completion))
            projects.append(project)
    return projects

def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Name', 'Start Date', 'Priority', 'Estimate', 'Completion'])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'), project.priority, project.estimate, project.completion])

def display_projects(projects):
    incomplete = []
    completed = []
    for project in projects:
        if project.completion < 100:
            incomplete.append(project)
        else:
            completed.append(project)

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed):
        print(f"  {project}")

def filter_projects_by_date(projects, date):
    filtered_projects = []
    filter_date = datetime.strptime(date, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > filter_date:
            filtered_projects.append(project)
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)

def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    project = Project(name, start_date, priority, estimate, completion)
    projects.append(project)

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    if 0 <= choice < len(projects):
        project = projects[choice]
        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")
        if new_completion:
            project.completion = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
    else:
        print("Invalid project choice.")

def main():
    filename = input("Enter the filename to load projects from: ")
    projects = load_projects(filename)

    while True:
        print("\nMenu:")
        print("(L)oad projects")
        print("(S)ave projects")
        print("(D)isplay projects")
        print("(F)ilter projects by date")
        print("(A)dd new project")
        print("(U)pdate project")
        print("(Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter the filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using custom-built project management software.")

if __name__ == '__main__':
    main()

