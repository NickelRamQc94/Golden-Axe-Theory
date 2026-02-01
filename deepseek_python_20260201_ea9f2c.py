def test_scaling_law(ATI, TCF, Pi_N):
    ratio = ATI / TCF
    # Ajustement linéaire en log-log
    coeffs = np.polyfit(np.log(ratio), np.log(Pi_N), 1)
    alpha = coeffs[0]  # L'exposant
    C = np.exp(coeffs[1])  # La constante
    
    # Qualité de l'ajustement
    residuals = np.log(Pi_N) - (coeffs[0]*np.log(ratio) + coeffs[1])
    R_squared = 1 - np.var(residuals) / np.var(np.log(Pi_N))
    
    return {"alpha": alpha, "C": C, "R^2": R_squared}