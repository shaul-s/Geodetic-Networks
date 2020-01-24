import numpy as np


def geodetic2geocentric(geodeticPoints, a, e):
    geocentric = []
    for row in geodeticPoints:
        N = a / np.sqrt(1 - (e ** 2) * (np.sin(np.deg2rad(row[0]))))
        X = (N + row[2]) * np.cos(np.deg2rad(row[0])) * np.cos(np.deg2rad(row[1]))
        Y = (N + row[2]) * np.cos(np.deg2rad(row[0])) * np.sin(np.deg2rad(row[1]))
        Z = ((1 - e ** 2) * N + row[2]) * np.sin(np.deg2rad(row[0]))
        geocentric.append([X, Y, Z])

    return np.array(geocentric)

def geocentric2topocentric(geocentricPoints):
    R = np.array([[-np.sin(np.deg2rad())*np.cos(np.deg2rad()), -np.sin(np.deg2rad), np.cos(np.deg2rad())*np.cos(np.deg2rad())]
                     ,[-np.sin(np.deg2rad())*np.sin(np.deg2rad()), np.cos(np.deg2rad()), np.cos(np.deg2rad())*np.sin(np.deg2rad())]
                     ,[np.cos(np.deg2rad()), 0, np.sin(np.deg2rad())]])
    refPoint = geocentricPoints[0, :]




if __name__ == "__main__":
    geodeticPoints = np.array([[32.7700627300000, 35.0234832300000, 398.584000000000],
                               [32.7882688900000, 35.0276684500000, 27.0940000000000],
                               [32.7565971400000, 35.0240785400000, 458.878000000000],
                               [32.7789391900000, 35.0231361100000, 221.677000000000],
                               [32.7808972200000, 35.0379888900000, 24.5000000000000],
                               [32.7811250000000, 35.0256222200000, 184.400000000000],
                               [32.7706972200000, 35.0185222200000, 381.800000000000],
                               [32.7794805600000, 35.0284527800000, 142.700000000000]])

    a = 6378137
    e = 0.081819190842622
    geocentric = geodetic2geocentric(geodeticPoints, a, e)


    print('hi')
