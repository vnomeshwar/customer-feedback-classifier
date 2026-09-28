# Decide priority based on the predicted category
def assign_priority(category):

    if category == "Technical Issue":
        return "High"

    elif category == "Refund":
        return "High"

    elif category == "Complaint":
        return "Medium"

    elif category == "Praise":
        return "Low"

    else:
        return "Medium"


# Decide which department should handle the ticket
def assign_department(category):

    if category == "Technical Issue":
        return "Tech Support"

    elif category == "Refund":
        return "Finance"

    elif category == "Complaint":
        return "Customer Success"

    elif category == "Praise":
        return "Customer Success"

    else:
        return "Customer Support"


# Test the routing system
if __name__ == "__main__":

    categories = [
        "Technical Issue",
        "Refund",
        "Complaint",
        "Praise"
    ]

    for category in categories:

        priority = assign_priority(category)
        department = assign_department(category)

        print("\nCategory:", category)
        print("Priority:", priority)
        print("Department:", department)