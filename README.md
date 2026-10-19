# Montreal Dataset (`montreal-bids`)

## Overview

This dataset contains MRI data from a sleep manipulation study conducted at the Concordia University (Canada). It is part of the ENIGMA-Sleep Working Group collection used to study the effects of sleep loss on glymphatic MRI indices. The data are organized according to the Brain Imaging Data Structure (BIDS) and managed with DataLad (git-annex).

## Sample

| Item | Value |
|---|---|
| Site | Montreal |
| Affiliation | Concordia University |
| Country | Canada |
| Participants (N) | 18 |
| Age, mean (SD), years | 21.1 (2.7) |
| Male (%) | 38.9 |

## Sleep protocol

- **SD**: total sleep deprivation, 36 h

Participants were scanned under baseline and sleep manipulation conditions.

## Imaging data

### T1-weighted (`anat/`)

| Parameter | Value |
|---|---|
| Scanner | GE Discovery MR750 |
| Sequence | BRAVO |
| TR (ms) | 8.2 |
| TE (ms) | 3.18 |
| TI (ms) | 450 |
| Flip angle (°) | 12 |

## Data organization

- `sub-<ID>/ses-<label>/`: raw BIDS data (`anat/`)
- `participants.tsv`: participant-level information
- `sub-<ID>/sub-<ID>_sessions.tsv`: session-level information (condition, visit, date, time)
- `derivatives/`: processed outputs, if present

File contents are tracked with git-annex. After cloning, retrieve data with `datalad get <path>`.

## Original publication

Cross, N. E., et al. (2021). An altered balance of integrated and segregated brain activity is a marker of cognitive deficits following sleep deprivation. *PLOS Biology*. [https://doi.org/10.1371/journal.pbio.3001232](https://doi.org/10.1371/journal.pbio.3001232)

## Contact

- Jorik D. Elberse: [j.elberse@fz-juelich.de](mailto:j.elberse@fz-juelich.de)
- Masoud Tahmasian: [m.tahmasian@fz-juelich.de](mailto:m.tahmasian@fz-juelich.de)
