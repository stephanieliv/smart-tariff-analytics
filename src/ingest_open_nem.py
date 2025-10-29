from openelectricity import OEClient
from openelectricity.types import DataMetric
from datetime import datetime
import pandas as pd
import requests
import os
import pathlib

# 1️⃣ Test your API connection
api_key = os.getenv("OPENNEM_API_KEY")
test_url = "https://api.openelectricity.org.au/v4/networks"
headers = {"Authorization": f"Bearer {api_key}"}

r = requests.get(test_url, headers=headers)
print("Connection test:", r.status_code)
networks = r.json()
print("Networks available:", [n["code"] for n in networks])

# 2️⃣ Initialize OEClient properly
client = OEClient(
    api_key=api_key,
    base_url="https://api.openelectricity.org.au/v4"
)

# 3️⃣ Fetch sample network data from NEM
response = client.get_network_data(
    network_code="NEM",
    metrics=[DataMetric.POWER],
    interval="1h",
    date_start=datetime(2024, 1, 1),
    date_end=datetime(2024, 1, 2),
    primary_grouping="network_region",
    secondary_grouping="fueltech"
)

# # 4️⃣ Display sample data
# for ts in response.data:
#     print(f"\nMetric: {ts.metric}")
#     for result in ts.results:
#         for dp in result.data[:5]:  # only first 5 points
#             print(f"  {dp.timestamp}: {dp.value}")

# 4️⃣ Flatten response into a dataframe
records = []
for ts in response.data:
    metric_name = ts.metric
    for result in ts.results:
        groups = getattr(result, "groups", {}) or {}
        region = groups.get("network_region")
        fueltech = groups.get("fueltech")
        for dp in result.data:
            records.append({
                "timestamp": dp.timestamp,
                "metric": metric_name,
                "region": region,
                "fueltech": fueltech,
                "value": dp.value
            })

df = pd.DataFrame(records)
print(f"✅ Retrieved {len(df)} rows")

# 5️⃣ Save to local parquet
output_dir = pathlib.Path("data/raw/open_electricity")
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / "nem_power_2024-01-01_to_2024-01-02.parquet"

df.to_parquet(output_path, index=False)
print(f"💾 Saved data to {output_path}")

# Optional: Preview few rows
print(df.head())