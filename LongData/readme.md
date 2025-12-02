# what's here

this folder contains files testing description of some water quality data with long data structure, and testing description of Prov using schema:HowTo and HowTo steps. The files star with a simple three column table 

- nwisData3Column.txt  -- simple short table with identifier, characteristic (the descriptor) and result measure value.  Described by LongDataTestMetadata-3Col.json
- nwisData-WAttribute.txt, adds one column with unit of measure strings, described as an attribute component of the resultMeasureValue in LongDataTestMetadata_wAttrib.json.
- NWISWaterQualityData.csv  a more complete dataset, with 19 columns 464 rows, the ResultIdentifier, characteristic, UOM, and ResultMeasureValue are like in the previous example, but have added fields providing context for the sampling activity,  analytical method, and result. The columns have been processed from the data download from the USGS/EPA Water Quality Portal, but details are not described in the associated metadata record LongDataTestMetadata_NWISAll.json
- LongDataTestMetadata_NWISAllwProv.json describes the same data (NWISWaterQualityData.csv), but adds a prov:wasGeneratedBy section documenting how the dataset was generated from the Water Quality Portal download. The description uses the schema:actionProcess/schema:HowTo/schema:step pattern suggested in Pier Luigi's proposal at [odis-arch/blob/414-update-provenance-recommendations](https://github.com/iodepo/odis-arch/blob/414-update-provenance-recommendations/book/thematics/provenance/common-provenance-cases.md)

## Things to think about:
- there is a lastUpdate field with a date.  What kind of DDI-CDI component would this be? its a attribute of the individual record, but the model only allows attributes to quality other components
- Some fields could be considered both attributes and Dimensions, e.g. MonitoringLocation and ResultAnalyticalMethod. Does DDI-CDI allow a variable to have multiple roles like this?
  
