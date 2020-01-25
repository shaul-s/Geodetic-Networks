import numpy as np
import pandas as pd


def geodetic2geocentric(geodeticPoints, a, e):
    """
    :param geodeticPoints:
    :param a:
    :param e:
    :return:
    """
    geocentric = []
    for row in geodeticPoints:
        N = a / np.sqrt(1 - (e ** 2) * (np.sin(row[0]) ** 2))
        X = (N + row[2]) * np.cos(row[0]) * np.cos(row[1])
        Y = (N + row[2]) * np.cos(row[0]) * np.sin(row[1])
        Z = ((1 - e ** 2) * N + row[2]) * np.sin(row[0])
        geocentric.append([X, Y, Z])

    return np.array(geocentric)

def geocentric2topocentric(geocentricPoints, geoRefPoint):
    """
    :param geocentricPoints:
    :param geoRefPoint:
    :return:
    """
    topocentric = []
    refPoint = geocentricPoints[0, :]
    R = np.array([[-np.sin(geoRefPoint[0])*np.cos(geoRefPoint[1]), -np.sin(geoRefPoint[1]), np.cos(geoRefPoint[0])*np.cos(geoRefPoint[1])]
                     ,[-np.sin(geoRefPoint[0])*np.sin(geoRefPoint[1]), np.cos(geoRefPoint[1]), np.cos(geoRefPoint[0])*np.sin(geoRefPoint[1])]
                     ,[np.cos(geoRefPoint[0]), 0, np.sin(geoRefPoint[0])]])

    for row in geocentricPoints:
        topo = np.dot(np.transpose(R), row - refPoint)
        topocentric.append(topo)

    return np.array(topocentric)


if __name__ == "__main__":
    geodeticPoints = np.array([[np.deg2rad(32.7700627300000), np.deg2rad(35.00681656), 398.584000000000],
                               [np.deg2rad(32.7882688900000), np.deg2rad(35.0276684500000), 27.0940000000000],
                               [np.deg2rad(32.7565971400000), np.deg2rad(35.0240785400000), 458.878000000000],
                               [np.deg2rad(32.7789391900000), np.deg2rad(35.0231361100000), 221.677000000000],
                               [np.deg2rad(32.7808972200000), np.deg2rad(35.0379888900000), 24.5000000000000],
                               [np.deg2rad(32.7811250000000), np.deg2rad(35.02562222), 184.400000000000],
                               [np.deg2rad(32.7706972200000), np.deg2rad(35.0185222200000), 381.800000000000],
                               [np.deg2rad(32.7794805600000), np.deg2rad(35.0284527800000), 142.700000000000]])

    a = 6378137
    e = 0.081819190842622
    geocentric = geodetic2geocentric(geodeticPoints, a, e)
    topocentric = geocentric2topocentric(geocentric, geodeticPoints[0, :])

    print(geocentric)
    print('hi')
