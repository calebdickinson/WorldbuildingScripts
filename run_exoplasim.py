# Run with: python run_exoplasim.py
# python ~/WorldbuildingScripts/koppenpasta.py runs koppen maps
# Input NetCDF filename or folder of files: myworld_output/MOST_EXP
# Set interpolation rescaling factor: 32 (32 x 128 = 4096)
# Topography map filename: heightmapOfficial4096.png
# Highest Map Elevation (m): 4572
# Lowest Map Elevation (m): 0
# Sea Level (m): 0
# Surface Gravity (m/s^2): 9.80665
# Black: 0, White: 255 Example: Entering '128' will mark values 128 and below as ocean: 16
# Input latitude resolution Example: '64' will produce a 128*64 output. Resolution: 64
# Enter beginning ocean value: 16

import exoplasim as exo

model = exo.Model(resolution="T42",
                  outputtype=".nc",
                  layers=10,
                  ncpus=4,
                  precision=8,
                  crashtolerant=True)

model.configure(topomap="HeightMapOfficial_surf_0129.sra",
                landmap="HeightMapOfficial_surf_0172.sra",
                pN2=0.7809,
                pO2=0.2095,
                pAr=0.0093,
                pCO2=1000e-6,
                fixedorbit=True,
                physicsfilter='gp|exp|sp',
                wetsoil=True,
                vegetation=2,
                initgrowth=0.5,
                glaciers={'toggle': True, 'mindepth': 2, 'initialh': -1},
                ozone=True)

model.runtobalance(baseline=10, maxyears=50, minyears=20, clean=True)

model.finalize("myworld_output", allyears=True, clean=True)