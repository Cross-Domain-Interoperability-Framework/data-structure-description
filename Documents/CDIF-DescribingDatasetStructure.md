# Describing DataStructure in which components might be datastructure

e.g. vector, array, or tensor values that aren't decomposed as separate components.

First consider the simple case typical of the XAS NEXUS files, in which each variable has an array of values. In the example below, the variables are energy, i0 and mutrans. Energy is a dimension (the independent variable); i0 and mutrans are the measures (the observed data). There is an assumption that for each energy value, there is an associated i0 and mutrans value; mapping between these 1-D arrays for each variable is done by the order (array index). To describe this structure, we have three instanceVariables (energy, i0, mutrans), each should map to a concept, has a dataType, format, and possibly units of measure. We only need to indicate how may values there are for the Dimension variable, because of the assumption that the measure arrays have corresponding values for each dimension value. For completeness, one would likely want to know the substantiveValueDomain at least for the dimension (energy). This would start with the min and max values for the dimension -- energy in the example. Also need a boolean to indicate if intervals along the dimension (sampling interval, resolution) are constant or variable. If the intervals are constant, then the spacing/resolution is given by (max-min)/(nrows - 1).  It might also be imporant if the measures are averages over the interval, or point observations at the dimension coordinate, interval center point, or some other strategy. 

| energy    | i0    | mutrans    |
|-----------|-------|------------|
| energy1   | i01   | mutrans1   |
| energy2   | i02   | mutrans2   |
| energy3   | i03   | mutrans3   |
| energy4   | i04   | mutrans4   |



Variable values are structured.  

## [NetCDF](https://docs.unidata.ucar.edu/netcdf-c/current/netcdf_data_model.html): 

This section is informative to indicate the kind of information of interest to scientists collecting data that gets put in structures like NetCDF or HDF5. In a NetCDF structure, the user can define compound types (like C structures), enumeration types, variable length arrays, and opaque types. Groups may contain variables, dimensions, and attributes. In this way, a group acts as a container for the classic netCDF dataset. But netCDF-4/HDF5 files can have many groups, organized hierarchically. [*NetCDF group is like cdi:DataStructure*]

