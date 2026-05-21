None selected

Skip to content
Using Gmail with screen readers
Enable desktop notifications for Gmail.
   OK  No thanks
2 of 94
(no subject)
Inbox

akkshetha m
Attachments
9:52 AM (22 minutes ago)
to me


 28 Attachments
  •  Scanned by Gmail
students = ["Aarik", "aadvik", "aaradya", "akkshe", "amritha"]

present = []
absent = []

print("================================")
print("      ATTENDANCE TRACKER")
print("================================")

for student in students:

    status = input(f"Is {student} present? (P/A): ").upper()

    if status == "P":
        present.append(student)
    else:
        absent.append(student)

print("\n================================")
print("      ATTENDANCE REPORT")
print("================================")

print("\nPresent Students:")
for p in present:
    print("-", p)

print("\nAbsent Students:")
for a in absent:
    print("-", a)

print("\nTotal Students:", len(students))
print("Present Count:", len(present))
print("Absent Count:", len(absent))
attendance tracker.py
Displaying attendance tracker.py.
