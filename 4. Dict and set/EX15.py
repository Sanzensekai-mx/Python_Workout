def get_rainfall():
    rainfall = {}
    while True:
        city_input = input('Enter city\'s name: ')
        if not city_input:
            break
        try:
            mm_input = int(input('Enter mm input: '))
        except ValueError:
            print('You didn\'t enter a valid integer; try again.')
            continue
        rainfall[city_input] = rainfall.get(city_input, 0) + mm_input
    for city, rain in rainfall.items():
        print(f'{city} - {rain}')


get_rainfall()


