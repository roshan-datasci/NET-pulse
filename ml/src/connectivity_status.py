def get_connectivity_status(suitability_score):
    """
    Convert a suitability score into a human-readable
    connectivity status.
    """

    if suitability_score >= 70:
        return "strong"

    if suitability_score >= 40:
        return "moderate"

    return "weak"


if __name__ == "__main__":

    test_scores = [
        85,
        68,
        52,
        35,
        19,
    ]

    print("=== WiSense Connectivity Status ===")
    print()

    for score in test_scores:

        status = get_connectivity_status(score)

        print(
            f"Suitability: {score}/100 "
            f"-> Status: {status}"
        )