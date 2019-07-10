def time_converter(time):
    time1=time.replace(':', ' ').split()
    hours=int(time1[0])
    minutes=str(time1[1])

    if hours > 24:
        return "Error"
    elif hours == 12:
        return str(hours) + ':' + str(minutes) + ' p.m'
    elif 13 <= hours <= 24:
        return str(hours-12) + ':' + str(minutes) + ' p.m'
    else:
        return str(hours) + ':' + str(minutes) + ' a.m'

if __name__ == '__main__':
    time = '09:00'
    print(time_converter(time))