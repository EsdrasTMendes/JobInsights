from src.jobs import read


def get_unique_job_types(path):
    file = read(
        path
    )  # realizando a leitura do arquivo através do caminho path
    job_list = (
        set()
    )  # criando um conjunto com a lista dos trabalhos utilizando  set()
    for job in file:  # realizando um loop for no arquivo passado no path
        job_list.add(
            job["job_type"]
        )  # adicionando os tipos de empregos no conjunto job_list
    return job_list  # retornando o conjunto job_list


def filter_by_job_type(jobs, job_type):
    jobs_filtered_by_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered_by_type.append(job)
    return jobs_filtered_by_type


def get_unique_industries(path):
    file = read(path)
    industries_list = set()
    for industrie in file:
        if industrie[
            "industry"
        ]:  # existe uma outra forma de resolver a questão com o discard()
            industries_list.add(industrie["industry"])
    return industries_list


def filter_by_industry(jobs, industry):
    jobs_filtered_by_industrie = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered_by_industrie.append(job)
    return jobs_filtered_by_industrie


def get_max_salary(path):
    file = read(path)
    max_salaries = []
    for salary in file:
        if salary["max_salary"].isdigit():
            max_salaries.append(int(salary["max_salary"]))
    return max(max_salaries)


def get_min_salary(path):
    file = read(path)
    min_salaries = []
    for salary in file:
        if salary["min_salary"].isdigit():
            min_salaries.append(int(salary["min_salary"]))
    return min(min_salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
