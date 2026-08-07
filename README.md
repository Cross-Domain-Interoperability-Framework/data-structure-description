# CDIF Data Structure (profile module)

This repository holds the published artifacts for the **CDIF Data Structure profile module** — the `cdifDataStructure` building block from the [metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks) source register.

> **Scope.** `cdifDataStructure` carries machine-readable data-structure metadata: keys, components, foreign keys, and the dimensional/long/wide structure variants. It is consumed by the composite application profile [doc-discoverydatadescriptionstructure](https://github.com/Cross-Domain-Interoperability-Framework/doc-discoverydatadescriptionstructure).

## Specification

- **[CDIFDataStructureImplementationGuide.md](CDIFDataStructureImplementationGuide.md)** — Implementation guide (auto-generated draft; hand-curated content pending).
- **[cdifDataStructureStructuredSchema.json](cdifDataStructureStructuredSchema.json)** — Resolved JSON Schema (Draft 2020-12) generated from the source register.
- **[dataStructureRules.shacl](dataStructureRules.shacl)** — Self-contained SHACL shapes, merged from every composing building block plus the profile-level shapes.
- **[CDIFDataStructure-frame.jsonld](CDIFDataStructure-frame.jsonld)** — JSON-LD frame for Dataset-rooted documents (a `schema:Dataset` whose distribution carries the structure via `cdi:isStructuredBy`).
- **[CDIFDataStructure-structure-frame.jsonld](CDIFDataStructure-structure-frame.jsonld)** — JSON-LD frame for **bare** DataStructure documents (root `@type` = `cdi:DataStructure` / `cdi:DimensionalDataStructure` / `cdi:LongDataStructure` / `cdi:WideDataStructure`). `FrameAndValidate.py` auto-selects between the two frames by the document's root `@type`.

## Examples

`examples/` holds JSON-LD examples illustrating the dimensional, long, wide, and minimal-complete data-structure shapes. Validate one with:

```bash
python FrameAndValidate.py examples/exampleCdifDataStructureComplete.json --validate
```

`FrameAndValidate.py` selects the matching frame by the document's root `@type` — the Dataset frame for `schema:Dataset` records, the structure frame for bare `cdi:*DataStructure` documents — array-wraps the multi-valued properties, then validates against the JSON Schema. Validation is open-world: unknown properties pass.

## Synced from metadataBuildingBlocks

These generated artifacts are re-synced when the source register changes:

| file | source command |
|---|---|
| `cdifDataStructureStructuredSchema.json` | `python tools/resolve_schema.py cdifDataStructure -o cdifDataStructureStructuredSchema.json` |
| `dataStructureRules.shacl` | `python tools/validate_shacl.py cdifDataStructure --emit-shapes dataStructureRules.shacl` |

Source profile: `_sources/profiles/cdifProfile/cdifDataStructure/`.

## Working materials

Background and exploratory material from the profile's development is kept under `archive/` for traceability — DDI-CDI samples and discussion notes, sample data files (`archive/ExampleData/`, `archive/LongData/`, `archive/TestCDIMetadata/`, `archive/XrayAbsorbtion/`, `archive/hierarchicalData/`, `archive/exampleMetadata/`), reference documents (`archive/PhysicalDataset2025.xmi`, SDMX glossary, format-description figures), and the earlier psdi/UML drafts. The `Documents/` directory holds the curated reference docs (`Documents/CDIF-DescribingDatasetStructure.md`, `Documents/hdf5Work/`). None of these are part of the release-artifact set.

## Development branch

Active work for the 2026-06 review revision is on the `reviewRevision202606` branch. `main` reflects the prior release state. New changes should target the review branch; it is merged to main on release.

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
