"""
pdfからcsvデータに変換する用のスクリプト
"""

import tabula
import pandas as pd

tabula.convert_into(
    "itiran1124.pdf",
    "saitama.csv",
    output_format="csv",
    pages="all")
