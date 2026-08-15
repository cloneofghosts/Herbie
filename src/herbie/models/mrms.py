## August 15, 2026

"""
A Herbie template for the NOAA Multi-Radar/Multi-Sensor System (MRMS).

The MRMS system provides high-resolution, real-time radar and sensor data for the contiguous United States (CONUS). It integrates data from multiple radar sources and other sensors to produce a comprehensive view of precipitation, storm structure, and other meteorological phenomena.

Description: https://www.nssl.noaa.gov/projects/mrms/
Data Source: https://noaa-mrms-pds.s3.amazonaws.com/index.html

- CONUS domain: https://noaa-mrms-pds.s3.amazonaws.com/{product}/{variable}/{YYYYMMDD}/MRMS_{variable}_{YYYYMMDD}-{HHMMSS}.grib2.gz

where `product` is the MRMS product, `variable` is the MRMS variable, `YYYYMMDD` is the date, `HHMMSS` is the time.
"""

_variable = {
    "NLDN_CG_001min_AvgDensity",
    "NLDN_CG_005min_AvgDensity",
    "NLDN_CG_015min_AvgDensity",
    "NLDN_CG_030min_AvgDensity",
    "LightningProbabilityNext30minGrid",
    "LightningProbabilityNext60minGrid",
    "LightningJumpGrid",
    "LightningJumpGrid_Max_005min",
    "MergedAzShear0to2kmAGL",
    "MergedAzShear3to6kmAGL",
    "RotationTrack30min",
    "RotationTrack60min",
    "RotationTrack120min",
    "RotationTrack240min",
    "RotationTrack360min",
    "RotationTrack1440min",
    "RotationTrackML30min",
    "RotationTrackML60min",
    "RotationTrackML120min",
    "RotationTrackML240min",
    "RotationTrackML360min",
    "RotationTrackML1440min",
    "SHI",
    "POSH",
    "MESH",
    "MESHMax30min",
    "MESHMax60min",
    "MESHMax120min",
    "MESHMax240min",
    "MESHMax360min",
    "MESHMax1440min",
    "VIL_Max_120min",
    "VIL_Max_1440min",
    "VIL",
    "VIL_Density",
    "VII",
    "EchoTop_18",
    "EchoTop_30",
    "EchoTop_50",
    "EchoTop_60",
    "H50AboveM20C",
    "H50Above0C",
    "H60AboveM20C",
    "H60Above0C",
    "Reflectivity_0C",
    "Reflectivity_-5C",
    "Reflectivity_-10C",
    "Reflectivity_-15C",
    "Reflectivity_-20C",
    "ReflectivityAtLowestAltitude",
    "ReflectivityAtLowestAltitude5km",
    "MergedReflectivityAtLowestAltitude",
    "PrecipFlag",
    "PrecipRate",
    "RadarOnly_QPE_01H",
    "RadarOnly_QPE_03H",
    "RadarOnly_QPE_06H",
    "RadarOnly_QPE_12H",
    "RadarOnly_QPE_24H",
    "RadarOnly_QPE_48H",
    "RadarOnly_QPE_72H",
    "MultiSensor_QPE_01H_Pass1",
    "MultiSensor_QPE_03H_Pass1",
    "MultiSensor_QPE_06H_Pass1",
    "MultiSensor_QPE_12H_Pass1",
    "MultiSensor_QPE_24H_Pass1",
    "MultiSensor_QPE_48H_Pass1",
    "MultiSensor_QPE_72H_Pass1",
    "MultiSensor_QPE_01H_Pass2",
    "MultiSensor_QPE_03H_Pass2",
    "MultiSensor_QPE_06H_Pass2",
    "MultiSensor_QPE_12H_Pass2",
    "MultiSensor_QPE_24H_Pass2",
    "MultiSensor_QPE_48H_Pass2",
    "MultiSensor_QPE_72H_Pass2",
    "SyntheticPrecipRateID",
    "RadarOnly_QPE_15M",
    "RadarOnly_QPE_Since12Z",
    "Model_SurfaceTemp",
    "Model_WetBulbTemp",
    "WarmRainProbability",
    "Model_0degC_Height",
    "BrightBandTopHeight",
    "BrightBandBottomHeight",
    "RadarQualityIndex",
    "GaugeInflIndex_01H_Pass1",
    "GaugeInflIndex_03H_Pass1",
    "GaugeInflIndex_06H_Pass1",
    "GaugeInflIndex_12H_Pass1",
    "GaugeInflIndex_24H_Pass1",
    "GaugeInflIndex_48H_Pass1",
    "GaugeInflIndex_72H_Pass1",
    "SeamlessHSR",
    "SeamlessHSRHeight",
    "RadarAccumulationQualityIndex_01H",
    "RadarAccumulationQualityIndex_03H",
    "RadarAccumulationQualityIndex_06H",
    "RadarAccumulationQualityIndex_12H",
    "RadarAccumulationQualityIndex_24H",
    "RadarAccumulationQualityIndex_48H",
    "RadarAccumulationQualityIndex_72H",
    "GaugeInflIndex_01H_Pass2",
    "GaugeInflIndex_03H_Pass2",
    "GaugeInflIndex_06H_Pass2",
    "GaugeInflIndex_12H_Pass2",
    "GaugeInflIndex_24H_Pass2",
    "GaugeInflIndex_48H_Pass2",
    "GaugeInflIndex_72H_Pass2",
    "MergedReflectivityQC",
    "MergedRhoHV",
    "MergedZdr",
    "MergedReflectivityQCComposite",
    "MergedReflectivityQCComposite5km",
    "HeightCompositeReflectivity",
    "LowLevelCompositeReflectivity",
    "HeightLowLevelCompositeReflectivity",
    "LayerCompositeReflectivity_Low",
    "LayerCompositeReflectivity_High",
    "LayerCompositeReflectivity_Super",
    "CREF_1HR_MAX",
    "LayerCompositeReflectivity_ANC",
    "BREF_1HR_MAX",
    "MergedBaseReflectivityQC",
    "MergedReflectivityComposite",
    "MergedReflectivityQComposite",
    "MergedBaseReflectivity",
    "FLASH_CREST_MAXUNITSTREAMFLOW",
    "FLASH_CREST_MAXSTREAMFLOW",
    "FLASH_CREST_MAXSOILSAT",
    "FLASH_SAC_MAXUNITSTREAMFLOW",
    "FLASH_SAC_MAXSTREAMFLOW",
    "FLASH_SAC_MAXSOILSAT",
    "FLASH_QPE_ARI30M",
    "FLASH_QPE_ARI01H",
    "FLASH_QPE_ARI03H",
    "FLASH_QPE_ARI06H",
    "FLASH_QPE_ARI12H",
    "FLASH_QPE_ARI24H",
    "FLASH_QPE_ARIMAX",
    "FLASH_QPE_FFG01H",
    "FLASH_QPE_FFG03H",
    "FLASH_QPE_FFG06H",
    "FLASH_QPE_FFGMAX",
    "FLASH_HP_MAXUNITSTREAMFLOW",
    "FLASH_HP_MAXSTREAMFLOW",
    "ANC_ConvectiveLikelihood",
    "ANC_FinalForecast",
    "LVL3_HREET",
    "LVL3_HighResVIL",
}

