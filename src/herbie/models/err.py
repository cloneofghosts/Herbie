## August 15, 2026
from datetime import timedelta

"""
A Herbie template for the NOAA Enterprise Rain Rate (ERR).

The ERR system provides high-resolution, real-time rain rate data worldwide. It integrates data from five different satellite sources to produce a comprehensive view of precipitation especially in regions with limited ground-based observations.

Description: https://www.ospo.noaa.gov/products/atmosphere/err/
Data Source: https://noaa-enterprise-rainrate-pds.s3.amazonaws.com/index.html

- Blended domain: https://noaa-enterprise-rainrate-pds.s3.amazonaws.com/BLEND/RainRate-Blend-INST/{YYYY}/{MM}/{DD}/RRQPE-INST-GLB-{product}_v1r1_blend_s{YYYYMMDDHHMMSS}_e{YYYYMMDDHHMMSS}_c{YYYYMMDDHHMMSS}.nc

where product is the ERR product, YYYY is the year, MM is the month, DD is the day, HHMMSS is the time.
"""

class err:
    def template(self):
        if self.product is None:
            self.product = "5"

        self.DESCRIPTION = "NOAA Enterprise Rain Rate (ERR)"
        self.DETAILS = {
            "Project description": "https://www.ospo.noaa.gov/products/atmosphere/err/",
            "Data source": "https://noaa-enterprise-rainrate-pds.s3.amazonaws.com/index.html",
        }
        self.PRODUCTS = {
            "2": "Global 0.02-degree grid (~2km)",
            "3": "Global 0.25-degree grid (~25km)",
            "4": "Global 0.10-degree grid (~10km)",
            "5": "Global 0.05-degree grid (~5km operational standard)",
        }

        # Calculate observation end time (9 minutes and 59 seconds after start)
        end_time = self.date + timedelta(minutes=9, seconds=59)

        # Format 15-digit start and end strings (YYYYMMDDHHMMSS + tenths digit)
        s_str = f"{self.date:%Y%m%d%H%M%S}0"
        e_str = f"{end_time:%Y%m%d%H%M%S}9"

        # Use wildcard '*' for 'c' timestamp so Herbie resolves the actual creation time from S3
        filename = f"RRQPE-INST-GLB-{self.product}_v1r1_blend_s{s_str}_e{e_str}_c*.nc"
        PATH = f"{self.date:%Y}/{self.date:%m}/{self.date:%d}/{filename}"

        self.SOURCES = {
            "aws": f"https://noaa-enterprise-rainrate-pds.s3.amazonaws.com/BLEND/RainRate-Blend-INST/{PATH}"
        }

        self.LOCALFILE = f"{self.get_remoteFileName}"