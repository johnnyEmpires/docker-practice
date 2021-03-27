# docker-practice
starting up with docker

## Prerequisite(s)

* docker

## Let's start

### 1. Project Directory

create a sample folder, name anything you want, in this case as `docker-practice`.

### 2. Create Dockerfile

Create docker file `docker-practice\Dockerfile`, with the following contents

```docker
FROM python:3.9.0

ADD sample.py requirements.txt .

RUN pip install -r requirements.txt --no-cache

CMD ["python", "sample.py"]
```

### 3. Sample application

Create a simple python application called `docker-practice\sample.py` and use a third party module to also test pip. 

```python
import time
from basiclog import module_logger

log = module_logger(__name__)

log.info("App running within docker")

for i in reversed(range(1, 6)):
    log.info(f'end of script in...{i}')
    time.sleep(1)

log.info('sample app in docker terminated.')
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

### 6. Start container

Start the container using below command and specifying the image name, in this case `sample-python-app`.

```
docker run sample-python-app
```

**done!** you should see something like below if the container run properly.

```
C:\projects\python\docker-practice>docker run sample-python-app
2021-03-27 10:13:27,826   9     INFO    App running within docker
2021-03-27 10:13:27,826   9     INFO    end of script in...5
2021-03-27 10:13:28,828 1010    INFO    end of script in...4
2021-03-27 10:13:29,829 2012    INFO    end of script in...3
2021-03-27 10:13:30,831 3014    INFO    end of script in...2
2021-03-27 10:13:31,833 4016    INFO    end of script in...1
2021-03-27 10:13:32,835 5018    INFO    sample app in docker terminated.

```

## Notes
* when using python `input` function, `EOFError` will be raised.
* use `-i` for interactive mode to prevent this error from appearing.