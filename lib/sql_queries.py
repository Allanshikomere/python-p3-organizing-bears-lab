# Query to select all female bears and return their name and age
select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

# Query to select the oldest bear's name and age
select_oldest_bears_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# Query to select the count of bears by sex
select_count_of_bears_by_sex = """
    SELECT
        sex,
        COUNT(*) AS count
    FROM bears
    GROUP BY sex;
"""


