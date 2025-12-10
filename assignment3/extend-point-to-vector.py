import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) == (other.x, other.y)
        return NotImplemented
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def euclidean(self, other):
        point_one = np.array([self.x, self.y])
        point_two = np.array([other.x, other.y])
        vector_value = point_two - point_one
        distance = np.linalg.norm(vector_value)
        return distance

point_one = Point(1,2)
point_two = Point(1,2)

print(point_one)
print(point_two)

print(point_one == point_two)

print(point_one.euclidean(point_two))




#Notes:
#https://www.pythonmorsels.com/overloading-equality-in-python/
#https://www.geeksforgeeks.org/python/calculate-the-euclidean-distance-using-numpy/