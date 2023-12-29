#The function of this program is to help the user enter phytochemical information

original_connections = []    #list of tuples in the form (ID=C_integer,SOURCE=SourceID,DESTINATION=DestinationID)

with open('connections.txt') as connections_data:
    connection_lines = connections_data.readlines()
    del connection_lines[0]
    for line in connection_lines:
        split_line = line.split(sep=',')
        if len(split_line) > 3:
            print("Error: item" + str(split_line) + " is not formatted correctly. Exiting...")
        else:
            new_tuple = (split_line[0], split_line[1], split_line[2])

def load_data(data_source, elements_per_line, separator):
    tuples_dict = {}
    with open(data_source) as data:
        lines = data.readlines()
        for line in lines:
