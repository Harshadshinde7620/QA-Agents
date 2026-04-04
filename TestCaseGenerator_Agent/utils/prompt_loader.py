def load_constraints():
    try:
        with open("constraints.md", "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error loading constraints: {str(e)}"