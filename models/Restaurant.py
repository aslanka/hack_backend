class Restaurant:
    def __init__(self, name, preferred_cuisines, budget, city, state, coordinates, preferred_ambiance, dietary_restrictions, menu_url, start_time, end_time):
        self.name = name
        self.preferred_cuisines = preferred_cuisines
        self.budget = budget
        self.city = city
        self.state = state
        self.coordinates = coordinates
        self.preferred_ambiance = preferred_ambiance
        self.dietary_restrictions = dietary_restrictions
        self.menu_url = menu_url
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {
            'name': self.name,
            'preferred_cuisines': self.preferred_cuisines,
            'budget': self.budget,
            'city': self.city,
            'state': self.state,
            'coordinates': self.coordinates,
            'preferred_ambiance': self.preferred_ambiance,
            'dietary_restrictions': self.dietary_restrictions,
            'menu_url': self.menu_url,
            'start_time':self.start_time,
            'end_time':self.end_time
        }

    def __str__(self):
        return f"Restaurant(name={self.name}, preferred_cuisines={self.preferred_cuisines}, budget={self.budget}, city={self.city}, state={self.state}, coordinates={self.coordinates}, preferred_ambiance={self.preferred_ambiance}, dietary_restrictions={self.dietary_restrictions}, menu_url={self.menu_url}, start_time={self.start_time}, end_time={self.end_time})"
