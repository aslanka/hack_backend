class User:
    def __init__(self, id, name, preferred_cuisines=None, budget=None, preferred_ambiance=None,
                 location_preference=(0.0, 0.0), dietary_restrictions=None, city=None, state=None,
                 preferred_language=None,current_time=None,feature_importance=None,password=None):
        self.id = id
        self.password = password
        self.name = name
        self.preferred_cuisines = preferred_cuisines or []
        self.budget = budget
        self.preferred_ambiance = preferred_ambiance
        self.location_preference = location_preference
        self.dietary_restrictions = dietary_restrictions or []
        self.city = city
        self.state = state
        self.preferred_language = preferred_language
        self.current_time= current_time
        self.feature_importance= feature_importance

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password' : self.password,
            'preferred_cuisines': self.preferred_cuisines,
            'budget': self.budget,
            'preferred_ambiance': self.preferred_ambiance,
            'location_preference': self.location_preference,
            'dietary_restrictions': self.dietary_restrictions,
            'city': self.city,
            'state': self.state,
            'preferred_language': self.preferred_language,
            'current_time': self.current_time,
            'feature_importance': self.feature_importance
        }

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, preferred_cuisines={self.preferred_cuisines}, budget={self.budget}, preferred_ambiance={self.preferred_ambiance}, location_preference={self.location_preference}, dietary_restrictions={self.dietary_restrictions}, city={self.city}, state={self.state}, preferred_language={self.preferred_language}, feature_importance = {self.feature_importance}, 'password' = {self.password})"
