Documentation
=============

Definitions and Conventions
---------------------------

Geographical Map Projection
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this package, we follow two conventions for positioning location, including World Geodetic System (WGS84, EPSG:4326) standard and (WGS84, EPSG:3395). Both projections are using WGS84. Here is a summary of these systems and projections.

**EPSG:4326**

This projection is based on latitude and longitude, which is the common projection that is used in daily GPS applications. Read more: `epsg.io/4326. <https://epsg.io/4326>`_

* Unit: degree   
* Scope: Used by GPS satellite navigation system.   
* Bounds: Lat: -90:90, Lon: -180:180  

**EPSG:3395**

This projection is used for very small scale mapping. Read more: `epsg.io/3395. <https://epsg.io/3395>`_

* Unit: meter
* Scope: Small scale mapping
* Projection bounds: Lat: -15496570.74:18764656.23, Lon -20026376.39:20026376.39 (based on Lat:-80.0:84, Lon:-180:180)

[TODO: Add graphical representation.]
