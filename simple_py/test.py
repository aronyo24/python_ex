class DataContainer:
    serial_number = 0

    def __init__(self, data):
        DataContainer.serial_number += 1
        self.serial_number = DataContainer.serial_number
        self.data = data

    def update_data(self, new_data):
        self.data = new_data


def main():
    data_containers = []

    while True:
        # Display the data containers in order of serial numbers
        data_containers.sort(key=lambda x: x.serial_number, reverse=True)
        print("Current data containers:")
        for container in data_containers:
            print(f"Serial Number: {container.serial_number}, Data: {container.data}")

        new_data = input("Enter new data (or 'exit' to quit): ")

        if new_data.lower() == 'exit':
            break

        # Reset serial numbers
        DataContainer.serial_number = 0

        # Create a new DataContainer instance and update the data
        container = DataContainer(data=new_data)
        data_containers.append(container)

    print("Program ended.")

if __name__ == "__main__":
    main()
