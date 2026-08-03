## July 19, 2026

"""
A Herbie template for Regional Deterministic Air Quality Analysis (RDAQA).

Meteorological Service of Canada (MSC)
The RDAQA is Canada's 10 km deterministic regional air quality analysis

Description: https://eccc-msc.github.io/open-data/msc-data/nwp_rdaqa/readme_rdaqa-datamart_en/
Data Source: https://dd.weather.gc.ca/today/model_rdaqa/

- Regional domain: https://dd.weather.gc.ca/{YYYYMMDD}/WXO-DD/model_rdaqa/10km/{HH}/

where `HH` is the models initialization time.

Data available for last 24 hours.
"""

_variable = {
    "FW_PM10",
    "FW-PM2.5",
    "PM2.5",
    "PM10",
    "NO2",
    "O3",
    "SO2",
    "NO",
    "Prelim_PM2.5",
    "Prelim_PM10",
    "Prelim_NO2",
    "Prelim_O3",
    "Prelim_SO2",
    "Prelim_NO",
}


class rdaqa:
    def template(self):
        if self.product is None:
            self.product = "10km"

        product_aliases = {
            "10km": "10km",
            "10km/grib2": "10km",
        }
        self.product = product_aliases.get(self.product, self.product)

        if self.product != "10km":
            raise ValueError(
                f"product={self.product} not recognized. Must be '10km/grib2' or '10km'"
            )

        if not hasattr(self, "variable"):
            print(
                f"RDAQA requires an argument for 'variable'. Here are some ideas:\n{_variable}."
            )
            print(
                f"For full list of files, see https://dd.weather.gc.ca/{self.date:%Y%m%d}/WXO-DD/model_rdaqa/10km/"
            )

        self.DESCRIPTION = "Regional Deterministic Air Quality Analysis (RDAQA)"
        self.DETAILS = {
            "Datamart product description": "https://eccc-msc.github.io/open-data/msc-data/nwp_rdaqa/readme_rdaqa-datamart_en/#data-location",
        }
        self.PRODUCTS = {
            "10km": "regional 10 km domain",
        }
        self.AVAILABLE_VARIABLES = sorted(_variable)

        # Handle MSC filename formatting rule (RDAQA- for preliminary vs RDAQA_ for standard)
        var_str = str(getattr(self, "variable", ""))
        sep = "-" if var_str.startswith("Prelim_") else "_"

        PATH = f"{self.date:%H}/{self.date:%Y%m%dT%HZ}_MSC_RDAQA{sep}{self.variable}_Sfc_RLatLon0.09_PT0H.grib2"
        self.SOURCES = {
            "msc": f"https://dd.weather.gc.ca/{self.date:%Y%m%d}/WXO-DD/model_rdaqa/{self.product}/{PATH}"
        }

        self.IDX_SUFFIX = [".grb2.idx", ".idx", ".grib.idx"]
        self.LOCALFILE = f"{self.get_remoteFileName}"
