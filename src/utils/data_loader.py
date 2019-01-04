import csv


def get_protocol_from_csv(csv_path):
    """

    :param csv_path: path to csv fille
    """
    with open(csv_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')

        records = []
        for row in csv_reader:
            try:

                sample_id = row[0]
                row_measurements = []
                for measurement_id in row[1:]:
                    row_measurements.append(measurement_id)

                records.append(
                    {
                        "sample_id": sample_id,
                        "row_measurements": row_measurements
                    }
                )
            except:
                print("row excluded due to error, row wl: {}".format(row[0]))
                

        return records


def get_data_from_csv(csv_path):

    with open(csv_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        
        headers = filter_headers(next(csv_reader))

        return load_dataset(csv_reader, headers)


def load_dataset(csv_reader, headers):
    records = []
    for row in csv_reader:
        try:
            record = {}

            record[headers[0][1]] = int(row[0])

            for i, h in headers[1:]:
                record[str(h)] = float(row[i])
            records.append(record)
        except:
            print("row excluded due to error, row wl: {}".format(row[0]))
            pass
    return records


def filter_headers(headers):
    headers_id_only = [headers[0]]+[__number_only(h) for h in headers[1:]]
    enu_headers = enumerate(headers_id_only)
    valid_headers = [(i, h) for i, h in enu_headers]
    return valid_headers


def __number_only(name: str):
    nums = "1234567890"
    digit_only = [c for c in name if c in nums]
    return int("".join(digit_only))
