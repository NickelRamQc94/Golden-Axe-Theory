def test_universality(Pi_N_critical_list):
    """
    Pi_N_critical_list: liste des Π_N au moment des blow-ups
    pour différentes simulations
    """
    mean_critical = np.mean(Pi_N_critical_list)
    std_critical = np.std(Pi_N_critical_list)
    cv = std_critical / mean_critical  # Coefficient de variation
    
    # Si cv < 0.1, l'hypothèse tient
    return cv < 0.1, mean_critical, cv