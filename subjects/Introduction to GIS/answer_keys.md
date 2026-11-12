# Introduction to GIS: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 88f79b4ce45c

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper d7f5f642e9db

- Departments: Civil
- Programmes: BTech Civil 7005
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Civil_7005/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 25d63c1a9fdf

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 28cea944a4d3

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_DS_7009/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper b5ffcbcfac0a

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_EXTC_7006/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper a39bb1676285

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper e7962cc0c086

- Departments: Mechanical
- Programmes: BTech Mechanical 7003
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Mechanical_7003/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 6ff595aaaa1b

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Mechatronics_7004/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 50000e2a2538

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_AI_7051/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper f153460642b6

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper eec8ace38408

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_IT_7041/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 290f22a61f80

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_Computer_7032/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 0d2843248401

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_DS_7038/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper e66edd1ade3f

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_IT_7037/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
Topographic maps produced by the Survey of India are detailed
representations of the Earth’s surface showing both natural and man-made
features. Their main components include relief (depicted using contours, spot
heights, and benchmarks), drainage (rivers, lakes, canals), cultural features
(roads, railways, settlements), vegetation and land use, grid and coordinate
system (latitude–longitude or UTM grid), scale, legend, and north direction.
Among these, contours and drainage networks can be easily generated using
GIS geo-processing tools. Contours are created from digital elevation models
(DEMs) through interpolation functions that convert elevation data into lines
of equal height, reflecting the concept of contour mapping. Similarly,
drainage patterns can be derived using hydrological tools in GIS, which
analyze terrain slope and flow direction to delineate streams and watersheds
automatically. These capabilities make GIS highly efficient in modern
CO-1   a   cartographic production.   (5)
BL: 3
In navigation and geodesy, a rhumb line, small circle, and great circle are
different types of paths on the Earth’s surface. A rhumb line (loxodrome) is a
path that cuts all meridians at a constant angle, making it useful for navigation
because it maintains a constant compass bearing, though it is not the shortest
distance. A small circle is any circle on the Earth’s surface whose center does
not coincide with the Earth’s center (e.g., lines of latitude except the equator).
In contrast, a great circle is the largest possible circle on a sphere, with its
center coinciding with the Earth’s center (e.g., the equator or meridians), and it
represents the shortest distance between two points on the globe, which is
why it is widely used in air and sea navigation.
********** 1 **********
--- page 2 ---
Types of map scales and their working
Maps use different kinds of scales to represent real-world distances, each
suited to specific purposes:
• Statement (Verbal) Scale
Expressed in words (e.g., “1 cm represents 1 km”). It is simple and
easy to understand, making it suitable for general-purpose maps like
atlases, but less precise for calculations.
• Representative Fraction (RF) Scale
Written as a ratio (e.g., 1:50,000), meaning 1 unit on the map equals
50,000 of the same units on the ground. It is universally applicable and
mathematically precise, making it ideal for scientific and engineering
maps.
• Graphic (Linear/Bar) Scale
Shown as a line divided into equal segments representing ground
distance. It remains accurate even if the map is resized
(enlarged/reduced), so it is very useful in printed and digital maps.
Appropriateness:
•   Small-scale maps (large areas) → RF or statement scales
CO-1   •   Large-scale maps (detailed areas) → RF and graphic scales
b   • Maps subject to resizing → graphic scale preferred   (5)
BL:4
Calculation of map distance
Given scale:
14 cm = 1000 km
So,
1 km = 1000cm 14
For 16754 km:
14
Map distance =   × 16754
1000
= 234.556 cm
Final Answer:
Map distance ≈ 234.56 cm (≈ 2.35 m)
Concept of space and time in layer coverage
CO-2 BL: 3   c   In GIS, especially in ArcGIS, a layer coverage represents spatial data as   (5)
organized thematic layers. The concept of space refers to the geographic
location and arrangement of features on the Earth’s surface—captured using
********** 2 **********
--- page 3 ---
coordinates (latitude–longitude or projected systems). Each feature (point,
line, polygon) has a defined position, shape, and spatial relationship with other
features (topology), such as adjacency, connectivity, and containment.
The concept of time adds a temporal dimension to these spatial layers. It
allows GIS to represent how features change over time—for example, land use
change, river course shifts, or urban expansion. In layer coverage, time can be
handled through time-stamped attributes or multiple temporal layers, enabling
spatio-temporal analysis. Thus, GIS integrates where (space) and when (time)
to study dynamic geographic phenomena.
Shapefiles: mandatory extensions and what they depict
A Shapefile is a widely used vector data format in GIS that represents
geographic features and their attributes.
Mandatory extensions of shapefiles
A shapefile must have at least three core files:
•   .shp → stores the geometry (shape of features: points, lines, polygons)
•   .shx → index file for quick access to geometry
•   .dbf → attribute table storing information about each feature
(Other optional files like .prj store projection information.)
What shapefiles depict
Shapefiles depict vector spatial data, meaning:
• Points → locations (e.g., wells, cities)
• Lines → linear features (e.g., roads, rivers)
• Polygons → area features (e.g., land parcels, lakes)
Each spatial feature is linked to descriptive data in the attribute table, allowing
both mapping and analysis. Thus, shapefiles are fundamental in representing
real-world geographic features digitally in GIS systems.
The Hierarchical Model is one of the earliest database models used to
organize data in a tree-like structure where records are arranged in parent–
child relationships. Its key feature is that each parent record can have multiple
child records, but each child has only one parent, creating a one-to-many
CO-1   relationship. The structure starts with a single root node at the top, from which   (5)
BL: 3   d   branches extend downward into levels, forming a clear hierarchy. Data is
accessed through predefined paths, meaning retrieval follows a top-down
approach. This makes the model highly efficient for structured and predictable
data but less flexible when relationships become complex. Another important
feature is data integrity, as the strict hierarchy reduces redundancy and
********** 3 **********
--- page 4 ---
enforces clear relationships. However, it lacks support for many-to-many
relationships and can be rigid when modifications are required.
In organizing non-spatial data, the hierarchical model is particularly useful
where information naturally follows a ranked or nested structure, such as
administrative divisions (country → state → district → city) or organizational
charts (company → department → employee). Each level stores attributes
relevant to that entity, and relationships are maintained through the hierarchy.
This allows efficient storage, quick retrieval, and logical grouping of related
data. For example, in a GIS context, non-spatial attributes like census data or
land records can be structured hierarchically, making it easier to query and
manage them systematically.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS ecosystem
Attribute tables are the backbone of GIS because they store the non-spatial
(descriptive) data linked to spatial features. Every feature (point, line,
polygon) in a layer has a corresponding row in the attribute table, and each
column represents a specific attribute such as name, type, elevation,
population, or road width. This linkage between geometry and attributes
enables querying, filtering, and analysis—for example, selecting all roads
wider than a certain width or identifying areas above a particular elevation.
Attribute tables also support operations like joins, relates, and statistical
analysis, making them essential for decision-making. In short, while maps
show where, attribute tables explain what and how much, enabling meaningful
geospatial analysis.
Terrain maps: Geodatabase, Feature Classes, and Feature Data
1
CO-2, 2   a   Sets   [10]
BL- 4, 6
In terrain mapping, spatial data is organized within a Geodatabase, which acts
as a central repository for storing and managing spatial and non-spatial data.
• Feature Classes
These are individual layers of similar geometry types:
o Points → elevation points, benchmarks
o Lines → rivers, contours, roads
o Polygons → landforms, watersheds, land-use zones
These are vector data types.
• Feature Data Sets
These are collections of related feature classes grouped together based
on a common coordinate system. For example, a “Terrain” dataset may
include contours, slope polygons, and drainage lines, all spatially
related.
• Other data types in geodatabase
o Raster data → DEMs (Digital Elevation Models), satellite
imagery
********** 4 **********
--- page 5 ---
o Tables → attribute and statistical data
Use in analysis
These components enable:
• Terrain analysis → slope, aspect, elevation modeling from DEMs
• Hydrological analysis → drainage networks, watershed delineation
• Network analysis → route optimization using road networks
• Overlay analysis → combining layers to derive new insights
Example: Transport system in a big city
Consider designing a transport network in a metropolitan city:
• Geodatabase structure
o Feature Dataset: “Urban Transport”
▪ Roads (line feature class)
▪ Bus stops (point feature class)
▪ Metro lines (line feature class)
▪ Land use (polygon feature class)
o Raster: DEM for terrain constraints
o Tables: Traffic volume, population density
• How data is added
o Import shapefiles or GPS survey data into feature classes
o Digitize roads and transport routes from satellite imagery
o Attach attribute data (e.g., road width, traffic load) via tables
• Use in analysis
o   Identify optimal routes avoiding steep slopes (terrain + roads)
o Locate new bus stops based on population density and
accessibility
o Perform shortest path or least-cost path analysis
Topological operations in GIS define how vector features relate to one another
in space, and they often change or reorganize geometry so that meaningful
analysis can be carried out. In a geospatial agriculture management system,
these operations are extremely useful because farm plots, irrigation lines, soil
zones, roads, water bodies, and administrative boundaries must often be
studied together. Overlay is a broad topological function in which two or
more layers are placed one above another so that their geometries and
b   attributes are combined. Step by step, the GIS first aligns the input layers in   [10]
the same coordinate system, then identifies where features overlap in space,
splits the original geometries at those overlap boundaries, and finally creates
new output features carrying attributes from all the input layers. For example,
if a farmer overlays a soil-type polygon layer with a crop parcel polygon
layer, the output divides the fields according to soil variation, helping decide
which crop or fertilizer is best suited to each part of the land.
********** 5 **********
--- page 6 ---
Intersection is a more specific overlay operation that keeps only the common
geographic area shared by the input layers. Its working begins with selecting
two or more thematic layers, such as farmland parcels and irrigation-command
areas. The GIS checks where the geometries spatially overlap, cuts the features
at the common boundaries, removes all non-overlapping parts, and creates a
new layer containing only the shared portions, along with combined attributes.
In agriculture, this is useful when identifying only those agricultural fields that
lie within a canal irrigation zone, a flood-prone zone, or a government subsidy
zone. This allows planners to target only relevant farms for irrigation
scheduling, compensation, or support schemes.
Adjacency refers to the topological relationship of features that share a
common boundary or touch one another. Unlike overlay or intersection,
adjacency does not always create entirely new geometry, but it helps GIS
understand neighboring relationships between polygons or connectedness
among features. Step by step, the system first stores topology rules, then
checks which polygons share edges or nodes, and then records these neighbor
relationships in a topological structure or attribute relationship. In some
analyses, this may be used to group or compare adjacent farm plots. For
instance, in an agriculture management system, adjacency can help identify
which farms are directly next to an infected pest-affected field, so that
preventive spraying can be planned in surrounding parcels as well. Thus,
overlay mainly combines layers, intersection extracts only common areas, and
adjacency identifies neighborhood relationships, all of which are essential for
precise agricultural planning and land management.
Choice of map scale
For a map of Tata Power users in a neighborhood, a large-scale map is
more appropriate. Large-scale maps represent a small area with great detail
(e.g., 1:5,000 or 1:10,000). At a neighborhood level, you need to show
individual houses, buildings, streets, and possibly exact service connections. A
large scale allows accurate plotting of users, infrastructure, and distribution
networks, enabling precise planning, maintenance, and load management.
In contrast, for a map of agricultural cover across different states of India,
a small-scale map is suitable. Small-scale maps (e.g., 1:1,000,000 or smaller)
2   cover large areas with less detail but provide a broader perspective. Since the
CO-1, 2   a   aim is to show general patterns of agriculture across states rather than   [10]
BL- 4, 6   individual fields, a small scale helps in visualizing regional distribution, crop
zones, and comparisons between states effectively.
Summary:
• Neighborhood-level analysis → Large-scale (more detail)
•   Country/state-level overview → Small-scale (broader coverage)
Heat Maps and Choropleth Maps
********** 6 **********
--- page 7 ---
7
1. Heat Maps
A heat map represents the density or intensity of point data using color
gradients (e.g., blue to red).
How it is made:
1. Collect point data (e.g., locations of users, events, or incidents)
2. Apply a density estimation method (like kernel density)
3. Assign colors based on concentration levels
4. Generate a continuous surface showing hotspots
Usage:
•   Identifying areas with high electricity demand (e.g., Tata Power users
clustering)
• Mapping crime hotspots or disease spread zones
2. Choropleth Maps
A choropleth map displays data aggregated over predefined regions (like
states or districts) using different colors or shades.
How it is made:
1. Divide the area into administrative units (polygons)
2. Attach statistical data to each unit
3. Classify the data into ranges (e.g., low to high)
4. Assign colors/shades to each class
Usage:
• Showing agricultural production across Indian states
•   Displaying population density, literacy rate, or income distribution
Cylindrical projections imagine the Earth projected onto a cylinder wrapped
around it. Meridians and parallels appear as straight, perpendicular lines. A   [10]
b
classic example is the Mercator projection. These projections preserve
direction (useful for navigation) but distort area and shape increasingly toward
********** 7 **********
--- page 8 ---
the poles. Hence, they are best suited for equatorial regions where distortion is
minimal.
Conical projections project the Earth onto a cone placed over it, usually
touching along one or two standard parallels. Parallels appear as arcs of circles
and meridians as straight lines converging at the apex. Distortion is minimal
along the standard parallels and increases away from them. These projections
are ideal for mid-latitude regions such as countries extending east–west (e.g.,
India, USA).
Azimuthal projections (planar projections) involve projecting the Earth onto
a flat plane touching it at a single point. Directions from the center are
preserved accurately. Distortion is minimal at the point of contact and
increases outward. These projections are commonly used for polar maps and
aviation/navigation purposes.
Importance of Geoid and Datum in cartography
The Geoid represents the true, irregular shape of the Earth based on
gravitational variations and approximates mean sea level. It is important
because it provides a realistic vertical reference for elevations and heights.
A Datum is a mathematical model that defines the position of the Earth’s
surface in a coordinate system. It includes a reference ellipsoid and control
points. Datums are essential for ensuring that spatial data from different
sources align correctly; without a common datum, maps may show positional
mismatches.
Region with least distortion in map projections
In any projection, distortion is least at the point or line of contact between
the Earth and the projection surface. Therefore:
•   In cylindrical projections → least distortion near the equator
•   In conical projections → least distortion along the standard parallels
•   In azimuthal projections → least distortion at the center point of
projection
Polygon Attribute Table (PAT)
A Polygon Attribute Table (PAT) is the tabular component associated with
3   polygon features in a GIS layer. Each row in the table corresponds to one
CO-2, 3   a   polygon (e.g., a land parcel, watershed, or administrative unit), and each   [10]
BL-4, 5   column stores attributes describing that feature—such as area, perimeter, land-
use type, soil class, or ownership. In systems like ArcGIS, a PAT also
maintains a unique identifier that links the geometry (shape) of the polygon to
its descriptive data. It enables operations such as querying (e.g., “select all
********** 8 **********
--- page 9 ---
agricultural plots > 2 hectares”), classification, thematic mapping, and spatial
analysis, making it essential for managing and interpreting polygon-based
datasets.
Connection between IoT and GIS
The Internet of Things (IoT) integrates seamlessly with GIS by providing
real-time, location-based data. IoT devices—such as environmental sensors,
GPS trackers, weather stations, and smart meters—continuously collect data
(temperature, moisture, traffic flow, energy usage) and transmit it to GIS
platforms. GIS then maps, analyzes, and visualizes this data spatially. For
example, in agriculture, soil moisture sensors can feed data into GIS to guide
irrigation decisions; in cities, traffic sensors can support dynamic route
planning. Thus, IoT adds the live data layer, while GIS provides the spatial
intelligence framework.
Ordinal vs Ratio levels in GIS analysis
Measurement levels influence how data can be analyzed:
• Ordinal Level
Data is ranked or ordered, but differences between values are not
quantitatively meaningful (e.g., soil quality classes: poor, moderate,
good). In GIS, ordinal data supports classification and comparison but
cannot be used for arithmetic operations like averaging.
• Ratio Level
Data has a true zero and equal intervals (e.g., rainfall in mm,
population, elevation above sea level). Ratio data allows all
mathematical operations—addition, subtraction, ratios, statistical
modeling—making it highly useful for quantitative spatial analysis.
Impact on GIS:
•   Ordinal → suitable for thematic mapping, ranking, suitability analysis
•   Ratio → suitable for precise modeling, interpolation, and statistical
analysis
Line-on-line overlay operation
Line-on-line overlay is a spatial operation where two line feature layers are
combined to analyze their intersections and relationships. Step by step:
1. Two line layers (e.g., roads and pipelines) are input into the GIS.
2. The system identifies where the lines intersect or overlap.
3. It splits the lines at intersection points.
********** 9 **********
--- page 10 ---
4. A new output layer is created, where each segment carries attributes
from both input layers.
Example: In an urban planning scenario, overlaying road networks with
utility lines helps identify crossing points for maintenance planning or risk
assessment. In agriculture, overlaying irrigation canals with field boundaries
can help determine which plots are directly served by specific channels.
Concept involved: topological relationships—especially intersection and
connectivity—govern how features are split and attributes are transferred.
Story Maps are interactive web-based applications—popularized by platforms
like ArcGIS StoryMaps—that combine maps with text, images, videos, and
multimedia to communicate geographic information in a compelling narrative
format. Instead of presenting raw data or static maps, they guide users through
a story, making complex spatial information easy to understand for planners,
administrators, and even local communities.
In a village management system, Story Maps become powerful tools for
planning, monitoring, and community engagement. For example, a village
development Story Map can integrate layers such as land use, water resources,
roads, schools, and healthcare facilities, along with descriptive content
explaining each aspect. A section on agriculture might show crop distribution
maps with photos and seasonal insights, helping farmers and officials
understand productivity patterns. Similarly, a water management Story Map
could highlight wells, boreholes, and irrigation canals, combined with real-
time or historical data, enabling better allocation of water resources during
droughts.
b   Story Maps are also useful for infrastructure planning. A village authority   [10]
can present road conditions, electrification coverage, and public transport
access visually, helping identify underserved areas. For instance, by mapping
households without electricity and overlaying them with existing grid lines,
decision-makers can prioritize expansion projects. In disaster management,
Story Maps can illustrate flood-prone zones, evacuation routes, and safe
shelters, making them accessible to villagers in an easy-to-understand format.
Another key benefit is community participation. Since Story Maps are
visually intuitive, they allow villagers to engage with data, provide feedback,
and contribute local knowledge. For example, a participatory Story Map can
include inputs from farmers about soil quality or pest issues, enriching the
dataset.
Overall, Story Maps transform GIS data into actionable insights by blending
spatial analysis with storytelling, making them highly effective for transparent
governance, informed decision-making, and inclusive rural development.
In GIS, spatial data is broadly represented as vector and raster formats, each
4   suited to different kinds of geographic phenomena. Vector data represents   [10]
CO- 2, 3   a
BL-4, 5   features using discrete geometries—points, lines, and polygons. For example,
a well can be a point, a road or river a line, and a village boundary or
********** 10 **********
--- page 11 ---
agricultural field a polygon. These datasets are precise, efficient for storing
boundaries, and ideal for network and cadastral analysis. In contrast, raster
data represents space as a grid of cells (pixels), where each cell holds a value
such as elevation, temperature, or reflectance. Examples include satellite
imagery, land surface temperature maps, and digital elevation models. Raster
is better for continuous phenomena where values change gradually over space.
Kinds of data represented
Vector datasets include:
• Points → wells, boreholes, bus stops
• Lines → roads, rivers, pipelines
• Polygons → land parcels, administrative boundaries, crop fields
•   Attributes (stored in tables) → population, crop type, soil category
Raster datasets include:
• Continuous data → elevation (DEM), rainfall, temperature
• Imagery → satellite images, aerial photos
• Thematic rasters → land-use classification grids, soil moisture maps
Key distinction:
• Vector → discrete, precise boundaries
•   Raster → continuous surfaces, cell-based representation
Buffering in GIS
Buffering is a spatial operation that creates zones of a specified distance
around features. It is widely used in proximity analysis.
Types of buffering options
1. Fixed (Uniform) Buffer
A constant distance is applied to all features.
Example: 100 m buffer around all roads to study noise impact.
2. Variable Buffer
Buffer distance varies based on an attribute field.
Example: Larger buffer around highways than local roads.
3. Multiple Ring Buffer
Creates several concentric zones at increasing distances.
Example: 0–1 km, 1–5 km, and 5–10 km zones around a city center.
4. Dissolved Buffer
Overlapping buffers are merged into a single feature.
Example: Combining buffers of nearby wells to show total influence
area.
5. Non-dissolved Buffer
Buffers remain separate even if they overlap.
Example: Maintaining individual service areas for different facilities.
********** 11 **********
--- page 12 ---
6. Network Buffer (Service Area)
Buffering based on travel distance/time along a network instead of
straight-line distance.
Example: Area reachable within 10 minutes from a hospital using road
networks.
Applications
• Environmental protection (buffer around rivers)
• Urban planning (setback zones)
•   Agriculture (buffer around irrigation canals)
•   Infrastructure (impact zones around roads or pipelines)
ArcGIS Pro embeds machine learning (ML) and deep learning (DL) through
its Image Analyst, Spatial Analyst, and Geoprocessing toolsets, enabling
end-to-end GeoAI workflows. Data (imagery, lidar, vectors) is prepared and
labeled using training sample tools; models are then trained or imported
(PyTorch/TensorFlow) via deep learning packages. Common tools include
Train Deep Learning Model, Classify Pixels Using Deep Learning
(semantic segmentation), and Detect Objects Using Deep Learning (object
detection). For non-imagery ML, tools like Forest-based Classification and
Regression (random forest) and Generalized Linear Regression operate on
vector/tabular data. Trained models are saved as deep learning packages
(.dlpk) and deployed for inference across large areas using raster analytics,
ModelBuilder, or Python (ArcPy). This integration lets users move seamlessly
from data prep → training → inference → mapping within one environment.
Predictive analysis for pothole management
b (workflow)   [10]
A pothole management system combines detection (what/where now) and
prediction (where next/when likely):
1) Data assembly
•   High-resolution road imagery (mobile mapping, drones, street-level
cameras)
• Road network layer with attributes (surface type, age, traffic load)
• Environmental layers (rainfall intensity, drainage, slope)
• Maintenance history (repairs, complaints)
2) Detection with deep learning
• Label potholes on sample images (bounding boxes or masks).
•   Train a model (e.g., Mask R-CNN/U-Net) using Train Deep Learning
Model.
********** 12 **********
--- page 13 ---
• Run Detect Objects Using Deep Learning to extract pothole locations
as points/polygons with confidence scores.
•   Result: a continuously updated pothole inventory.
3) Feature engineering for prediction
•   Join detected potholes to road segments (spatial join).
• Derive predictors: traffic (AADT), rainfall, pavement type, age,
drainage proximity, previous failures, slope from DEM.
• Aggregate to segments (e.g., potholes per km, recent repair counts).
4) Predictive modeling (ML)
• Use Forest-based Classification/Regression to model:
o Classification: probability a segment will develop potholes
(risk class).
o Regression: expected pothole density in the next time window.
•   Validate with holdout data; assess accuracy (AUC, RMSE).
5) Deployment & mapping
• Apply the trained model to all road segments.
• Produce a risk map (low–high likelihood) and priority list.
• Automate with ModelBuilder/ArcPy for periodic updates (e.g., after
monsoon).
Practical examples
• Post-monsoon rapid assessment (Mumbai):
Use vehicle-mounted cameras to capture road imagery; a DL model
detects potholes citywide overnight. Segments with high counts and
heavy traffic are flagged for immediate repair. A random forest model
then predicts which nearby segments (similar traffic + poor drainage)
are likely to fail within 2–4 weeks, enabling preemptive patching.
• Corridor prioritization for highways:
Combine DL-detected potholes with pavement age and rainfall grids. A
regression model estimates future pothole density per 10 km stretch.
Maintenance teams schedule crews on stretches with the highest
predicted growth, reducing emergency repairs.
•   Citizen-report integration:
Crowd-sourced points (apps) are fused with DL detections;
discrepancies trigger field verification. The predictive model learns
from both sources, improving hotspot forecasting.
Why this works
• DL excels at extracting features from imagery (accurate, scalable
detection).
********** 13 **********
--- page 14 ---
• ML excels at learning relationships among multiple predictors (traffic,
weather, materials) to forecast risk.
• ArcGIS Pro unifies both with spatial context—linking predictions
directly to where actions should occur—supporting data-driven,
proactive road maintenance.
In GIS, especially when dealing with topological relationships in vector data,
the terms contiguity, area definition, and connectivity describe how spatial
features relate to each other.
Contiguity refers to the relationship between adjacent polygon features that
share a common boundary. It helps identify which areas are neighbors. For
example, in a map of agricultural fields or administrative districts, contiguity
allows GIS to determine which parcels or districts touch each other. This is
important in analyses such as spread of pests, land-use planning, or regional
clustering, where neighboring relationships matter.
Area definition refers to the correct representation and identification of
polygon features as closed, bounded regions. In GIS, a polygon must be
properly defined by a series of connected lines forming a closed loop so that it
represents a valid area (e.g., a farm, lake, or village boundary). This ensures
that calculations such as area, perimeter, and spatial overlays are accurate. It
also involves maintaining proper topology so there are no gaps or overlaps   [10]
a
unless intended.
Connectivity refers to how line features are linked together through nodes,
enabling movement or flow across a network. It is especially important in
5   network analysis involving roads, rivers, pipelines, or utility systems. For
CO-1, 2   example, in a transport network, connectivity ensures that roads intersect
BL-3   correctly at junctions, allowing route optimization and shortest-path analysis.
Together, these concepts ensure spatial integrity:
• Contiguity → identifies neighboring relationships
• Area definition → ensures correct polygon formation
• Connectivity → ensures proper linkage in networks
They form the basis of accurate spatial analysis and modeling in GIS.
Both operations are topological overlay functions in GIS, but they differ in
the type of input features and the kind of output generated:
• Point-in-Polygon
This operation determines whether a point lies inside, outside, or on the
b   boundary of a polygon. The GIS checks the location of each point   [10]
relative to polygon boundaries and assigns the attributes of the
containing polygon to the point.
Example: Assigning each well (point) to a village boundary (polygon)
to know which administrative unit it belongs to.
Output: Points with added polygon attributes (no change in geometry).
********** 14 **********
--- page 15 ---
• Line-in-Polygon
This operation analyzes how line features interact with polygons. The
GIS identifies where lines cross polygon boundaries, splits them at
those boundaries, and assigns polygon attributes to each segment.
Example: Dividing a road network (line) based on districts (polygons)
to analyze road length in each district.
Output: New line segments with polygon attributes (geometry is
modified).
Key Difference:
•   Point-in-polygon → containment check (no geometry change)
•   Line-in-polygon → intersection + segmentation (geometry changes)
Raster data map: what it consists of
6
A raster data map is a spatial representation made up of a grid of cells
(pixels), where each cell contains a value representing a specific attribute of
that location. The concept is based on dividing space into uniform units and
assigning numerical or categorical values to each unit.
Main components of a raster map:
•   Cells (pixels): Smallest unit of the raster; each holds a value
• Rows and columns: Arrange cells in a matrix/grid structure
•   Cell value: Represents data (e.g., elevation, temperature, land-use
class)
•   Resolution: Size of each cell; smaller cells = higher detail
• Extent: Total area covered by the raster
Types of raster data:
• Continuous data: Elevation (DEM), rainfall, temperature
• Categorical data: Land-use classes, soil types
• Imagery: Satellite and aerial images
6   Insurance (underwriting, pricing, claims):   [10]
a
CO-3
********** 15 **********
--- page 16 ---
BL-3, 4   • Data integration: Flood hazard maps, elevation (DEM), drainage,
historical claims, building footprints, construction type.
• Risk zoning: Overlay hazards with properties to produce parcel-level
risk scores.
•   Pricing & underwriting: Premiums and coverage limits are
differentiated by micro-risk (e.g., properties within 100 m of flood
channels get higher deductibles).
• Loss prevention: Buffering around drains/low-lying areas flags assets
needing mitigation (e.g., sump pumps, plinth elevation).
• Claims triage: Post-event satellite imagery + field apps prioritize
inspections where damage likelihood is highest, reducing settlement
time.
Banking (site selection, credit, collections):
• Branch/ATM placement: Heat maps of population density, footfall,
competitor locations, and road accessibility define optimal catchments.
• Credit risk: Combine borrower addresses with socio-economic layers
and hazard exposure to refine risk-based lending (e.g., tighter terms in
flood-prone wards).
•   Portfolio monitoring: Map delinquency clusters to target field
collections and outreach.
• Fraud detection: Spatial outliers (multiple high-value transactions
from unlikely locations) trigger alerts.
Outcome: Faster decisions, better risk-adjusted pricing, reduced losses, and
improved customer access—because “where” is built into every decision.
Enhancing mammal conservation with GeoAI
6
GeoAI combines GIS with machine learning/deep learning to analyze large,
multi-source ecological data for smarter conservation.
1) Habitat suitability & species distribution
•   Inputs: Land cover, vegetation indices (NDVI), water sources,
elevation, human disturbance.
• Method: ML models (e.g., random forest) predict where species are
likely to occur.
********** 16 **********
--- page 17 ---
• Use: Identify priority habitats for mammals (tigers, elephants,
leopards) and guide reserve expansion.
2) Movement & corridor protection
•   Inputs: GPS-collar tracks, terrain, roads, settlements.
• Method: Least-cost path and DL-based movement modeling to map
wildlife corridors.
• Use: Secure and restore corridors to reduce human–wildlife conflict
and roadkill.
3) Automated monitoring (camera traps & drones)
• Method: Deep learning (object detection/segmentation) classifies
animals in images/videos at scale.
• Use: Near real-time population estimates, behavior insights, and rapid
detection of rare/poached species.
4) Anti-poaching intelligence
•   Inputs: Patrol logs, past incidents, access routes, night-time lights.
• Method: Predictive risk maps highlight poaching hotspots; network
analysis optimizes patrol routes.
• Use: Proactive deployment of rangers and resources.
5) Climate & water stress forecasting
• Method: Time-series models on rainfall, temperature, and vegetation
predict drought stress.
• Use: Plan artificial water points and seasonal protection measures.
Example (India): Elephant conservation programs map seasonal migration
using GPS collars and satellite data; GeoAI pinpoints high-conflict villages
and critical crossings. Mitigations (early-warning systems, fencing,
underpasses) are then targeted precisely, reducing conflict while preserving
connectivity.
In a large Indian metro (e.g., Mumbai), agencies use ArcGIS to run last-mile
delivery for LPG cylinders and fresh milk.
Data layers (foundation):
• Road network (with speed, turn restrictions)
• Customer points (households, shops)
b   • Depots/warehouses (LPG godowns, milk chilling plants)   [10]
• Demand attributes (daily milk volumes, cylinder bookings)
•   Constraints (time windows, no-entry streets, vehicle capacity)
Workflow (step-by-step):
1. Geocoding & segmentation: Convert addresses to map points; cluster
customers into delivery zones (polygons) by demand and proximity.
********** 17 **********
--- page 18 ---
2. Service area analysis: Create 10–20 min catchments around depots to
assign customers to the nearest facility.
3. Route optimization (VRP): Solve a Vehicle Routing Problem to
minimize distance/time while respecting capacity and delivery time
windows (morning milk runs, LPG slot deliveries).
4. Dynamic re-routing: Ingest live traffic (IoT feeds) to update routes;
push changes to driver apps.
5. Equity & coverage: Use buffers around underserved areas to plan new
mini-depots or milk booths.
6. Performance monitoring: Dashboards track on-time delivery, fuel
use, and missed orders; heat maps reveal recurring bottlenecks.
Outcomes: shorter routes, lower fuel costs, reliable morning milk supply, and
faster LPG fulfillment with transparent service coverage.
How GIS mapping helps during crimes in cities
6
GIS supports analysis, prevention, and response:
1. Hotspot mapping:
o Aggregate incident points to produce density/heat maps.
o Police identify burglary or assault clusters and deploy patrols
accordingly.
2. Spatio-temporal analysis:
o Link time with location to find patterns (e.g., theft peaks near
transit nodes after 9 pm).
o Schedule patrol shifts and lighting interventions.
3. Network-based response:
o Use the road network to compute fastest routes for dispatch;
nearest patrol car is routed in seconds.
o Define service areas for stations to balance workload.
4. Geofencing & alerts:
o Virtual boundaries around sensitive zones (schools, events).
o Real-time alerts when tagged offenders or suspicious
movements enter zones.
5. CCTV & sensor integration (IoT + GIS):
o Map camera feeds; analyze with video analytics (vehicle
counts, anomaly detection).
o Link detections to locations for rapid situational awareness.
6. Predictive risk mapping:
********** 18 **********
--- page 19 ---
o Combine past incidents, land use, lighting, footfall, and
socioeconomic data to model risk surfaces.
o Target preventive measures (patrols, surveillance, community
outreach) before crimes occur.
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 8c176de03210

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_Computer_7047/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 Feb 2026
- Text: mixed (25 pages), mean OCR confidence 34.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech
(DS)/B. Tech (EXTC)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (Comp)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 12 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 25 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Draw diagrams whenever necessary
5. Try and keep answers chronological
6. Question 1 is compulsory. Attempt any four sub-questions from Question 2
Q1   Compulsory Question   [20]
In a Geographic Information System (GIS), the three key components —
Methods, People, and Software — are interdependent and together determine
how effectively spatial data is collected, analyzed, and applied. Methods refer
to the systematic techniques, procedures, and models used to process and
interpret geographic information. They define how a GIS operates, including
data collection methods, spatial analysis techniques, and visualization
approaches. The relevance of methods lies in ensuring that data handling and
interpretation are scientifically accurate, consistent, and efficient. For
instance, using appropriate interpolation or overlay techniques can
significantly influence the accuracy of spatial outputs in environmental
mapping or urban planning.
People form the most critical component of GIS because they are the users,
decision-makers, and developers who design, operate, and interpret the
CO-1   system. The effectiveness of any GIS project ultimately depends on the skill,   (5)
A
BL: 4   knowledge, and creativity of the people involved — from GIS analysts and
cartographers to engineers and policymakers. People determine what data to
collect, how to analyze it, and how to apply results to solve real-world
problems such as land-use planning, disaster management, or infrastructure
development. Without trained and motivated professionals, even the most
advanced GIS technology remains ineffective.
Software, meanwhile, provides the technological platform that enables GIS
operations. It includes the programs, applications, and algorithms that allow
for data input, storage, manipulation, analysis, and visualization. Examples
include tools like ArcGIS, QGIS, and ERDAS Imagine, which help users
perform spatial queries, overlay maps, and generate 3D visualizations. The
relevance of software lies in its capability, compatibility, and analytical
power, which define what kinds of spatial problems can be addressed.
********** 1 **********
--- page 2 ---
In essence, methods provide the framework, software provides the tools,
and people provide the intelligence to apply GIS effectively. A well-
functioning GIS depends on the balance and integration of all three, where
advanced software is guided by sound methods and used by skilled
professionals to produce meaningful, actionable geographic insights.
A bar scale (or graphic scale) is a visual representation of distance on a
map, usually drawn as a horizontal line divided into equal segments that
correspond to specific ground distances. Unlike numerical scales, a bar scale
remains accurate even if the map is enlarged or reduced, because it visually
adjusts with the map size. For example, a bar labeled “0–100–200 km” shows
that each segment represents 100 km on the ground, allowing users to directly
measure real-world distances using a ruler or even by eye. This makes the bar
scale particularly convenient for field use and maps that may undergo resizing.
For small-scale maps, which cover large geographic areas such as countries or
continents, the representative fraction (R.F.) scale or bar scale is best
suited. Small-scale maps (e.g., 1:10,000,000) depict vast regions with less
detail, so a bar scale provides a quick and practical way to estimate long
distances visually without complex calculations.
CO-1
B   In the given problem, the original map scale is 4 cm : 1000 km. This means 1   (5)
BL:4, 5   cm on the map represents 250 km on the ground (since 1000 ÷ 4 = 250). Now,
if the distance on the ground is 1358 km, then the corresponding map distance
can be calculated using the ratio:
1358
Map distance =   = 5.432 cm (approximately 5.43 cm).
250
Hence, on this map, a ground distance of 1358 km would be represented by
about 5.43 cm, and the scale remains 1 cm = 250 km or equivalently
expressed as a representative fraction (R.F.) of 1 : 25,000,000. This type of
scale is most appropriate for small-scale maps that depict continental or
global extents with minimal detail.
Yes, most GIS mapping projects begin with a shapefile, which is one of the
most widely used formats for storing geospatial vector data. A shapefile is
not a single file but a collection of multiple files that work together to
represent geographic features and their associated attributes. It is developed
and maintained by Esri (Environmental Systems Research Institute) and is
compatible with most GIS software such as ArcGIS, QGIS, and Global
CO-2   C Mapper.   (5)
BL: 3
A shapefile primarily depicts geometric features such as points, lines, and
polygons that represent real-world objects on the Earth’s surface. For
example, points can represent locations like wells or cities, lines can represent
roads, rivers, or pipelines, and polygons can represent larger areas like
districts, land parcels, or lakes. Each of these geometric elements is linked to a
********** 2 **********
--- page 3 ---
database table that stores attribute information — such as names, population,
or land use type — making shapefiles ideal for both visualization and analysis.
For a shapefile to function properly in any GIS system, certain mandatory file
extensions must be present in the same directory with the same file name
prefix. These essential components are:
1. .shp – This is the main file that stores the geometric data (the actual
shapes or features such as points, lines, or polygons).
2. .shx – This is the index file, which allows quick access to the geometry
in the .shp file by indexing feature locations.
3. .dbf – This is the attribute table, stored in dBASE format, which
contains non-spatial data (such as names, values, or other descriptive
attributes) linked to each feature.
In addition to these, several optional files may accompany a shapefile, such as
.prj (projection information), .sbn/.sbx (spatial indexes), and .cpg (character
encoding), but the three core extensions .shp, .shx, and .dbf are mandatory for
the shapefile to function correctly.
The Hierarchical Model is a type of data organization model used primarily
for managing non-spatial data in databases, including those linked with
Geographic Information Systems (GIS). It was one of the earliest database
models developed to store and retrieve structured information efficiently
before the advent of relational databases. In a hierarchical model, data is
organized into a tree-like structure consisting of parent and child records,
where each child has only one parent, but a parent can have multiple
children. This structure reflects a clear one-to-many relationship, similar to a
family tree or organizational chart.
At the top of the hierarchy is the root node (parent), which represents the
main data category or entity. Beneath it, child nodes represent subordinate
entities that are dependent on the parent. Each relationship is maintained
through pointers or links, which establish how the records are connected. For
example, in a GIS-related database managing city infrastructure, a city could
CO-1   be the parent node, with roads, water networks, and buildings as child   (5)
D
BL: 3   nodes. Each of these child nodes may further have their own sub-levels — for
instance, a “building” node could have children like “floors” or “rooms.”
The main advantage of the hierarchical model is its data integrity,
simplicity, and speed of access for predictable, structured relationships. Since
all data follows a fixed hierarchy, retrieval of related records is very fast and
consistent. However, it has limitations in flexibility — because each child can
only have one parent, many-to-many relationships cannot be easily
represented. Modifying the structure (such as adding new relationships or
nodes) can also be complex and time-consuming.
In the context of non-spatial data management, the hierarchical model is
particularly useful for organizing information that naturally follows a layered
or nested structure — such as administrative boundaries (country → state
→ district → city) or environmental datasets (ecosystem → biome →
habitat → species). It provides a logical and efficient framework for
********** 3 **********
--- page 4 ---
representing and retrieving structured, dependent data, which can later be
linked to spatial layers in GIS for integrated analysis. In essence, the
hierarchical model is a top-down data organization approach that ensures
orderly data storage and quick retrieval, best suited for datasets with clearly
defined parent-child relationships.
Q2   Answer any (4) four
Importance of Attribute Tables in the ArcGIS Ecosystem
In the ArcGIS ecosystem, the attribute table forms the foundation for
storing and managing descriptive information about spatial features. While
the spatial data in a GIS defines where things are located (the geometry), the
attribute table describes what those things are (the information about each
feature). Each row in an attribute table corresponds to a spatial feature (such
as a point, line, or polygon), and each column represents a field or attribute
describing a property of that feature — such as name, area, population, soil
type, elevation, or land use. For example, in a shapefile showing cities, the
geometry defines city locations, while the attribute table stores data like
population, GDP, or literacy rate.
Attribute tables are vital for data querying, spatial analysis, and
visualization. They enable users to perform operations such as selecting
features by attribute, joining tables, symbolizing data, and performing
statistical analysis. For instance, a planner can use an attribute table to
highlight all districts with a population density above a certain threshold or
calculate average rainfall across different zones. In essence, the attribute table
allows ArcGIS to go beyond simple mapping — it transforms raw geographic
data into meaningful analytical insights, linking spatial geometry with non-
1   [10
spatial attributes.
CO-2, 2   A
]
BL- 4, 6
Concept of Geodatabase and Feature Datasets
A Geodatabase is the core data storage model in ArcGIS, designed to store,
organize, and manage both spatial and non-spatial data in an integrated,
relational structure. It acts as a container that can hold multiple datasets —
such as feature classes, raster datasets, tables, and relationships — within a
single database environment. Geodatabases are more advanced than shapefiles
because they support topology rules, domains, subtypes, and versioning,
allowing for complex spatial relationships and multi-user editing.
Within a geodatabase, Feature Datasets are logical groupings of related
feature classes that share the same coordinate system and spatial reference.
For example, in an urban GIS model, a feature dataset might include layers
like roads, buildings, waterlines, and utility networks — all aligned to the
same spatial projection. This structure ensures spatial integrity and enables
topological relationships (such as connectivity and adjacency) to be
maintained between layers.
********** 4 **********
--- page 5 ---
Applications in Network Analysis and Terrain Modeling
In network analysis, feature datasets are used to model and analyze
connected systems such as transportation networks, water supply systems,
or electrical grids. The topology rules in a geodatabase define how lines and
nodes connect, ensuring accurate pathfinding, route optimization, and flow
analysis. For instance, in a road network, nodes represent intersections and
edges represent roads — enabling ArcGIS to calculate the shortest path,
service areas, or optimal delivery routes using attribute data like travel time
or distance.
In terrain modeling, geodatabases store elevation and surface data (e.g.,
digital elevation models, contour lines, and slope layers) that can be used to
build 3D surfaces. These are crucial for applications such as watershed
delineation, slope stability analysis, and visibility studies. By integrating
attribute data (like soil type or rainfall) with elevation models, ArcGIS can
perform advanced spatial analyses, including hydrological modeling and
landform classification.
In summary, attribute tables in ArcGIS link spatial and descriptive data,
enabling meaningful analysis. The geodatabase provides a robust, scalable
framework to manage complex spatial datasets, while feature datasets
organize related data layers for spatial consistency. Together, they enable
powerful operations like network analysis and terrain modeling,
transforming GIS from a mere mapping tool into a comprehensive decision-
support and analytical system.
Topological overlays change vector geometry by splitting, trimming, and
(re)building features where layers overlap, while also combining their
attributes. In practice you snap/note all intersections between
boundaries/edges, then rebuild features from the resulting planar graph.
Intersection (keeps only the overlap)
What it does to geometry: It creates new features only where inputs overlap
and trims them to the exact common area/line/point. In ArcGIS/QGIS-style
[10
tools the output geometry takes the lowest dimension of the inputs
B
(point∩line → points at crossings; line∩polygon → the parts of the line inside   ]
the polygon; polygon∩polygon → polygons of overlap). Attributes from all
inputs are joined for those overlapping pieces.
How it operates (step-by-step):
1. Prepare/validate: Project layers to a common CRS; fix geometry
errors; snap small gaps; set a tolerance to avoid slivers.
2. Node the graph: Compute all true intersections between feature
boundaries/edges; insert vertices at crossings.
********** 5 **********
--- page 6 ---
3. Trim & build: Keep only edges/areas that are inside all inputs (e.g.,
line segments inside the polygon), delete the rest; dissolve tiny artifacts
under tolerance.
4. Attach attributes: Join fields from each input; non-overlapping
features contribute nothing (they’re dropped).
5. Post-checks: Merge multipart where needed, validate topology.
Traffic management example: Intersect a road centerline layer with a 500
m buffer around an incident (or a flood polygon). The result is just the road
segments inside the impact zone; attach live speed and lane data from the
road table + incident attributes from the buffer to prioritize closures and
diversion routing. Likewise, intersect bus routes with work-zone polygons to
list only affected route segments for detour planning.
Union (keeps everything; polygons only)
What it does to geometry: It overlays two (or more) polygon layers and
produces a mosaic where every boundary from either layer becomes a
boundary. Overlaps are split into separate polygons (with attributes from
both), and non-overlapping areas are also kept (with NULLs for missing
attributes).
How it operates (step-by-step):
1. Prepare/validate: Same as above—consistent CRS, fix self-
intersections, snap coincident edges.
2. Node & split: Build a combined planar graph from all polygon
boundaries; split polygons at every crossing.
3. Classify pieces: Tag each new piece by inside/outside status for each
source layer.
4. Assemble attributes: Join fields from all inputs; fill NULLs where a
piece didn’t exist in a source.
5. Clean up: Remove sliver polygons below a mapped area threshold;
enforce topology (no gaps/overlaps, unless intended).
Traffic management example: Union municipal jurisdiction polygons with
school/hospital safety zones to create a single map where each tiny polygon
“knows” which jurisdiction it’s in and whether it’s inside one or more
sensitive zones. You can then publish speed-limit regimes, set enforcement
priorities, or compute congestion charges that vary by both jurisdiction and
zone membership. Another use: union congestion-pricing zones with
accident hot-spot polygons to target dynamic pricing or signal timing where
both issues co-occur.
• CRS & units: Always overlay in a projected CRS suitable for
distance/area.
•   Tolerance/slivers: Set a small cluster tolerance and minimum-area
filter to avoid micro-polygons.
• Attribute design: After union, expect many NULLs; after intersection,
expect fewer features but richer rows.
• Geometry dimension rule (Intersect): Lowest-dimension geometry is
returned—handy for extracting crossing points (signals/rail crossings)
or in-polygon road segments.
********** 6 **********
--- page 7 ---
•   Planarity: Overlays assume planar graphs; clean self-overlaps and
dangles first for reliable results.
In short, Intersection answers “where do these layers overlap (and only
there)?” and produces trimmed features ideal for targeted actions (closures,
detours). Union answers “what is the full partition when I consider all
boundaries together?” and is ideal for policy and zoning maps where every
place must carry the combined designations from multiple sources.
A map scale expresses the relationship between a distance on a map and the
corresponding distance on the ground, and the distinction between small-scale
and large-scale maps lies in how much area they cover and the level of detail
they show. A large-scale map represents a smaller area with greater
detail—for example, a city map at 1:10,000 shows streets, buildings, and
landmarks clearly. In contrast, a small-scale map represents a larger area
with less detail—for example, a world map at 1:10,000,000 compresses vast
distances into limited space, making it ideal for showing general patterns like
climate zones or global boundaries. In simple terms, large-scale maps zoom in,
while small-scale maps zoom out.
A Choropleth Map is a thematic map that uses shading, color gradients, or
patterns to represent the statistical variation of a particular attribute across
predefined geographic areas, such as countries, states, or districts. The process
of creating a choropleth map begins with gathering spatial boundary data
(often in the form of shapefiles) and linking it with attribute data—for
example, population density, literacy rate, or rainfall levels. Next, the chosen
variable is classified into ranges or categories using methods like equal
intervals, quantiles, or natural breaks (Jenks classification). Each class is then   [10
A   assigned a distinct color or shade, where darker hues typically indicate higher
]
2   values and lighter ones represent lower values.
CO-1, 2
BL- 4, 6   Choropleth maps are widely used because they allow quick visual
comparison of spatial patterns and regional disparities. In demography,
they can depict population density or literacy rates; in economics, they show
income levels or employment rates; and in environmental studies, they can
display pollution intensity or rainfall distribution. In GIS platforms like
ArcGIS or QGIS, these maps are dynamically generated by linking an
attribute table to geographic boundaries and applying a color ramp.
In essence, while large-scale maps focus on local detail and precision, small-
scale maps reveal broader spatial relationships. Choropleth maps, on the
other hand, transform statistical data into visually interpretable patterns,
helping users identify trends, inequalities, and regional contrasts at any chosen
scale.
Difference Between Cylindrical, Conical, and Azimuthal Map Projections
[10
B
Map projections are mathematical methods used to represent the curved   ]
surface of the Earth on a flat map. Since the Earth is roughly spherical,
********** 7 **********
--- page 8 ---
projecting it onto a plane inevitably causes some distortion in shape, area,
distance, or direction. The three major types of projections—cylindrical,
conical, and azimuthal—differ based on the surface onto which the globe is
projected.
1. Cylindrical Projection:
In a cylindrical projection, the Earth’s surface is projected onto a
cylinder that is wrapped around the globe, tangent along the equator.
When the cylinder is unrolled into a flat surface, the parallels and
meridians appear as straight lines intersecting at right angles. This
projection preserves direction (conformality) but distorts areas,
especially near the poles. A common example is the Mercator
projection, used for navigation because it accurately represents
bearings and compass directions, though landmasses near the poles
(like Greenland) appear much larger than they are.
2. Conical Projection:
In a conical projection, the Earth’s surface is projected onto a cone that
is either tangent to or cuts through the globe along a standard parallel
(or two parallels). When the cone is unrolled, meridians appear as
straight lines converging toward the pole, and parallels form arcs of
circles. This type of projection minimizes distortion along the standard
parallels and is ideal for mid-latitude regions such as Europe, North
America, and India. The Lambert Conformal Conic and Albers
Equal-Area Conic projections are widely used for regional mapping,
aviation charts, and topographic maps.
3. Azimuthal (Planar) Projection:
In an azimuthal projection, the Earth’s surface is projected onto a flat
plane that touches the globe at a single point—usually a pole or the
equator. Directions from the center point to any other point on the map
are preserved, making this projection useful for air-route navigation
and polar region mapping. Distortion increases away from the central
point. The Polar Stereographic projection, for example, is often used
for Arctic and Antarctic maps because it preserves direction from the
pole outward.
Concept of Datum
A Datum in cartography and geodesy is a mathematical model of the Earth
that serves as a reference framework for measuring locations, elevations, and
distances. It defines the size and shape of the Earth (ellipsoid) and the origin
and orientation of coordinate systems like latitude and longitude. In simpler
terms, it tells the GIS or mapping system where “zero” is and how to align all
other coordinates to it.
There are two main types of datums:
• Horizontal Datum, which provides a reference for measuring
locations on the Earth’s surface (e.g., latitude and longitude).
Examples: WGS84 (World Geodetic System 1984) used for GPS, and
NAD83 (North American Datum 1983).
********** 8 **********
--- page 9 ---
•   Vertical Datum, which serves as a reference for measuring elevations
or depths (e.g., sea level). Examples: EGM96 (Earth Gravitational
Model 1996) and NAVD88 (North American Vertical Datum 1988).
Importance of the Geoid and Datum in Cartography
The Geoid represents the Earth’s true physical shape, defined by mean sea
level extended under the continents, influenced by gravity and Earth’s
rotation. It is an irregular but smooth surface that approximates where
gravity is equal in all directions. The Geoid serves as the reference surface
for measuring elevations—mountains, valleys, and sea depths are measured
relative to it.
The Datum, on the other hand, provides the mathematical and coordinate-
based framework that links the Geoid to mapping systems. Because the
Earth’s shape is not a perfect sphere or ellipsoid everywhere, datums adjust the
coordinate system to fit local or global geoid variations. Without an accurate
datum, spatial data from different regions or time periods would not align
correctly, causing positional errors.
In summary, while map projections determine how the curved Earth is
flattened for mapping, datums and the geoid define the true reference
surfaces from which all positions and elevations are calculated. Together, they
ensure that spatial data, whether from GPS, GIS, or remote sensing, remains
accurate, consistent, and globally comparable in cartographic applications.
A Polygon Attribute Table (PAT) is a fundamental data structure in
Geographic Information Systems (GIS) that stores and manages non-spatial
(attribute) information related to polygon features in a vector dataset. Each
polygon in a GIS layer—representing areas such as administrative boundaries,
land parcels, lakes, or forest zones—has a unique record in the PAT. This table
is directly linked to the spatial data through an identifier field (usually called
ID or FID), ensuring that every polygon’s geometric shape (its boundaries,
area, and perimeter) is connected to its corresponding descriptive data.
The Polygon Attribute Table typically contains system fields and user-
defined fields. System fields include properties automatically generated by the
3   [10
GIS, such as AREA, PERIMETER, and POLY# (polygon identification
CO-2, 3   A
number). User-defined fields store descriptive information like land use type,   ]
BL-4, 5
soil classification, ownership, or vegetation density. For instance, in a land
cover map, the PAT might include columns such as Polygon ID, Area (sq km),
Land Use Type, and Average Elevation. The PAT enables users to perform
attribute-based queries, classification, and statistical analyses—for
example, selecting all polygons classified as “agricultural land” or calculating
the total area under a specific land use category. Thus, the PAT serves as a
bridge between the geometric representation of features and their
descriptive information, making spatial analysis and thematic mapping
possible.
********** 9 **********
--- page 10 ---
When analyzing and interpreting spatial data in GIS, the level of
measurement—that is, how data values are categorized and quantified—
significantly affects the types of analyses that can be performed. The Ordinal
Level and Ratio Level of measurement are particularly important for
understanding data behavior.
1. Ordinal Level:
Ordinal data represent ranked or ordered categories where the
sequence matters, but the difference between ranks is not uniform or
measurable. Examples include land suitability ratings (e.g., high,
medium, low), soil erosion classes, or hazard risk levels. In GIS,
ordinal data can be mapped using graduated color or symbol
schemes to visualize ranking, but mathematical operations like
addition or subtraction are not meaningful. Analysts can perform
operations such as ranking, classification, and comparison, but not
direct arithmetic calculations.
2. Ratio Level:
Ratio data represent quantitative measurements with a true zero
point, allowing for the full range of mathematical operations (addition,
subtraction, multiplication, and division). Examples include elevation
(in meters), population density, rainfall (in mm), or distance (in
km). Because ratio data have both consistent intervals and a true zero,
GIS analysts can perform advanced operations such as buffering,
interpolation, normalization, and statistical modeling.
In summary, the Polygon Attribute Table (PAT) provides the core
framework for linking polygon geometry with descriptive information,
enabling spatial queries and thematic analysis. Meanwhile, understanding
ordinal and ratio measurement levels ensures that analysts apply the correct
statistical and visualization techniques—ordinal data guiding qualitative
comparisons, and ratio data supporting quantitative, model-based, and metric-
driven spatial analyses. Together, these concepts ensure both data integrity
and analytical accuracy in GIS-based decision-making.
Story Maps are interactive digital storytelling tools that combine maps,
multimedia content (like text, photos, videos, and graphics), and narrative
flow to communicate information about a place, event, or issue in an engaging,
visually rich format. Developed primarily through platforms like ArcGIS
StoryMaps (by Esri), they transform complex spatial data into a storytelling
experience, making geography and data-driven insights accessible to a wide
[10
audience. Story Maps are used across disciplines—from education and tourism
B
to urban planning and disaster management—because they help audiences see   ]
and understand spatial relationships through compelling visual narratives.
How Story Maps Are Created
********** 10 **********
--- page 11 ---
Creating a Story Map involves combining geographic data with narrative
design. The general steps include:
1. Gather and Prepare Data:
Spatial data layers such as population density, land use, or
transportation routes are created or imported into a GIS platform (like
ArcGIS Online). Relevant text, images, videos, and charts are also
collected to support the story.
2. Choose a Story Map Template or Format:
ArcGIS StoryMaps offers several formats—such as Map Tour (a
sequence of locations with descriptions), Map Journal (a scrolling
narrative with maps and multimedia), Cascade (a linear visual
storytelling format), and Map Series (tabbed layouts for multiple
maps).
3. Integrate Maps and Multimedia:
The creator embeds interactive web maps, adds explanatory text,
inserts images or videos, and organizes content into sections or panels.
This step transforms raw data into an understandable, visually cohesive
story.
4. Customize and Publish:
After design customization (color themes, typography, and transitions),
the Story Map is published online. It can then be shared publicly or
within an organization, often embedded in websites or social media
posts for easy access.
Uses and Importance of Story Maps
Story Maps are powerful because they merge data visualization with
narrative communication, helping people not only see where things happen
but also understand why. Their applications span numerous fields:
• Urban Planning: Cities use Story Maps to display zoning plans,
housing development, and transportation systems. For example, a
municipal Story Map might illustrate traffic congestion patterns and
proposed metro routes, helping planners engage with citizens.
• Environmental Studies: Researchers use Story Maps to show
deforestation, wildlife migration, or climate change effects over
time, combining satellite imagery with field data to convey
environmental trends effectively.
• Tourism and Culture: Tourism boards create Story Maps that
highlight heritage sites, trekking routes, or city tours, guiding
visitors interactively through points of interest. For instance, “Discover
Rajasthan” could use a Story Map showing fort locations, cultural
festivals, and desert trails.
•   Disaster Management: Emergency agencies develop Story Maps to
visualize real-time flood zones, wildfire perimeters, or relief camp
locations, helping authorities and citizens make informed decisions
quickly.
********** 11 **********
--- page 12 ---
Examples
• The UN Environment Programme (UNEP) uses Story Maps to
depict global plastic pollution hotspots and cleanup projects,
combining data layers with photographs and field reports.
• The New York City Vision Zero Story Map visualizes traffic
accidents and pedestrian safety measures, helping citizens and
policymakers analyze danger zones.
•   In education, geography students use Story Maps to narrate research
on urban growth, migration patterns, or water scarcity, blending
storytelling with spatial analysis.
Conclusion
In summary, Story Maps are modern geographic storytelling tools that
make spatial information intuitive and meaningful. They are created by
integrating maps with multimedia elements on GIS platforms and are used to
inform, persuade, and engage audiences. By turning spatial data into a
narrative journey, Story Maps transform static maps into interactive,
impactful communication tools—bridging the gap between geography, data,
and human understanding.
In Geographic Information Systems (GIS), spatial data is broadly
categorized into Vector Data and Raster Data, each representing the Earth’s
features in distinct ways. The choice between them depends on the type of
phenomenon being modeled, the scale of analysis, and the nature of the data
being represented.
Vector Data
Vector data represents the Earth’s surface using discrete geometric shapes—
points, lines, and polygons—each of which corresponds to a specific spatial
4   feature with precise boundaries. It is best suited for representing objects with   [10
CO- 2, 3 A   fixed locations and defined shapes, such as buildings, roads, or property
]
BL-4, 5   boundaries. Vector data is coordinate-based, storing data as pairs of latitude
and longitude values.
Types of Vector Data:
1. Point Data: Represents features with a specific, single location and no
area—for example, wells, trees, streetlights, or survey stations.
2. Line (Polyline) Data: Represents linear features with length but
negligible width, such as rivers, roads, railways, or power lines.
3. Polygon Data: Represents area-based features with well-defined
boundaries, such as lakes, land parcels, forest zones, or
administrative boundaries.
********** 12 **********
--- page 13 ---
Example:
A city map showing the layout of roads (lines), buildings (polygons), and
bus stops (points) uses vector data. Each element carries attribute
information—for instance, road names, building heights, or bus stop
capacities—stored in attribute tables linked to the geometry.
Advantages of Vector Data:
• Highly precise for defining boundaries and coordinates.
•   Efficient for thematic mapping, spatial queries, and network
analysis (like route optimization).
•   Requires less storage for discrete features.
Raster Data
Raster data, in contrast, represents the Earth’s surface as a grid of cells
(pixels), where each cell holds a value corresponding to a particular attribute
such as temperature, elevation, or land cover type. Raster data is ideal for
representing continuous phenomena—features that change gradually over
space rather than having fixed boundaries.
Each pixel in a raster grid has a uniform size and value, and the spatial
resolution depends on pixel size—smaller pixels mean higher resolution and
more detail. Raster data is commonly derived from satellite imagery, aerial
photographs, or digital elevation models (DEMs).
Types of Raster Data:
1. Continuous Data: Represents smoothly varying phenomena, such as
temperature gradients, elevation, rainfall, or pollution
concentration.
2. Discrete Data (Categorical): Represents distinct, classified zones,
such as land use categories, soil types, or vegetation cover.
Example:
A Digital Elevation Model (DEM) represents terrain elevation as a grid of
values, where each cell records the height above sea level. Similarly, a
satellite image representing vegetation health using Normalized Difference
Vegetation Index (NDVI) is another example of raster data.
Advantages of Raster Data:
•   Well-suited for modeling and analyzing continuous surfaces.
•   Ideal for remote sensing, image processing, and terrain modeling.
•   Easily integrated with mathematical and statistical analyses.
Comparison Summary
********** 13 **********
--- page 14 ---
Aspect   Vector Data   Raster Data
Points, lines, polygons with   Grid of equally
Data Structure
coordinates   sized cells (pixels)
Continuous
Discrete objects with defined   phenomena
Best For
boundaries   varying across
space
Temperature,
Examples   Roads, land parcels, rivers, cities   elevation, satellite
imagery
Larger file sizes
Storage   Compact for discrete features   for high-resolution
data
High—coordinates define exact   Depends on pixel
Precision
boundaries   resolution
Common   TIFF, GRID,
Shapefiles (.shp), GeoJSON, KML
Formats   JPEG, IMG
Remote sensing,
Urban planning, cadastral mapping, environmental
Common Uses
network analysis   modeling, terrain
analysis
GeoAI, or Geospatial Artificial Intelligence, is an emerging field that
combines Geographic Information Systems (GIS), artificial intelligence
(AI), and machine learning (ML) to analyze, interpret, and predict spatial
patterns and relationships on the Earth’s surface. In simple terms, GeoAI
enhances traditional GIS by enabling automated learning from spatial data,
improving the accuracy, speed, and intelligence of geospatial analysis. It
uses advanced computational techniques—such as deep learning, neural
networks, and predictive modeling—to extract meaningful insights from
massive amounts of spatial data like satellite imagery, drone captures, LiDAR
scans, and sensor networks.
Concept of GeoAI
[10
B
At its core, GeoAI integrates AI’s data-driven learning capabilities with   ]
GIS’s spatial analysis power. Traditional GIS tools rely heavily on human-
defined rules and spatial queries, while GeoAI systems learn from examples
and patterns in data to make predictions or classifications automatically. For
instance, GeoAI can be trained to recognize land-use types, detect urban
growth, or identify deforestation areas from satellite imagery without manual
digitization.
GeoAI works by applying machine learning algorithms to spatial datasets,
often in conjunction with big data analytics and cloud computing. These
systems can process and interpret vast datasets with both spatial and temporal
dimensions. The workflow generally includes:
1. Data Preparation: Collecting and preprocessing geospatial data such
as imagery, elevation models, and vector layers.
********** 14 **********
--- page 15 ---
2. Model Training: Using labeled data to train an AI model to recognize
specific spatial features or patterns.
3. Prediction and Classification: Applying the trained model to new
datasets to automatically identify, classify, or predict features.
4. Visualization and Validation: Displaying results on maps and
validating accuracy through field verification or statistical methods.
GeoAI in ArcGIS Pro
ArcGIS Pro, Esri’s advanced desktop GIS platform, has fully integrated
GeoAI capabilities through its “Deep Learning” and “Machine Learning”
toolsets, allowing users to automate complex spatial analyses and feature
extractions. These tools are part of the ArcGIS Image Analyst, Spatial
Analyst, and ArcGIS Pro AI frameworks, and they connect seamlessly with
ArcGIS Online and ArcGIS Living Atlas for cloud-based processing.
Key GeoAI Features in ArcGIS Pro:
1. Deep Learning Tools:
o Tools like “Train Deep Learning Model,” “Detect Objects
Using Deep Learning,” and “Classify Pixels Using Deep
Learning” enable users to train custom neural networks to
identify objects such as roads, buildings, or vehicles from
imagery.
o Example: Automatically mapping damaged buildings after an
earthquake using satellite imagery and convolutional neural
networks (CNNs).
2. Machine Learning Classification:
o ArcGIS Pro supports ML algorithms like Random Forest,
Support Vector Machine (SVM), and Decision Trees for
land cover classification, change detection, or clustering.
o Example: Classifying land cover types (forest, urban, water,
agriculture) from multi-spectral imagery for environmental
monitoring.
3. Predictive Modeling and Spatial Analysis:
o GeoAI in ArcGIS uses regression, clustering, and neural
networks to model spatial phenomena—such as predicting
traffic congestion, disease spread, or urban heat islands.
o Example: Using GeoAI to predict flood risk zones by
combining topographic, hydrological, and rainfall data.
4. Integration with Python and Deep Learning Frameworks:
o ArcGIS Pro’s integration with Python (ArcPy) and AI libraries
such as TensorFlow, PyTorch, and Keras allows users to
design custom AI models directly within GIS workflows.
Practical Examples of GeoAI Applications
********** 15 **********
--- page 16 ---
1. Environmental Monitoring: Detecting illegal mining or deforestation
by training models on historical imagery to spot changes in vegetation
patterns.
2. Urban Planning: Using AI to identify informal settlements or predict
urban sprawl, helping planners manage infrastructure growth more
efficiently.
3. Disaster Management: Rapid damage assessment after floods,
hurricanes, or earthquakes through automated image classification,
allowing faster response and recovery planning.
4. Transportation Analysis: Predicting traffic congestion patterns and
optimizing routes using real-time GPS and sensor data integrated with
AI-driven prediction models.
5. Agriculture: Monitoring crop health and predicting yield based on
satellite imagery and weather data using machine learning algorithms.
Attribute Measurement Levels are fundamental to how data is stored,
analyzed, and interpreted in a Geographic Information System (GIS). They
define the type of information represented by an attribute and determine
which mathematical, statistical, and spatial operations can be validly
performed on it. Understanding attribute measurement levels is essential
because GIS integrates both spatial data (location) and attribute data
(descriptive information)—and analyzing them correctly depends on treating
each attribute according to its measurement level.
The Four Levels of Attribute Measurement in GIS
1. Nominal Level (Categorical Data):
o Represents data that classify features into distinct categories
with no inherent order or ranking.
o Examples: Land use type (residential, commercial, forest), soil
5   [10
type, or road names.
CO-1, 2   A
o Operations possible: Equality or inequality checks (e.g., “Is   ]
BL-3
this area forest or not?”).
o Usefulness in GIS: Used for thematic mapping, symbol
classification, and overlay operations where categories are
compared or grouped.
2. Ordinal Level:
o Represents data with a logical order or ranking, but without
consistent intervals between ranks.
o Examples: Land suitability ratings (high, medium, low), soil
erosion severity (slight, moderate, severe).
o Operations possible: Comparisons such as greater than or less
than, but not arithmetic operations (e.g., "high" minus "low" is
meaningless).
o Usefulness in GIS: Applied in ranking analyses, such as
environmental vulnerability assessment or suitability modeling.
3. Interval Level:
o Represents numeric data where the difference between values
is meaningful, but there is no true zero point.
********** 16 **********
--- page 17 ---
o Examples: Temperature in Celsius or Fahrenheit, years in time
series.
o Operations possible: Addition and subtraction (e.g.,
calculating temperature difference).
o Usefulness in GIS: Suitable for change detection, trend
analysis, and temporal modeling, such as comparing
temperature changes over time or between locations.
4. Ratio Level:
o Represents numeric data with equal intervals and a true zero,
allowing all mathematical operations.
o Examples: Elevation, rainfall, population density, distance, or
area.
o Operations possible: Addition, subtraction, multiplication, and
division. Ratios and percentages are meaningful (e.g., “This
area receives twice as much rainfall”).
o Usefulness in GIS: Used in quantitative spatial analyses such
as hydrological modeling, slope analysis, or spatial
interpolation.
Use and Usefulness of Attribute Measurement Levels in GIS
1. Ensuring Analytical Accuracy:
Each measurement level dictates which operations are valid. For
instance, arithmetic operations are meaningful for ratio data but not
for ordinal or nominal data. Misclassifying data (e.g., treating land
use types as numeric values) can lead to false or misleading results.
2. Appropriate Data Representation and Visualization:
In GIS mapping, attribute levels determine the symbology and
visualization technique used:
o Nominal data use unique colors or patterns to differentiate
categories.
o Ordinal data use graduated color ramps to indicate rank or
intensity.
o Interval and ratio data use continuous color gradients for
quantitative representation (e.g., elevation or rainfall maps).
3. Facilitating Spatial Analysis and Modeling:
Many GIS functions—like buffering, overlay analysis, interpolation,
and suitability modeling—require an understanding of measurement
levels to apply appropriate operations. For example, a weighted
overlay analysis in suitability modeling combines multiple raster
layers, each standardized according to its measurement scale (often
ordinal or ratio).
4. Improving Data Integration and Interoperability:
When combining datasets from different sources (e.g., census data with
land cover maps), knowing each attribute’s measurement level ensures
consistent scaling, reclassification, and data compatibility, avoiding
analytical bias.
5. Supporting Statistical and Machine Learning Applications:
In advanced GIS workflows such as GeoAI and spatial statistics,
recognizing attribute measurement levels allows for the correct choice
of algorithms and models. For example, categorical (nominal) data
********** 17 **********
--- page 18 ---
require classification models, while ratio data can feed into regression
or predictive models.
Example
Consider a land suitability analysis for agriculture:
• Nominal data: Land use categories (forest, agriculture, urban).
• Ordinal data: Soil fertility ranking (low, medium, high).
• Ratio data: Annual rainfall (in mm) and elevation (in meters).
Each layer is processed according to its measurement level—reclassified,
normalized, and weighted—before being combined to generate a final
suitability map. Incorrectly treating nominal or ordinal attributes as numeric
could distort results, showing unsuitable areas as highly suitable.
Conclusion
In essence, Attribute Measurement Levels are the foundation of data
accuracy, analysis integrity, and visualization quality in GIS. They
determine how data can be manipulated, interpreted, and displayed.
Understanding the differences between nominal, ordinal, interval, and ratio
data ensures that spatial analyses yield reliable insights, enabling GIS
professionals to make scientifically valid, data-driven decisions in planning,
environmental management, and geospatial modeling.
What is a Graticule?
A graticule is a network of intersecting lines representing latitude and
longitude on maps and globes, used to define the precise geographic location
of any point on Earth. It forms the foundation of the geographic coordinate
system, helping in measuring and locating positions through angular distance.
The lines of the graticule are imaginary great circles drawn on the Earth’s
surface to represent coordinates in degrees (°), minutes (′), and seconds (″).
• Lines of Latitude (Parallels):   [10
B   These are horizontal lines that run east–west around the Earth, parallel
]
to the Equator. They measure angular distance north or south of the
Equator, ranging from 0° at the Equator to 90° at the poles.
Important parallels include the Tropic of Cancer (23.5° N), Tropic of
Capricorn (23.5° S), and Arctic/Antarctic Circles (66.5° N/S).
• Lines of Longitude (Meridians):
These are vertical lines that run from the North Pole to the South
Pole, converging at both poles. They measure angular distance east or
west of the Prime Meridian (0° longitude), which passes through
Greenwich, England, up to 180° east and west.
********** 18 **********
--- page 19 ---
Together, these lines form a global grid that allows for the identification of
exact geographic coordinates—for example, Mumbai, India, is located
approximately at 19.07° N latitude and 72.87° E longitude.
Importance of Graticules in Cartography and GIS:
• They provide a reference framework for mapping and navigation.
• Help in accurately projecting the curved Earth onto flat maps.
• Enable spatial analysis in GIS by linking data to real-world
geographic locations.
•   Useful in creating gridded reference maps, global climate models,
and remote sensing datasets.
In digital GIS applications (like ArcGIS or QGIS), graticules can be added as
overlays to maps for orientation, allowing users to visualize data within real-
world geographic coordinates.
What is Geo-referencing of Data?
Geo-referencing is the process of assigning real-world geographic
coordinates (latitude and longitude or projected coordinates like UTM) to
spatial data—such as maps, satellite images, or drawings—so that it aligns
correctly with other geographically referenced data. It essentially transforms a
non-spatial image (like an old paper map) into spatially accurate, GIS-ready
data that can be overlaid with other modern datasets.
In simpler terms, geo-referencing connects an image or map to its true
geographic position on Earth, enabling it to be used for spatial analysis,
digitization, and mapping.
Applications of Geo-referencing:
•   Integrating scanned maps, aerial photos, or CAD drawings into a GIS
environment.
•   Aligning historical maps with modern satellite imagery for land-use
change detection.
• Enabling the extraction of geographic features (roads, rivers,
boundaries) from old maps.
•   Supporting heritage conservation and archaeological studies through
temporal analysis.
How Can an Antique Map Be Geo-referenced?
Geo-referencing an antique or historical map involves aligning it with modern
coordinate systems using identifiable reference points. The general steps
include:
1. Scanning the Map:
The antique map is scanned using a high-resolution scanner to
********** 19 **********
--- page 20 ---
produce a digital image (e.g., TIFF or JPEG). This converts the paper
map into a format compatible with GIS software.
2. Importing into GIS Software:
The scanned image is loaded into a GIS platform such as ArcGIS Pro
or QGIS, where it is displayed as a raster layer without any geographic
reference initially.
3. Identifying Control Points (Ground Control Points - GCPs):
Select well-known and identifiable locations that appear on both the
antique map and a modern reference map (e.g., river confluences,
mountain peaks, road intersections, or historic landmarks).
o These GCPs serve as anchors for aligning the old map to the
correct position on Earth.
4. Assigning Real-World Coordinates:
Using the GIS Geo-referencing tool, assign the corresponding
latitude and longitude (or UTM coordinates) to each control point.
The more evenly distributed and accurate these points are, the better
the alignment.
5. Transformation and Resampling:
The software then performs a mathematical transformation—such as
Affine, Polynomial, or Spline transformation—to warp the antique
map image to fit the chosen coordinate system.
o Affine transformation preserves straight lines and parallelism,
often sufficient for small distortions.
o Polynomial or Spline transformations handle more complex
distortions due to aging or stretching of old paper maps.
6. Saving and Verification:
The geo-referenced image is saved as a GeoTIFF or other spatially
enabled format. Its accuracy is verified by checking the alignment of
major features (like rivers or city boundaries) with modern map layers.
Example
An 18th-century colonial map of Mumbai may be geo-referenced to study
how the city’s coastline and land use have changed over centuries. Historical
features like forts or old roads can be matched with modern landmarks or
coastlines visible on satellite imagery. Once geo-referenced, the map can be
analyzed spatially—revealing urban expansion, reclaimed land areas, or
changes in drainage patterns.
Conclusion
In summary, a graticule provides the essential coordinate framework that
defines positions on Earth, while geo-referencing is the process of aligning
spatial data (like antique maps or aerial photos) with that framework. Geo-
referencing gives historical or analog maps new life within digital GIS
systems, allowing them to be analyzed, compared, and integrated with
modern geospatial data for research, planning, and preservation purposes.
********** 20 **********
--- page 21 ---
Using GIS to Optimize the Education Sector – A Case Study Approach
Geographic Information Systems (GIS) have become powerful tools in
transforming how educational systems are planned, managed, and made
more accessible, particularly in regions with geographic or socioeconomic
disparities. By integrating spatial data with demographic, economic, and
institutional information, GIS helps policymakers and educators make data-
driven decisions about the placement, accessibility, and performance of
educational institutions.
A notable example is the “School Mapping and Location Analysis Project”
carried out by UNICEF and the Indian Ministry of Education in several
states of India, including Uttar Pradesh and Assam. The project aimed to
ensure that every child had a school within a reasonable distance from
home. Using GIS, data was collected on the locations of existing schools,
student populations, road connectivity, and demographic density. Spatial
analysis revealed areas where schools were clustered too close together and
regions where entire communities lacked access to nearby educational
facilities.
By overlaying population maps with road and transportation networks,
authorities identified “education deserts”—zones underserved by schools.
Buffer and network analyses were performed to determine the travel time and
6   distance between households and schools, accounting for terrain and road   [10
CO-3   A   conditions. The insights guided the strategic establishment of new schools,
]
BL-3, 4   upgradation of existing facilities, and optimization of resource
allocation—ensuring that every region received equitable access to education.
This spatially enabled planning not only improved enrollment rates but also
reduced school dropout in remote and rural communities.
How GIS Can Make College Exploration Accessible to Students from
Remote Areas
GIS technology can also revolutionize college exploration and higher
education accessibility by bridging the information gap between students
and institutions, especially for those in remote, far-flung regions. Many
students in rural or geographically isolated areas lack awareness of the
colleges, courses, scholarships, and career opportunities available to them.
A GIS-based College Explorer Platform can solve this issue through
spatially interactive and data-integrated tools.
Here’s how it works:
1. Creation of a GIS-Based College Database:
All higher education institutions (universities, colleges, vocational
centers) are mapped as point features on a digital map. Each
institution is tagged with attribute data—including available
********** 21 **********
--- page 22 ---
programs, admission requirements, faculty, facilities, scholarship
options, and placement statistics.
2. Interactive Online Map Interface:
Students can access an interactive GIS dashboard that allows them to
search colleges by course, location, ranking, or specialization. For
example, a student from a remote village in Himachal Pradesh can
explore engineering or nursing colleges within a 200 km radius, along
with transportation routes, hostel facilities, and nearby towns.
3. Accessibility and Connectivity Analysis:
GIS performs network analysis to calculate the nearest and most
accessible institutions based on travel distance, road connectivity, and
public transport availability. It can display isochrones (time-based
accessibility zones) to show which colleges are reachable within, say, 1
or 2 hours of travel.
4. Socioeconomic and Demographic Integration:
Layers showing literacy rates, population age groups, and income
levels help identify where educational outreach programs or digital
learning hubs should be established. Policymakers can focus
resources on underserved areas to reduce inequality in access to higher
education.
5. Mobile and Offline Access:
Through mobile GIS apps or progressive web maps, students in areas
with limited internet access can still download offline maps showing
colleges and educational resources near them.
6. Real-Time Data and Career Guidance:
Geo-linked data layers can integrate job market trends and industry
clusters, helping students understand which regions offer better
prospects for their chosen field of study. For instance, a student
interested in biotechnology can visualize how colleges in Pune or
Bengaluru are geographically linked to research centers and biotech
industries.
Practical Example – India’s National Education GIS (NEGIS)
The National Education GIS (NEGIS) initiative, spearheaded by India’s
Ministry of Education, is an ongoing real-world example of how GIS is
being leveraged to digitize and democratize educational data. NEGIS
consolidates spatial information about schools, colleges, teacher distribution,
student enrollment, and infrastructure quality across the country. It
provides policymakers and citizens with map-based visualization tools for
planning new institutions and identifying underserved regions. For students,
NEGIS can evolve into an interactive education map portal, allowing them
to locate institutions, access admission information, and plan their educational
journey through a spatial lens.
Use of GIS in Insurance and Reinsurance Strategies – A Case Study
Approach   [10
B
]
Geographic Information Systems (GIS) play a transformative role in the
insurance and reinsurance industries, helping companies analyze, manage,
********** 22 **********
--- page 23 ---
and mitigate risks that are inherently spatial in nature. Every insured asset—
whether it’s a house, factory, farm, or vehicle—exists in a geographic location
exposed to different environmental, climatic, and socioeconomic conditions.
GIS integrates spatial data with insurance models to assess risk exposure,
calculate premiums, plan reinsurance strategies, and manage disaster
recovery operations.
Case Study: GIS in Catastrophe Risk Management – Munich Re and
Hurricane Katrina
A practical example of GIS in insurance can be seen in how Munich Re, one
of the world’s largest reinsurance companies, used GIS-based catastrophe
modeling to evaluate and manage losses during and after Hurricane Katrina
(2005).
Before the event, Munich Re’s risk modeling team used GIS-based hazard
maps that incorporated data on hurricane tracks, wind speeds, storm
surges, and flood-prone areas along the Gulf Coast of the United States.
Each policyholder’s asset—ranging from residential properties to industrial
plants—was mapped in relation to these hazard zones. GIS helped the
company visualize clusters of high-risk properties, enabling them to adjust
premiums, underwriting policies, and reinsurance coverage levels
accordingly.
When Hurricane Katrina struck, GIS technology was used for real-time
damage assessment and loss estimation. Satellite imagery, weather radar
data, and aerial photos were overlaid on insured property maps to identify
areas of maximum impact. This allowed rapid estimation of total insured
losses, prioritization of claims verification, and more efficient coordination
between insurers and reinsurers. Post-disaster, GIS helped refine risk models
by comparing predicted losses with actual damages, improving future
catastrophe reinsurance pricing and portfolio diversification.
How GIS Supports Insurance and Reinsurance Strategies
1. Risk Assessment and Underwriting:
GIS allows insurers to map and analyze risk exposure based on
geographic hazards such as floods, earthquakes, cyclones, or wildfires.
By overlaying hazard maps with property locations, companies can
determine vulnerability zones and set premiums accordingly.
o Example: Insurers in Japan use GIS to map buildings near
seismic fault lines to determine earthquake coverage rates.
2. Portfolio Management and Diversification:
Reinsurers use GIS to visualize geographic concentrations of insured
assets across multiple countries or regions. This helps prevent
overexposure in one high-risk zone. For instance, a reinsurer might
diversify coverage by reducing the number of coastal properties
insured against hurricanes in Florida while increasing inland portfolios.
********** 23 **********
--- page 24 ---
3. Claims Management and Fraud Detection:
After a disaster, GIS helps insurers identify actual affected areas
using post-event imagery. This enables quick claims validation and
helps detect false claims from regions unaffected by the event.
o Example: During the 2019 Kerala floods, Indian insurance
firms used GIS and drone imagery to verify agricultural
damage before disbursing payouts under crop insurance
schemes.
4. Premium Pricing and Predictive Modeling:
Spatial analytics in GIS can identify correlations between
environmental conditions and historical claim frequencies,
allowing predictive modeling of risk. Insurers can adjust pricing
dynamically based on real-time hazard data such as rainfall or
cyclone forecasts.
5. Reinsurance Strategy Optimization:
GIS enables reinsurers to visualize global risk exposure, helping them
design treaties that balance coverage across various perils and regions.
For instance, reinsurance treaties for flood and cyclone risks can be
tailored geographically to ensure balanced risk transfer and capital
efficiency.
How GIS Mapping Helps During Disasters
During disasters, GIS serves as a decision-support tool for insurers,
reinsurers, and emergency managers.
1. Real-Time Disaster Monitoring:
GIS integrates live feeds from satellites, sensors, and meteorological
agencies to monitor storm paths, flood extents, or wildfire spreads.
Insurers can track which policyholders are in harm’s way and pre-
emptively alert them or deploy emergency support.
2. Damage Assessment and Rapid Response:
After a disaster, GIS combines before-and-after satellite imagery to
map the extent of destruction. Insurers use this data to prioritize
claims processing in the most affected zones and estimate the total
financial exposure almost immediately.
o Example: After the 2011 Japan tsunami, GIS mapping helped
insurance companies estimate damage to coastal properties
within days, expediting claims settlement.
3. Recovery Planning and Risk Mitigation:
Post-disaster, GIS analysis identifies areas repeatedly hit by hazards,
guiding zoning regulations, reconstruction planning, and insurance
coverage adjustments. This helps reduce future risk and supports
resilience planning.
4. Integration with Emergency Services:
Insurance firms often collaborate with government agencies using GIS
dashboards to coordinate relief, rescue, and rehabilitation operations.
Shared maps showing infrastructure damage, policyholder clusters,
and accessibility routes improve efficiency and transparency.
********** 24 **********
--- page 25 ---
FI ICR AC KH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 7278098b2180

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_DS_7009/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
The Survey of India produces detailed topographic maps that include key components
such as scale, contour lines, relief features, drainage patterns, settlements,
transportation networks, vegetation, grid/reference system, and map legend.
These maps provide a comprehensive representation of both natural and cultural
features. In a GIS environment, certain components can be easily generated using
geoprocessing tools—for example, contours can be derived from Digital Elevation
Models (DEMs) using contour generation tools, and drainage networks can be created
through hydrological analysis by processing elevation data to extract flow direction and
stream networks. Regarding lines on the Earth’s surface, a great circle is the shortest
path between two points on a sphere (used in aviation routes), a rhumb line
(loxodrome) maintains a constant bearing or direction but is longer than a great circle,
and a small circle is any circle on the globe whose plane does not pass through the
CO-1   Earth’s center, often representing lines of latitude other than the equator.   (5)
a
BL: 3
A bar scale (graphic scale) represents map distance using a visual line divided into
segments marked with real-world units, allowing users to directly measure distances
CO-1   on the map. Its key function is that it remains accurate even if the map is resized,   (5)
b
BL:4   because it scales proportionally with the map itself, making it highly reliable for
practical use. In contrast, a relative scale (representative fraction, e.g., 1:50,000)
expresses the ratio between map distance and ground distance numerically, but it
********** 1 **********
--- page 2 ---
becomes inaccurate if the map is enlarged or reduced, since the ratio no longer holds
true. For small-scale maps (covering large areas with less detail), a bar scale is best
suited because such maps are often reproduced or viewed at different sizes, and the bar
scale continues to provide correct distance measurements despite these changes.
Given the scale 2 cm : 1500 km, first find the map distance per km:
2
= 0.001333 cm per km
1500
Now multiply by the actual ground distance:
2376 × 0.001333 = 3.168 cm
Final Answer: The map distance will be 3.168 cm (≈ 3.17 cm).
Geospatial data refers to data that is linked to a specific location on the Earth’s
surface using coordinates such as latitude and longitude, enabling it to be mapped,
analyzed, and visualized in a GIS environment. The difference between information
and geo-information lies in the spatial component—information is general processed
data that conveys meaning (e.g., population figures), whereas geo-information includes
a geographic reference, allowing that information to be tied to a specific place (e.g.,
population of Mumbai mapped spatially). The concepts of space and time in layer
coverage are central to GIS analysis: space refers to how geographic features are
distributed and organized across different layers (such as roads, land use, or elevation),
while time refers to changes in these layers over periods, enabling temporal analysis.
By combining spatial and temporal dimensions, GIS can track patterns such as urban
growth, climate change, or land-use transformation, making layer-based coverage a
powerful tool for dynamic geographic analysis.
CO-2   c   (5)
BL: 3
The hierarchical model organizes non-spatial data in a tree-like structure, where data
is arranged in parent–child relationships, with a single root node at the top and multiple
levels of dependent records beneath it. Each child record is linked to only one parent,
creating a one-to-many relationship that ensures a clear and structured data path. Data
CO-1   is accessed by traversing this hierarchy from the root through predefined links, making   (5)
d
BL: 3   retrieval efficient when relationships are well defined. Key features of this model
include simplicity of structure, data integrity through strict relationships, fast
access for hierarchical queries, and data dependency, where child records cannot
exist without a parent. However, it is less flexible for complex relationships, especially
many-to-many connections, as it requires data duplication or restructuring.
********** 2 **********
--- page 3 ---
Q2   Answer any (4)
In ArcGIS Pro, geodatabases are important because they provide a centralized and
structured system for storing spatial and attribute data. They allow efficient data
management, support large datasets, and enable advanced functionalities such as
topology rules, relationships, and data validation. This makes geodatabases essential
for organizing complex GIS projects and ensuring consistency and accuracy in analysis.
Feature Classes are collections of similar geographic features stored within a
geodatabase and represented as points, lines, or polygons. For example, in a tourism
project, point feature classes can represent tourist spots, line feature classes can
represent trekking routes, and polygon feature classes can represent protected areas or
regions.
Feature Data Sets are groups of related feature classes that share a common coordinate
system, allowing them to be analyzed together seamlessly. In a Tourism in the
Himalayas project, a feature dataset (e.g., “Himalayan Tourism”) could include feature
classes such as trekking trails, tourist attractions, and forest zones. These datasets can
be added to the geodatabase and used collectively for spatial analysis like route
planning, accessibility studies, and environmental impact assessment.
a   [10]
1
CO-2, 2
BL- 4, 6
Intersection is a topology-based overlay operation in GIS that creates a new vector
layer containing only the areas or parts of features that are spatially common to all input
b   layers. It affects the geometry of vector features by cutting them wherever they overlap   [10]
and retaining only the shared portion. Step by step, the GIS first takes two or more input
layers, such as land parcels and utility service zones in a smart city system. It then
********** 3 **********
--- page 4 ---
compares their geometries, detects where they overlap, and splits the original polygons,
lines, or points at those overlap boundaries. A new output layer is generated that
contains only the intersecting geometry, while the attributes from all input layers are
combined in the result. For example, in a smart city system, intersection can be used to
identify which buildings fall within both a high-energy-consumption zone and a
proposed underground cable upgrade corridor, helping planners focus only on the
common area requiring intervention.
Union is another topology-based overlay operation in GIS that combines the full spatial
extent of all input polygon layers into one output layer. It affects vector geometry by
merging the boundaries of all input features and subdividing the space into new
polygons based on every overlap and non-overlap area. Step by step, the GIS begins
with two polygon layers, such as land use zones and municipal service districts in a
smart city project. It overlays the layers, identifies all boundaries and intersections, and
then splits the entire mapped area into smaller polygons wherever any boundary crosses
another. Unlike intersection, union keeps all areas from both layers, whether they
overlap or not, and transfers the attributes from each input layer into the output table.
In a smart city system, union can be used to combine flood-risk zones with road
maintenance wards so that planners can see the entire city broken into smaller
management units, showing where flood risk and maintenance responsibility coincide
as well as where they do not.
These operations are important because they directly change the geometry of vector
features. Intersection reduces geometry to only shared spaces, while union expands
and reorganizes geometry to include all spaces from all inputs. In practical GIS
analysis, this means original parcels, roads, or service areas may be cut into many
smaller pieces, each carrying new attribute combinations. In a smart city context, such
geometry changes are extremely useful for integrated planning, because urban systems
such as utilities, transport, hazard zones, and land use often overlap in complex ways,
and topology operations make those relationships visible and analysis worthy.
Small-scale maps represent large geographic areas with less detail (e.g., world or
country maps), while large-scale maps represent smaller areas with greater detail
2   (e.g., city or neighborhood maps). Small-scale maps are best suited for regional or [10]
CO-1, 2   a
global analysis, trend identification, and comparisons across large areas, whereas
BL- 4, 6
large-scale maps are ideal for detailed, local-level analysis such as infrastructure
planning, site selection, and resource management.
********** 4 **********
--- page 5 ---
For a map of tourist towns in a state of India, a large-scale map would be easier to
use because it provides sufficient detail to locate towns accurately, understand
connectivity, and analyze accessibility within the state. In contrast, for a map of
leopard populations in the world, a small-scale map is more appropriate as it helps
visualize global distribution patterns and compare populations across continents
without requiring fine local detail.
Choropleth maps are thematic maps that represent data using different colors or
shading for predefined areas such as states, districts, or countries. They are created
by first collecting attribute data (e.g., population density or literacy rate), linking it to
geographic boundaries, classifying the data into ranges (using methods like equal
interval or quantiles), and then assigning color gradients where darker or more intense
colors represent higher values. Choropleth maps are widely used in applications such
as demographic analysis (population, literacy) and environmental studies (rainfall,
forest cover), as they effectively communicate spatial patterns and variations across
regions.
The Geoid and Datum are important in cartography because they define how the
Earth’s shape and position are represented. The geoid represents the Earth’s true,
b   irregular shape based on gravity and mean sea level, making it important for accurate   [10]
elevation measurements. A datum is a mathematically defined reference system (based
on an ellipsoid) used to locate positions on the Earth’s surface. Together, they ensure
that spatial data is accurately positioned and consistent across maps and GIS systems.
The least distortion in any map projection occurs along the line or point of contact
between the projection surface and the Earth, such as the equator in cylindrical
projections, standard parallels in conical projections, or the center point in azimuthal
projections. This is because distortion increases as one moves away from the area of
contact, making those regions the most accurate.
If studying topography in Greenland, an azimuthal projection (specifically a polar
azimuthal projection) would be most suitable because Greenland lies in high latitudes
near the pole. This projection minimizes distortion in polar regions and provides a more
accurate representation of shapes, distances, and terrain features compared to
cylindrical projections, which heavily distort polar areas.
********** 5 **********
--- page 6 ---
The spaghetti data model is a simple vector data structure in which points, lines, and
polygons are stored as independent geometries without explicit topological
relationships between them. In the context of pandemic management (such as
COVID-19), this model can be used to map locations like hospitals, containment
zones, testing centers, and movement paths of individuals. However, since it lacks
connectivity and adjacency information, it may lead to redundancy and makes
complex analyses (like tracking spread through connected networks or containment
boundaries) less efficient. It is useful for basic visualization and rapid mapping during
early stages of a pandemic but less suitable for advanced spatial analysis.
A polygon-on-line overlay operation involves analyzing how polygon features
interact with line features. Step by step, the GIS takes a polygon layer (e.g.,
administrative zones or containment areas) and a line layer (e.g., roads or utility
lines), identifies where the lines pass through or intersect the polygons, and then splits
the lines at polygon boundaries. The resulting line segments inherit attributes from
both the original line and the polygon they fall within. This operation is useful for
understanding how linear networks behave across different regions—for example,
identifying which road segments pass through high-risk COVID containment zones
for movement control or sanitation planning.
3
CO-2, 3   a   [10]
BL-4, 5
The connection between IoT (Internet of Things) and GIS lies in the integration of
real-time spatial data collection and analysis. IoT devices such as sensors, GPS
trackers, and smart meters continuously collect location-based data (e.g., temperature,
air quality, traffic flow), which is then fed into GIS platforms for mapping and
analysis. This integration enables dynamic monitoring and decision-making—for
instance, tracking patient movement during a pandemic, monitoring crowd density, or
managing smart city infrastructure. GIS provides the spatial context and visualization,
while IoT supplies continuous, real-time data, making the combination powerful for
applications like urban management, environmental monitoring, and disaster
response.
********** 6 **********
--- page 7 ---
Story Maps are interactive GIS-based presentations that combine maps, text, images,
videos, and multimedia to communicate spatial information in a narrative format.
They can be created using tools like ArcGIS StoryMaps by first preparing map layers
(such as trails, elevation, viewpoints), then adding descriptive content, images, and
route details into a structured story layout. For a trekking route, a Story Map can
include the trail path, altitude profiles, campsites, risk zones, and scenic viewpoints,
b   along with photos and safety instructions, allowing users to virtually experience the   [10]
journey. In a university campus management system, Story Maps can be used to
showcase campus infrastructure, navigation routes, emergency facilities, and
development plans. For example, a Story Map can guide new students through
departments, hostels, and amenities, or help administrators present campus expansion
projects interactively.
Raster datasets can be downloaded from several reliable global and national data
portals. Common sources include the USGS EarthExplorer for satellite imagery and
DEMs, NASA Earthdata for climate and remote sensing datasets, and India’s ISRO
Bhuvan platform for Indian geospatial data. Other sources include Copernicus (Sentinel
data) and open data repositories that provide elevation, land cover, and environmental
raster datasets used in GIS analysis.
Vector operators are spatial analysis tools used to manipulate and analyze vector data.
The main kinds include buffering (creating zones around features), overlay operations
such as intersection, union, and clip (combining or extracting spatial relationships),
a   merge and dissolve (combining features), and spatial join (linking attributes based on [10]
spatial relationships). These operators help in analyzing proximity, connectivity, and
spatial relationships between geographic features.
Latitudes and longitudes are components of the map projection graticule that form the
Earth’s coordinate system. Latitudes are horizontal lines running east–west that
measure angular distance north or south of the equator, while longitudes are vertical
lines running from pole to pole that measure angular distance east or west of the Prime
Meridian. Together, they create a grid that enables precise location referencing and
mapping on the Earth’s surface.
4   GeoAI in ArcGIS Pro enables advanced analysis by integrating machine learning and
CO- 2, 3   deep learning directly into GIS workflows. For image classification, GeoAI can
BL-4, 5   categorize satellite or aerial imagery into land-use or land-cover classes (e.g., urban,
vegetation, water) using supervised or unsupervised learning. For object detection,
deep learning models (such as convolutional neural networks) can automatically
identify and locate features like buildings, roads, vehicles, or trees from high-resolution
imagery. For spatial prediction, machine learning algorithms can analyze
relationships between multiple spatial variables (e.g., rainfall, elevation, land use) to
predict outcomes such as flood risk, crop yield, or urban expansion. These tools are
integrated through geoprocessing toolboxes, deep learning frameworks, and Python-
based workflows within ArcGIS Pro.
b   [10]
A detailed example can be seen in urban flood risk prediction. First, spatial datasets
such as a Digital Elevation Model (DEM), rainfall data, drainage networks, and land-
use maps are collected and preprocessed in ArcGIS Pro. Next, training data is prepared
by identifying known flood-prone and non-flood-prone areas. A machine learning
model (e.g., random forest or gradient boosting) is then trained using these variables as
inputs. For object detection, deep learning can also be used to extract features like
buildings and impervious surfaces from satellite imagery, which influence runoff. Once
trained, the model is applied across the study area to generate a predictive flood risk
map, highlighting high-risk zones. The output can then be visualized, validated, and
used by planners for disaster mitigation, drainage planning, and zoning regulations,
demonstrating how GeoAI transforms raw spatial data into actionable insights.
********** 7 **********
--- page 8 ---
Several open-source GIS systems are widely used as alternatives to proprietary
platforms like ArcGIS Pro. For example, QGIS is highly popular due to its user-friendly
interface, strong plugin ecosystem, and cross-platform support, making it accessible for
both beginners and advanced users. GRASS GIS is known for its powerful analytical
and geospatial modeling capabilities, especially for raster and environmental analysis.
gvSIG offers robust desktop and mobile GIS solutions with strong support for spatial
data editing. These open-source systems are unique in that they are free to use,
customizable, and community-driven, allowing users to modify code and extend
functionality without licensing constraints. While ArcGIS Pro offers more integrated
enterprise solutions and polished tools, open-source GIS platforms provide flexibility,
transparency, and cost-effectiveness, making them widely used in academia, research,
a   and government sectors.   [10]
Point-in-polygon and polygon-on-line are spatial analysis operations that examine
relationships between different vector geometries. In a point-in-polygon operation,
point features are tested to determine whether they fall within a polygon boundary, and
the attributes of the polygon are typically assigned to the point. This is useful for tasks
like identifying which administrative region a sampling point belongs to. In contrast, a
polygon-on-line operation analyzes how polygon features interact with line features. It
identifies where lines pass through polygons and often splits the lines at polygon
boundaries, assigning polygon attributes to each resulting segment. This is useful for
understanding how linear features such as roads, rivers, or pipelines traverse different
zones, such as land use areas or risk zones.
5
CO-1, 2   In GIS, contiguity, area definition, and connectivity are key concepts that
BL-3   describe spatial relationships between features. Contiguity refers to the sharing
of common boundaries between adjacent spatial units, such as neighboring
polygons that touch each other (e.g., administrative districts sharing borders).
Area definition relates to how polygons are formed using closed boundaries to
represent discrete spatial units like land parcels, forest patches, or zones,
ensuring that each area is uniquely identified and properly enclosed.
Connectivity describes how linear features are linked together in a network,
such as roads, rivers, or pipelines, allowing analysis of flow, movement, and
routing. Together, these concepts form the basis of topological relationships in
GIS and are essential for accurate spatial analysis.
b   [10]
Coverage resolution in terms of coordinate precision refers to the level of
detail and accuracy with which spatial data is represented based on the precision
of its coordinate values. Higher coordinate precision (more decimal places or
finer units) allows features to be represented more accurately, resulting in higher
resolution and more detailed spatial analysis. Conversely, lower precision leads
to generalized representations and potential loss of detail. Coverage resolution
is important because it influences the accuracy of measurements, overlay
operations, and spatial modeling, ensuring that GIS outputs are reliable and
suitable for the intended scale of analysis.
GIS can greatly optimize the crime management sector by enabling spatial
analysis of crime patterns and supporting predictive policing. For example, in
6   cities like Los Angeles, law enforcement agencies have used GIS to map [10]
CO-3   a
BL-3, 4   historical crime data, identify hotspots, and analyze trends based on time,
location, and type of crime. By integrating layers such as population density,
street networks, lighting conditions, and past incident reports, GIS helps predict
********** 8 **********
--- page 9 ---
high-risk areas and allocate police patrols more efficiently. It also supports real-
time monitoring, faster emergency response, and better coordination between
departments. As a result, resources are used more effectively, and preventive
measures can be implemented in vulnerable zones.
GIS can also make college exploration accessible to students in remote and
far-flung areas by providing interactive, map-based platforms that showcase
institutions, courses, infrastructure, and facilities. Through web-based GIS
applications, students can explore campuses virtually, view locations of
departments, hostels, libraries, and transport connectivity, and even analyze
proximity to their hometowns. For instance, platforms built using tools like
ArcGIS Online can integrate multimedia content such as photos, videos, and
admission details into interactive maps. This allows students who cannot
physically visit campuses to make informed decisions about education options,
compare institutions geographically, and understand accessibility, thereby
bridging the gap between urban and remote learners.
GIS can be used to understand gender patterns in census data by mapping and
analyzing the spatial distribution of indicators such as sex ratio, literacy rates,
workforce participation, and access to amenities. For example, in Delhi, census
data has been integrated into GIS to create ward-level maps showing variations
in female literacy, employment, and sex ratio. By overlaying these with layers
like education facilities, healthcare access, and public transport, planners can
identify gender disparities and underserved areas. This helps in targeted policy
interventions, such as improving safety infrastructure, increasing access to
education, or enhancing healthcare services for women, making gender-focused
planning more data-driven and location-specific.
GIS mapping is extremely valuable during urban disasters as it provides real- [10]
b
time spatial information for effective emergency response. During events like
floods, earthquakes, or fires, GIS can map affected zones, identify vulnerable
populations, and locate critical infrastructure such as hospitals, shelters, and
evacuation routes. It enables authorities to analyze the extent of damage,
prioritize rescue operations, and allocate resources efficiently. For instance,
during urban flooding, GIS can combine rainfall data, drainage networks, and
elevation models to predict flood spread and guide evacuation planning.
Overall, GIS enhances situational awareness, coordination among agencies, and
rapid decision-making, making it an essential tool for disaster management in
cities.
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 73ca715c7534

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_IT_7001/Introduction to GIS/ANS_Introduction to GIS(702CI0I007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech (DS)/B. Tech (EXTC)/B.
Tech Intg. (CE)/B. Tech Intg. (DS)/B. Tech Intg. (IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to GIS
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Give diagrams even if not asked for.
5. Try to keep answers chronological
6. Question 1 is compulsory. Any 4 (four) from the rest of the questions in Section II
Q1   Compulsory Question   [20]
The Survey of India produces detailed topographic maps that include key components
such as scale, contour lines, relief features, drainage patterns, settlements,
transportation networks, vegetation, grid/reference system, and map legend.
These maps provide a comprehensive representation of both natural and cultural
features. In a GIS environment, certain components can be easily generated using
geoprocessing tools—for example, contours can be derived from Digital Elevation
Models (DEMs) using contour generation tools, and drainage networks can be created
through hydrological analysis by processing elevation data to extract flow direction and
stream networks. Regarding lines on the Earth’s surface, a great circle is the shortest
path between two points on a sphere (used in aviation routes), a rhumb line
(loxodrome) maintains a constant bearing or direction but is longer than a great circle,
and a small circle is any circle on the globe whose plane does not pass through the
CO-1   Earth’s center, often representing lines of latitude other than the equator.   (5)
a
BL: 3
A bar scale (graphic scale) represents map distance using a visual line divided into
segments marked with real-world units, allowing users to directly measure distances
CO-1   on the map. Its key function is that it remains accurate even if the map is resized,   (5)
b
BL:4   because it scales proportionally with the map itself, making it highly reliable for
practical use. In contrast, a relative scale (representative fraction, e.g., 1:50,000)
expresses the ratio between map distance and ground distance numerically, but it
********** 1 **********
--- page 2 ---
becomes inaccurate if the map is enlarged or reduced, since the ratio no longer holds
true. For small-scale maps (covering large areas with less detail), a bar scale is best
suited because such maps are often reproduced or viewed at different sizes, and the bar
scale continues to provide correct distance measurements despite these changes.
Given the scale 2 cm : 1500 km, first find the map distance per km:
2
= 0.001333 cm per km
1500
Now multiply by the actual ground distance:
2376 × 0.001333 = 3.168 cm
Final Answer: The map distance will be 3.168 cm (≈ 3.17 cm).
Geospatial data refers to data that is linked to a specific location on the Earth’s
surface using coordinates such as latitude and longitude, enabling it to be mapped,
analyzed, and visualized in a GIS environment. The difference between information
and geo-information lies in the spatial component—information is general processed
data that conveys meaning (e.g., population figures), whereas geo-information includes
a geographic reference, allowing that information to be tied to a specific place (e.g.,
population of Mumbai mapped spatially). The concepts of space and time in layer
coverage are central to GIS analysis: space refers to how geographic features are
distributed and organized across different layers (such as roads, land use, or elevation),
while time refers to changes in these layers over periods, enabling temporal analysis.
By combining spatial and temporal dimensions, GIS can track patterns such as urban
growth, climate change, or land-use transformation, making layer-based coverage a
powerful tool for dynamic geographic analysis.
CO-2   c   (5)
BL: 3
The hierarchical model organizes non-spatial data in a tree-like structure, where data
is arranged in parent–child relationships, with a single root node at the top and multiple
levels of dependent records beneath it. Each child record is linked to only one parent,
creating a one-to-many relationship that ensures a clear and structured data path. Data
CO-1   is accessed by traversing this hierarchy from the root through predefined links, making   (5)
d
BL: 3   retrieval efficient when relationships are well defined. Key features of this model
include simplicity of structure, data integrity through strict relationships, fast
access for hierarchical queries, and data dependency, where child records cannot
exist without a parent. However, it is less flexible for complex relationships, especially
many-to-many connections, as it requires data duplication or restructuring.
********** 2 **********
--- page 3 ---
Q2   Answer any (4)
In ArcGIS Pro, geodatabases are important because they provide a centralized and
structured system for storing spatial and attribute data. They allow efficient data
management, support large datasets, and enable advanced functionalities such as
topology rules, relationships, and data validation. This makes geodatabases essential
for organizing complex GIS projects and ensuring consistency and accuracy in analysis.
Feature Classes are collections of similar geographic features stored within a
geodatabase and represented as points, lines, or polygons. For example, in a tourism
project, point feature classes can represent tourist spots, line feature classes can
represent trekking routes, and polygon feature classes can represent protected areas or
regions.
Feature Data Sets are groups of related feature classes that share a common coordinate
system, allowing them to be analyzed together seamlessly. In a Tourism in the
Himalayas project, a feature dataset (e.g., “Himalayan Tourism”) could include feature
classes such as trekking trails, tourist attractions, and forest zones. These datasets can
be added to the geodatabase and used collectively for spatial analysis like route
planning, accessibility studies, and environmental impact assessment.
a   [10]
1
CO-2, 2
BL- 4, 6
Intersection is a topology-based overlay operation in GIS that creates a new vector
layer containing only the areas or parts of features that are spatially common to all input
b   layers. It affects the geometry of vector features by cutting them wherever they overlap   [10]
and retaining only the shared portion. Step by step, the GIS first takes two or more input
layers, such as land parcels and utility service zones in a smart city system. It then
********** 3 **********
--- page 4 ---
compares their geometries, detects where they overlap, and splits the original polygons,
lines, or points at those overlap boundaries. A new output layer is generated that
contains only the intersecting geometry, while the attributes from all input layers are
combined in the result. For example, in a smart city system, intersection can be used to
identify which buildings fall within both a high-energy-consumption zone and a
proposed underground cable upgrade corridor, helping planners focus only on the
common area requiring intervention.
Union is another topology-based overlay operation in GIS that combines the full spatial
extent of all input polygon layers into one output layer. It affects vector geometry by
merging the boundaries of all input features and subdividing the space into new
polygons based on every overlap and non-overlap area. Step by step, the GIS begins
with two polygon layers, such as land use zones and municipal service districts in a
smart city project. It overlays the layers, identifies all boundaries and intersections, and
then splits the entire mapped area into smaller polygons wherever any boundary crosses
another. Unlike intersection, union keeps all areas from both layers, whether they
overlap or not, and transfers the attributes from each input layer into the output table.
In a smart city system, union can be used to combine flood-risk zones with road
maintenance wards so that planners can see the entire city broken into smaller
management units, showing where flood risk and maintenance responsibility coincide
as well as where they do not.
These operations are important because they directly change the geometry of vector
features. Intersection reduces geometry to only shared spaces, while union expands
and reorganizes geometry to include all spaces from all inputs. In practical GIS
analysis, this means original parcels, roads, or service areas may be cut into many
smaller pieces, each carrying new attribute combinations. In a smart city context, such
geometry changes are extremely useful for integrated planning, because urban systems
such as utilities, transport, hazard zones, and land use often overlap in complex ways,
and topology operations make those relationships visible and analysis worthy.
Small-scale maps represent large geographic areas with less detail (e.g., world or
country maps), while large-scale maps represent smaller areas with greater detail
2   (e.g., city or neighborhood maps). Small-scale maps are best suited for regional or [10]
CO-1, 2   a
global analysis, trend identification, and comparisons across large areas, whereas
BL- 4, 6
large-scale maps are ideal for detailed, local-level analysis such as infrastructure
planning, site selection, and resource management.
********** 4 **********
--- page 5 ---
For a map of tourist towns in a state of India, a large-scale map would be easier to
use because it provides sufficient detail to locate towns accurately, understand
connectivity, and analyze accessibility within the state. In contrast, for a map of
leopard populations in the world, a small-scale map is more appropriate as it helps
visualize global distribution patterns and compare populations across continents
without requiring fine local detail.
Choropleth maps are thematic maps that represent data using different colors or
shading for predefined areas such as states, districts, or countries. They are created
by first collecting attribute data (e.g., population density or literacy rate), linking it to
geographic boundaries, classifying the data into ranges (using methods like equal
interval or quantiles), and then assigning color gradients where darker or more intense
colors represent higher values. Choropleth maps are widely used in applications such
as demographic analysis (population, literacy) and environmental studies (rainfall,
forest cover), as they effectively communicate spatial patterns and variations across
regions.
The Geoid and Datum are important in cartography because they define how the
Earth’s shape and position are represented. The geoid represents the Earth’s true,
b   irregular shape based on gravity and mean sea level, making it important for accurate   [10]
elevation measurements. A datum is a mathematically defined reference system (based
on an ellipsoid) used to locate positions on the Earth’s surface. Together, they ensure
that spatial data is accurately positioned and consistent across maps and GIS systems.
The least distortion in any map projection occurs along the line or point of contact
between the projection surface and the Earth, such as the equator in cylindrical
projections, standard parallels in conical projections, or the center point in azimuthal
projections. This is because distortion increases as one moves away from the area of
contact, making those regions the most accurate.
If studying topography in Greenland, an azimuthal projection (specifically a polar
azimuthal projection) would be most suitable because Greenland lies in high latitudes
near the pole. This projection minimizes distortion in polar regions and provides a more
accurate representation of shapes, distances, and terrain features compared to
cylindrical projections, which heavily distort polar areas.
********** 5 **********
--- page 6 ---
The spaghetti data model is a simple vector data structure in which points, lines, and
polygons are stored as independent geometries without explicit topological
relationships between them. In the context of pandemic management (such as
COVID-19), this model can be used to map locations like hospitals, containment
zones, testing centers, and movement paths of individuals. However, since it lacks
connectivity and adjacency information, it may lead to redundancy and makes
complex analyses (like tracking spread through connected networks or containment
boundaries) less efficient. It is useful for basic visualization and rapid mapping during
early stages of a pandemic but less suitable for advanced spatial analysis.
A polygon-on-line overlay operation involves analyzing how polygon features
interact with line features. Step by step, the GIS takes a polygon layer (e.g.,
administrative zones or containment areas) and a line layer (e.g., roads or utility
lines), identifies where the lines pass through or intersect the polygons, and then splits
the lines at polygon boundaries. The resulting line segments inherit attributes from
both the original line and the polygon they fall within. This operation is useful for
understanding how linear networks behave across different regions—for example,
identifying which road segments pass through high-risk COVID containment zones
for movement control or sanitation planning.
3
CO-2, 3   a   [10]
BL-4, 5
The connection between IoT (Internet of Things) and GIS lies in the integration of
real-time spatial data collection and analysis. IoT devices such as sensors, GPS
trackers, and smart meters continuously collect location-based data (e.g., temperature,
air quality, traffic flow), which is then fed into GIS platforms for mapping and
analysis. This integration enables dynamic monitoring and decision-making—for
instance, tracking patient movement during a pandemic, monitoring crowd density, or
managing smart city infrastructure. GIS provides the spatial context and visualization,
while IoT supplies continuous, real-time data, making the combination powerful for
applications like urban management, environmental monitoring, and disaster
response.
********** 6 **********
--- page 7 ---
Story Maps are interactive GIS-based presentations that combine maps, text, images,
videos, and multimedia to communicate spatial information in a narrative format.
They can be created using tools like ArcGIS StoryMaps by first preparing map layers
(such as trails, elevation, viewpoints), then adding descriptive content, images, and
route details into a structured story layout. For a trekking route, a Story Map can
include the trail path, altitude profiles, campsites, risk zones, and scenic viewpoints,
b   along with photos and safety instructions, allowing users to virtually experience the   [10]
journey. In a university campus management system, Story Maps can be used to
showcase campus infrastructure, navigation routes, emergency facilities, and
development plans. For example, a Story Map can guide new students through
departments, hostels, and amenities, or help administrators present campus expansion
projects interactively.
Raster datasets can be downloaded from several reliable global and national data
portals. Common sources include the USGS EarthExplorer for satellite imagery and
DEMs, NASA Earthdata for climate and remote sensing datasets, and India’s ISRO
Bhuvan platform for Indian geospatial data. Other sources include Copernicus (Sentinel
data) and open data repositories that provide elevation, land cover, and environmental
raster datasets used in GIS analysis.
Vector operators are spatial analysis tools used to manipulate and analyze vector data.
The main kinds include buffering (creating zones around features), overlay operations
such as intersection, union, and clip (combining or extracting spatial relationships),
a   merge and dissolve (combining features), and spatial join (linking attributes based on [10]
spatial relationships). These operators help in analyzing proximity, connectivity, and
spatial relationships between geographic features.
Latitudes and longitudes are components of the map projection graticule that form the
Earth’s coordinate system. Latitudes are horizontal lines running east–west that
measure angular distance north or south of the equator, while longitudes are vertical
lines running from pole to pole that measure angular distance east or west of the Prime
Meridian. Together, they create a grid that enables precise location referencing and
mapping on the Earth’s surface.
4   GeoAI in ArcGIS Pro enables advanced analysis by integrating machine learning and
CO- 2, 3   deep learning directly into GIS workflows. For image classification, GeoAI can
BL-4, 5   categorize satellite or aerial imagery into land-use or land-cover classes (e.g., urban,
vegetation, water) using supervised or unsupervised learning. For object detection,
deep learning models (such as convolutional neural networks) can automatically
identify and locate features like buildings, roads, vehicles, or trees from high-resolution
imagery. For spatial prediction, machine learning algorithms can analyze
relationships between multiple spatial variables (e.g., rainfall, elevation, land use) to
predict outcomes such as flood risk, crop yield, or urban expansion. These tools are
integrated through geoprocessing toolboxes, deep learning frameworks, and Python-
based workflows within ArcGIS Pro.
b   [10]
A detailed example can be seen in urban flood risk prediction. First, spatial datasets
such as a Digital Elevation Model (DEM), rainfall data, drainage networks, and land-
use maps are collected and preprocessed in ArcGIS Pro. Next, training data is prepared
by identifying known flood-prone and non-flood-prone areas. A machine learning
model (e.g., random forest or gradient boosting) is then trained using these variables as
inputs. For object detection, deep learning can also be used to extract features like
buildings and impervious surfaces from satellite imagery, which influence runoff. Once
trained, the model is applied across the study area to generate a predictive flood risk
map, highlighting high-risk zones. The output can then be visualized, validated, and
used by planners for disaster mitigation, drainage planning, and zoning regulations,
demonstrating how GeoAI transforms raw spatial data into actionable insights.
********** 7 **********
--- page 8 ---
Several open-source GIS systems are widely used as alternatives to proprietary
platforms like ArcGIS Pro. For example, QGIS is highly popular due to its user-friendly
interface, strong plugin ecosystem, and cross-platform support, making it accessible for
both beginners and advanced users. GRASS GIS is known for its powerful analytical
and geospatial modeling capabilities, especially for raster and environmental analysis.
gvSIG offers robust desktop and mobile GIS solutions with strong support for spatial
data editing. These open-source systems are unique in that they are free to use,
customizable, and community-driven, allowing users to modify code and extend
functionality without licensing constraints. While ArcGIS Pro offers more integrated
enterprise solutions and polished tools, open-source GIS platforms provide flexibility,
transparency, and cost-effectiveness, making them widely used in academia, research,
a   and government sectors.   [10]
Point-in-polygon and polygon-on-line are spatial analysis operations that examine
relationships between different vector geometries. In a point-in-polygon operation,
point features are tested to determine whether they fall within a polygon boundary, and
the attributes of the polygon are typically assigned to the point. This is useful for tasks
like identifying which administrative region a sampling point belongs to. In contrast, a
polygon-on-line operation analyzes how polygon features interact with line features. It
identifies where lines pass through polygons and often splits the lines at polygon
boundaries, assigning polygon attributes to each resulting segment. This is useful for
understanding how linear features such as roads, rivers, or pipelines traverse different
zones, such as land use areas or risk zones.
5
CO-1, 2   In GIS, contiguity, area definition, and connectivity are key concepts that
BL-3   describe spatial relationships between features. Contiguity refers to the sharing
of common boundaries between adjacent spatial units, such as neighboring
polygons that touch each other (e.g., administrative districts sharing borders).
Area definition relates to how polygons are formed using closed boundaries to
represent discrete spatial units like land parcels, forest patches, or zones,
ensuring that each area is uniquely identified and properly enclosed.
Connectivity describes how linear features are linked together in a network,
such as roads, rivers, or pipelines, allowing analysis of flow, movement, and
routing. Together, these concepts form the basis of topological relationships in
GIS and are essential for accurate spatial analysis.
b   [10]
Coverage resolution in terms of coordinate precision refers to the level of
detail and accuracy with which spatial data is represented based on the precision
of its coordinate values. Higher coordinate precision (more decimal places or
finer units) allows features to be represented more accurately, resulting in higher
resolution and more detailed spatial analysis. Conversely, lower precision leads
to generalized representations and potential loss of detail. Coverage resolution
is important because it influences the accuracy of measurements, overlay
operations, and spatial modeling, ensuring that GIS outputs are reliable and
suitable for the intended scale of analysis.
GIS can greatly optimize the crime management sector by enabling spatial
analysis of crime patterns and supporting predictive policing. For example, in
6   cities like Los Angeles, law enforcement agencies have used GIS to map [10]
CO-3   a
BL-3, 4   historical crime data, identify hotspots, and analyze trends based on time,
location, and type of crime. By integrating layers such as population density,
street networks, lighting conditions, and past incident reports, GIS helps predict
********** 8 **********
--- page 9 ---
high-risk areas and allocate police patrols more efficiently. It also supports real-
time monitoring, faster emergency response, and better coordination between
departments. As a result, resources are used more effectively, and preventive
measures can be implemented in vulnerable zones.
GIS can also make college exploration accessible to students in remote and
far-flung areas by providing interactive, map-based platforms that showcase
institutions, courses, infrastructure, and facilities. Through web-based GIS
applications, students can explore campuses virtually, view locations of
departments, hostels, libraries, and transport connectivity, and even analyze
proximity to their hometowns. For instance, platforms built using tools like
ArcGIS Online can integrate multimedia content such as photos, videos, and
admission details into interactive maps. This allows students who cannot
physically visit campuses to make informed decisions about education options,
compare institutions geographically, and understand accessibility, thereby
bridging the gap between urban and remote learners.
GIS can be used to understand gender patterns in census data by mapping and
analyzing the spatial distribution of indicators such as sex ratio, literacy rates,
workforce participation, and access to amenities. For example, in Delhi, census
data has been integrated into GIS to create ward-level maps showing variations
in female literacy, employment, and sex ratio. By overlaying these with layers
like education facilities, healthcare access, and public transport, planners can
identify gender disparities and underserved areas. This helps in targeted policy
interventions, such as improving safety infrastructure, increasing access to
education, or enhancing healthcare services for women, making gender-focused
planning more data-driven and location-specific.
GIS mapping is extremely valuable during urban disasters as it provides real- [10]
b
time spatial information for effective emergency response. During events like
floods, earthquakes, or fires, GIS can map affected zones, identify vulnerable
populations, and locate critical infrastructure such as hospitals, shelters, and
evacuation routes. It enables authorities to analyze the extent of damage,
prioritize rescue operations, and allocate resources efficiently. For instance,
during urban flooding, GIS can combine rainfall data, drainage networks, and
elevation models to predict flood spread and guide evacuation planning.
Overall, GIS enhances situational awareness, coordination among agencies, and
rapid decision-making, making it an essential tool for disaster management in
cities.
********** 9 **********
````
