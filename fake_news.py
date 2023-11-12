#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 01:05:07 2023

@author: fibonacci
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data =[
       Date,Agent_name,Response,uid,Converted,average_payment_delay_before_weekly,revenue_per_day_before_weekly,revenue_per_day_after_weekly
       8/6/2023,Rose_Kanyiri,No-financial_constraints,126022,No,2,43.00,43.00
       7/6/2023,Allan_Mutuota,No-low_priority,101372,No,1,33.00,33.00
       7/5/2023,Greyson_Ochanda,No-low_priority,104620,No,5,28.00,28.00
       8/31/2023,Allan_Mutuota,No-service_dissatisfaction,28997,No,3,41.00,41.00
       9/13/2023,Rose_Kanyiri,No-low_priority,76405,No,4,29.00,29.00
       9/15/2023,Lutta_Mboya,Yes-affordable,133146,No,6,29.00,29.00
       7/13/2023,Allan_Mutuota,No-low_priority,113507,No,2,29.00,29.00
       9/22/2023,Lutta_Mboya,Yes-affordable,73528,No,6,24.00,24.00
       6/14/2023,Allan_Mutuota,Yes-affordable,75402,No,6,35.00,35.00
       8/2/2023,Allan_Mutuota,Not_reachable,93169,No,6,26.00,26.00
       8/20/2023,Greyson_Ochanda,No-low_priority,127597,No,1,47.00,47.00
       7/24/2023,Greyson_Ochanda,Yes-affordable,75872,No,2,33.00,33.00
       8/24/2023,Rose_Kanyiri,No-low_priority,65697,No,7,24.00,24.00
       8/28/2023,Allan_Mutuota,No-financial_constraints,61670,No,6,47.00,47.00
       9/6/2023,Lutta_Mboya,No-financial_constraints,37851,No,3,24.00,24.00
       9/28/2023,Lutta_Mboya,Yes-affordable,40690,Yes,4,25.00,50.00
       7/15/2023,Rose_Kanyiri,No-financial_constraints,30863,No,5,45.00,45.00
       9/13/2023,Allan_Mutuota,No-financial_constraints,110000,No,1,46.00,46.00
       7/13/2023,Allan_Mutuota,No-low_priority,28145,No,4,24.00,24.00
       6/18/2023,Rose_Kanyiri,Yes-affordable,83395,No,3,43.00,43.00
]
# Read the TSV data into a pandas DataFrame
df = pd.read_csv(pd.compat.StringIO(data), sep='\t')