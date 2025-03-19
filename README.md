# medicalCourseSchedule
Project to provide medical course schedule 

# Inputs
1- All students pass courses in 2 years

2- Each year has 13 periods/rotations

3- Group colors(5): Internal classification(BLUE, GREEN, ORANGE, REDS, YELLOW)

4- Group Name:

        4-1- ResidentI(RI) -> First Year
        4-2- ResidentII(RI) -> Second Year

# Abbreviations & keywords
- FM: Family Medical rotation (in Home courses)
- FM/{course name}: FM are in home courses  
- PC: Parent/Child

# Course names
  - FM courses(9)
    
    1- FM/PC
    
    2- FM/PC<-
    
    3- FM/MH-1
    
    4- FM/MH-Diamond
    
    5- FM/MH-2
    
    6- FM/Community
    
    7- FM/acute care
    
    8- FM/PS1
    
    9- FM/PS2

  - Outside courses(17)
    
    1- Elective1
    
    2- Elective2
     
    3- Elective3
    
    4- Selective
    
    5- Peds Amb
    
    6- Peds ER

    7- Peds Ward

    8- COE
    
    9- OBS
    
    10- ER1 (First Year)

    11- ER2 (Second Year)

    12- IM1 (First Year)

    13- IM2 (Second Year)

    14- Rural1 (Second Year)

    15- Rural2 (Second Year)

    16- Palliative Care

    17- Acute Care Selective

    

# Rules:

1- Schedule get current status of each resident and provides schedule for 
the following year

2- Residents R1 must get first course from FM courses

3- Each resident MUST consider following sequence in getting FM/ outside courses:
    
    - 1(FM)-3(outside)-1(FM)....
    or 
    - 1(FM)-4(outside)-1(FM)....

4- Maximum resident for each input schedule is 52
    
    - 26 NEW residents

    - 26 SAECOND year residents

5- Some courses are only for first year, some courses are only for second year
    
    - FM courses: All FM courses are first or second courses except
        
        - FM/Community -> second year
        - FM/acute care -> second year
    - Outside courses
        - ER1, IM1 -> first year
        - ER2, IM2, Rural1, Rural2, Acute Care Selective -> second year
    

6- Pre-requisites:
   
     - FM: N/A
        -  So for example resident could get FM/PS2 before FM/PS1
     - Outside: N/A 

7- Max course limit in each period/rotation

    - FM:
        -  FM/PS1,2 -> 7 (R1 + R2)
        -  FM/MH1,2 -> 6 (R1 + R2)
        -  FM/MH Diamond -> 2 (R1 + R2)
        -  FM/PC -> 4 (R1 + R2)
        -  FM/PC<-  -> 2 (R1 + R2)
        -  FM/Community -> 3 (R1 + R2)
        -  FM/acute care -> 2 (R1 + R2)
    - Outside:
        - OBS -> R1: 5, R2: 1
        - IM1 -> R1: 3
        - IM2 -> R2: 2
        - ER1 -> R1: 3
        - ER2 -> R2: 2
        - COE -> R1: 1, R2: 2
        - Palliative Care -> R1: 4, R2: 1
        - Others: R1: 1, R2: 1 
    
8- Match Rules:
    
courses which should come next/before each others 

(example OBS should come before/after FM/PC)

    - OBS <--> FM/PC
    - FM/MH <--> COE or Palliative Care
    - FM/PS1,2 <--> ER1,2 or Medicine
Note: FN/PS1,2 could be in year1 or year2. Since ER1 is for year1 and ER2
is for year2 this match should be done if possible.

9- Minimum Residents(R1, R2) for each FM group in each period/rotation is 4

10-  Minimum Residents for each outside group in each period/rotation is N/A


Final result:

    - Rotation schedule for each group/period  

Questions:
- Can residents get more than one course in a period/rotation?
- Can resident get course FM/PS2 and FM/PS1 together?
- So input includes list of residents in each group/resident???
  - Please provide input list
- Do you provide resident/group/ and if they are R1/R2 as input?
- Do we have always 5 Groups(BLUE, GREEN, ORANGE, REDS, YELLOW)
- Verify ????
  -  FM/MH1,2 -> 6 (R1 + R2)
  -  FM/MH Diamond -> 2 (R1 + R2) 