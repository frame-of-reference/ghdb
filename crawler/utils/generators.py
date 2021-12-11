class UdemyCourses(object):
    """Generate URLs for Udemy Courses API
    @:param query - udemy search term
    :return
    """
    def __init__(self, query: str):
        self.page = 1
        self.query = query

    def __next__(self):
        return_value = f"https://www.udemy.com/api-2.0/search-courses/?p={self.page}&q={self.query}&src=ukw&skip_price=true"
        self.page += 1
        return return_value

    def __iter__(self):
        return self
