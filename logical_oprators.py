temp = 25
is_raining = False
if temp > 35 or is_raining:
    print("Outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

## -------------
temp = 10
is_sunny = True
if temp >= 28 and is_sunny:
    print("Its HOT outside")
    print("its SUNNY")
elif temp <= 0 and is_sunny:
    print("Its too cold outside")
elif 28 > temp > 0 and is_sunny:
    print("its warm outside")
elif temp >= 28 and not is_sunny:
    print("Its cloudy outside")
else:
    print("Its perfect...!")