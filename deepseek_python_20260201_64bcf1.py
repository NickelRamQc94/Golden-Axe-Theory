def test_threshold_hypothesis(Pi_N, omega, threshold=2.5, window=5):
    alarms = Pi_N > threshold
    events = np.gradient(omega) > np.std(np.gradient(omega))
    
    true_positives = 0
    for i in range(len(alarms)-window):
        if alarms[i] and np.any(events[i:i+window]):
            true_positives += 1
    
    return true_positives / np.sum(alarms)  # Précision