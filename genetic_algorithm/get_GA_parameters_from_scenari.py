import re

# Function to extract numerical values from the string
def extract_value(pattern, string):
    match = re.search(pattern, string)
    return float(match.group(1)) if match else None

def get_GA_parameters_from_scenari(slurm_scenari):
    base_scenario = slurm_scenari.split('_GAHPDEF')[0]
    # Check if "GAHPDEF" is in the string
    if "GAHPDEF" in slurm_scenari:
        pmutQuant = extract_value(r"pmutQuant(\d+)", slurm_scenari) / 1000
        pmutCat = extract_value(r"pmutCat(\d+)", slurm_scenari) / 1000
        sigmahalv = 1/extract_value(r"sigmahalv(\d+)", slurm_scenari)
    else:
        pmutQuant = 0.5
        pmutCat = 0.25
        sigmahalv = 0.1
    
    # Create a dictionary with the values
    params = {
        "scenari": base_scenario,
        "pmutQuant": pmutQuant,
        "pmutCat": pmutCat,
        "sigmahalv": sigmahalv
    }
    return params

# get_GA_parameters_from_scenari("GeneticSingleIs_GA_GAHPDEF_pmutQuant100_pmutCat10_sigmahalv5")
# get_GA_parameters_from_scenari("GeneticSingleIs_GA")
