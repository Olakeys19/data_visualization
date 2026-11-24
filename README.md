# Data Visualisation Projects

Charts and maps built with Python, Matplotlib and Pygal while working through *Python Crash Course* (SIWES II training).

**View the gallery:** https://olakeys-data-visualisation.netlify.app

## What's inside

| Topic | Scripts |
|---|---|
| Matplotlib basics | `mpl_squares.py`, `scatter_squares.py`, `cubes_plot.py` |
| Random walks | `random_walk.py`, `rw_visual.py`, `rw_visual2.py`, `rw_visual_pg.py` |
| Rolling dice | `die.py`, `die_visual.py`, `dice_visual.py`, `three_dice.py`, `two_d8.py`, `different_dice.py`, `die_visual_mp.py` |
| Weather data (CSV) | `highs_lows.py` with `sitka_weather_*.csv` and `death_valley_2014.csv` |
| World maps (JSON) | `world_population.py`, `americas.py`, `na_populations.py`, `country_codes.py` |
| Web APIs | `working_with_APIs/python_repos.py`, `hn_submissions.py`, `bar_descriptions.py` |

All the Python source is in [`src/`](src). The gallery website is in [`site/`](site).

## Running the scripts

```bash
pip install matplotlib pygal pygal_maps_world requests
cd src
python rw_visual.py
```

`render_charts.py` runs the Matplotlib scripts without opening windows and saves each chart as an image for the gallery.
