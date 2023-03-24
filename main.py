from util_func.parse_file import parse_njson_file

if __name__ == '__main__':
    df = parse_njson_file('discoveries.njson')
    print(df.head(50))
