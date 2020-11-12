

"""

"""
class DataProvider:

    def __init__(self, layer):
        self.filename = 'modules/DataProvider/data/data_' + layer + '.tif'
        self.boundaries = 'modules/DataProvider/boundaries/boundaries.shp'

    def get_data(self, ):
        return self.filename

    def set_data(self, layer):
        self.filename = 'modules/DataProvider/data/data_' + layer + '.tif'

    def get_boundaries(self, ):
        return self.boundaries

    def set_boundaries(self, boundaries):
        self.boundaries = 'modules/DataProvider/boundaries/' + boundaries + '.shp'
