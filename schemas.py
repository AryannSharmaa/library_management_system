def individual_serial(student):
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": student["address"],
    }


def list_serial(students):
    return [individual_serial(student) for student in students]
