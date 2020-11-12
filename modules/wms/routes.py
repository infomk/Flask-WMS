import flask
from . import routes
from .wms.wms import Wms

wmsController = Wms()

"""

"""
def get_args_from_request():
    args = {}
    for attribute, value in flask.request.args.items():
        args[attribute.lower()] = value
    
    return args

"""

"""
@routes.route('/wms')
def wms():

    args = get_args_from_request()

    # TODO creating dynamic XML
    if args['request'] == 'GetCapabilities':
        return wmsController.get_capabilities()

    if args['request'] == 'GetMap':
        return wmsController.get_map(args)

    return {'status': 'error', 'message': 'not implemented'}
