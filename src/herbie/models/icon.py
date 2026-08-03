## August 3, 2026

"""
A Herbie template for the Icosahedral Nonhydrostatic (ICON) model.

Deutscher Wetterdienst (DWD)
The ICON is a global numerical weather prediction model.

Description: https://www.dwd.de/EN/research/weatherforecasting/num_modelling/01_num_weather_prediction_modells/icon_description.html
Data Source: https://opendata.dwd.de/weather/nwp/icon/grib/

- Global domain: https://opendata.dwd.de/weather/nwp/icon/grib/{HH}/

where `HH` is the models initialization time.

Data available for last 24 hours.
"""

_variable = {
    "alb_rad",
    "alb_seaice",
    "alhfl_s",
    "ashfl_s",
    "asob_s",
    "asob_s_cs",
    "asob_t",
    "aswdifd_s",
    "aswdifu_s",
    "aswdir_s",
    "athb_s",
    "athb_t",
    "aumfl_s",
    "avmfl_s",
    "c_t_lk",
    "cape_con",
    "cape_ml",
    "clat",
    "clc",
    "clch",
    "clcl",
    "clcm",
    "clct",
    "clct_mod",
    "cldepth",
    "clon",
    "depth_lk",
    "elat",
    "elon",
    "evap_pl",
    "fi",
    "fr_ice",
    "fr_lake",
    "fr_land",
    "freshsnw",
    "h_ice",
    "h_ml_lk",
    "h_snow",
    "hbas_con",
    "hhl",  
    "hsnow_max",
    "hsurf",
    "htop_con",
    "htop_dc",
    "hzerocl",
    "lai",  
    "ndviratio",
    "p",
    "plcov",
    "pmsl",
    "ps",
    "qc",
    "qi",
    "qv",
    "qv_s",
    "rain_con",
    "rain_gsp",
    "relhum",
    "relhum_2m",
    "rho_snow",
    "rootdp",
    "runoff_g",
    "runoff_s",
    "snoag",
    "snow_con",
    "snow_gsp",
    "soiltyp",
    "t",
    "t_2m",
    "t_bot_lk",
    "t_g",
    "t_ice",
    "t_mnw_lk",
    "t_snow",
    "t_so",
    "t_wml_lk",
    "tch",
    "tcm",
    "td_2m",
    "tke",
    "tmax_2m",
    "tmin_2m",
    "tot_prec",
    "tqc",
    "tqc_dia",
    "tqi",
    "tqi_dia",
    "tqr",
    "tqs",
    "tqv",
    "u",
    "u_10m",
    "v",
    "v_10m",
    "vmax_10m",
    "w",
    "w_i",
    "w_snow",
    "w_so",
    "w_so_ice",
    "ww",
    "z0",
}

class icon:
    def template(self):
        if self.product is None:
            self.product = "single-level"

        # Handle potential product aliases
        product_aliases = {
            "icon": "single-level",
            "icon_global": "single-level",
            "single": "single-level",
            "model": "model-level",
            "invariant": "time-invariant",
        }
        self.product = product_aliases.get(self.product, self.product)

        if self.product not in ["single-level", "model-level", "time-invariant"]:
            raise ValueError(
                f"product={self.product} not recognized. Must be 'single-level', 'model-level', or 'time-invariant'"
            )

        if not hasattr(self, "variable"):
            print(
                f"ICON requires an argument for 'variable'. Here are some ideas:\n{_variable}."
            )
            print(
                f"For full list of files, see https://opendata.dwd.de/weather/nwp/icon/grib/{self.date:%H}/"
            )

        self.DESCRIPTION = "Icosahedral Nonhydrostatic (ICON) model"
        self.DETAILS = {
            "Model description": "https://www.dwd.de/EN/research/weatherforecasting/num_modelling/01_num_weather_prediction_modells/icon_description.html",
        }
        self.PRODUCTS = {
            "single-level": "Global ICON single-level / surface variables",
            "model-level": "Global ICON icosahedral model-level 3D variables",
            "time-invariant": "Time-invariant surface parameters (e.g. HSURF, CLAT, CLON)",
        }
        
        self.AVAILABLE_VARIABLES = sorted(_variable)

        upper_var = self.variable.upper()
        base_path = f"{self.variable}/icon_global_icosahedral_{self.product}_{self.date:%Y%m%d%H}"

        if self.product == "time-invariant":
            PATH = f"{base_path}_{upper_var}.grib2.bz2"
        elif self.product == "single-level":
            PATH = f"{base_path}_{self.fxx:03d}_{upper_var}.grib2.bz2"
        elif self.product == "model-level":
            # Safely check if level was passed to Herbie (defaults to None if missing)
            level = getattr(self, "level", None)

            if level is None:
                PATH = f"{base_path}_{self.fxx:03d}_{upper_var}.grib2.bz2"
            else:
                PATH = f"{base_path}_{self.fxx:03d}_{level}_{upper_var}.grib2.bz2"
        
        self.SOURCES = {
            "dwd": f"https://opendata.dwd.de/weather/nwp/icon/grib/{self.date:%H}/{PATH}",
        }

        self.IDX_SUFFIX = [".bz2.idx", ".grib2.bz2.idx", ".grb2.idx", ".idx"]
        self.LOCALFILE = f"{self.get_remoteFileName}"