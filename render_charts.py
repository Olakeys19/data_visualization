"""Run each Matplotlib script from src/ and save its figure(s) to charts/ instead of showing them."""
import builtins
import os
import runpy
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")
OUT = os.path.join(HERE, "charts")
SCRIPTS = ["mpl_squares", "scatter_squares", "cubes_plot", "highs_lows", "rw_visual", "rw_visual2", "die_visual_mp"]

os.chdir(SRC)
sys.path.insert(0, SRC)
builtins.input = lambda *a, **k: "n"   # answer "no" to "Make another walk?" prompts

for name in SCRIPTS:
    count = 0

    def save(*args, **kwargs):
        global count
        count += 1
        path = os.path.join(OUT, f"{name}.png" if count == 1 else f"{name}_{count}.png")
        plt.gcf().savefig(path, dpi=110, bbox_inches="tight")
        plt.close("all")

    plt.show = save
    plt.savefig = lambda *a, **k: None   # don't overwrite files in src/
    try:
        runpy.run_path(os.path.join(SRC, f"{name}.py"), run_name="__main__")
        print(f"{name}: saved {count} chart(s)")
    except Exception as e:
        print(f"{name}: FAILED {type(e).__name__}: {e}")
