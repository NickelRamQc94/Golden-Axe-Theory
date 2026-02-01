class DynamiqueCritique:
    """
    Équation maîtresse de l'évolution de Π_N
    """
    def __init__(self, menes, geometry_factor):
        self.menes = menes
        self.kappa = 0.1  # Constante d'évolution
        self.Pi_crit = self.calculer_Pi_crit(menes)
        self.Pi_max = 3.2  # Limite physique
    
    def equation_evolution(self, Pi, t):
        """
        dΠ_N/dt = κ·(Π_N - Π_crit)·(1 - Π_N/Π_max) + ξ(t)
        """
        # Terme déterministe
        terme_det = self.kappa * (Pi - self.Pi_crit) * (1 - Pi/self.Pi_max)
        
        # Bruit corrélé (ξ(t))
        # Auto-corrélation : ⟨ξ(t)ξ(t')⟩ = σ² exp(-|t-t'|/τ)
        bruit = self.bruit_correle(t)
        
        return terme_det + bruit
    
    def bruit_correle(self, t):
        """
        Modèle de bruit avec mémoire
        """
        tau_correlation = 4.8  # Temps de corrélation
        amplitude = 0.05 * self.menes  # Amplitude dépend de MENeS
        
        # Processus d'Ornstein-Uhlenbeck
        return amplitude * np.exp(-t/tau_correlation) * np.random.randn()