import ee
import ee

# ✅ Specify your Earth Engine project ID
ee.Initialize(project='agroinfosystem-3faf6')

ee.Authenticate()
ee.Initialize()


# Initialize Earth Engine
ee.Initialize()

def get_ndvi_from_location(lat, lon):
    point = ee.Geometry.Point(lon, lat)

    image = ee.ImageCollection('MODIS/006/MOD13Q1') \
        .filterBounds(point) \
        .filterDate('2024-01-01', '2024-12-31') \
        .sort('system:time_start', False) \
        .first()

    ndvi = image.select('NDVI')
    ndvi_value = ndvi.reduceRegion(
        reducer=ee.Reducer.first(),
        geometry=point,
        scale=250
    ).getInfo()

    raw_ndvi = ndvi_value.get('NDVI', None)
    return raw_ndvi / 10000 if raw_ndvi is not None else None

