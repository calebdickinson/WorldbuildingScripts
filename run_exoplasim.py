# Run with: python run_exoplasim.py
import exoplasim as exo

model = exo.Model(resolution="T42",
                  outputtype=".nc",
                  layers=10,
                  ncpus=4,
                  precision=8,
                  crashtolerant=True)

model.configure(topomap="myworldclimate_surf_0129.sra",
                landmap="myworldclimate_surf_0172.sra",
                fixedorbit=True,
                physicsfilter='gp|exp|sp',
                wetsoil=True,
                vegetation=2,
                initgrowth=0.5,
                glaciers={'toggle': True, 'mindepth': 2, 'initialh': -1},
                ozone=True)

model.runtobalance(baseline=10, maxyears=50, minyears=20, clean=True)

model.finalize("myworld_t42_output", allyears=True, clean=True)