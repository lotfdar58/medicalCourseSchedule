import csv
import string
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Course:
    course_name: str
    course_type: str
    year_to_register: Optional[str] = None

    @staticmethod
    def read_courses_from_csv() -> List["Course"]:
        courses = []
        csv_file = 'inputs/courses.csv'
        # Open and read the CSV file
        try:
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)  # Reads the CSV as a dictionary
                for row in csv_reader:
                    course_name = row["course_name"].strip()
                    course_type = row["course_type"].strip()
                    year_to_register = row["year_to_register"].strip()

                    # Create a Course instance and append to the list
                    courses.append(Course(course_name, course_type, year_to_register))
        except Exception as ex:
            raise ex

        return courses
