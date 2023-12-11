import re


def input_to_map():
    """Parses input data"""
    problem_input = open(
        "example-input.txt", "r"
    ).readlines()  # Add input.txt in the directory
    seeds = []
    seed_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []
    for i, line in enumerate(problem_input):
        if "seeds" in line:
            seeds = [
                int(seed) for seed in re.sub(r"seeds: ", "", line).strip().split(" ")
            ]
        elif "seed-to-soil" in line:
            j = 1
            while problem_input[i + j] != "\n":
                seed_soil.append(
                    [int(num) for num in problem_input[i + j].strip().split(" ")]
                )
                j += 1
        elif "soil-to-fertilizer" in line:
            j = 1
            while problem_input[i + j] != "\n":
                soil_fertilizer.append(
                    [int(num) for num in problem_input[i + j].strip().split(" ")]
                )
                j += 1
        elif "fertilizer-to-water" in line:
            j = 1
            while problem_input[i + j] != "\n":
                fertilizer_water.append(
                    [int(num) for num in problem_input[i + j].strip().split(" ")]
                )
                j += 1
        elif "water-to-light" in line:
            j = 1
            while problem_input[i + j] != "\n":
                water_light.append(
                    [int(num) for num in problem_input[i + j].strip().split(" ")]
                )
                j += 1
        elif "light-to-temperature" in line:
            j = 1
            while problem_input[i + j] != "\n":
                light_temperature.append(
                    [int(num) for num in problem_input[i + j].strip().split(" ")]
                )
                j += 1
        elif "temperature-to-humidity" in line:
            j = 1
            while problem_input[i + j] != "\n":
                temperature_humidity.append(
                    [int(num) for num in problem_input[i + j].strip().split(" ")]
                )
                j += 1
        elif "humidity-to-location" in line:
            j = 1
            while i + j < len(problem_input) and problem_input[i + j] != "\n":
                humidity_location.append(
                    [int(num) for num in problem_input[i + j].strip().split(" ")]
                )
                j += 1

    return (
        seeds,
        seed_soil,
        soil_fertilizer,
        fertilizer_water,
        water_light,
        light_temperature,
        temperature_humidity,
        humidity_location,
    )


def map_phase(phase_map, nums, indicator=""):
    print(f"PHASE: {indicator}")
    destinations = [m[0] for m in phase_map]
    sources = [m[1] for m in phase_map]
    ranges = [m[2] for m in phase_map]
    map_len = len(phase_map)

    mapped_nums = []
    for num in nums:
        found_in_map = False
        for i in range(map_len):
            if sources[i] <= num < sources[i] + ranges[i]:
                dif = num - sources[i]
                mapped_nums.append(destinations[i] + dif)
                found_in_map = True
        if not found_in_map:
            mapped_nums.append(num)

    return mapped_nums


SEEDS, SS, SF, FW, WL, LT, TH, HL = input_to_map()

print(map_phase(SS, SEEDS, "seeds -> soil"))
