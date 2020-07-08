#! /usr/bin/env python
# https://docs.python.org/3/library/argparse.html

import argparse
import json
import math

from collections import defaultdict

#import matplotlib as mil
#mil.use('TkAgg') # To dodge the error with matplotlib on Linux
import matplotlib.pyplot as plt

class Agent:
    #def say_hello(self, first_name):
    #    return "Bien le bonjour " + first_name + "!"

    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value) # setattr is equivalent to my_object.attribute = value

class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees

    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        return self.latitude_degrees * math.pi / 180

class Zone:

    ZONES = []
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1 # Degrees of longitude
    HEIGHT_DEGREES = 1 # Degrees of latitude
    EARTH_RADIUS_KILOMETERS = 6371

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = []

    @property
    def width(self):
        return (abs((self.corner1.longitude - self.corner2.longitude) *
                self.EARTH_RADIUS_KILOMETERS))

    @property
    def height(self):
        return (abs((self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS))

    @property
    def area(self):
        return self.height * self.width

    def population_density(self):
        return self.population / self.area

    def average_agreeableness(self):
        if not self.inhabitants:
            return 0
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants]) / self.population # is equivalent to :
        # agreeableness = []
        # for inhabitant in self.inhabitants:
        #     agreeableness.append(inhabitant.agreeableness)
        # return sum(agreeableness) / self.population

    @property
    def population(self):
        return len(self.inhabitants)

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude,
                                            self.corner2.longitude) and \
                position.longitude < max(self.corner2.longitude,
                                            self.corner2.longitude) and \
                position.latitude >= min(self.corner1.latitude,
                                            self.corner2.latitude) and \
                position.latitude < max(self.corner1.latitude,
                                            self.corner2.latitude)

    @classmethod
    def find_zone_that_contains(cls, position):
        if not cls.ZONES:
            # Initialize zones automatically if necessary
            cls._initialize_zones()

        # Compute the index in the ZONES array that contains the given position
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)
                                / cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)
                                / cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES)
                                / cls.WIDTH_DEGREES) # 180 - (-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index

        # Just checking that the index is correct
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone

    @classmethod
    def _initialize_zones(cls):
        for latitude in range(cls.MIN_LATITUDE_DEGREES,
                                cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES,
                                    cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES,
                                        latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)

class BaseGraph:

    def __init__(self):
        self.title = "Your graph title"
        self.x_label = "X-axis label"
        self.y_label = "Y-axis label"
        self.show_grid = True

    def show(self, zones):
        x_values, y_values = self.xy_values(zones)
        self.plot(x_values, y_values)

        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()

    def plot(self, x_values, y_values):
        plt.plot(x_values, y_values, '.')

    def xy_values(self, zones):
        """
        Returns x_values and y_values
        """
        raise NotImplementedError

class AgreeablenessGraph(BaseGraph):
    # Inherit from its parent: BaseGraph
    def __init__(self):
        super(AgreeablenessGraph, self).__init__() # executes the parent's __init__() method

        self.title = "Nice people live in the countryside"
        self.x_label = "Population density"
        self.y_label = "Agreeableness"

    def xy_values(self, zones):
        x_values = [zone.population_density() for zone in zones]
        y_values = [zone.average_agreeableness() for zone in zones]
        return x_values, y_values

class IncomeGraph(BaseGraph):
    def __init__(self):
        super(IncomeGraph, self).__init__()

        self.title = "Older people have more money"
        self.x_label = "age"
        self.y_label = "income"

    def xy_values(self, zones):
        income_by_age = defaultdict(float)
        population_by_age = defaultdict(int)
        for zone in zones:
            for inhabitant in zone.inhabitants:
                income_by_age[inhabitant.age] += inhabitant.income
                population_by_age[inhabitant.age] += 1

        x_values = range(0, 100)
        y_values = [income_by_age[age] / (population_by_age[age] or 1)
                    for age in range(0, 100)]
        return x_values, y_values

def main():
    parser = argparse.ArgumentParser("Display population stats")
    parser.add_argument("src", help="Path to source json agents file")
    args = parser.parse_args()

    # Load agents
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        # Store agent position in radians
        position = Position(longitude, latitude)

        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)


    # Graph initialization
    agreeableness_graph = AgreeablenessGraph()
    # Display graph
    agreeableness_graph.show(Zone.ZONES)

    income_graph = IncomeGraph()
    income_graph.show(Zone.ZONES)

if __name__ == "__main__":
    main()
