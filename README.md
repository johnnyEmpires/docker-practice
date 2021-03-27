# docker-practice
starting up with docker

## Prerequisite(s)

* docker

## Let's start

### 1. Project Directory

create a sample folder, name anything you want, in this case as `docker-practice`.

### 2. Create Dockerfile

Create docker file `docker-practice\Dockerfile`, with the following contents

```
FROM python:3.9.0

ADD sample.py requirements.txt .

RUN pip install -r requirements.txt --no-cache

CMD ["python", "sample.py"]
```

### 3. Sample application

Create a simple python application called `docker-practice\sample.py` and use a third party module to also test pip. 

```
from basiclog import module_logger

log = module_logger(__name__)

log.info("App running within docker")
```

### 4. Add dependency list

Create `docker-practice\requirements.txt` and list the [basiclog](https://github.com/johnnyEmpires/basiclog) module as dependency.

```
-e git+https://github.com/johnnyEmpires/basiclog.git#egg=basiclog
```

### 5. Build

Build the docker image running below command in the terminal and specifying `sample-python-app` as image name.

```
docker build -t sample-python-app .
```

### 6. 