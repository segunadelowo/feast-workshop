from datetime import timedelta

from feast import (
    FeatureView,
    Field,
)
from feast.types import Float32

from data_sources import *
from entities import *

driver_hourly_stats_view = FeatureView(
    name="driver_hourly_stats",
    description="Hourly features",
    entities=[driver],
    ttl=timedelta(seconds=8640000000),
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
        Field(name="miles_driven", dtype=Float32),
    ],
    online=True,
    source=driver_stats,
    tags={"production": "True"},
    owner="adelowo5@gmail.com",
)
