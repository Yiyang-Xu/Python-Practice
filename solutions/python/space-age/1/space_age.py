class SpaceAge:
    
    PLANET_RATIOS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }
    
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_year_seconds = 31557600
        
    def _get_age(self, planet):
        age = (self.seconds / self.earth_year_seconds) / self.PLANET_RATIOS[planet]
        return round(age, 2)

    def on_mercury(self): return self._get_age("mercury")
    def on_venus(self):   return self._get_age("venus")
    def on_earth(self):   return self._get_age("earth")
    def on_mars(self):    return self._get_age("mars")
    def on_jupiter(self): return self._get_age("jupiter")
    def on_saturn(self):  return self._get_age("saturn")
    def on_uranus(self):  return self._get_age("uranus")
    def on_neptune(self): return self._get_age("neptune")