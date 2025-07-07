# recommend_crop.py

def recommend_crop(ndvi, rainfall, moisture):
    if ndvi > 6000 and rainfall > 180 and moisture > 25:
        return "Rice"
    elif 5000 < ndvi <= 6000 and 120 < rainfall <= 180 and 15 < moisture <= 25:
        return "Wheat"
    elif ndvi > 4000 and rainfall < 100 and moisture < 15:
        return "Millet"
    elif ndvi > 5500 and 100 < rainfall <= 200 and 15 < moisture <= 22:
        return "Sugarcane"
    elif ndvi > 3000 and rainfall > 90 and moisture > 18:
        return "Soybean"
    else:
        return "Groundnut"

