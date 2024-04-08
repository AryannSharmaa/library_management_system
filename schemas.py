def individual_serial(student, full=True):
    if full:
        return {
            "id": str(student["_id"]),
            "name": student["name"],
            "age": student["age"],
            "address": student["address"],
        }
    else:
        return {
            "id": str(student["_id"]),
            "name": student["name"],
            "age": student["age"],
        }


def list_serial(students):
    return [individual_serial(student, full=False) for student in students]
