
from course import Course
from resident import Resident, ResidentOff, ResidentPassedCourse
from scheduler import Scheduler


def main():
    try:
        courses = Course.read_courses_from_csv()

        resident = Resident.read_residents_from_csv()

        residents_off = ResidentOff.read_resident_off_rotation_from_csv()

        passed_course = ResidentPassedCourse.read_passed_course_from_csv()

        scheduler = Scheduler(courses, resident, residents_off, passed_course)
        scheduler.calculate_next_schedule()

        #_input_verification(residents_info)
    except Exception as ex:
        print(ex)

# def _input_verification(resident_info):
#     # check minimum R1/R2 in groups
#     pass


if __name__ == '__main__':
    main()
