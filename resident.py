import csv
import string
import traceback
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class ResidentPassedCourse:
    resident_id: int
    # resident_name: str
    course_name: str

    @staticmethod
    def read_passed_course_from_csv() -> List["ResidentPassedCourse"]:
        passed_courses = []
        csv_file = 'inputs/resident_passed_course.csv'
        # Open and read the CSV file
        try:
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)  # Reads the CSV as a dictionary
                for row in csv_reader:
                    resident_id = row["id"].strip()
                    course_name = row["course_name"].strip()

                    passed_courses.append(ResidentPassedCourse(resident_id, course_name))
        except Exception as ex:
            traceback.print_exc()
            raise ValueError(ex)

        return passed_courses


@dataclass
class ResidentOff:
    resident_id: str
    rotation: int

    @staticmethod
    def read_resident_off_rotation_from_csv() -> List["ResidentOff"]:
        residents_off = []
        csv_file = 'inputs/resident_off_rotation.csv'
        # Open and read the CSV file
        try:
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)  # Reads the CSV as a dictionary
                for row in csv_reader:
                    resident_id = row["resident_id"].strip()
                    rotation = row["rotation"].strip()

                    residents_off.append(ResidentOff(resident_id, rotation))
        except Exception as ex:
            traceback.print_exc()
            raise ValueError(ex)

        return residents_off


@dataclass
class Resident:
    resident_id: str
    name: str
    group_color: str
    group_name: str

    @staticmethod
    def read_residents_from_csv() -> List["Resident"]:
        residents = []
        csv_file = 'inputs/residents.csv'
        # Open and read the CSV file
        try:
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)  # Reads the CSV as a dictionary
                for row in csv_reader:
                    resident_id = row["resident_id"].strip()
                    name = row["name"].strip()
                    group_color = row["group_color"].strip()
                    group_name = row["group_name"].strip()

                    residents.append(Resident(resident_id, name, group_color, group_name))
        except Exception as ex:
            traceback.print_exc()
            raise ValueError(ex)

        return residents
