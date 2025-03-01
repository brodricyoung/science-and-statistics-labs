import random

def main():
    data_file = "airplane-data.csv"
    random_sample_size = 30
    return_simple_ranodm_sample(data_file, random_sample_size)


def return_simple_ranodm_sample(all_data_csv_filename, random_sample_size):
    data_rows = []
    # read the file
    with open(all_data_csv_filename, "r") as file:
        header = file.readline().strip().split(",")[0] # saves header of column 1 (original data header)

        # get the data from each row and add it to a list
        for row in file:
            row_parts = row.strip().split(",")
            data_rows.append(row_parts[0])
            

    with open(all_data_csv_filename, "w") as file:
        # get random integers for the indexs of values to use in the random sample
        # use those indexes to get the value and add all sample values to a list
        column2_data = []
        rand_ints = []
        random_int = random.randint(0, len(data_rows) - 1) # any row number index
        for i in range(0, random_sample_size): # get a specific number of sample values
            while random_int in rand_ints: # make sure its a unique index (not counting the same row twice)
                random_int = random.randint(0, len(data_rows) - 1) 
            rand_ints.append(random_int)
            column2_data.append(data_rows[random_int])


        ########## write all values back to the file. ##########
        # write original data column back the same way in column 1
        # write simple random sampled values to column 2 
        file.write(f"{header},Simple Random Sample")
        for i, row_data in enumerate(data_rows):
            if i < len(column2_data):
                file.write(f"\n{row_data},{column2_data[i]}")
            else:
                file.write(f"\n{row_data}")


if __name__ == "__main__":
    main()
    