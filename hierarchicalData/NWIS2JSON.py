import csv
import json
import argparse
from collections import defaultdict




def csv_to_jsonld(csv_file, jsonld_file):
    context = {
        "schema": "http://schema.org/",
        "ex": "https://example.org/",
    }

    # Helper functions
    def ns_for(loc_id):
# return "usgs" if loc_id.startswith("USGS") else "azdeq"
        return "ex"

    def safe_float(val):
        try:
            return float(val) if val not in (None, "",) else None
        except ValueError:
            return None

    def clean_id(val):
        if not val:
            return "unknown"
        return str(val).strip().replace(" ", "_").replace("/", "-")

    # Group rows by location → project
    locations = defaultdict(lambda: defaultdict(list))

    rows = []
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
            loc_id = row.get("MonitoringLocationIdentifier", "").strip()
            # proj = (row.get("ProjectName") or "").strip() or "UnknownProject"
            proj = row.get("ActivityIdentifier", "").strip() or "UnknownActivity"
            locations[loc_id][proj].append(row)

    graph = []

    for loc_id, projects in locations.items():
        ns = ns_for(loc_id)
        # Use first row to get lat/lon and sample collection methods
        sample_methods = set()
        lat, lon = None, None
        proj_label = None
        for proj_rows in projects.values():
            for row in proj_rows:
                if row.get("Latitude"): lat = float(row["Latitude"])
                if row.get("Longitude"): lon = float(row["Longitude"])
                if row.get("SampleCollectionMethod"):
                    sample_methods.add(row["SampleCollectionMethod"])
                if row.get("ProjectName"): proj_label = row["ProjectName"]
                if row.get("ActivityConductingOrganizationText"): proj_org = row["ActivityConductingOrganizationText"]

        loc_node = {
            "@id": f"{ns}:MonitoringLocation/{loc_id}",
            "@type": f"{ns}:MonitoringLocation",
            "schema:locationName": loc_id,
            "schema:latitude": lat,
            "schema:longitude": lon,
            "ex:sampleCollectionMethod": list(sample_methods) if sample_methods else None,
            "projects": []
        }

        for proj_name, proj_rows in projects.items():
            proj_id = clean_id(proj_name)
            proj_node = {
                "@id": f"{ns}:Project/{proj_id}",
                "@type": "schema:Project",
                "schema:name": proj_label,
                "ex:organization": proj_org,
                "results": []
            }

            for row in proj_rows:
                result = {
                    "@id": f"{ns}:Result/{row.get('ResultIdentifier')}",
                    "@type": f"{ns}:Result",
                    "schema:value": safe_float(row.get("ResultMeasureValue")),
                    "schema:unitCode": row.get("UOM"),
                    "schema:dateObserved": row.get("ActivityDateTime"),
                    f"{ns}:characteristic": {
                        "@id": f"{ns}:Characteristic/{clean_id(row.get('CharacteristicURI') or row.get('Characteristic'))}",
                        "schema:name": row.get("Characteristic")
                    },
                    f"{ns}:method": {
                        "@id": f"{ns}:AnalyticalMethod/{clean_id(row.get('ResultAnalyticalMethod') or row.get('MethodName'))}",
                        "schema:name": row.get("MethodName")
                    },

                    "ex:resultSampleFractionText": row.get("ResultSampleFractionText") or None,
                    "ex:resultValueTypeName": row.get("ResultValueTypeName") or None,
                    "ex:comment": row.get("ResultCommentText") or None,
                    **({"ex:depthMeasure": row.get("DepthMeasure")} if row.get("DepthMeasure") else {}),

                }
                proj_node["results"].append(result)

            loc_node["projects"].append(proj_node)

        graph.append(loc_node)

    jsonld = {
        "@context": context,
        "@graph": graph
    }

    with open(jsonld_file, "w", encoding="utf-8") as out:
        json.dump(jsonld, out, indent=2, ensure_ascii=False)

    print(f"JSON-LD written to {jsonld_file}")


def main():
    csv_file = "C:/Users/smrTu/OneDrive/Documents/GithubC/CDIF/integrationPublic/LongData/NWISWaterQualityData.csv"
    jsonld_file = "testJSON.json"
#   parser = argparse.ArgumentParser(description="Transform denormalized water quality CSV to grouped JSON-LD by location and project.")
#    parser.add_argument("input_csv", help="Path to input CSV file", default=csv_file)
#    parser.add_argument("output_jsonld", help="Path to output JSON-LD file",default=jsonld_file)
#    args = parser.parse_args()
    csv_to_jsonld(csv_file, jsonld_file)

if __name__ == "__main__":
    main()