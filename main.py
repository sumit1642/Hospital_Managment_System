from database import *


def initialize_database():
    connection = connect_to_database()
    create_database()
    create_table(connection)
    connection.close()


def add_patient():
    connection = connect_to_database()
    cursor = connection.cursor()
    room_id = int(input("Enter Room ID: "))
    patient_name = input("Enter Patient Name: ")
    patient_address = input("Enter Patient Address: ")
    patient_phone = input("Enter Patient Phone: ")
    patient_disease = input("Enter Patient Disease: ")

    query = """
        INSERT INTO Patient (room_id, Patient_Name, Patient_Address, Patient_Phone, Patient_Disease)
        VALUES (%s, %s, %s, %s, %s)
    """
    data = (room_id, patient_name, patient_address, patient_phone, patient_disease)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()
    connection.close()


def search_patient():
    connection = connect_to_database()
    cursor = connection.cursor()
    room_id = int(input("Enter Room ID to search: "))

    query = "SELECT * FROM Patient WHERE room_id = %s"
    data = (room_id,)
    print("Searching for patient...")
    cursor.execute(query, data)
    result = cursor.fetchone()

    if result:
        print("Patient Details:")
        print(f"Patient ID: {result[0]}")
        print(f"Room ID: {result[1]}")
        print(f"Name: {result[2]}")
        print(f"Address: {result[3]}")
        print(f"Phone: {result[4]}")
        print(f"Disease: {result[5]}")
    else:
        print("Patient not found.")

    cursor.close()
    connection.close()


def discharge_patient():
    connection = connect_to_database()
    cursor = connection.cursor()
    room_id = int(input("Enter Room ID to discharge: "))

    query_check = "SELECT * FROM Patient WHERE room_id = %s"
    data_check = (room_id,)
    cursor.execute(query_check, data_check)
    result_check = cursor.fetchone()

    if result_check:
        query_discharge = "DELETE FROM Patient WHERE room_id = %s"
        data_discharge = (room_id,)
        cursor.execute(query_discharge, data_discharge)
        connection.commit()

        if cursor.rowcount > 0:
            print("Patient discharged successfully!")
        else:
            print("Error discharging patient.")
    else:
        print("Patient not found.")

    cursor.close()
    connection.close()


def patient_details():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Patient")
    results = cursor.fetchall()

    if results:
        print("+" + "+".join(["=" * 20] * 6) + "+")
        print(
            "|| {:^18} || {:^18} || {:^18} || {:^18} || {:^18} ||".format(
                "ID", "Name", "Address", "Phone", "Disease"
            )
        )
        print("+" + "+".join(["=" * 20] * 6) + "+")
        for result in results:
            print(
                "|| {:^18} || {:^18} || {:^18} || {:^18} || {:^18} ||".format(
                    result[0], result[2], result[3], result[4], result[5]
                )
            )
            print(
                "+" + "+".join(["=" * 20] * 6) + "+"
            )  # Separate border for each patient
    else:
        print("No patients in the database.")

    cursor.close()
    connection.close()


def exit_program():
    print("Exiting Hospital Management System. Goodbye!")
    exit()


def main_menu():
    while True:
        print("\n|=== Hospital Management System ===|")
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. Discharge Patient")
        print("4. View All Patient Details")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            search_patient()
        elif choice == "3":
            discharge_patient()
        elif choice == "4":
            patient_details()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    initialize_database()  # Initialize the database before starting the program
    main_menu()
