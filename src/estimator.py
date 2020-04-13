

# sample_input_data = {
#     "region": {
#         "name": "Africa",
#         "avgAge": 19.7,
#         "avgDailyIncomeInUSD": 4,
#         "avgDailyIncomePopulation": 0.73
#     },
#     "periodType": "days",
#     "timeToElapse": 38,
#     "reportedCases": 2747,
#     "population": 92931687,
#     "totalHospitalBeds": 678874
# }

# sample_output_data = {
#     data: {},
#     impact: {},
#     severeImpact: {}
# }


def estimator(data):

    currentlyInfected = data["reportedCases"] * 10
    currentlyInfected_severe = data["reportedCases"] * 50

    infectionsByRequestedTime = currentlyInfected * \
        (2 ** (data["timeToElapse"]//3))
    infectionsByRequestedTime_severe = currentlyInfected_severe * \
        (2 ** (data["timeToElapse"]//3))

    data = {
        "data": data,
        "impact": {
            "currentlyInfected": currentlyInfected,
            "infectionsByRequestedTime": infectionsByRequestedTime,
        },
        "severeImpact": {
            "currentlyInfected": currentlyInfected_severe,
            "infectionsByRequestedTime": infectionsByRequestedTime_severe,
        }
    }

    return data


# print(estimator(sample_input_data))
