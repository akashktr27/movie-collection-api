def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")

def after_scenario(context, scenario):
    print(f"Finished scenario: {scenario.name}")
