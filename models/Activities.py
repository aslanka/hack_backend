class Activities:
    def __init__(self, name, location, date, time, description):
        self.name = name
        self.location = location
        self.date = date
        self.time = time
        self.description = description
    
    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'time': self.time,
            'description': self.description
        }


    def __str__(self):
        return f"Event(name={self.name}, location={self.location}, date={self.date}, time={self.time}, description={self.description})"
