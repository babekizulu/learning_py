name = 'Johan van Doeburg'
age = 22
is_new = False
new_patient_msg = f'{name} is a new patient at the hospital'
existing_patient_msg = f'{name} has an existing patient file at this hospital'

if (is_new):
    print(new_patient_msg)
else:
    print(f'Name: {name}')
    print(f'Age: {age}')
    print(existing_patient_msg)
