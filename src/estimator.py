

# sample_input_data = {
#     region: {
#         name: "Africa",
#         avgAge: 19.7,
#         avgDailyIncomeInUSD: 5,
#         avgDailyIncomePopulation: 0.71
#     },
#     periodType: "days",
#     timeToElapse: 58,
#     reportedCases: 674,
#     population: 66622705,
#     totalHospitalBeds: 1380614
# }

# sample_output_data = {
#     data: {},
#     impact: {},
#     severeImpact: {}
# }


def estimator(data):

    currentlyInfected = data["reportedCases"] * 10
    currentlyInfected_severe = data["reportedCases"] * 50

    infectionsByRequestedTime = (currentlyInfected * 512) / 2
    infectionsByRequestedTime_severe = (currentlyInfected_severe * 512) / 2

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