_level = {
    "00.00",
    "00.50",
    "00.75",
    "01.00",
    "01.25",
    "01.50",
    "01.75",
    "02.00",
    "02.25",
    "02.50",
    "02.75",
    "03.00",
    "03.50",
    "04.00",
    "04.50",
    "05.00",
    "05.50",
    "06.00",
    "06.50",
    "07.00",
    "07.50",
    "08.00",
    "08.50",
    "09.00",
    "10.00",
    "11.00",
    "12.00",
    "13.00",
    "14.00",
    "15.00",
    "16.00",
    "17.00",
    "18.00",
    "19.00",
    "scale_1",
}

class mrms:
    def template(self):
        if self.product is None:
            self.product = "CONUS"

        if not hasattr(self, "variable"):
            print(
                f"MRMS requires an argument for 'variable'. Here are some ideas:\n{_variable}."
            )
            print(
                f"For full list of files, see https://noaa-mrms-pds.s3.amazonaws.com/{self.product}/"
            )

        if not hasattr(self, "level"):
            print(
                f"MRMS requires an argument for 'level'. Here are some ideas:\n{_level}."
            )

        self.DESCRIPTION = "NOAA Multi-Radar/Multi-Sensor System (MRMS)"
        self.DETAILS = {
            "Project description": "https://www.nssl.noaa.gov/projects/mrms/",
            "Data source": "https://noaa-mrms-pds.s3.amazonaws.com/index.html",
        }
        self.PRODUCTS = {
            "ALASKA": "Alaska domain",
            "CARIB": "Caribbean domain",
            "CONUS": "Contiguous United States domain",
            "GUAM": "Guam domain",
            "HAWAII": "Hawaii domain",
        }
        self.AVAILABLE_VARIABLES = sorted(_variable)

        PATH = f"{self.date:%Y%m%d}/MRMS_{self.variable}_{self.level}_{self.date:%Y%m%d}-{self.date:%H%M%S}.grib2.gz"
        self.SOURCES = {
            "aws": f"https://noaa-mrms-pds.s3.amazonaws.com/{self.product}/{self.variable}/{PATH}"
        }

        self.IDX_SUFFIX = [".grb2.idx", ".idx", ".grib.idx"]
        self.LOCALFILE = f"{self.get_remoteFileName}"
