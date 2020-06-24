### Flask TinyURL Service

#### Run your own URL shrinking service such as bit.ly or goo.gl.

[Project implementation plan](./develop-plan.md)

#### Installation 

```
# clone app
git clone https://github.com/BondaiKa/tinyurl.git

# change your working dir to project's path
cd project/path
```

* Install docker [Docker](https://docs.docker.com/)   

#### environment variables 

* rename `.env_example` to `env`

#### Running docker containers :whale:

* To run container:

```bash
docker-compose up --build
```