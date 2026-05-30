# CDIF Data Structure (profile module)

This repository holds the published artifacts for the **CDIF Data Structure profile module** — the `cdifDataStructure` building block from the [metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks) source register.

> **Scope.** `cdifDataStructure` carries machine-readable data-structure metadata: keys, components, foreign keys, and the dimensional/long/wide structure variants. It is consumed by the composite application profile [doc-discoverydatadescriptionstructure](https://github.com/Cross-Domain-Interoperability-Framework/doc-discoverydatadescriptionstructure).

## Specification

- **[cdifDataStructureStructuredSchema.json](cdifDataStructureStructuredSchema.json)** — Resolved JSON Schema (Draft 2020-12) generated from the source register.
- **[dataStructureRules.shacl](dataStructureRules.shacl)** — Self-contained SHACL shapes, merged from every composing building block plus the profile-level shapes.
- **[CDIFDataStructure-frame.jsonld](CDIFDataStructure-frame.jsonld)** — JSON-LD frame used by `FrameAndValidate.py`.

## Examples

`examples/` holds JSON-LD examples illustrating the dimensional, long, wide, and minimal-complete data-structure shapes. Validate one with:

```bash
python FrameAndValidate.py examples/exampleCdifDataStructureComplete.json --validate
```

`FrameAndValidate.py` frames the document against `CDIFDataStructure-frame.jsonld`, array-wraps the multi-valued properties, then validates against the JSON Schema. Validation is open-world: unknown properties pass.

## Synced from metadataBuildingBlocks

These generated artifacts are re-synced when the source register changes:

| file | source command |
|---|---|
| `cdifDataStructureStructuredSchema.json` | `python tools/resolve_schema.py cdifDataStructure -o cdifDataStructureStructuredSchema.json` |
| `dataStructureRules.shacl` | `python tools/validate_shacl.py cdifDataStructure --emit-shapes dataStructureRules.shacl` |

Source profile: `_sources/profiles/cdifProfile/cdifDataStructure/`.

## Working materials

This repository also contains background and exploratory material from the profile's development — DDI-CDI samples and discussion notes (`DDI-CDI_SimpleSample.zip`, `DDI-CDI-forDataIntegration.txt`, `DataTypesDiscussion.txt`), sample data files (`ExampleData/`, `LongData/`, `TestCDIMetadata/`, `XrayAbsorbtion/`, `hierarchicalData/`, `hdf5Work/`), and reference documents (`Documents/`, `PhysicalDataset2025.xmi`, SDMX glossary, format-description figures). These are kept for traceability and are not part of the release-artifact set.

## Development branch

Active work for the 2026-06 review revision is on the `reviewRevision202606` branch. `main` reflects the prior release state. New changes should target the review branch; it is merged to main on release.

## License

This work is dedicated to the public domain under [CC0 1.0 Universal](LICENSE).
