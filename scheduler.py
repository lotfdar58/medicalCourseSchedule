class Scheduler:
    match_course_map = {
        "OBS": ["FM/PC"],
        "FM/PC": ["OBS"],
        "FM/MH": ["COE", "Palliative Care"],  # Now stores both values
        "COE": ["Palliative", "FM/MH"],
        "Palliative Care": ["COE", "FM/MH"],
        "FM/PS1": ["ER1", "ER2", "Medicine"],
        "FM/PS2": ["ER1", "ER2", "Medicine"],
        "Medicine": ["ER1", "ER2", "FM/PS2"],
        "ER1": ["Medicine", "FM/PS1", "FM/PS2"],
        "ER2": ["Medicine", "FM/PS1", "FM/PS2"],
    }
    def __init__(self, courses, residents, residents_off, passed_course):
        self.courses = courses
        self.residents = residents
        self.residents_off = residents_off
        self.passed_course = passed_course

    def calculate_next_schedule(self):
        first_year_residents = [resident for resident in self.residents if resident.group_name == "ResidentI"]
        second_year_residents = [resident for resident in self.residents if resident.group_name == "ResidentII"]

        # Start from Second Resident which are in priority in selecting courses
        self.schedule_second_year_residents(second_year_residents)

        self.schedule_first_year_residents(first_year_residents)

    def schedule_first_year_residents(self, first_year_residents):
        resident_select_courses = {}
        rotations = 13
        for resident in first_year_residents:
            possible_courses_for_first_year = [course for course in self.courses if course.year_to_register != '2']
            first_year_courses = [course for course in self.courses if course.year_to_register == '1']
            # First course must be from FM
            # print(possible_courses_for_first_year)
            print(first_year_courses)

    def schedule_second_year_residents(self, second_year_residents):
        resident_select_courses = {}
        rotations = 13
        for resident in second_year_residents:
            resident_select_courses[resident.resident_id] = []
            remain_courses = self.get_resident_remain_courses(resident)
            print(f"length of remain course {len(remain_courses)}")

            while len(resident_select_courses[resident.resident_id]) <= rotations and len(remain_courses) > 0:
                course, *remain_courses = remain_courses
                resident_select_courses[resident.resident_id].append(course)
                self.add_match_course(course, resident, resident_select_courses)

    def add_match_course(self, course, resident, resident_select_courses):
        match_courses = Scheduler.match_course_map.get(course.course_name)
        if match_courses is not None and len(match_courses) > 0 and len(
                resident_select_courses[resident.resident_id]) < 13:
            resident_select_courses[resident.resident_id].append(match_courses[0])

    def get_resident_remain_courses(self, resident):
        # ER1 COULD NOT BE IN SECOND YEAR
        # If there is match courses, choose and add first one
        resident_pass_courses = [item.course_name for item in self.passed_course if
                                 item.resident_id == resident.resident_id]
        remain_courses = [course for course in self.courses if course.course_name not in resident_pass_courses]
        return remain_courses
