class AlbumParametersValidator:
    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year

    def is_valid(self):
        if self.title is None or self.title == "":
            return False
        if self.release_year is None or self.release_year == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.title is None or self.title == "":
            errors.append("Title can't be blank")
        if self.release_year is None or self.release_year == "":
            errors.append("Release year can't be blank")
        if len(errors) == 0:
            return None 
        else:
            return ", ".join(errors)