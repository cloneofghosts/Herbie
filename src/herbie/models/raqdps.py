## Based on the Pirate Weather RAQDPS template.
## July 19, 2026

"""
A Herbie template for the Regional Air Quality Deterministic Prediction System (RAQDPS).

Meteorological Service of Canada (MSC)
The RAQDPS is Canada's 10 km deterministic regional air quality model

Description: https://eccc-msc.github.io/open-data/msc-data/nwp_raqdps/readme_raqdps-datamart_en/
Data Source: https://dd.weather.gc.ca/today/model_raqdps/

- Regional domain: https://dd.weather.gc.ca/{YYYYMMDD}/WXO-DD/model_raqdps/10km/grib2/{HH}/{hhh}

where `HH` is the models initialization time and `hhh` is the forecast lead time.

Data available for last 24 hours.

Levels (match Datamart filenames exactly)
-----------------------------------------
Other levels: 'Sfc' or 'EAtm'
"""

_variable = {
    "PM2.5",
    "PM10",
    "NO2",
    "O3",
    "SO2",
    "NO",
    "PM2.5-WildfireSmokePlume",
    "PM10-WildfireSmokePlume",
}

_level = {
    # Other levels
    "Sfc",
    "EAtm",
}


class raqdps:
    def template(self):
        if self.product is None:
            self.product = "10km/grib2"

        product_aliases = {
            "10km": "10km/grib2",
            "10km/grib2": "10km/grib2",
        }
        self.product = product_aliases.get(self.product, self.product)

        if self.product != "10km/grib2":
            raise ValueError(
                f"product={self.product} not recognized. Must be '10km/grib2' or '10km'"
            )

        if not hasattr(self, "variable"):
            print(
                f"RAQDPS requires an argument for 'variable'. Here are some ideas:\n{_variable}."
            )
            print(
                f"For full list of files, see https://dd.weather.gc.ca/{self.date:%Y%m%d}/WXO-DD/model_raqdps/10km/"
            )
        if not hasattr(self, "level"):
            print(
                f"RAQDPS requires an argument for 'level'. Here are some ideas:\n{_level}"
            )
            print(
                f"For full list of files, see https://dd.weather.gc.ca/{self.date:%Y%m%d}/WXO-DD/model_raqdps/10km/"
            )

        self.DESCRIPTION = "Regional Air Quality Deterministic Prediction System (RAQDPS)"
        self.DETAILS = {
            "Datamart product description": "https://eccc-msc.github.io/open-data/msc-data/nwp_raqdps/readme_raqdps-datamart_en/#data-location",
        }
        self.PRODUCTS = {
            "10km/grib2": "regional 10 km domain",
        }
        self.AVAILABLE_VARIABLES = sorted(_variable)
        self.AVAILABLE_LEVELS = sorted(_level)

        PATH = f"{self.date:%H}/{self.fxx:03d}/{self.date:%Y%m%dT%HZ}_MSC_RAQDPS_{self.variable}_{self.level}_RLatLon0.09_PT{self.fxx:03d}H.grib2"
        self.SOURCES = {
            "msc": f"https://dd.weather.gc.ca/{self.date:%Y%m%d}/WXO-DD/model_raqdps/{self.product}/{PATH}"
        }

        self.IDX_SUFFIX = [".grb2.idx", ".idx", ".grib.idx"]
        self.LOCALFILE = f"{self.get_remoteFileName}"
