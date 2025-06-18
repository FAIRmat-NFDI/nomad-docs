# Prepare Gromacs trajectories for upload to NOMAD

**Options 1 to 3** rely only on Gromacs on-board tools: [`gmx trjconv`](https://manual.gromacs.org/current/onlinehelp/gmx-trjconv.html), [`gmx editconv`](https://manual.gromacs.org/current/onlinehelp/gmx-editconf.html), and [`gmx make_ndx`](https://manual.gromacs.org/current/onlinehelp/gmx-make_ndx.html).
**Option 4** uses [_MDAnalysis_](https://docs.mdanalysis.org/stable/index.html) to process the trajectory.

## 1. Reduce the number of frames in the trajectory

Specify which time steps to keep by only copying every n-th frame:

- `gmx trjconv -f [<.xtc/.trr/...>] -dt n -o [<.xtc/.trr/...>]`

## 2. Remove solvent from the trajectory file using Gromacs tools

#### **WARNING: May not work if more than one solute type need to be retained!!!**

(E.g. a complex of two different molecules.)

- Specify elements in your system to retain in the index file:
  `gmx make_ndx -f original.tpr -o modified.ndx`
- Remove all other parts of the system from the trajectory:
  `gmx trjconv -f original.xtc -o modified.xtc -n modified.ndx`
- Remove all other parts of the system from the _\*.gro_ file:
  `gmx editconf -f original.gro -o modified.gro -n modified.ndx`
- Remove all other parts of the system from the _\*.tpr_ file:
  `gmx convert-tpr -s original.tpr -o modified.tpr -n modified.ndx`

## 3. Manually remove solvent from the trajectory

- Manually delete solvent entries from \*_.top_ file using a text editor:

  - Remove solvent entry under `[ molecules ]`.
  - (Optional: Remove solvent topology by deleting the corresponding sections or _#include solvent.itp_ statements.)
  - **The name of the [ moleculetype ] in the _\*.top_ file defines the name of the system component in the NOMAD entry!**

- Adjust \*_.mdp_ file
    - Remove solvent group(s) for temperature (pressure) coupling.
   _Group names must match either [moleculetype] names or custom index group names._
- Manually delete solvent entries from index file:
    - Remove solvent indices from `[ system ]`.
    - Remove solvent indices from `[ other ]`.
    - Remove section corresponding to your solvent.
    - (Optional: remove indices and sections corresponding to ions.)
- Generate new _\*.gro_ file:
  `gmx editconf -f original.gro -o modified.gro -n modified.ndx`
- Generate new _\*.tpr_ file from edited _\*.top_ and _\*.mdp_ files:
  `gmx grompp -f modified.mdp -c modified.gro -p modified.top -o modified.tpr`
- Remove all other parts of the system from the trajectory:
  `gmx trjconv -f original.xtc -o modified.xtc -n modified.ndx`

## 4. Use MDAnalysis to modify your trajectory and remove solvent

```python
import MDAnalysis as mda

# Set up trajectory and topology files and locations for the conversion

dir_path = '/path/to/original/gromacs/files' # Path to the directory containing the trajectory and topology files
top_file = f'{dir_path}/<original>.tpr' # Topology file
traj_file = f'{dir_path}/<original>.xtc' # Trajectory file
new_name = '<modified>' # Name for the modified trajectory
solvent = 'SOL' # Name of your solvent you want to remove (resname)
mol_name = 'POL' # Name of one molecule you want to retain (resname)
lig_name = 'LIG' # Name of a second molecule you want to retain (resname)

# Load the trajectory and topology files as a MDAnalysis Universe object
u = mda.Universe(top_file, traj_file)

# MDAnalysis allows full control over the components of the system that are selected:
# https://docs.mdanalysis.org/stable/documentation_pages/selections.html
# https://userguide.mdanalysis.org/stable/selections.html

# Example: Select all system components that are not the solvent
solutes = u.select_atoms(f'not resname {solvent}')

# Write a new trajectory where each frame only contains the solute molecules
with mda.Writer(f'{dir_path}/{new_name}.xtc', n_atoms=solutes.n_atoms) as w:
    for ts in u.trajectory[:]: # Using the python slicing operator [start:stop:step], the number of frames can be reduced at this point
        w.write(solutes)

# Write a new gro file containing only the solute molecules
with mda.Writer(f'{dir_path}/{new_name}.gro') as w:
    w.write(solutes.atoms)

# Optional: Write a new index file containing only the solute molecules:

# If multiple individual solute groups are needed, they need to be individually written to the index file.
with mda.selections.gromacs.SelectionWriter(f'{dir_path}/{new_name}.ndx', mode='w') as ndx:
    ndx.write(u.select_atoms(f'resname {mol_name}'), name=f'{mol_name}')
    ndx.write(u.select_atoms(f'resname {lig_name}'), name=f'{lig_name}')
```

- Adjust \*_.mdp_ file using a text editor:
  - Remove solvent group(s) for temperature (pressure) coupling.
- Manually delete solvent entries from \*_.top_ file using a text editor:
  - Remove solvent entry under _[molecules]_ in the _[system]_ section at the end of the \*_.top_ file.
  - **The name of the [ moleculetype ] in the _\*.top_ file defines the name of the system component in the NOMAD entry.**
- Generate new _\*.tpr_ file from edited _\*.top_, _\*.mdp_ and _\*.gro_ files:
  `gmx grompp -f modified.mdp -c modified.gro -p modified.top -o modified.tpr`
  - (**Optional:** An updated \*_.tpr_ file can be written in a script using [_GromacsWrapper_](https://gromacswrapper.readthedocs.io/en/latest/index.html))

# Prepare VASP trajectories for upload to NOMAD

!!! warning
Under construction.

# Prepare LAMMPS trajectories for upload to NOMAD

!!! warning
Under construction.