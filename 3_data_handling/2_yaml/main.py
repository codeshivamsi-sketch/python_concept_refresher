import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

print(data["name"])
print(data["skills"])