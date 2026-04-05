# CDIF Data Structure Description

Properties and patterns for documenting the internal structure of datasets, including variables, data types, physical layout, and value domains. This repository develops the CDIF data description and integration profile using DDI-CDI (Data Documentation Initiative - Cross Domain Integration) concepts mapped to schema.org JSON-LD.

## Documentation

- **[Documents/CDIF-DescribingDatasetStructure.md](Documents/CDIF-DescribingDatasetStructure.md)** — Discussion of how to describe structured data (arrays, hierarchical, dimensional) using DDI-CDI concepts
- **[psdi-metadata-cdif-implementation.md](psdi-metadata-cdif-implementation.md)** — How PSDI (Physical Sciences Data Infrastructure) implements CDIF metadata recommendations

## Example data and metadata

### ExampleData

Source data files in various formats used for testing DDI-CDI JSON-LD documentation:

- `SimpleSample.csv` / `.jsonld` — Simple tabular CSV with CDI metadata
- `xdi_example_ss.xdi` / `nonxafs_2d.xdi` — X-ray Data Interchange (XDI) format files
- `Therm_6_2.hdf` — HDF5 data file
- `20231120_002_1mg_Murchison_Smithsonian.cdf` — CDF (Common Data Format) file
- `csvTable-DDICDI.jsonld` — CSV table documented with DDI-CDI

### TestCDIMetadata

CDI-DDI metadata instances documenting the example data, in JSON-LD format:

- `CDIF-XAS-FullExample.jsonLD` — Full XAS (X-ray Absorption Spectroscopy) metadata
- `CDIFmin-XAS.jsonLD` — Minimal XAS metadata
- `ESS11-subset_DDICDI.jsonld` — European Social Survey subset
- `WeatherObsKeyValue_DDICDI.jsonld` — Weather observations in key-value format
- `se_na2so4-XDI-CDI-CDIF.jsonld` — Sodium selenate XAS with CDI data structure
- `HealthResearchdata-WorldFairWP7.json` — WorldFAIR health research data

### exampleMetadata

Additional metadata examples organized by domain:

- `CDIF2026/` — Current CDIF 2026 schema examples
- `FeXAS/` — Iron X-ray absorption spectroscopy
- `CMIP-NetCDF/` — Climate model NetCDF metadata
- `ESS11/` — European Social Survey
- SDMX examples (merchandise trade statistics, Pacific fisheries)

### LongData

Long/narrow format data examples (NWIS water quality data) with DDI-CDI metadata demonstrating `DescriptorComponent` and `ReferenceValueComponent` roles.

### XrayAbsorbtion

X-ray absorption spectroscopy metadata examples with various levels of CDI-CDI detail.

### hierarchicalData

Hierarchical JSON data with CDI-DDI metadata (NWIS water quality as JSON structure).

### hdf5Work

Python scripts and metadata for reading HDF5 and NetCDF files and extracting structure metadata.

## Background materials

- `EC_GeoCodes_encodingFormat.xlsx` — Compilation of file formats from EarthCube GeoCodes catalog, scoping the spectrum of data serialization schemes
- `SDMX_3-1-0_SECTION_2_FINAL.pdf` — SDMX statistical data exchange standard
- `PhysicalDataset2025.xmi` — UML model for physical dataset structure
- `newModel.qea` — Enterprise Architect model file

### Archive

The `archive/` directory contains earlier versions of XAS mapping documents, the ADA-CDIF Reader tool, presentation materials, and working documents from the CDIF-for-XAS development.

## Related repositories

- **[cdif-core](https://github.com/Cross-Domain-Interoperability-Framework/core)** — CDIF Core profile (base properties)
- **[Discovery](https://github.com/Cross-Domain-Interoperability-Framework/Discovery)** — CDIF Discovery profile (spatial, temporal, variables)
- **[metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)** — Building block schemas including CDIFDataDescriptionProfile, cdifDataDescription, cdifTabularData, cdifLongData, cdifDataCube
- **[validation](https://github.com/Cross-Domain-Interoperability-Framework/validation)** — Validation tools (JSON Schema, SHACL, framing)

## License

See [LICENSE](LICENSE).
