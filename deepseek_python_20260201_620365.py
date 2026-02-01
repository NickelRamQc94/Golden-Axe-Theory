# 1. Charge tes données (exemple)
# ATI_list = [...], TCF_list = [...], time_list = [...], omega_list = [...]

# 2. Lance l'analyse
from goldeneye_nickel_scale_invariant import analyze_your_data

results = analyze_your_data(
    ATI_series=ATI_list,
    TCF_series=TCF_list,
    time_series=time_list,
    omega_norm_series=omega_list  # optionnel
)

# 3. Voir les résultats
print(f"Statut: {results['critical_report']['status']}")
print(f"Π_N max: {results['max_Pi_N']:.3e}")
print(f"Corrélation avec ω: {results['correlation_with_omega']:.3f}")

# 4. Sauvegarder
import json
with open('nickel_analysis_results.json', 'w') as f:
    json.dump(results, f, indent=2)