import re

# Function to extract numerical values from the string
def extract_value(pattern, string):
    match = re.search(pattern, string)
    return float(match.group(1)) if match else None

def get_GA_parameters_from_scenari(slurm_scenari):
    # Baseline
    pmutQuant = 0.5
    pmutCat = 0.25
    sigmahalv = 0.1
    base_scenario = slurm_scenari
    NbFeaturesPenalty = 0
    TournamentFeaturesPenalty = False
    Ntournament = 2
    
    if "GAHPDEF" in slurm_scenari:
        base_scenario = slurm_scenari.split('_GAHPDEF')[0]
        pmutQuant = extract_value(r"pmutQuant(\d+)", slurm_scenari) / 1000
        pmutCat = extract_value(r"pmutCat(\d+)", slurm_scenari) / 1000
        sigmahalv = extract_value(r"sigmahalv(\d+)", slurm_scenari) / 1000
    elif "GAPENAL" in slurm_scenari:
        base_scenario = slurm_scenari.split('_GAPENAL')[0]
        NbFeaturesPenalty = extract_value(r"NbFeaturesPenalty(\d+)", slurm_scenari)
        if NbFeaturesPenalty != 9999 :
            NbFeaturesPenalty = NbFeaturesPenalty/1000
        
        TournamentFeaturesPenalty = extract_value(r"TournamentFeaturesPenalty(\d+)", slurm_scenari) == 1
        Ntournament = 3
    
    # Create a dictionary with the values
    params = {
        "scenari": base_scenario,
        "pmutQuant": pmutQuant,
        "pmutCat": pmutCat,
        "sigmahalv": sigmahalv,
        "NbFeaturesPenalty": NbFeaturesPenalty,
        "TournamentFeaturesPenalty": TournamentFeaturesPenalty,
        "Ntournament": Ntournament
    }
    return params

# get_GA_parameters_from_scenari("GeneticSingleIs_GA_GAHPDEF_pmutQuant100_pmutCat10_sigmahalv5")
# get_GA_parameters_from_scenari("GeneticSingleIs_GA")
# get_GA_parameters_from_scenari("GeneticSingleIs_GA_GAPENAL_NbFeaturesPenalty1_TournamentFeaturesPenalty0")
