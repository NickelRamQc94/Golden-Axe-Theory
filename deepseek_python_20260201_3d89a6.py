class TransformationGoldenAxe:
    """
    Transformée qui préserve MENeS
    """
    def transform(self, signal_ecoulement):
        # FFT standard
        spectre = np.fft.fft(signal_ecoulement)
        frequences = np.fft.fftfreq(len(signal_ecoulement))
        
        # Extraction de la signature MENeS
        # MENeS est invariant par transformation
        menes = self.calculer_invariant_spectral(spectre)
        
        # Filtrage qui préserve MENeS
        spectre_filtre = self.filtre_conserve_MENeS(spectre, menes)
        
        return {
            'spectre': spectre_filtre,
            'menes': menes,
            'frequences': frequences
        }
    
    def calculer_invariant_spectral(self, spectre):
        """
        MENeS spectral = ∫ |S(f)|² / f df (pondérée)
        """
        puissance = np.abs(spectre)**2
        f = np.linspace(0.1, 10, len(puissance))  # Éviter division par 0
        
        menes_spectral = np.trapz(puissance / f, f)
        return menes_spectral