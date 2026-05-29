def calculate_score(
    total_wait,
    weights
):

    individual = (
        total_wait
        * weights["individual"]
    )

    operator = (
        total_wait
        * weights["operator"]
    )

    overall = (
        total_wait
        * weights["overall"]
    )

    return (
        individual
        + operator
        + overall
    )