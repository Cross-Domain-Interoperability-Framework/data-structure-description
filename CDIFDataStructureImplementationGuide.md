# CDIF Data Structure Profile — Implementation Guide

The data structure profile defined metadata elements to document a data structure based on a set of represented variables, their role as components in a data implementation, value domains assigned to variables. This profile introduces the concept of a represented variable in the CDIF framework, as a logical variable that plays a role in a data structure, but is not bound to a particular physical datatype or position in the data serialization. Represented variable roles in the data structure are documented via a data structure component class.

Adds data-structure description to a CDIF metadata record. Defines the cdi:DataStructure family of types ($defs DataStructure / DimensionalDataStructure / LongDataStructure / WideDataStructure, plus the supporting Component / Key / RepresentedVariable types). A distribution attaches a structure via cdi:isStructuredBy on its schema:DataDownload item; the structure value is one of the four DataStructure variants. 

# Table of contents

- [Conformance](#conformance)
  - [Validation](#validation)
- [DataDownload Properties added by the CDIF Data Structure Profile](#datadownload-properties-added-by-the-cdif-data-structure-profile)
  - [schema:isStructuredBy](#schemaisstructuredby)
- [Class Definitions](#class-definitions)
  - [AttributeComponent](#attributecomponent)
  - [cdi:DimensionalDataStructure](#cdidimensionaldatastructure)
  - [cdi:LongDataStructure](#cdilongdatastructure)
  - [cdi:WideDataStructure](#cdiwidedatastructure)
  - [cdif:DimensionComponent](#cdifdimensioncomponent)
  - [cdif:RepresentedVariable](#cdifrepresentedvariable)
  - [CdifCodelistConcept](#cdifcodelistconcept)
  - [ForeignKey](#foreignkey)
  - [Identifier](#identifier)
  - [IdentifierComponent](#identifiercomponent)
  - [MeasureComponent](#measurecomponent)
  - [PrimaryKey](#primarykey)
  - [VariableDescriptorComponent](#variabledescriptorcomponent)
  - [VariableValueComponent](#variablevaluecomponent)
- [Provenance of the artifacts](#provenance-of-the-artifacts)

# Conformance

[↑ Back to TOC](#table-of-contents)

A resource conforms to the CDIF Data Structure profile when its catalog record declares conformance to the profile identifier. The catalog record is carried on `schema:subjectOf` as a `dcat:CatalogRecord`:

```json
"schema:subjectOf": {
  "@type": ["schema:CreativeWork", "dcat:CatalogRecord"],
  "dcterms:conformsTo": [
    "https://w3id.org/cdif/data_structure/1.0"
  ]
}
```
Other properties added in this profile are optional; conformance requires only that the constraints in the JSON Schema and SHACL rules are satisfied.

## Validation

[↑ Back to TOC](#table-of-contents)

Two validators ship with this repository:
- **JSON Schema** — `cdifDataStructureStructuredSchema.json` (Draft 2020-12), generated from the source register.
- **SHACL** — `dataStructureRules.shacl`, a self-contained shapes graph merged from every composing building block plus the profile-level shapes.

```bash
python FrameAndValidate.py examples/<file>.json --validate \
  --schema cdifDataStructureStructuredSchema.json --frame <frame.jsonld>
```
Validation is **open-world**: properties not described by the profile are allowed.

# DataDownload Properties added by the CDIF Data Structure Profile

[↑ Back to TOC](#table-of-contents)

## schema:isStructuredBy

[↑ Back to TOC](#table-of-contents)

- property of a schema:DataDownload that links to an externally defined data structure via an object reference, or includes a DataStructure definition in line.  Value is one of cdi:WideDataStructure, cdi:DimensionalDataStructure, cdi:LongDataStructure,  

- 

# Class Definitions

[↑ Back to TOC](#table-of-contents)

## AttributeComponent

[↑ Back to TOC](#table-of-contents)

- Role given to a represented variable in the context of a data structure to qualify observations or provide other types of supplementary information.

### @type

- **Cardinality:** Required
- **Content:** array of string

### @id

- **Cardinality:** Optional
- **Content:** string
- **Description:** Identifier for this AttributeComponent node

### cdi:qualifies

- **Cardinality:** Optional
- **Content:** array of one of: object, [object reference](#/$defs/CdifDataStructureComponent_id-reference)

### cdi:identifier

- **Cardinality:** Optional
- **Content:** [object reference](#/$defs/Identifier)
- **Description:** Identifier for objects requiring short- or long-lasting referencing and management.

### cdif:isDefinedBy_RepresentedVariable

- **Cardinality:** Optional
- **Content:** cdif:RepresentedVariable or object reference to cdif:Represented Variable

### cdi:semantic

- **Cardinality:** Optional
- **Content:** array of one of: string, [object reference](#/$defs/CdifDataStructureComponent_cdifConceptOrTerm)
- **Description:** Qualifies the purpose or use expressed as a paired external controlled vocabulary.

## cdi:DimensionalDataStructure

[↑ Back to TOC](#table-of-contents)

- Structure of a dimensional data set (organized collection of multidimensional data). It is described by dimension, measure and attribute components.

### @type

- array of strings, contains 'cdi:DimensionalDataStructure'

### cdi:has_DataStructureComponent

- array of links to data structure components that link representedVariables to roles in the data structure. Values are one of **cdif:DimensionComponent**, **cdif:MeasureComponent**, or **cdif:AttributeComponent**

### cdi:has_PrimaryKey

- property that specifies variables in the structure that uniquely identify a unit in the population described. value: cdif:PrimaryKey or object reference to a cdif:PrimaryKey. 

### cdi:has_ForeignKey

- specifies a variable with values that identify data records in a different dataset. value: cdif:ForeignKey or object reference to a cdif:ForeignKey. 

## cdi:LongDataStructure

[↑ Back to TOC](#table-of-contents)

- Structure of a long dataset (organized collection of long data). It is described by identifier, measure, attribute, variable descriptor and variable value components.

### @type

- array of strings, contains 'cdi:LongDataStructure'

### cdi:has_DataStructureComponent

- array of links to data structure components that link representedVariables to roles in the data structure. Values are one of **cdif:IdentifierComponent**, **cdif:VariableDescriptorComponent**, **cdif:VariableValueComponent**, or **cdif:AttributeComponent**

### cdi:has_PrimaryKey

- property that specifies variables in the structure that uniquely identify a unit in the population described. value: cdif:PrimaryKey or object reference to a cdif:PrimaryKey. 

### cdi:has_ForeignKey

- specifies a variable with values that identify data records in a different dataset. value: cdif:ForeignKey or object reference to a cdif:ForeignKey. 

## cdi:WideDataStructure

[↑ Back to TOC](#table-of-contents)

- Structure of a wide dataset (organized collection of wide data). It is described by identifier, measure and attribute components. Each record represents properties for one unit (instance) in the population described by the dataset.

### @type

- array of strings, contains 'cdi:WideDataStructure'

### cdi:has_DataStructureComponent

- array of links to data structure components that link representedVariables to roles in the data structure. Values are one of **cdif:IdentifierComponent**, **cdif:MeasureComponent**, or **cdif:AttributeComponent**

### cdi:has_PrimaryKey

- property that specifies variables in the structure that uniquely identify a unit in the population described. value: cdif:PrimaryKey or object reference to a cdif:PrimaryKey. 

### cdi:has_ForeignKey

- specifies a variable with values that identify data records in a different dataset. value: cdif:ForeignKey or object reference to a cdif:ForeignKey. 

## cdif:DimensionComponent

[↑ Back to TOC](#table-of-contents)

- Role given to a represented variable that acts as a field in the compound identifier (the key structure) to disambiguate the cells in the multi-dimensional "cube".  Components are part of a compound identifier in which each variable is an axis in a coordinate system addressing a location in a matrix. These variables are often categorical, but also commonly include time, space or other continuous phenomena. Dimensions typically encompass a limited range of values, and are quantized.

### @type

- **Cardinality:** Required
- **Content:** array of string, contains 'cdif:VariableValueComponent'

### @id

- **Cardinality:** Optional
- **Content:** string
- **Description:** Identifier for this node

### cdif:isDefinedBy_RepresentedVariable

- **Cardinality:** Optional
- **Content:** cdif:RepresentedVariable or object reference to cdif:Represented Variable

## cdif:RepresentedVariable

[↑ Back to TOC](#table-of-contents)

- Conceptual variable with a substantive value domain specified.

### @type

- **Cardinality:** Required
- **Content:** array of string

### @id

- **Cardinality:** Optional
- **Content:** string
- **Description:** Identifier for this RepresentedVariable node

### cdi:describedUnitOfMeasure

- **Cardinality:** Optional
- **Content:** one of: string, [object reference](#/$defs/cdifConceptOrTerm)
- **Description:** The unit in which the data values are measured (kg, pound, euro), expressed as a value from a controlled system of entries (i.e., QDT). Supports the provision of an identifier for the entry in the authoritative source (a URI, etc.), and the specific vocabulary.

### cdi:hasIntendedDataType

- **Cardinality:** Optional
- **Content:** one of: string, [object reference](#/$defs/cdifConceptOrTerm)
- **Description:** The data type intended to be used by this variable. Supports the optional use of an external controlled vocabulary.

### cdi:takesSentinelValuesFrom

- **Cardinality:** Optional
- **Content:** array of one of: one of: —, —, [object reference](#/$defs/CdifRepresentedVariable_id-reference)
- **Description:** Sentinel (missing / not-applicable) value domain(s) for this RepresentedVariable (RepresentedVariable.takesSentinelValuesFrom).

### cdi:takesSubstantiveValuesFrom

- **Cardinality:** Optional
- **Content:** one of: one of: —, —, [object reference](#/$defs/CdifRepresentedVariable_id-reference)
- **Description:** The substantive value domain for this RepresentedVariable - the set of valid, meaningful values (RepresentedVariable.takesSubstantiveValuesFrom).

### cdi:simpleUnitOfMeasure

- **Cardinality:** Optional
- **Content:** string
- **Description:** The unit in which the data values are measured (kg, pound, euro), expressed as a simple string, in cases where no additional information is available (in the legacy system) or needed (as in the case of broad agreement within the community of use [i.e., ISO country codes, currencies, etc. in SDMX])

### cdif:descriptiveText

- **Cardinality:** Optional
- **Content:** string
- **Description:** A short natural language account of the characteristics of the object.

### cdi:measures

- **Cardinality:** Optional
- **Content:** one of: object, [object reference](#/$defs/CdifRepresentedVariable_id-reference)

### cdi:unitOfMeasureKind

- **Cardinality:** Optional
- **Content:** one of: string, [object reference](#/$defs/cdifConceptOrTerm)
- **Description:** Kind of unit of measure, so that it may be prone to translation to equivalent UOMs. Example values include "acceleration," "temperature," "salinity", etc. This description exists at the conceptual level, indicating a limitation on the type of representations which may be used for the variable as it is made more concrete.

### cdif:definition

- **Cardinality:** Optional
- **Content:** string
- **Description:** Natural language statement conveying the meaning of a concept, differentiating it from other concepts. Supports the use of multiple languages and structured text. 'externalDefinition' can't be used if 'definition' is used.

### cdif:displayLabel

- **Cardinality:** Optional
- **Content:** array of string
- **Description:** A human-readable display label for the object. Supports the use of multiple languages. Repeat for labels with different content, for example, labels with differing length limitations.

### cdi:externalDefinition

- **Cardinality:** Optional
- **Content:** object
- **Description:** A reference to an external definition of a concept (that is, a concept which is described outside the content of the DDI-CDI metadata description). An example is a SKOS concept. The definition property is assumed to duplicate the external one referenced if externalDefinition is used. Other corresponding properties are assumed to be included unchanged if used.

### cdi:identifier

- **Cardinality:** Optional
- **Content:** [object reference](#/$defs/Identifier)
- **Description:** Identifier for objects requiring short- or long-lasting referencing and management.

### cdif:name

- **Cardinality:** Optional
- **Content:** array of string
- **Description:** Human understandable name (linguistic signifier, word, phrase, or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context provided to specify usage.

### cdif:uses_Concept

- **Cardinality:** Optional
- **Content:** array of one of: object, [object reference](#/$defs/CdifRepresentedVariable_id-reference)

### id-reference

- Reference to a node defined elsewhere in the document via its @id.

### @id

- **Cardinality:** Required
- **Content:** string that identifies an object in the local document, or might be an external identifier.

## CdifCodelistConcept

[↑ Back to TOC](#table-of-contents)

- A SKOS Concept constrained for CDIF codelist use. Must have a resolvable @id, skos:inScheme, skos:notation, and skos:prefLabel. Becasue JSON-LD is an open-world implementation, any other skos properties may be included.

### @id

- **Cardinality:** Required
- **Content:** string
- **Description:** Globally unique, resolvable URI for this concept.

### skos:inScheme

- **Cardinality:** Required
- **Content:** array of object
- **Description:** The concept scheme this concept belongs to. Required for CDIF codelist concepts.

### skos:prefLabel

- **Cardinality:** Required
- **Content:** string
- **Description:** Preferred lexical label for this concept. A single string, a single language-tagged value, or an array of language-tagged values. Each language should appear at most once.

### skos:notation

- **Cardinality:** Required
- **Content:** string
- **Description:** Classification code for this concept within a scheme.

### skos:definition

- **Cardinality:** Optional
- **Content:** string
- **Description:** Formal definition of this concept. Optional for CDIF codelist concepts. A plain string.

### skos:narrower

- **Cardinality:** Optional
- **Content:** array of one of: object, —
- **Description:** Narrower (child) concepts. If present, each inline concept must also declare skos:broader pointing back to the parent concept. Both skos:narrower and skos:broader must be explicit in CDIF codelists.

### skos:broader

- **Cardinality:** Optional
- **Content:** array of object
- **Description:** Broader (parent) concepts. Required on any concept that appears as a skos:narrower value of another concept. CDIF requires both directions to be explicit for hierarchy traversal.

## ForeignKey

[↑ Back to TOC](#table-of-contents)

- a set of variables whose values uniquely identify a related record in another dataset, for content referencing purposes.

### @type

- **Cardinality:** Required
- **Content:** array of strings, contains 'cdi:ForeignKey'

### @id

- **Cardinality:** Optional
- **Content:** string
- **Description:** Identifier for this ForeignKey node

### cdi:isComposedOf

- array of objects that include a reference to a cdif:RepresentedVariable in the DataStructure and a cdif:position property with an integer value that orders the variable in an order key structure.

### cdi:references

-- an object reference to a primary key in a different dataset. type: id-reference'

## Identifier

[↑ Back to TOC](#table-of-contents)

- Properties for a schema.org identifier (schema:PropertyValue pattern). **Union-type policy:** In CDIF profile UML models an attribute typed as schema:Identifier / schema:PropertyValue is represented by a single attribute of that class type. The JSON Schema implementation permits the property value to be EITHER a plain string (interpreted as the bare identifier value) OR a full schema:PropertyValue object (with explicit @type, propertyID, value). Consumers should accept either form.

### @type

- **Cardinality:** Optional
- **Content:** 'schema:PropertyValue'

### schema:propertyID

- **Cardinality:** Optional
- **Content:** string
- **Description:** In this context for the schema:PropertyValue, this field is an identifier for the identifier schema, e.g. DOI, ARK. Get values from https://registry.identifiers.org/registry/ for interoperability

### schema:value

- **Cardinality:** Optional
- **Content:** string
- **Description:** the identifier string. E.g. 10.5066/F7VX0DMQ

### schema:url

- **Cardinality:** Optional
- **Content:** string
- **Description:** web-resolveable string for the identifier; host name part is location of a resolver that will return some representation for the given identifier value. E.g. https://doi.org/10.5066/F7VX0DMQ

## IdentifierComponent

[↑ Back to TOC](#table-of-contents)

- Role given to a represented variable in the context of a long or wide data structure to identify the units associated to data points, and in dimensional and key value data structures to provide identifying fields for the instance values.

### @type

- **Cardinality:** Required
- **Content:** array of string

### @id

- **Cardinality:** Optional
- **Content:** string
- **Description:** Identifier for this IdentifierComponent node

### cdif:isDefinedBy_RepresentedVariable

- **Cardinality:** Required
- **Content:**  cdif:RepresentedVariable or object reference to cdif:Represented Variable

## MeasureComponent

[↑ Back to TOC](#table-of-contents)

- Role given to a represented variable in the context of a data structure to hold the observed/derived values.

### @type

- **Cardinality:** Required
- **Content:** array of string

### @id

- **Cardinality:** Optional
- **Content:** string
- **Description:** Identifier for this MeasureComponent node

### cdif:name

- **Cardinality:** Optional
- **Content:** array of string
- **Description:** Human understandable name (liguistic signifier, word, phrase, or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context provided to specify usage.

### cdi:identifier

- **Cardinality:** Optional
- **Content:** [object reference](#/$defs/Identifier)
- **Description:** Identifier for objects requiring short- or long-lasting referencing and management.

### cdif:isDefinedBy_RepresentedVariable

- **Cardinality:** Optional
- **Content:** cdif:RepresentedVariable or object reference to cdif:Represented Variable)

### cdi:semantic

- **Cardinality:** Optional
- **Content:** array of one of: string, [object reference](#/$defs/CdifDataStructureComponent_cdifConceptOrTerm)
- **Description:** Qualifies the purpose or use expressed as a paired external controlled vocabulary.

## PrimaryKey

[↑ Back to TOC](#table-of-contents)

-set of Variables that uniquely identify a data instance. Array order of cdif:isComposedOf items is the cdif:position; no intermediate ComponentPosition wrapper.

### @type

- **Cardinality:** Required
- **Content:** array of strings, contains 'cdif:PrimaryKey'

### @id

- **Cardinality:** Optional
- **Content:** string
- **Description:** Identifier for this PrimaryKey node

### cdif:isComposedOf

- array of objects that include a reference to a cdif:RepresentedVariable in the datastructure and a cdif:position property with an integer value that orders the variable in an order key structure.

## VariableDescriptorComponent

[↑ Back to TOC](#table-of-contents)

- Role given to a represented variable in the context of a data structure to provide codes for variable identification.

### @type

- **Cardinality:** Required
- **Content:** array of string

### @id

- **Cardinality:** Optional
- **Content:** string
- **Description:** Identifier for this VariableDescriptorComponent node

### cdif:isDefinedBy_DescriptorVariable

- **Cardinality:** Required
- **Content:** object
- **Description:** Variable that provides codes for variable identification in the context of a data structure. Descriptor Variables hold values which reference the logical variables in the data set, indicating which one the associated value in the corresponding Reference Variable is a measure/value for. Descriptor Variables are presentational variables found only in Long Data Sets.

### cdi:refersTo

- **Cardinality:** Optional
- **Content:** [object reference](#/$defs/CdifDataStructureComponent_id-reference)

### cdi:identifier

- **Cardinality:** Optional
- **Content:** [object reference](#/$defs/Identifier)
- **Description:** Identifier for objects requiring short- or long-lasting referencing and management.

### cdi:semantic

- **Cardinality:** Optional
- **Content:** array of one of: string, [object reference](#/$defs/CdifDataStructureComponent_cdifConceptOrTerm)
- **Description:** Qualifies the purpose or use expressed as a paired external controlled vocabulary.

## VariableValueComponent

[↑ Back to TOC](#table-of-contents)

- Role given to a represented variable in the context of a data structure to record values of multiple variables. The descriptor component value specifies the property that the variable value is asserting for the unit identified by the identifier component.

### @type

- **Cardinality:** Required
- **Content:** array of string, contains 'cdif:VariableValueComponent'

### @id

- **Cardinality:** Optional
- **Content:** string
- **Description:** Identifier for this node

### cdif:isDefinedBy_RepresentedVariable

- **Cardinality:** Optional
- **Content:** one of: object reference or #/$defs/CdifRepresentedVariable

### cdi:semantic

- **Cardinality:** Optional
- **Content:** array of one of: string, object reference, or #/$defs/cdifConceptOrTerm.
- **Description:** Qualifies the purpose or use expressed as a paired external controlled vocabulary.

# Provenance of the artifacts

[↑ Back to TOC](#table-of-contents)

The schema and SHACL files are generated from the canonical source register, [metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks):

- `cdifDataStructureStructuredSchema.json` ← `tools/resolve_schema.py cdifDataStructure`
- `dataStructureRules.shacl` ← `tools/validate_shacl.py cdifDataStructure --emit-shapes`

Source profile directory: `_sources/profiles/cdifProfile/cdifDataStructure/`.