[NetCDF](https://docs.unidata.ucar.edu/netcdf-c/current/netcdf_data_model.html) views the world as sets of related arrays. For example there are various physical quantities (such as pressure and temperature) located at points at a particular latitude, longitude, vertical level, and time (atmospheric data).  A scientist might also like to store supporting information, such as the units, or some information about how the data were produced. The axis information (latitude, longitude, level, and time) would be stored as netCDF dimensions. **Dimensions have a length and a name** [*CDIF DataStructure/DimensionComponent or InstanceVariable/hasRole*]. The physical quantities (pressure, temperature) would be stored as netCDF variables [*CDIF: MeasureComponent*]. Variables are N-dimensional arrays of data, with a name and an associated set of netCDF dimensions. It is also customary to add one variable for each dimension, to hold the values along that axis. These variables are called “coordinate variables.” The latitude coordinate variable would be a one-dimensional variable (with latitude as its dimension), and it would hold the latitude values at each point along the axis.  The additional bits of metadata would be stored as netCDF attributes. Attributes are always single values [*CDIF: properties of InstanceVariable*] or one-dimensional arrays [*CDIF: AttributeComponents*]. 
### NetCDF climate and forecasting conventions. 
Attributes for dimensions, with CDIF notes.
#### Structural / indexing attributes: 

| Attribute    | Purpose    | Example   | CDIF Note |
| -------------- | --------------- | -------------- | ---- |
| **bounds** | Name of a variable giving cell boundaries | "lat_bnds" | AttributeComponent |
| **valid_min** | Min legal value | 'valid_min = -90.f' | Property of Represented Variable |
| **valid_max** | Max legal value | 'valid_max = 90.f' | Property of Represented Variable  |
| **valid_range** | Legal numeric range | 'valid_range = -90.f, 90.f' | Property of Represented Variable |
| **_FillValue**    | Internal fill used for missing values     | '1.0e20' | Property of Represented Variable, Sentinel Value |
| **missing_value**   | Identifies missing entries      | '1.0e20'  | Property of Represented Variable, Sentinel Value |
| **positive** (vertical only)  | Direction ('up' or 'down')   | "up"  | Property of Represented Variable |
| **calendar** (time only)   | Calendar type    | "gregorian"  | Property of Represented Variable |

#### Geospatial & grid-related attributes

| Attribute  | Purpose  | Example  | CDIF Note |
| ----------------- | ---------- | ---- | --- |
| **grid_mapping**  | Reference to a projection variable | "crs" | Property of Represented Variable  |
| **cell_methods**  | How values are computed in a cell  | "area: mean" | Property of Represented Variable  |
| **cell_measures** | Links to measures like area or volume for each 'cell' in the dimension space | "area: areacella"| Attribute Component |

#### Time-specific attributes
| Attribute   | Example  | CDIF Note |
| --------- | --------------- | --- |
| **units** (required by CF) | "days since 1850-01-01 00:00:00"  | Property of Represented Variable  |
| **calendar**  | "noleap"', "gregorian"', "360_day", etc. | Property of Represented Variable  |

### Arrays
In the Nexus HDF5 file for XAS data the Scan variable has an array for a value. This array contains the variables (Dimension, Measure) that are defined as separate variables with a separate locator path, but has 28 other columns with various measurement-specific variables.  We need a way to describe such array (compound) value types for Measures. To represent Data with complex value types, the Dataset/DataStructure/DataStructureComponent [choose subclass for concrete implementation] schema must be used. 
	
The DDI-CDI model has DataStructure as a SubClass of DataStructureComponent, and a DataStructure is an aggregation of DataStructureComponents. If a component has an array value, we are assuming that the array is logically like a wide data structure-- each column of the array quantifies a variable, and is a dimension, measure, or attribute of some other column in the array.  Note that this structure might be transposed in some implementations such that the rows are the variables and the columns are observation instances, in which case the rows need to be considered as columns.  For an example implementation see the cdi:isStructuredBy value in  [NEXUS-withDataStructureComponentSimplified](https://github.com/Cross-Domain-Interoperability-Framework/data-structure-description/blob/main/exampleMetadata/FeXAS/NEXUS-withDataStructureComponentSimplified.json)

## Long Data Structure

In a long data structure, the variable quantified by a Measure Component in a data set is specified by the value of another variable. Typically, long data are serialized in delimited tabular text formats, but the interpretation of the columns is different from wide data structure. The structure is described in terms of logical variables that are bound to the observation instance, and presentation variables that are bound to the columns in the data.  Here is an example using some water quality data:

| ResultIdentifier | CharacteristicName | ResultMeasureValue |
|------------------|--------------------|--------------------|
| NWIS-96934881     | Nitrogen           | 14.07             |
| NWIS-96936145     | Nitrate            | 2.53              |
| NWIS-96936147     | Orthophosphate     | 0.031             |
| NWIS-96936148     | Orthophosphate     | 0.01              |
| NWIS-96936610     | Nitrate            | 11.2              |
| NWIS-97019203     | Nitrogen           | 14.07             |
| NWIS-47324265     | Nitrate            | 6.54              |

The ResultIdentifier column identifies each observation result; the CharacteristicName identifies the chemical constituent that awas measured, and the ResultMeasureValue is the observation result (we'll assume for the time being the units of measure are constant mg/l and defined elsewhere). 

The logical variables are ResultIdentifier, Nitrogen, Nitrate, Orthophosphate. These are the Instance Variables in the metadata. The columns in the table (that are not logical variables) are considered Presentational Variables, these are CharacteristicName and ResultMeasureValue.

The presentation consists of an Identifier Component (ResultIdentifier), a column giving us the constituent measured (CharacteristicName), and a column with the measurement (ResultMeasureValue). In the ResultMeasureValue column each cell contains a measurement, but they are different types of measures. In order to understand the measurement, you have to consult the CharacteristicName column, which tells you what constituent is reported. This dependency is the characteristic feature of Long Data Sets.

CharacteristicName is a Descriptor Variable (cdi:DescriptorVariable), and ResultMeasureValue is a Reference Variable (cdi:ReferenceVariable). A Reference Variable can present measurement values from several logical Instance Variables. The Descriptor and Reference variables together are refered to as a Variable Descriptor Component (cdi:VariableDescriptorComponent) defined by a Descriptor Variable (CharacteristicName), and a Variable Value Component (cdi:VariableValueComponent), which is defined by a Reference Variable (ResultMeasureValue).

Descriptor Variables take their values from a Descriptor Value Domain (cdi:DescriptorValueDomain) that specifies a set of codes (strings) that identify logical Instance Variables in the presentation. The code in the Descriptor Component indicates which Instance Variable the value provided in the corresponding Reference Variable should be associated with. Thus, in the example above, when the CharacteristicName column has a value of ‘Nitrogen’, we know that the value in the ResultMeasureValue column is a measurement of Nitrogen concentration, associated with the 'Nitrogen' InstanceVariable.

### Serialization of Long Data Structure
In the schema.org implementation for CDIF (see [example](https://github.com/Cross-Domain-Interoperability-Framework/data-structure-description/blob/main/LongData/LongDataTestMetadata.json)), all variables are defined in the schema:variableMeasured section. DescriptorVariables have an associated cdi:enumerationDomain that provides the mapping from the DescriptorVariable (CharacteristicName) values to the associated InstanceVariable. The InstanceVariable cdi:name must match the string that appears in the DescriptorVariable (CharacteristicName) value.

The cdi:LongDataStructure defines three components-- an IdentifierComponent, the VariableDescriptorComponent, and VariableValueComponent, that are linked (cdi:isDefinedBy) the appropriate variable defined in schema:variableMeasured element. The array in schema:variableMeasured thus plays the role of cdi:LogicalRecord. 

The physical dataset structure description is in the schema:distribution object, typed as both "schema:DataDownload" and "cdi:TabularTextDataset". because from the physical structure point of view, the data are just a three column tabular text dataset. There is one header row with the column names. The cdi:LocatorMapping associates column name (cdi:locator) and column number (cdi:index) with the appropriate variable.

A machine agent using this metadata to parse a data file would first look at the cdi:LocatorMapping to determine which column is the descriptor and which is contains the result values. The access the descriptor variable definition to get the mapping from descriptor string values to instance variable. Given this information, the table could be read processing each row as appropriate for the InstanceVariable result value it contains.

## Attribute components
Next, consider adding a unit of measure for each result value. The updated table looks like this:

| ResultIdentifier | CharacteristicName | ResultMeasureValue | MeasureUnitCode }
|-----------------|-----------------|----------|
| NWIS-96934881   | Nitrogen         | 14.07     | mg/l |
| NWIS-96936145   | Nitrate          | 2.53      | mg/l as N |
| NWIS-96936147   | Orthophosphate   | 0.031     | mg/l as PO4 |
| NWIS-96936148   | Orthophosphate   | 0.01      | mg/l as P 
| NWIS-96936610   | Nitrate          | 11.2      | mg/l as NO3 |
| NWIS-97019203   | Nitrogen         | 14.07     | mg/l |
| NWIS-47324265   | Nitrate          | 6.54      | mg/l as N |

The MeasureUnitCode is an attribute of the ResultMeasureVallue (we'll ignore for now the question of whether the 'as ...' should be part of the characteristicName...). So we need to 
1. add a new InstanceVariable for MeasureUnitCode in the schema:variableMeasuredSection
1. add a cdi:AttributeComponent in the cdi:isStructuredBy section with a cdi:qualifies link to the resultMeasureComponent
1. add a cdi:has_LocatorMapping indicating the column name and index for the measurement units property.

See CDIF implementation at [LongDataTestMetadata_wAttrib.json](https://github.com/Cross-Domain-Interoperability-Framework/data-structure-description/blob/main/LongData/LongDataTestMetadata_wAttrib.json)

### Nested (Hierarchical) structures
In hierarchical data structures like JSON, YAML, or XML, the value of a variable might be a Literal, or an Object that has a DataStructure describing components of its own. This pattern is recursive-- Objects can have components that are Objects having components.  There are two possible approaches to describeing such data.  The hierarchical structure can be flattened, with each variable located by a JSON path in the DDI-CDI value mapping. Alternatively nodes in the structure that have values that are objects can be described as data structure components that are data structures, analogous to the approach described above for array values in HDF5 data structures. 