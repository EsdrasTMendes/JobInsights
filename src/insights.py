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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError(
            "Não existem as chaves 'min_salary' ou 'max_salary' no Job"
        )
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError(
            "min_salary, max_salary e salary devem ser do tipo int"
        )
    if job["min_salary"] > job["max_salary"]:
        raise ValueError(
            "O valor de min_salary deve ser menor que o o valor de max_salary"
        )
    return job["min_salary"] <= salary <= job["max_salary"]
    pass


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs
