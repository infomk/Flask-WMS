import mapnik

class MapProcessing:

    def __init__(self, input, width, height):
        self.map = mapnik.Map(width, height)
        self.layer = mapnik.Layer('raster')
        self.layer.datasource = mapnik.Gdal(file = input, band = 1)

    def get_map(self, ):
        return self.map
    
    def set_map(self, map):
        self.map = map

    def fit_to_bbox(self, bbox):
        bbox = bbox.split(',')
        
        xmin = float(bbox[1])
        xmax = float(bbox[3])
        ymin = float(bbox[0])
        ymax = float(bbox[2])

        self.map.zoom_to_box(mapnik.Envelope(xmax, ymax, xmin, ymin))

    def get_srs(self, ):
        return self.map.srs

    def set_srs(self, srs):
        self.map.srs = srs

    def colorize_map(self, layer):
	    
	    # TODO According to layer personalize color palette
        rc = mapnik.RasterColorizer(mapnik.COLORIZER_LINEAR, mapnik.Color(0, 0, 0, 0))
        for value, color in [
			(0, '#ffffd9'),
			(1, '#edf8b1'),
			(1.5, '#c7e9b4'),
			(2, '#7fcdbb'),
			(2.5, '#41b6c4'),
			(3, '#1d91c0'),
			(3.5, '#225ea8'),
			(4, '#253494'),
			(120, '#081d58')
			]:
            rc.add_stop(value, mapnik.Color(color))

        style = mapnik.Style()
        rule = mapnik.Rule()
        sym = mapnik.RasterSymbolizer()
        
        sym.colorizer = rc
        rule.symbols.append(sym)
        style.rules.append(rule)
        
        self.map.append_style('Raster', style)
        
        self.layer.styles.append('Raster')
        self.map.layers.append(self.layer)

    def add_boundaries(self, boundaries):
        polygons = mapnik.LineSymbolizer()
        
        rPolygons = mapnik.Rule()
        rPolygons.symbols.append(polygons)
        
        sPolygons = mapnik.Style()
        sPolygons.rules.append(rPolygons)
        self.map.append_style('Shape', sPolygons)
        
        lPolygons = mapnik.Layer('shp')
        lPolygons.datasource = mapnik.Shapefile(file=boundaries)
        lPolygons.styles.append('Shape')
        
        self.map.layers.append(lPolygons)
    
    def map_to_image(self, bbox):
	    
	    xmin = float(bbox[1])
	    xmax = float(bbox[3])
	    ymin = float(bbox[0])
	    ymax = float(bbox[2])
	    
	    self.map.zoom_to_box(mapnik.Envelope(xmax, ymax, xmin, ymin))
	    
	    im = mapnik.Image(1800, 1200)
	    mapnik.render(self.map, im, 1)
	    return im