# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.1
#   kernelspec:
#     display_name: 'Python 3.7.6 64-bit (''base'': conda)'
#     language: python
#     name: python37664bitbasecondac5c9ea5e1be34210b10b0adf3cfc2816
# ---

# %% [markdown]
# # 世界地图

# %% [markdown]
# 导入模块。

# %%
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# 读入内置世界地图。

# %%
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# %% [markdown]
# 去除南极洲。

# %%
world = world[world.continent != 'Antarctica']

# %% [markdown]
# 更改投影。

# %%
world = world.to_crs("EPSG:3395")

# %% [markdown]
# 查看数据。

# %%
world

# %% [markdown]
# 初步查看地图。

# %%
world.plot()

# %% [markdown]
# 查看国家或地区列表。

# %%
np.unique(world.name)

# %% [markdown]
# 给国家或地区赋值，存入表格。

# %%
country_number = {'United States of America': 144060,
                  'Italy': 97689,
                  'Spain': 85199,
                  'China': 81470,
                  'Taiwan': 81470,
                  'Germany': 63929,
                  'Iran': 41495,
                  'France': 40174,
                  'United Kingdom': 22141,
                  'Switzerland': 15668,
                  'Belgium': 11899,
                  'Netherlands': 11750,
                  'South Korea': 9661,
                  'Canada': 6671,
                  'Norway': 4436,
                  'Brazil': 4330,
                  'Australia': 4247,
                  'Sweden': 4106,
                  'Japan': 1866,
                  'Russia': 1836,
                  }

df_country_number = pd.DataFrame(
    country_number.items(), columns=['name', 'number'])

# %% [markdown]
# 数据表格和地理表格合并。

# %%
world = pd.merge(world, df_country_number, on='name', how='left')

# %% [markdown]
# 填补空缺数字。

# %%
world['number'] = world['number'].fillna(0).astype('int')

# %% [markdown]
# 绘图。

# %%
fig, ax = plt.subplots(figsize=(15, 10), dpi=200)
world.plot(ax=ax,
           linewidth=0.2, edgecolor='gray',
           column='number', cmap='Reds',
           legend=True)

# %% [markdown]
# 去除边边框和坐标轴，加标题。

# %%
fig, ax = plt.subplots(figsize=(15, 10), dpi=200)
world.plot(ax=ax,
           linewidth=0.2, edgecolor='gray',
           column='number', cmap='Reds',
           legend=True)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

ax.set_title(
    'Confirmed cases of COVID-19 per selected country (20200330)', size=20)
