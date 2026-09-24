from suitability import calculate_suitability
from candidate_filter import filter_candidates
from recommendation import recommend_network
from recommendation_result import build_recommendation_result
from recommendation_reasons import generate_recommendation_reasons
from no_recommendation import build_no_recommendation_result


def prepare_observations(observations):
    prepared = []

    for observation in observations:
        observation = observation.copy()

        observation["suitability_score"] = calculate_suitability(
            observation
        )

        prepared.append(observation)

    return prepared


def get_recommendation(observations, task):
    prepared_observations = prepare_observations(observations)

    candidates = filter_candidates(
        prepared_observations,
        task
    )

    no_recommendation = build_no_recommendation_result(
        task,
        candidates
    )

    if no_recommendation is not None:
        return no_recommendation

    recommended = recommend_network(candidates)

    result = build_recommendation_result(
        recommended,
        task
    )

    result["reasons"] = generate_recommendation_reasons(
        recommended
    )

    return result