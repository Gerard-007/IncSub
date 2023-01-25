
![Logo](https://res.cloudinary.com/geetechlab-com/image/upload/v1674630764/incsub/IncSub_waked9.png)


# A Flask TODO Project API Endpoint

A TODO API web application utilizing the Flask framework





## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Authors

- [@Gerard-007](https://github.com/Gerard-007)


## License

IncSub is released under the [MIT](https://choosealicense.com/licenses/mit/)


## Run Locally

Clone the project

```bash
  git clone https://github.com/Gerard-007/IncSub
```

Go to the project directory

```bash
  cd my-project
```

Create virtual environment

```bash
  python -m venv flask_venv
```

Activate virtual environment(Linux/Mac Machine)

```bash
  flask_venv/bin/activate
```

Activate virtual environment(Windows Machine)

```bash
  flask_venv/Script/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```




## API Reference

You can use "Postman" or any other Tool to run this Endpoint locally.


#### Get all Todos

```http
  GET 
  http://localhost/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
|     None  |  `list[]`  | Gets all Todos or Empty List[]|


#### Create Todo

```http
  POST 
  http://localhost/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**. Name of todo |
| `status` | `string` | **Required**. "completed" or "pending" |


#### Get Todo

```http
  GET 
  http://localhost/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of Todo to fetch |


#### Update Todo

```http
  PUT 
  http://localhost/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of Todo to Update |


#### Delete Todo

```http
  DELETE 
  http://localhost/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of Todo to Delete |


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://dev.to/geetechlab)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gerard-nwazuruoke-geetechlab/)

