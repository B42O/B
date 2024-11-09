f = {
    "A": {"s": "B", "c": ["C", "D"]},  # Grandfather
    "B": {"s": "A", "c": ["C", "D"]},  # Grandmother
    "C": {"s": "E", "p": ["A", "B"], "c": ["G", "H"]},  # First son
    "D": {"s": "F", "p": ["A", "B"], "c": ["I", "J"]},  # Second son
    "E": {"s": "C", "c": ["G", "H"]},  # Spouse of first son
    "F": {"s": "D", "c": ["I", "J"]},  # Spouse of second son
    "G": {"p": ["C", "E"]},  # Child 1 of C and E
    "H": {"p": ["C", "E"]},  # Child 2 of C and E
    "I": {"p": ["D", "F"]},  # Child 1 of D and F
    "J": {"p": ["D", "F"]},  # Child 2 of D and F
}

def find_relationship(n1, n2):
  
    if n1 not in f or n2 not in f:
        return "Please enter valid names (A-J) only."
    elif n1 == n2:
        return "The same name was entered twice."
    elif f.get(n1, {}).get("s") == n2:
        return f"{n1} is the spouse of {n2}."
    elif n2 in f.get(n1, {}).get("c", []):
        return f"{n1} is the parent of {n2}."
    elif n1 in f.get(n2, {}).get("c", []):
        return f"{n1} is the child of {n2}."
    elif f.get(n1, {}).get("p") == f.get(n2, {}).get("p"):
        return f"{n1} and {n2} are siblings."
    elif set(f.get(n1, {}).get("p", [])).intersection(f.get(n2, {}).get("p", [])):
        return f"{n1} is an uncle/aunt of {n2}."
    elif set(f.get(n2, {}).get("p", [])).intersection(f.get(n1, {}).get("c", [])):
        return f"{n2} is a nephew/niece of {n1}."
    else:
        return "Relationship not found."


n1 = input("Enter name1 (A-J): ")
n2 = input("Enter name2 (A-J): ")
print(find_relationship(n1, n2))
