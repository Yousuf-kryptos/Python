def average(number):
    return sum(number)/len(number)

subject_marks ={}

with open("student_marks.csv","r") as file:
    lines = file.readlines()
    headers = lines[0].strip().split(",")
    subjects = headers[1:]

    for subject in subjects:
        subject_marks[subject] = []

    for line in lines[1:]:
        data = line.strip().split(",")
        marks = [int(mark) for mark in data[1:]]

        for subject, mark in zip(subjects, marks):
            subject_marks[subject].append(mark)

report = []

for subject, marks in subject_marks.items():
    avg = average(marks)
    highest = max(marks)
    lowest = min(marks)

    report.append(f"{subject}: Average={avg:.2f}, Highest={highest}, Lowest={lowest}")

with open("reports.txt","w") as file:
    for line in report:
        file.write(line+'\n')

print("Report generated successfully")