import flask

# submodules
from modules.MapProcessing.MapProcessing import MapProcessing
from modules.DataProvider.DataProvider import DataProvider


"""

"""
class Wms:


    def __init__(self, ):
        self.mandatory_attributes = ['request', 'layers', 'width', 'height', 'format', 'bbox']
    
    def check_mandatory_args(self, args):
        for attr in self.mandatory_attributes:
            if attr not in args:
                return False

        return True

    def get_capabilities(self, ):
        with open('./modules/wms/wms.xml', 'r') as xms_file: 
            return xms_file.read()

    def get_map(self, args):

        # double check mandatory params
        if self.check_mandatory_args(args) == False:
            return {'status': 'error', 'message': 'invalid params'}
            
        # Get data based on input params
        print(args)
        self.data_provider = DataProvider(args['layers'])

        map = MapProcessing(self.data_provider.get_data(), int(args['width']), int(args['height']))
        map.colorize_map(args['layers'])
        map.add_boundaries(self.data_provider.get_boundaries())
        
        resp = flask.Response(map.map_to_image(args['bbox'].split(',')).tostring('png'))
        resp.headers['Content-Type:'] = 'image/png'

        return resp
        